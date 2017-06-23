import pickle
import numpy as np
import singlecloud as cloud
import sentiment as senti
from wordcloud import *
import matplotlib.pyplot as plt
from scipy.misc import imread

def generate_img(tag, img_name, back_image, blkcolor):
	data = ' '.join(tag)
	# im = Image.open("01.png")
	# Lim = im.convert('L')
	# Lim.save("01_grey.png")
	mask_img = imread(back_image, flatten=True)
	wordcloud = WordCloud(font_path='msyh.ttc',background_color=blkcolor,mask=mask_img).generate(data)
	plt.imshow(wordcloud)
	plt.axis('off')
	plt.savefig(img_name, dpi=600)

# pic_name = "Marry"
# tag = ['Google', 'Apple', 'Google']
def person_tag(pic_name, type, tag):
	if type == 'like':
		generate_img(tag, './static/' + pic_name + '_like', './static/03.jpg', '#ebebeb')
	else:
		generate_img(tag, './static/' + pic_name + '_hate', './static/06.jpg', '#8e8e8e')

# username = "Marry"
# comments = ['Ok!', 'No!']
# comments_idx = [112423,342123]
## return comments_idx -- parent_dix -- tag  	
def person_prefer_pred(cid, content, tag):
	#f = open('./static/data/model_senti.pickle', 'rb')
	f = open('model_senti.pickle', 'rb')
	model = pickle.load(f)
	f.close()
	#f = open('./static/data/voc_senti.pickle', 'rb')
	f = open('voc_senti.pickle', 'rb')
	voc = pickle.load(f)
	f.close()
	
	like_idx, hate_idx = senti.pred(cid, content, model, voc)
	like_tag = []
	hate_tag = []
	for i in like_idx:
		like_tag.append(tag[i])
	for i in hate_idx:
		hate_tag.append(tag[i])
	return like_tag, hate_tag

# user = "Marry"
# like_tag, hate_tag
def person_prefer_tag(username, like_tag, hate_tag):
	person_tag(username, 'like', like_tag)
	person_tag(username, 'hate', hate_tag)
	
def user2tag(username):
	cur = conn.cursor()
	cur.execute('select cid, label, content from comments, stories where comments=stories and author = ? ;', [username])
	data = cur.fetchall()
	cid = []
	tag = []
	content = []
	for i in range(len(data)):
		cid.append(data[i][0])
		content.append(data[i][2])
		tag.extend(data[i][1][2:-2].split(','))
	return cid, content, tag
	
def tag_most_pupolar(tag):
	tag_story = []
	for i in tag:
		cur = conn.cursor()
		cur.execute('select sid, title, url, count from stories where tag like ? ;', ['%'+tag+'%'])
		data = cur.fetchall()
		level = []
		for j in range(len(data)):
			level.append(data[j][0])
		tag_story.extend(level)
	pair_sort = sorted(tag_story, key=lambda d: d[3], reverse=True)
	
	result = []
	for item in tag_story[:10]:
		subresult = {}
		subresult['title'] = item[1]
		subresult['url']= item[2]
		subresult = json.dumps(subresult)
		result.append(subresult)
	cur.close()
	return jsonify(result)
		
	
		
	
	
	
	
