__author__ = 'JohannWong'
#coding=UTF-8
import traceback
from dbConnection import msSqlConnect
from logHelper import getLogger
class iRecorderListModuleObj:
    """
    录音打分系统-录音资源数据访问处理类
    author:J.Wong
    """
    def getiRecorderListByFileName(self,filename):
        """
        通过录音文件名查找到录音资源
        author: J.Wong
        args: filename,string 录音文件名
        return: iRecorderList,list 对应的录音资源list
        """
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
            if len(result):
                return result
            else:
                return 'No data.'
        except Exception,ex:
            logger.error("exception occur, see the traceback.log")
            logger.error("sql:"+sqlstr+"\n filename:"+filename)
            #异常写入日志文件.
            f = open('Logs/traceback.txt','a')
            traceback.print_exc()
            traceback.print_exc(file = f)
            f.flush()
            f.close()
            return ex.message
        else:
           pass
        finally:
            conn.close()

    def getiRecorderListByParams(self,params):
        """
        通过其他查询条件查找到录音资源
        author: J.Wong
        args: params,string 查询录音的querystring，格式参见doc目录下“座席录音资源接口说明文档.xlsx”
        return: iRecorderList,list 对应的录音资源list
        """
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
        except Exception,ex:
            logger.error("exception occur, see the traceback.log")
            logger.error("sql:"+sqlstr+"\n params:"+params)
            #异常写入日志文件.
            f = open('Logs/traceback.txt','a')
            traceback.print_exc()
            traceback.print_exc(file = f)
            f.flush()
            f.close()
            return ex.message
        else:
            pass
        finally:
            conn.close()
