#!/usr/bin/python3
import pymysql

#link to database
db=pymysql.connect(host='localhost',user='root',password='cuicyz1996',db='miniproject3',port=33060,unix_socket="/tmp/mysql.sock")
cur=db.cursor()   

#see whole table
sql="select * from information"
try:
	cur.execute(sql) 	#run sql sentence
	results = cur.fetchall()	#fetch all results
	print('The whole table is:')
	print(results)
	print('\n')
except Exception as e:
	raise e

#search for certain words
sql="select * from information where keyword='Food'"  #write sql sentence
try:
	cur.execute(sql) 	#run sql sentence
	results = cur.fetchall()	#fetch all results
	print('Information where keyword=food:')
	print(results)
	print('\n')
except Exception as e:
	raise e


#see number of images per feed
sql="select * from information"
a=0
try:
	cur.execute(sql) 	
	results = cur.fetchall()
	print('See how many pictures from different users:')
	for row in results :
		id = row[0]
		username = row[1]
		keyword = row[2]
		number_of_pictures = row[3]
		print(id,username,keyword,number_of_pictures)
		a+=number_of_pictures
	number_of_row=row[0]
	print('the average number of images per feed:',a/number_of_row)
	print('\n')
except Exception as e:
	raise e


#see most popular descriptors
sql="select keyword,count(*) as count from information group by keyword order by count desc"
try:
	cur.execute(sql) 	
	results = cur.fetchall()
	print('See most popular description:')
	print(results)

except Exception as e:
	raise e
finally:
	db.close()