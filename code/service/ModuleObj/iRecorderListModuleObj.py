__author__ = 'JohannWong'
#coding=UTF-8
import traceback
from dbConnection import dbConnect
from logHelper import getLogger
"""

"""
class iRecorderListModuleObj:
    def getiRecorderListByFileName(self,filename):
        try:
            logger = getLogger()
            logger.debug("start iRecorderListModuleObj.getiRecorderListByFileName")
            dbConn = dbConnect()
            sql = """SELECT [HOSTNAME]
                ,[FILENAME]
                ,[CHANNELNO]
                ,[STARTTIME]
                ,[SPENDTIME]
                ,[AVAILABLE]
                ,[AGENTID]
                ,[FILEPATH]
                ,[CHANNELDN]
                ,[CALLTYPE]
                ,[TELNO]
                ,[TELDNIS]
                ,[CALLID]
                ,[ENDTIME]
                ,[TRQ_SCORE].[TOTAL]
            FROM [T_RECORDER]
            LEFT JOIN [TRQ_SCORE]
            ON [T_RECORDER].[FILENAME] = [TRQ_SCORE].[RECKEY]
            WHERE [T_RECORDER].[FILENAME] = '"""+filename+"""'
            """
            iRecorderDicList = dbConn.query(sql)
            return iRecorderDicList
        except :
            logger.error("exception occur, see the traceback.log")
            #异常写入日志文件.
            f = open('Logs/traceback.txt','a')
            traceback.print_exc()
            traceback.print_exc(file = f)
            f.flush()
            f.close()
        else:
            pass
        finally:
            return None

    def getiRecorderListByParams(self,params):
        try:
            logger = getLogger()
            logger.debug("start iRecorderListModuleObj.getiRecorderListByFileName")
            dbConn = dbConnect()
            sql = """SELECT [HOSTNAME]
                ,[FILENAME]
                ,[CHANNELNO]
                ,[STARTTIME]
                ,[SPENDTIME]
                ,[AVAILABLE]
                ,[AGENTID]
                ,[FILEPATH]
                ,[CHANNELDN]
                ,[CALLTYPE]
                ,[TELNO]
                ,[TELDNIS]
                ,[CALLID]
                ,[ENDTIME]
                ,[TRQ_SCORE].[TOTAL]
            FROM [T_RECORDER]
            LEFT JOIN [TRQ_SCORE]
            ON [T_RECORDER].[FILENAME] = [TRQ_SCORE].[RECKEY]
            WHERE 1=1"""
            if params["startdate"] != None:
                sql += " AND [T_RECORDER].[STARTTIME] >= "+params["startdate"]
            if params["enddate"] != None:
                sql += " AND [T_RECORDER].[STARTTIME] <= "+params["enddate"]
            if params["calltype"] != None:
                sql += " AND [T_RECORDER].[CALLTYPE] = "+params["calltype"]
            if params["agentid"] != None:
                sql += " AND [T_RECORDER].[AGENTID] = "+params["agentid"]
            if params["telno"] != None:
                sql += " AND [T_RECORDER].[TELNO] = "+params["telno"]
            if params["available"] != None:
                sql += " AND [T_RECORDER].[AVAILABLE] = "+params["available"]
            if params["totalmin"] != None:
                sql += " AND [TRQ_SCORE].[TOTAL] >= "+params["totalmin"]
            if params["totalmax"] != None:
                sql += " AND [TRQ_SCORE].[TOTAL] <= "+params["totalmax"]
            if params["channeldn"] != None:
                sql += " AND [T_RECORDER].[CHANNELDN] = "+params["channeldn"]
            if params["teldnis"] != None:
                sql += " AND [T_RECORDER].[TELDNIS] = "+params["teldnis"]
            iRecorderDicList = dbConn.query(sql)
            return iRecorderDicList
        except :
            logger.error("exception occur, see the traceback.log")
            #异常写入日志文件.
            f = open('Logs/traceback.txt','a')
            traceback.print_exc()
            traceback.print_exc(file = f)
            f.flush()
            f.close()
        else:
            pass
        finally:
            return None
