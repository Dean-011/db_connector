from unicodedata import name
import mysql.connector
import datetime 
import time

def main():
    print("Connecting to db -  ")
    time.sleep(1)
    pbx_connect()



def pbx_connect():
    date = datetime.datetime.now()
    name=date
    hq_db = mysql.connector.connect(host='',user='',password='',database='',port='')

    mycursor = hq_db.cursor()
    mycursor.execute("SELECT *;")
    extensions = mycursor.fetchall()

    with open(f"{name}.txt", "a") as f:
        for extension in extensions:
            f.write(str(extension[0]))
            f.write('\n')

    mycursor.close()
