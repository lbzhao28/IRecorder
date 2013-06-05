__author__ = 'Johann Wong'
#coding=UTF-8
import traceback
from dbConnection import msSqlConnect
from logHelper import getLogger
class iRecorderQuestionModuleObj:
    """
    录音打分系统-录音问卷问题资源数据访问处理类
    author:J.Wong
    """
    def getiRecorderQuestionByFid(self,fid):
        """
        通过fid查找到录音问题资源
        author: J.Wong
        args: fid,string 问卷ID
        return: iRecorderList,list 对应的录音资源list
        """
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
                     " WHERE [TRQ_SCRIPT].[FID] = %s" \
                     " ORDER BY [ITEMDESC]"
            cur.execute(sqlstr,fid)
            logger.info("sql:"+str(sqlstr)+"\n fid:"+str(fid))
            result = []
            for row in cur:
                result.append(row)

            return result
        except Exception,ex:
            logger.error("exception occur, see the traceback.log")
            logger.error("sql:"+str(sqlstr)+"\n fid:"+str(fid))
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

    def getQuestionCount(self,itemID):
        """
        通过itemID查找到录音问题的答案数量
        author: J.Wong
        args: itemID,string 问题ID
        return: itemCount,int 答案数量
        """
        try:
            logger = getLogger()
            logger.debug("start iRecorderQuestionModuleObj.getQuestionCount")
            conn = msSqlConnect()
            cur = conn.cursor()
            sqlstr = "SELECT ITEMID"\
                     " FROM [TRQ_SCRSUB]"\
                     " WHERE [TRQ_SCRSUB].[ITEMID] = %s"
            cur.execute(sqlstr,itemID)
            logger.info("sql:"+str(sqlstr)+"\n itemID:"+str(itemID))
            result = []
            for row in cur:
                result.append(row)

            return len(result)
        except Exception,ex:
            logger.error("exception occur, see the traceback.log")
            logger.effof("sql:"+str(sqlstr)+"\n itemID:"+str(itemID))
            #异常写入日志文件.
            f = open('Logs/traceback.txt','a')
            traceback.print_exc()
            traceback.print_exc(file = f)
            f.flush()
            f.close()
            return 0
        else:
            pass
        finally:
            conn.close()