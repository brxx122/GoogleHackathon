import codecs
import nltk
import numpy as np
import time
import pandas as pd
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import TfidfVectorizer,CountVectorizer
from sklearn.naive_bayes import MultinomialNB
#filename = 'temp.txt'
def document(filename):
	input = codecs.open(filename, 'rb', encoding='utf8')
	raw = [l.strip() for l in input.readlines()]
	input.close()
	return raw

'''
def document(filename):
	data = pd.read_csv(filename)
	raw = list(data['title'].values)
	return doc
'''
def tag_sents(sents):
	start = time.time()
	tagged_sents = []
	for s in sents:
		text = nltk.word_tokenize(s)
		tagged_sents.append(nltk.pos_tag(text))
	end = time.time()
	print 'Time:\t' + str(end - start)
	return tagged_sents
'''
def tag_words(tagged_sent):
	tagged_words = []
	for s in tagged_sent:
		tagged_words.append(s)
	return tagged_words
'''

def str_n(tagged_words):
	N = [w for (w, t) in tagged_words if t.startswith('N')]
	return ' '.join(N)

	
def remove_url(s, remove_list):
	s = s.split(' ')

	def erase(x):
		for keyword in remove_list:
			if keyword in x:
				return True
		return False

	cleaned = np.array(map(erase, s))
	return ' '.join(np.array(s)[~cleaned])
	
def remove(doc):
	r = ['http', 'rel', '\u', 'href', '---', '\n', '|']
	clean = []
	for i in range(len(doc)):
		clean.append(remove_url(doc[i], r))
	tagged_sents = tag_sents(clean)
	nstr = []
	for i in range(len(tagged_sents)):
		nstr.append(str_n(tagged_sents[i]))
	return nstr
	
def tfidf_create(documents):
	vector=TfidfVectorizer(max_df = 0.5,stop_words='english')
	vector.fit_transform(documents).todense()
	tfidf = vector.fit_transform(documents).todense()
	voc = vector.vocabulary_
	#vector.vocabulary_
	return tfidf, voc

def tfidf_most(tfidf, voc):
	most = []
	dict = sorted(voc.items(), key=lambda d: d[1])
	for i in range(tfidf.shape[0]):
		temp = tfidf[i].tolist()
		freq = [w for w in temp[0]]
		pair = zip(freq, range(len(freq)))
		most.append(sorted(pair, reverse=True))
	return most, dict
	
def keyword(most, dict, threshold):
	key = []
	for i in range(len(most)):
		key.append([dict[j] for (_,j) in most[i][:threshold]])
	return key
	
def story_key(doc, threshold):
	nstr = remove(doc)
	tfidf, voc = tfidf_create(doc)
	most, dict = tfidf_most(tfidf, voc)
	key = keyword(most, dict, threshold)
	return key
	
def create_voc(most, dict, threshold):
	idx = []
	voc = []
	for i in range(tfidf.shape[0]):
		idx.extend([id for (w, id) in most[i][:threshold]])
	idx = set(idx)
	for id in idx:
		voc.append(dict[id][0])
	return voc
	
def show_tag(doc, key, num, cnt):
	pair_key = []
	for i in range(len(doc)):
		keylist = []
		keylist = [w for (w, t) in key[i][:num]]
		pair_key.append([doc[i], keylist])
	for i in range(cnt):
		print pair_key[i]
		print '\n'
	return pair_key
	
	
	
	