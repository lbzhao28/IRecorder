__author__ = 'JohannWong'
#coding=UTF-8
import traceback
from dbConnection import msSqlConnect
from logHelper import getLogger
class iRecorderQuestionModuleObj:
    """

    """
    def getiRecorderQuestionByFid(self,fid):
        try:
            logger = getLogger()
            logger.debug("start iRecorderQuestionModuleObj.getiRecorderQuestionByFid")
            conn = msSqlConnect()
            cur = conn.cursor()
            sqlstr = "SELECT [FID]"\
                     ",[ITEMID]"\
                     ",[ITEMDESC]"\
                     ",[ITEMPERC]"\
                     ",[HASREMARK]"\
                     " FROM [TRQ_SCRIPT]"\
                     " WHERE [TRQ_SCRIPT].[FID] = %s"
            cur.execute(sqlstr,fid)
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

    def getQuestionCount(self,itemID):
        try:
            logger = getLogger()
            logger.debug("start iRecorderQuestionModuleObj.getQuestionCount")
            conn = msSqlConnect()
            cur = conn.cursor()
            sqlstr = "SELECT ITEMID"\
                     " FROM [TRQ_SCRSUB]"\
                     " WHERE [TRQ_SCRSUB].[ITEMID] = %s"
            cur.execute(sqlstr,itemID)
            result = []
            for row in cur:
                result.append(row)
            return len(result)
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