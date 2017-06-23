import numpy as np
import time
import pandas as pd
import pickle
from sklearn.feature_extraction.text import TfidfVectorizer,CountVectorizer
from sklearn.naive_bayes import MultinomialNB

def split_train(doc, label):
	label = np.array(label)
	doc = np.array(doc)
	idx = (label != '')
	tag = list(label[idx])
	train_doc = list(doc[idx])
	
	test_doc = list(doc[label == ''])
	return train_doc, test_doc, tag
	
	
#filename = 'stories_with_label.csv'
def doc_with_tab(filename):
	data = pd.read_csv(filename)
	doc = list(data['title'].values)
	temp_label = [t[1:-1] for t in data['label'].values]
	train_temp, test_doc, tag = split_train(doc, temp_label)
	
	label = []
	train_doc = []
	for i in range(len(tag)):
		c = tag[i].split(', ')
		sent = train_temp[i]
		if len(c) > 1:
			for j in range(len(c)):
				train_doc.append(sent)
				label.append(c[j])
		else:
			train_doc.append(sent)
			label.append(tag[i])
	
	return train_doc[:10000], test_doc[:10000], label[:10000]
	
def get_voc(train_doc, test_doc):
	train_vec=TfidfVectorizer(max_df = 0.95,min_df=2, stop_words='english')
	train_tf = train_vec.fit_transform(train_doc).todense()
	test_vec=TfidfVectorizer(vocabulary = train_vec.vocabulary_)
	test_tf = test_vec.fit_transform(test_doc).todense()
	temp = test_vec.vocabulary_
	dic = sorted(temp.items(), key=lambda d: d[1], reverse = True)[:30000]
	voc = dict(temp)
	f = open('train_tf1.pickle', 'wb')
	f.write(pickle.dumps(train_tf))
	f.close()
	print 'train_tf1.pickle\n'
	del train_vec, train_tf
	f = open('test_tf1.pickle', 'wb')
	f.write(pickle.dumps(test_tf))
	f.close()
	print 'test_tf1.pickle\n'
	del test_vec, test_tf
	f = open('voc.pickle', 'wb')
	f.write(pickle.dumps(voc))
	f.close()
	print str(len(voc)) + '\n'
	return voc
	
def get_feature(train_doc, test_doc):
	voc = get_voc(train_doc, test_doc)
	train_vec=TfidfVectorizer(max_df = 0.95, min_df=2, stop_words='english', vocabulary = voc)
	train_tf = train_vec.fit_transform(train_doc).todense()
	test_vec=TfidfVectorizer(vocabulary = train_vec.vocabulary_)
	test_tf = test_vec.fit_transform(test_doc).todense()
	
	f = open('train_tf2.pickle', 'wb')
	f.write(pickle.dumps(train_tf))
	f.close()
	f = open('test_tf2.pickle', 'wb')
	f.write(pickle.dumps(test_tf))
	f.close()
	return train_tf, test_tf
	
	
def train(train_doc, test_doc, tag):
	start = time.time()
	model=MultinomialNB(alpha=0.01)
	print "Getting the features...\n"
	train_feature, test_feature = get_feature(train_doc, test_doc)
	'''f = open('train_tf2.pickle', 'rb')
	train_feature = pickle.load(f)
	f.close()
	f = open('test_tf2.pickle', 'rb')
	test_feature = pickle.load(f)
	f.close()
	f = open('voc.pickle', 'rb')
	voc = pickle.load(f)
	f.close()'''
	print "The Training Start!\n"
	model.fit(train_feature, tag)
	end = time.time()
	print 'Time:\t' + str(end - start)
	print "The Training Finish!\n"
	return model, test_feature
	
def predict(test_feature, model):
	pred = model.predict(test_feature)
	pred_prob = model.predict_log_proba(test_feature)
	return pred, pred_prob	

def pred_list(model, pred_prob, num):
	cls = list(model.classes_)
	prob_l = []
	for i in range(len(pred_prob)):
		pair = zip(list(pred_prob[i]), range(len(cls)))
		re_pair = sorted(pair, reverse=True)
		prob_l.append(re_pair[:num])
	return prob_l, cls
	
def show_tag(prob_l, cls, num, threshold):
	showist = []
	cnt = []
	for i in range(len(prob_l)):
		temp = []
		for j in range(num):
			pair_prob = prob_l[i][j]
			if pair_prob[0] < threshold:
				if temp == []:
					temp.append('others')
				break
			else:
				temp.append(cls[pair_prob[1]])
		cnt = len(temp)
		temp.append(cnt)
		showist.append(temp)
	return showist
	
if __name__ == "__main__":
	filename = 'stories_with_label.csv'
	train_doc, test_doc, tag = doc_with_tab(filename)
	
	model, test_feature = train(train_doc, test_doc, tag)
	
	f = open('model.pickle', 'wb')
	f.write(pickle.dumps(model))
	f.close()
	
	num = 4
	pred, pred_prob = predict(test_feature, model)
	prob_l, cls = pred_list(model, pred_prob, num)
	
	threshold = -2.5
	showist = show_tag(prob_l, cls, num, threshold)

	f = open('showist.txt', 'w')
	for i in range(len(showist)):
		f.write(test_doc[i] + '\t' + str(showist[i]))
		f.write('\n')
	f.close()
	
	f = open('showist.pickle', 'wb')
	f.write(pickle.dumps(test_doc))
	f.write(pickle.dumps(showist))
	f.close()
	
	