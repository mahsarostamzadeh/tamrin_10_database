#Pyhon-sql

import sqlite3

#connecting

db = sqlite3.connect('amiralidb my first project.db')

cursor = db.cursor()

#create table

cursor.execute("CREATE TABLE  alitable books(id INTEGER PRIMARY KEY,name TEXT, price INTEGER , count INTEGER)")



#insert

                        #basic
id='1'
name = 'aprtement'
price ='800'
count='1'



cursor.execute(''' INSERT INTO books(id,name, price,count) VALUES(?,?) ''' ,
               (id,name,price,count))
db.commit()



#update

pr1='300'
pr2='40'
pr3='200'
id1='1'
id2='2'
id3='3'
cursor.execute('''UPDATE books SET title = ? WHERE id = ?''',(pr1 ,id1))
cursor.execute('''UPDATE books SET title = ? WHERE id = ?''',(pr2 ,id2))
cursor.execute('''UPDATE books SET title = ? WHERE id = ?''',(pr3 ,id3))


#delete
cursor.execute('''DELETE FROM books WHERE id = ?''',(id1))
cursor.execute('''SELECT name, pricr FROM alitable''')
print(cursor.fetchall())

cursor.execute('''DELETE FROM books WHERE id = ?''',(id2))
cursor.execute('''SELECT name, pricr FROM alitable''')
print(cursor.fetchall())



id='2'
name = 'chash'
price ='40'
count='22500'



cursor.execute(''' INSERT INTO books(id,name, price,count) VALUES(?,?) ''' ,
               (id,name,price,count))
db.commit()



#update
pr2='280'
id2='2'
cursor.execute('''UPDATE books SET title = ? WHERE id = ?''',(pr2 ,id2))


#insert

                        #basic
id='3'
name = 'eos'
price ='40'
count='5'

id5='4'
name5 = 'eth'
price5 ='60'
count5='7'




cursor.execute(''' INSERT INTO books(id,name, price,count) VALUES(?,?) ''' ,
               (id5,name5,price5,count5))

cursor.execute(''' INSERT INTO books(id,name, price,count) VALUES(?,?) ''' ,
               (id,name,price,count))
db.commit()