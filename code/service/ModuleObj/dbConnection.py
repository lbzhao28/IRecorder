__author__ = 'JohannWong'
import web
import pymssql
from configData import getConfig
def dbConnect():
    db = web.database(dbn=getConfig('db','dbname','str'),db=getConfig('db','dbservice','str'),user=getConfig('db','dbuser','str'),pw=getConfig('db','dbpwd','str'))
    return db

def dbSqliteConnect():
    db = web.database(dbn=getConfig('dbSqlite','dbname','str'),db=getConfig('dbSqlite','dbfile','str'))
    return db

def dbMSSqlConnect():
    db = web.database(dbn=getConfig('dbMSSql','dbname','str'),host=getConfig('dbMSSql','dbhost','str'),db=getConfig('dbMSSql','db','str'),user=getConfig('dbMSSql','dbuser','str'),pw=getConfig('dbMSSql','dbpwd','str'))
    return db

def msSqlConnect():
    db = pymssql.connect(host=getConfig('dbMSSql','dbhost','str'),user=getConfig('dbMSSql','dbuser','str'),password=getConfig('dbMSSql','dbpwd','str'),database=getConfig('dbMSSql','db','str'),charset = "utf8", as_dict=True)
    return db