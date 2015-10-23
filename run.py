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
	(db, cursor) = connectdb()
	cursor.execute('select * from taxi order by timezone asc')
	taxi = cursor.fetchall()
	taxi = json.dumps(taxi)
	return render_template('mecro.html', taxi=taxi)

@app.route('/evacuate')
def evacuate():
	return render_template('evacuate.html')

@app.route('/traffic', methods=['POST'])
def traffic():
	data = request.form
	name = data['name']
	(db, cursor) = connectdb()
	cursor.execute('select * from subway_traffic where name=%s order by date asc', [name])
	traffic = cursor.fetchall()
	closedb(db, cursor)
	return json.dumps({"traffic": traffic})

if __name__ == '__main__':
	app.run(debug=True)