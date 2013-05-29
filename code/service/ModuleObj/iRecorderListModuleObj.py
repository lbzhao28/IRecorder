__author__ = 'JohannWong'
#coding=UTF-8
import traceback
from dbConnection import msSqlConnect
from logHelper import getLogger
class iRecorderListModuleObj:
    """

    """
    def getiRecorderListByFileName(self,filename):
        try:
            logger = getLogger()
            logger.debug("start iRecorderListModuleObj.getiRecorderListByFileName")
            conn = msSqlConnect()
            cur = conn.cursor()
            sqlstr = "SELECT [HOSTNAME]"\
            ",[FILENAME]"\
            ",[CHANNELNO]"\
            ",[STARTTIME]"\
            ",[SPENDTIME]"\
            ",[AVAILABLE]"\
            ",[AGENTID]"\
            ",[FILEPATH]"\
            ",[CHANNELDN]"\
            ",[CALLTYPE]"\
            ",[TELNO]"\
            ",[TELDNIS]"\
            ",[CALLID]"\
            ",[ENDTIME]"\
            ",[TRQ_SCORE].[TOTAL]"\
            " FROM [T_RECORDER]"\
            " LEFT JOIN [TRQ_SCORE]"\
            " ON [T_RECORDER].[FILENAME] = [TRQ_SCORE].[RECKEY]"\
            " WHERE [T_RECORDER].[FILENAME] = %s"
            cur.execute(sqlstr,filename)
            result = []
            for row in cur:
                result.append(row)
            return result
        except :
            logger.error("exception occur, see the traceback.log")
            #异常写入日志文件.
            f = open('Logs/traceback.txt','a')
            traceback.print_exc()
            traceback.print_exc(file = f)
            f.flush()
            f.close()
            return None
        else:
            return None
        finally:
            conn.close()

    def getiRecorderListByParams(self,params):
        try:
            logger = getLogger()
            logger.debug("start iRecorderListModuleObj.getiRecorderListByParams")
            conn = msSqlConnect()
            cur = conn.cursor()
            if "pageno" in params.keys() and params["pageno"] is not None:
                pageNo = int(params["pageno"])
            else:
                pageNo = 1
            if "pagesize" in params.keys() and params["pagesize"] is not None:
                pageSize = int(params["pagesize"])
            else:
                pageSize = 10
            startIndex = (pageNo-1)*pageSize+1
            endIndex = pageNo*pageSize
            sqlstr = "SELECT * FROM ("\
                 "SELECT row_number()over(order by getdate())ROWNUMBER"\
                 ",[HOSTNAME]"\
                 ",[FILENAME]"\
                 ",[CHANNELNO]"\
                 ",[STARTTIME]"\
                 ",[SPENDTIME]"\
                 ",[AVAILABLE]"\
                 ",[AGENTID]"\
                 ",[FILEPATH]"\
                 ",[CHANNELDN]"\
                 ",[CALLTYPE]"\
                 ",[TELNO]"\
                 ",[TELDNIS]"\
                 ",[CALLID]"\
                 ",[ENDTIME]"\
                 ",[TRQ_SCORE].[TOTAL]"\
                 " FROM [T_RECORDER]"\
                 " LEFT JOIN [TRQ_SCORE]"\
                 " ON [T_RECORDER].[FILENAME] = [TRQ_SCORE].[RECKEY]"\
                 " WHERE 1=1"
            if "startdate" in params.keys() and params["startdate"] is not None:
                sqlstr += " AND [T_RECORDER].[STARTTIME] >= '"+params["startdate"]+"'"
            if "enddate" in params.keys() and params["enddate"] is not None:
                sqlstr += " AND [T_RECORDER].[STARTTIME] <= '"+params["enddate"]+"'"
            if "calltype" in params.keys() and params["calltype"] is not None:
                sqlstr += " AND [T_RECORDER].[CALLTYPE] = '"+params["calltype"]+"'"
            if "agentid" in params.keys() and params["agentid"] is not None:
                sqlstr += " AND [T_RECORDER].[AGENTID] = '"+params["agentid"]+"'"
            if "telno" in params.keys() and params["telno"] is not None:
                sqlstr += " AND [T_RECORDER].[TELNO] = '"+params["telno"]+"'"
            if "available" in params.keys() and params["available"] is not None:
                sqlstr += " AND [T_RECORDER].[AVAILABLE] = '"+params["available"]+"'"
            if "totalmin" in params.keys() and params["totalmin"] is not None:
                sqlstr += " AND [TRQ_SCORE].[TOTAL] >= '"+params["totalmin"]+"'"
            if "totalmax" in params.keys() and params["totalmax"] is not None:
                sqlstr += " AND [TRQ_SCORE].[TOTAL] <= '"+params["totalmax"]+"'"
            if "channeldn" in params.keys() and params["channeldn"] is not None:
                sqlstr += " AND [T_RECORDER].[CHANNELDN] = '"+params["channeldn"]+"'"
            if "teldnis" in params.keys() and params["teldnis"] is not None:
                sqlstr += " AND [T_RECORDER].[TELDNIS] = '"+params["teldnis"]+"'"
            sqlstr += ")t"\
                      " WHERE ROWNUMBER BETWEEN "+str(startIndex)+\
                      " AND "+str(endIndex)
            cur.execute(sqlstr)
            result = []
            for row in cur:
                result.append(row)
            return result
        except :
            logger.error("exception occur, see the traceback.log")
            #异常写入日志文件.
            f = open('Logs/traceback.txt','a')
            traceback.print_exc()
            traceback.print_exc(file = f)
            f.flush()
            f.close()
            return None
        else:
            return None
        finally:
            conn.close()
