__author__ = 'JohannWong'
#coding=UTF-8
import traceback
from dbConnection import msSqlConnect
from logHelper import getLogger

class iRecorderScoreModuleObj:
    """
    录音打分系统-打分资源数据访问处理类
    author:J.Wong
    """
    def getiRecorderScoreByFileName(self,filename):
        try:
            logger = getLogger()
            logger.debug("start iRecorderScoreModuleObj.getiRecorderScoreByFileName")
            conn = msSqlConnect()
            cur = conn.cursor()
            sqlstr = "SELECT [RECKEY]"\
            ",[RATERS]"\
            ",[TOTAL]"\
            ",[UPDT]"\
            ",[REMARK]"\
            ",[SCRVALS]"\
            ",[SCRVAL0]"\
            ",[SCRVAL1]"\
            ",[SCRVAL2]"\
            ",[SCRVAL3]"\
            ",[SCRVAL4]"\
            ",[SCRVAL5]"\
            ",[SCRVAL6]"\
            ",[SCRVAL7]"\
            ",[SCRVAL8]"\
            ",[SCRVAL9]"\
            ",[SCRVAL10]"\
            ",[SCRVAL11]"\
            ",[SCRVAL12]"\
            ",[SCRVAL13]"\
            ",[SCRVAL14]"\
            ",[SCRVAL15]"\
            " FROM [TRQ_SCORE]"\
            " WHERE [TRQ_SCORE].[RECKEY] = %s"
            cur.execute(sqlstr,filename)
            row = cur.fetchone()
            logger.info("sql:"+sqlstr+"\n filename:"+filename)
            if row:
                return row
            else:
                return 'No data.'
        except Exception,ex:
            logger.error("exception occur, see the traceback.log")

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

    def postiRecorderScoreByJson(self,scoreDic):
        try:
            logger = getLogger()
            logger.debug("start iRecorderScoreModuleObj.postiRecorderScoreByJson")
            conn = msSqlConnect()
            cur = conn.cursor()
            sqlstr = "INSERT INTO [TRQ_SCORE]"\
                     "([RECKEY]"\
                     ",[RATERS]"\
                     ",[TOTAL]"\
                     ",[UPDT]"\
                     ",[REMARK]"\
                     ",[SCRVALS]"\
                     ",[SCRVAL0]"\
                     ",[SCRVAL1]"\
                     ",[SCRVAL2]"\
                     ",[SCRVAL3]"\
                     ",[SCRVAL4]"\
                     ",[SCRVAL5]"\
                     ",[SCRVAL6]"\
                     ",[SCRVAL7]"\
                     ",[SCRVAL8]"\
                     ",[SCRVAL9]"\
                     ",[SCRVAL10]"\
                     ",[SCRVAL11]"\
                     ",[SCRVAL12]"\
                     ",[SCRVAL13]"\
                     ",[SCRVAL14]"\
                     ",[SCRVAL15]"\
                     ")"\
                     "VALUES"\
                     "('"+scoreDic['RECKEY']+"'"\
                     ",'"+scoreDic['RATERS']+"'"\
                     ",'"+scoreDic['TOTAL']+"'"\
                     ",CONVERT(varchar(32), GETDATE(), 20)"\
                     ",'"+scoreDic['REMARK']+"'"\
                     ",'"+scoreDic['SCRVALS']+"'"\
                     ",'"+scoreDic['SCRVAL0']+"'"\
                     ",'"+scoreDic['SCRVAL1']+"'"\
                     ",'"+scoreDic['SCRVAL2']+"'"\
                     ",'"+scoreDic['SCRVAL3']+"'"\
                     ",'"+scoreDic['SCRVAL4']+"'"\
                     ",'"+scoreDic['SCRVAL5']+"'"\
                     ",'"+scoreDic['SCRVAL6']+"'"\
                     ",'"+scoreDic['SCRVAL7']+"'"\
                     ",'"+scoreDic['SCRVAL8']+"'"\
                     ",'"+scoreDic['SCRVAL9']+"'"\
                     ",'"+scoreDic['SCRVAL10']+"'"\
                     ",'"+scoreDic['SCRVAL11']+"'"\
                     ",'"+scoreDic['SCRVAL12']+"'"\
                     ",'"+scoreDic['SCRVAL13']+"'"\
                     ",'"+scoreDic['SCRVAL14']+"'"\
                     ",'"+scoreDic['SCRVAL15']+"'"\
                     ")"
            cur.execute(sqlstr)
            conn.commit()
            logger.info("sql:"+sqlstr)

            sqlstr = "SELECT *"\
                     " FROM [TRQ_SCORE]"\
                     " WHERE [TRQ_SCORE].[RECKEY] = %s"
            cur.execute(sqlstr,scoreDic['RECKEY'])
            row = cur.fetchone()
            logger.info("sql:"+sqlstr)
            if row:
                return scoreDic['RECKEY']
            else:
                return 'No data.'
        except Exception,ex:
            logger.error("exception occur, see the traceback.log")

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

    def putiRecorderScoreByJson(self,scoreDic):
        try:
            logger = getLogger()
            logger.debug("start iRecorderScoreModuleObj.putiRecorderScoreByJson")
            conn = msSqlConnect()
            cur = conn.cursor()
            sqlstr = "UPDATE [TRQ_SCORE]"\
                     "SET"\
                     "[RATERS] = '"+scoreDic['RATERS']+"'"\
                     ",[TOTAL] = '"+scoreDic['TOTAL']+"'"\
                     ",[UPDT] =  CONVERT(varchar(32), GETDATE(), 20)"\
                     ",[REMARK] = '"+scoreDic['REMARK']+"'"\
                     ",[SCRVALS] ='"+scoreDic['SCRVALS']+"'"\
                     ",[SCRVAL0] ='"+scoreDic['SCRVAL0']+"'"\
                     ",[SCRVAL1] ='"+scoreDic['SCRVAL1']+"'"\
                     ",[SCRVAL2] ='"+scoreDic['SCRVAL2']+"'"\
                     ",[SCRVAL3] ='"+scoreDic['SCRVAL3']+"'"\
                     ",[SCRVAL4] ='"+scoreDic['SCRVAL4']+"'"\
                     ",[SCRVAL5] ='"+scoreDic['SCRVAL5']+"'"\
                     ",[SCRVAL6] ='"+scoreDic['SCRVAL6']+"'"\
                     ",[SCRVAL7] ='"+scoreDic['SCRVAL7']+"'"\
                     ",[SCRVAL8] ='"+scoreDic['SCRVAL8']+"'"\
                     ",[SCRVAL9] ='"+scoreDic['SCRVAL9']+"'"\
                     ",[SCRVAL10] ='"+scoreDic['SCRVAL10']+"'"\
                     ",[SCRVAL11] ='"+scoreDic['SCRVAL11']+"'"\
                     ",[SCRVAL12] ='"+scoreDic['SCRVAL12']+"'"\
                     ",[SCRVAL13] ='"+scoreDic['SCRVAL13']+"'"\
                     ",[SCRVAL14] ='"+scoreDic['SCRVAL14']+"'"\
                     ",[SCRVAL15] ='"+scoreDic['SCRVAL15']+"'"\
                     "WHERE [RECKEY] = '"+scoreDic['RECKEY']+"'"
            cur.execute(sqlstr)
            conn.commit()
            logger.info("sql:"+sqlstr)
            return scoreDic['RECKEY']
        except Exception,ex:
            logger.error("exception occur, see the traceback.log")

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