__author__ = 'JohannWong'
import web
from configData import getConfig
def dbConnect():
    db = web.database(dbn=getConfig('db','dbname','str'),db=getConfig('db','dbservice','str'),user=getConfig('db','dbuser','str'),pw=getConfig('db','dbpwd','str'))
    return db

def dbSqliteConnect():
    db = web.database(dbn=getConfig('dbSqlite','dbname','str'),db=getConfig('dbSqlite','dbfile','str'))
    return db