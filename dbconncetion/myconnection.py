import pymysql
conn=pymysql.connect(host="localhost", user="root", password="atul123@", db="coders_kitchen")
mycur=conn.cursor()