# coding:utf-8

import sys
reload(sys)
sys.setdefaultencoding( "utf-8" )
from flask import *
import MySQLdb
import MySQLdb.cursors
import warnings
warnings.filterwarnings("ignore")
from config import *

app = Flask(__name__)
app.config.from_object(__name__)

def connectdb():
	db = MySQLdb.connect(host=HOST, user=USER, passwd=PASSWORD, db=DATABASE, port=PORT, charset=CHARSET, cursorclass = MySQLdb.cursors.DictCursor)
	db.autocommit(True)
	cursor = db.cursor()
	return (db,cursor)

# 关闭数据库
def closedb(db,cursor):
	db.close()
	cursor.close()

@app.route('/')
def macro():
	return render_template('macro.html')

@app.route('/micro')
def micro():
	return render_template('micro.html')

@app.route('/mecro')
def mecro():
	return render_template('mecro.html')

if __name__ == '__main__':
	app.run(debug=True)