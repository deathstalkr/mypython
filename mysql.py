import pymysql as sql
con= sql.connect(user='solomon',passwd='azsxdcfv',host='localhost',database='maria')
sql_lang=con.cursor()
'''
sql_lang.execute('show databases;')
sql_lang.fetchall()
sql_lang.execute('show tables')
sql_lang.
'''
sql_lang.execute('insert into cumberpatch (name,email_id,gender) values("Croiden","croiden@adhoc.org","male")')
con.commit()
con.close()
