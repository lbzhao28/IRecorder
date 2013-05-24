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
                 " WHERE 1=1"
            if params["startdate"] is not None:
                sqlstr += " AND [T_RECORDER].[STARTTIME] >= "+params["startdate"]
            if params["enddate"] is not None:
                sqlstr += " AND [T_RECORDER].[STARTTIME] <= "+params["enddate"]
            if params["calltype"] is not None:
                sqlstr += " AND [T_RECORDER].[CALLTYPE] = "+params["calltype"]
            if params["agentid"] is not None:
                sqlstr += " AND [T_RECORDER].[AGENTID] = "+params["agentid"]
            if params["telno"] is not None:
                sqlstr += " AND [T_RECORDER].[TELNO] = "+params["telno"]
            if params["available"] is not None:
                sqlstr += " AND [T_RECORDER].[AVAILABLE] = "+params["available"]
            if params["totalmin"] is not None:
                sqlstr += " AND [TRQ_SCORE].[TOTAL] >= "+params["totalmin"]
            if params["totalmax"] is not None:
                sqlstr += " AND [TRQ_SCORE].[TOTAL] <= "+params["totalmax"]
            if params["channeldn"] is not None:
                sqlstr += " AND [T_RECORDER].[CHANNELDN] = "+params["channeldn"]
            if params["teldnis"] is not None:
                sqlstr += " AND [T_RECORDER].[TELDNIS] = "+params["teldnis"]
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
        else:
            pass
        finally:
            return None
