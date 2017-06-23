import re
import time
import pickle
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer as TFIV

def review_to_wordlist(review):
	soup = BeautifulSoup(review,"html.parser")
	review_text = soup.get_text()
	review_text = re.sub("[^a-zA-Z]"," ", review_text)
	words = review_text.lower().split()
	return words
	
def get_trainset():
	train = pd.read_csv('labeledTrainData.tsv', delimiter="\t", quoting=3)
	y_train = train['sentiment'][:10000]
	train_data = []
	#for i in xrange(0,len(train['review'])):
	for i in xrange(0,10000):
		train_data.append(" ".join(review_to_wordlist(train['review'][i])))

	f = open('train_data.pickle', 'wb')
	f.write(pickle.dumps(train_data))
	f.close()

	print "TrainSet Starting!\n"
	from sklearn.feature_extraction.text import TfidfVectorizer as TFIV
	tfv = TFIV(min_df=3, max_features=None, strip_accents='unicode', analyzer='word',token_pattern=r'\w{1,}', ngram_range=(1, 2), use_idf=1,smooth_idf=1,sublinear_tf=1, stop_words = 'english')
	X = tfv.fit_transform(train_data).todense()
	voc = tfv.vocabulary_
	#f = open('X.pickle', 'wb')
	#f.write(pickle.dumps(X))
	#f.close()
	#print 'TrainSet End!\n'

	del train_data

	return X, y_train, voc

def train():
	X, y_train, voc = get_trainset()
	from sklearn.naive_bayes import MultinomialNB as MNB
	model_NB = MNB(alpha=1.0, class_prior=None, fit_prior=True)
	
	print 'Start Training!\n'
	start = time.time()
	model_NB.fit(X, y_train) 
	end = time.time()
	f = open('model2.pickle', 'wb')
	f.write(pickle.dumps(model_NB))
	f.close()
	print 'Finish Training!\n'
	
	from sklearn.cross_validation import cross_val_score
	import numpy as np
	print np.mean(cross_val_score(model_NB, X, y_train, cv=5, scoring='roc_auc'))

	f = open('voc_senti.pickle', 'wb')
	f.write(pickle.dumps(voc))
	f.close()

	return voc

def pred(test_idx, test_doc, model, voc):
	test_data = []
	for i in xrange(len(test_doc)):
		test_data.append(" ".join(review_to_wordlist(test_doc[i])))
	tfv = TFIV(min_df=3, max_features=None, strip_accents='unicode', analyzer='word', token_pattern=r'\w{1,}',
			   ngram_range=(1, 2), use_idf=1, smooth_idf=1, sublinear_tf=1, stop_words='english', vocabulary=voc)
	X_test = tfv.fit_transform(test_data).todense()
	X_test = np.array(X_test)
	pred = model.predict(X_test)
	test_idx = np.array(test_idx)
	like_idx = list(np.array(range(len(tag)))[pred == 1])
	hate_idx = list(np.array(range(len(tag)))[pred == 0])
	return like_idx, hate_idx
