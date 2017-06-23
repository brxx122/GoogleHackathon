import numpy as np
import time
import pandas as pd
import pickle
from sklearn.feature_extraction.text import TfidfVectorizer,CountVectorizer
from sklearn.naive_bayes import MultinomialNB

import trainNB as NB

def get_test_idx(filename):
	data = pd.read_csv(filename)
	label = [t[1:-1] for t in data['label'].values]
	doc = [l for l in data['title'].values]
	idx = [id for id in data['id'].values]
	label = np.array(label)
	idx = np.array(idx)
	doc = np.array(doc)
	test_idx = list(idx[label == ''])
	test_doc = list(doc[label == ''])
	return test_idx, test_doc
	
def Loop_mark(test_doc, test_idx):
	f = open('model.pickle', 'rb')
	model = pickle.load(f)
	f.close()
	f = open('voc.pickle', 'rb')
	voc = pickle.load(f)
	f.close()
	for i in range(len(test_doc)/10000):
	#for i in range(2):
		start = time.time()
		doc_temp = test_doc[10000*i:10000*(i+1)]
		idx_temp = test_idx[10000*i:10000*(i+1)]
		
		test_vec = TfidfVectorizer(vocabulary = voc)
		test_tf = test_vec.fit_transform(doc_temp).todense()
		num = 4
		pred, pred_prob = NB.predict(test_tf, model)
		prob_l, cls = NB.pred_list(model, pred_prob, num)
		threshold = -2.5
		showist = NB.show_tag(prob_l, cls, num, threshold)
		show_with_idx = zip(idx_temp, showist)
		
		f = open('show_with_idx' + str(i) + '.pickle', 'wb')
		f.write(pickle.dumps(show_with_idx))
		f.close()
		finish = time.time()
		print 'Turn ' + str(i) + ' has finished! Time: ' + str(finish - start) + '.\n'