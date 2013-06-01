__author__ = 'JohannWong'
#coding=UTF-8
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
    """
    获取pymssql的数据库连接
    """
    db = pymssql.connect(host=getConfig('dbMSSql','dbhost','str'),user=getConfig('dbMSSql','dbuser','str'),password=getConfig('dbMSSql','dbpwd','str'),database=getConfig('dbMSSql','db','str'), as_dict=True)
    return db

def msSqlConnectutf():
    """
    获取pymssql的数据库连接
    """
    db = pymssql.connect(host=getConfig('dbMSSql','dbhost','str'),user=getConfig('dbMSSql','dbuser','str'),password=getConfig('dbMSSql','dbpwd','str'),database=getConfig('dbMSSql','db','str'), as_dict=True,charset='utf8')
    return db