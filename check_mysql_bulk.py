#!/usr/bin/env python
import MySQLdb
import os
import argparse
from datetime import datetime

parser = argparse.ArgumentParser()
parser.add_argument('database')
parser.add_argument('-q','--query')
parser.add_argument('--options', nargs='+')
args = parser.parse_args()
options = args.options

if options is None:
    options = ["empty","empty"]

try:
    test=options[1]
except IndexError:
    options.append("empty")

DB_USER = 'DATABASE_USERNAME'
DB_PASS = 'DATABASE_PASSWORD'
DB_HOST = str(args.database)

def queryFromArgs(query):
    switcher = {
        "globalStatus": "SHOW GLOBAL STATUS",
        "globalVariables": "SHOW GLOBAL VARIABLES",
    }
    return switcher.get(query, "nothing")

if args.query == "globalStatus":
    itemKey = "mysql.status"
if args.query == "globalVariables":
    itemKey = "mysql.variable"

class DB:
  conn = None

  def connect(self):
    self.conn = MySQLdb.connect(host=DB_HOST,user=DB_USER, passwd=DB_PASS)

  def query(self, sql):
    try:
     cursor = self.conn.cursor()
     cursor.execute(sql)
    except (AttributeError, MySQLdb.OperationalError):
     self.connect()
     cursor = self.conn.cursor()
     cursor.execute(sql)
    return cursor

db = DB()
queryString = str(queryFromArgs(args.query))
queryResult = db.query(queryString)
for row in queryResult:
    if str(row[1]) != "":
        print '"'+ DB_HOST +'" "'+ itemKey +'['+ str(row[0]) +']" "'+ str(row[1]) +'"'
