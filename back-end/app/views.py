from app import app, conn
from flask import Flask, render_template, url_for,jsonify

@app.route('/')
def Login():
    return render_template('index.html')

@app.route('/_return_news_by_year')
def return_news_by_year(year, index):
    cur = conn.cursor()
    cur.execute('select * from stories limit 10;')
    data = cur.fetchall()
    result = []
    for i in range(10):
        subresult = {}
        subresult['author'] = data[i][1]
        subresult['title'] = data[i][4]
        subresult['time'] = data[i][3][:10]
        subresult['url'] = data[i][5]
        result.append(subresult)
    return jsonify(result)


@app.route('/_he', methods=["POST", "GET"])
def he():
    path = url_for('static', filename='image/1.jpeg')
    dic = {"name": path}
    return jsonify(dic)

