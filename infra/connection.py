from infra.config import config ,url
import mysql.connector
from mysql.connector.cursor import MySQLCursor
from mysql.connector import errorcode
from sqlalchemy import create_engine
from sqlalchemy.exc import SQLAlchemyError


class Database():

  def __init__(self):
    self.connect()
    self.raw_connect()
    self.connect_engine()

  def connect(self):
    try:
      self.cnx = mysql.connector.connect(**config)
      print("Connection succefully established")
    except mysql.connector.Error as err:
      if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("Something is wrong with your user name or password")
      elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("Database does not exist")
      else:
        print(err)
  def connect_engine(self):
    try:
      self.encnx = create_engine(url)
      print("Engine succefully generated")
    except SQLAlchemyError as err:
      error = str(err._dict_['orig'])
      return error

  def raw_connect(self):
    try:
      self.cnx2 = mysql.connector.connect(**config, raw=True)
      print("Raw_Connection succefully established")
    except mysql.connector.Error as err:
      if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("Something is wrong with your user name or password")
      elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("Database does not exist")
      else:
        print(err)
    except mysql.connector.Error as err:
      if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("Something is wrong with your user name or password")
      elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("Database does not exist")
      else:
        print(err)      

  def close(self):
       self.cnx.close()
       self.cnx2.close() 