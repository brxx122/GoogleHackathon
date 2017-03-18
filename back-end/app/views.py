from app import app
from flask import Flask, render_template, session, request, redirect, flash, g,url_for,jsonify

@app.route('/')
def Login():
    return render_template('index.html')


@app.route('/_hhh', methods=["POST", "GET"])
def hhh():
    dict = {'a': 1, 'b': 2}
    return jsonify(dict)


@app.route('/_he', methods=["POST", "GET"])
def he():
    path = url_for('static', filename='image/1.jpeg')
    dic = {"name": path}
    return jsonify(dic)

