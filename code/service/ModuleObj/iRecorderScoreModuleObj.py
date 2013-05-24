__author__ = 'JohannWong'
#coding=UTF-8
import traceback
from dbConnection import msSqlConnect
from logHelper import getLogger

class iRecorderScoreModuleObj:
    """

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