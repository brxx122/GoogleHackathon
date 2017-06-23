from flask import Flask
import MySQLdb

try:
    conn = MySQLdb.connect(host='localhost',user='root',passwd='hu19980209',db='hackathon',port=3306)
except MySQLdb.Error,e:
    print "Mysql Error %d: %s" % (e.args[0], e.args[1])

app = Flask(__name__)
from app import views
