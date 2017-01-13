import MySQLdb

if __name__ == '__main__':
	db = MySQLdb.connect(
	    host='localhost',
	    user='mary',
	    passwd='123mary123',
	    db='lab6',
	    charset='utf8'
	)
	
	cur = db.cursor()
	
	cur.execute("INSERT INTO lab6_lesson (name,description) VALUES (%s, %s);", ('Математика','Подготовим к ЕГЭ'))
	
	db.commit()
	
	cur.execute("SELECT * FROM lab6_lesson;")
	
	entries = cur.fetchall()
	
	for e in entries:
		print(e)
	
	cur.close()
	db.close()
