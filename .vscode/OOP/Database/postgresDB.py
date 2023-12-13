
'''

Class 27

python connector for postgreql

https://www.postgresqltutorial.com/postgresql-getting-started/install-postgresql/


https://www.postgresqltutorial.com/postgresql-getting-started/install-postgresql/
 for install postgres
 for mysql


https://www.mysqltutorial.org/getting-started-with-mysql/
pip3 install psycopg2

[8:02 am, 28/09/2023] +1 (267) 808-9569: if using MAC then try this and if it doestn work
[8:02 am, 28/09/2023] +1 (267) 808-9569: then try this
[8:02 am, 28/09/2023] +1 (267) 808-9569: pip3 install psycopg2-binary
[8:33 am, 28/09/2023] +1 (267) 808-9569: pyodbc
https://docs.djangoproject.com/en/stable/
pip install Django

https://docs.djangoproject.com/en/4.2/
[8:42 am, 28/09/2023] +1 (267) 808-9569: make sure u r ready guys with the project related stuff
[8:42 am, 28/09/2023] +1 (267) 808-9569: DataBASE

while installing dont uncheck pgadmin4
stack builder already unchecked its ok

use try to download workbench

first project:

firstdjango	project login name
password	: admin123

python -c "import psycopg2; print(psycopg2.__version__)"
2.9.9 (dt dec pq3 ext lo64)

Check if it is working or not. Do it simply by importing psycopg2 library and checking its version. Open the command prompt and put the command given below. Showing no error means our package is successfully installed.

python -c "import psycopg2; print(psycopg2.__version__)"

since tables are created using python not with sql, we use conenctor.

WE EXECUte query using the connector
All the way we are verifying in to database

django details
https://pypi.org/project/Django/
https://docs.djangoproject.com/en/stable/
instead of this all database handling we do using django
pyodbc  is also support python connector instead of pyscopg2
'''
import psycopg2 
#step 1: open a connection

connection=psycopg2.connect(dbname='firstdb',user='firstdjango',password='admin123')

db_pointer=connection.cursor()
# SQL_QUERY='''
#         CREATE TABLE PERSON(
#         ID INT PRIMARY KEY NOT NULL,
#         NAME TEXT NOT NULL,
#         AGE INT NOT NULL,
#         ADDRESS CHAR(50),
#         INCOME REAL
#         )
# '''
# # db_pointer.execute(SQL_QUERY)
# # connection.commit()
# # print("Table is created successfully")

# #insert the data in to DB table
# connection.close()

# SQL_QUERY='''
#     INSERT INTO PERSON(ID,NAME,AGE,ADDRESS,INCOME) 
#       VALUES(1002,'VIJAY',42,'INDIA',450)
# '''
# db_pointer.execute(SQL_QUERY)

SQL_QUERY='''
    SELECT * FROM PERSON
'''
db_pointer.execute(SQL_QUERY)
records=db_pointer.fetchall()       # we can use fetchone or fetchmany if given number fetches row
for record in records:
    print(record)

SQL_QUERY='''
    UPDATE PERSON set ADDRESS='TX' where ID in (1002)
'''
db_pointer.execute(SQL_QUERY)
connection.commit()
connection.close()