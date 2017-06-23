from app import app, conn
from flask import Flask, render_template, url_for,jsonify

# copylaravel, post, personal, bigdata

@app.route('/')
def Login():
    return render_template('copylaravel.html')

@app.route('/_return_news_by_year', methods=["POST", "GET"])
def return_news_by_year():
	year = request.form.get('year')
	index = request.form.get('index')
    cur = conn.cursor()
    cur.execute('select * from stories where time_ts contains %s;', year)
    data = cur.fetchall()
    result = []
    for i in range(12*i, 12*(i+1)):
        subresult = {}
        subresult['author'] = data[i][1]
        subresult['title'] = data[i][4]
        subresult['time'] = data[i][3][:10]
        subresult['url'] = data[i][5]
		subresult = json.dumps(subresult)
        result.append(subresult)
    return jsonify(result)
	
@app.route('/_return_news_by_tag', methods=["POST", "GET"])
def return_news_by_tag():
	tag = request.form.get('tag')
	cur = conn.cursor()
    cur.execute('select * from stories where tag contains ? limit 12;', [tag])
    data = cur.fetchall()
	
	
@app.route('/_return_most_comments', methods=["POST", "GET"])
def return_most_comments():
	title = request.form.get('title')
	
    result = []
    for i in range(12*i, 12*(i+1)):
        subresult = {}
        subresult['author'] = data[i][1]
        subresult['title'] = data[i][4]
        subresult['time'] = data[i][3][:10]
        subresult['url'] = data[i][5]
		subresult = json.dumps(subresult)
        result.append(subresult)
    return jsonify(result)

@app.route('/_return_post_info', methods=["POST", "GET"])
def return_post_info():
	title = request.form.get('title')
	cur = conn.cursor()
    #cur.execute('select sid, author, url, time_ts, tag from stories where title = ? ;', [title])
    story = cur.fetchall()
	cur = conn.cursor()
    #cur.execute('select comments.author, comments.time comments.text where title = ? and select * from stories, comments where stories.sid = ? and stories.sid = comments.father, [title])
    comment = cur.fetchall()
	cur = conn.cursor()
    #cur.execute('select title from stories where tag contain ? limit 10;', [tag])
    recommand = cur.fetchall()
	
	result = []
	storyresult = {}
	storyresult['sid'] = story[0][0]
	storyresult['author'] = story[0][1]
	storyresult['url'] = story[0][2]
	storyresult['time'] = story[0][3]
	storyresult['tag'] = story[0][4]
	storyresult = json.dumps(storyresult)
	result.append(subreault)
	
	comment_result = []
	for i in range(len(comment)):
		subresult = {}
		subresult['comment_author'] = comment[i][0]
		subresult['comments_time'] = comment[i][1]
		subresult['comments_text'] = comment[i][2]
		subresult = json.dumps(subresult)
		comment_result.append(subreault)
	comment_result = json.dumps(comment_result)
	result.append(comment_result)
	
	recommand_result = []
	for i in range(len(recommand)):
		recommand_result.append(recommend[i][0])
	recommand_result = json.dumps(recommand_result)
	result.append(recommand_result)
	return jsonify(result)
	
	
@app.route('/personal')
def personal_page():
	return render_template('personal.html')	
	
@app.route('/bigdata')
def bigdata_page():
	return render_template('bigdata.html')

@app.route('/_he', methods=["POST", "GET"])
def he():
    path = url_for('static', filename='image/1.jpeg')
    dic = {"name": path}
    return jsonify(dic)


