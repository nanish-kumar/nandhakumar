#install the following packages fastapi uvicorn sqlalchemy sqlite
from datetime import date
from fastapi import FastAPI, Depends
import sqlite3
from sqlite3 import Error
 
app = FastAPI()
DB = "./phonebook.db"
def create_connection():
 conn = None
 try:
  conn = sqlite3.connect(DB)
 except Error as e:
  print(e)
 return conn
def create_table():
 conn = create_connection()
 if conn is not None:
  try:
   query = """CREATE TABLE IF NOT EXISTS phonebook (id INTEGER PRIMARY KEY AUTOINCREMENT,name TEXT NOT NULL,number TEXT NOT NULL);"""
   conn.ececute(query)
   conn.commit()
  except Error as e:
    print(e)
  finally:
   conn.close()
 
# can put the below to the fastapi lifespan function
create_table()
 
def get_db():
 conn = create_connection()
 try: 
  yield conn
 except:
  pass
 finally:
  conn.close()
 
@app.post("/phonebook")
def create(name:str, number:str,db = Depends(get_db)):
 cursor = db.cursor()
 cursor.execute("insert into phonebook (name,number) values (?,?)",(name,number))
 db.commit()
 id = cursor.lastrowid
 return {"id":id}
 
@app.get("/phonebook/{id}")
def get(id:int,db = Depends(get_db)):
 cursor = db.cursor()
 cursor.exrecute("select * from phonebook where id=?",(id,))
 res = cursor.fetchone()
 return {date:res}
 
@app.put("/phonebook/{id}")
def update(id:int,name:str,number:str,db=Depends(get_db)):
 cursor = db.cursor()
 cursor.exrecute("select * from phonebook where id=?",(id,))
 res = cursor.fetchone()
 if res:
  cursor.execute("update phonebook set name=?, number=? where id=?",name,number,id)
  db.commit()
def update_status(successful):
    if successful:
        msg = "Update Successful"
    else:
        msg = "Update not Successful, record may not be present"
    return {"msg": msg}
@app.delete("/phonebook/{id}")
def delete(id:int,db = Depends(get_db)):
 cursor = db.cursor()
 cursor.exrecute("select * from phonebook where id=?",(id,))
 res = cursor.fetchone()
 if res:
  cursor.execute("delete from phonebook where id=?",(id,))
  db.commit()
def delete_status(deleted):
    if deleted:
        msg = "Deleted"
    else:
        msg = "Not deleted, record may not be present"
    return {"msg": msg}

#to run the server use the below command
# uvicorn main:app
