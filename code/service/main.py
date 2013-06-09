__author__ = 'Johann.Wong'
#coding=UTF-8
import web
import json
import mimerender

import traceback
from logHelper import getLogger

from LogicObj.iRecorderListLogicObj import iRecorderListLogicObj
from LogicObj.iRecorderScoreLogicObj import iRecorderScoreLogicObj
from LogicObj.iRecorderQuestionLogicObj import iRecorderQuestionLogicObj
from ModuleObj.dbConnection import msSqlConnect
from ModuleObj.iRecorderReport import iRecorderReport

mimerender = mimerender.WebPyMimeRender()

render_xml = lambda message,error: '<message>%s</message><error>%s</error>'%(message,error)
render_json = lambda **args: json.dumps(args)
render_html = lambda message,error: '<html><body>Message:%s<br />Error:%s</body></html>'%(message,error)
render_txt = lambda message,error: message+';'+error+';'

render_xml_report = lambda message,error,filename: '<message>%s</message><error>%s</error><filename>%s</filename>'%(message,error,filename)
render_json_report = lambda **args: json.dumps(args)
render_html_report = lambda message,error,filename: '<html><body>Message:%s<br />Error:%s<br />Filename:%s</body></html>'%(message,error,filename)
render_txt_report = lambda message,error,filename: message+';'+error+';'+filename+';'

urls = (
    "/irecorderservice/irecorderlist","iRecorderList",
    "/irecorderservice/irecorderlistcount","iRecorderListCount",
    "/irecorderservice/irecorderscore","iRecorderScore",
    "/irecorderservice/irecorderquestion","iRecorderQuestion",
    "/irecorderservice/login","login",
    "/irecorderservice/report","report",
    )
app = web.application(urls,globals())

class iRecorderList:
    """
    录音打分系统-录音列表
    author:J.Wong
    """
    @mimerender(
        default = 'json',
        html = render_html,
        xml  = render_xml,
        json = render_json,
        txt  = render_txt
    )
    def GET(self):
        """
        Get iRecorderList资源
        author: J.Wong
        return: JSON
        """
        try:
            logger = getLogger()
            logger.debug("start iRecorderList GET response")
            #获取queryString
            params  = web.input()

            logicObj = iRecorderListLogicObj()
            if "filename" in params.keys() and params["filename"] is not None:
                #根据文件名精确查询
                iRecorderList = logicObj.getiRecorderListByFileName(params["filename"]);
            else:
                #各个查询字段精确查询
                iRecorderList = logicObj.getiRecorderListByParams(params);
            if isinstance(iRecorderList, basestring):
                return {'message':None,'error':iRecorderList}
            else:
                return {'message':iRecorderList,'error':''}
        except:
            logger.error("iRecorderList GET exception, see the traceback.log")
            #异常写入日志文件.
            f = open('Logs/traceback.txt','a')
            traceback.print_exc()
            traceback.print_exc(file = f)
            f.flush()
            f.close()

class iRecorderScore:
    """
    录音打分系统-打分
    author:J.Wong
    """
    @mimerender(
        default = 'json',
        html = render_html,
        xml  = render_xml,
        json = render_json,
        txt  = render_txt
    )
    def GET(self):
        """
        Get iRecorderScore资源
        author: J.Wong
        return: JSON
        """
        try:
            logger = getLogger()
            logger.debug("start iRecordeScore GET response")
            #获取queryString
            params  = web.input()

            logicObj = iRecorderScoreLogicObj()
            if "filename" in params.keys() and params["filename"] is not None:
                #根据文件名精确查询
                iRecorderScore = logicObj.getiRecorderScoreByFileName(params["filename"])
                if isinstance(iRecorderScore, basestring):
                    return {'message':None,'error': iRecorderScore}
                else:
                    return {'message': iRecorderScore,'error':''}
            return  {'message':None,'error': 'Must set the value of filename.'}
        except:
            logger.error("iRecorderScore GET exception, see the traceback.log")
            #异常写入日志文件.
            f = open('Logs/traceback.txt','a')
            traceback.print_exc()
            traceback.print_exc(file = f)
            f.flush()
            f.close()

    def POST(self):
        """
        POST iRecorderScore资源
        author: J.Wong
        return: JSON
        """
        try:
            logger = getLogger()
            logger.debug("start iRecorderScore POST response")

            webData = web.data()
            iRecorderScoreJson = json.loads(webData)

            logicObj = iRecorderScoreLogicObj()

            iRecorderScore = logicObj.postiRecorderScoreByJson(iRecorderScoreJson)

            if isinstance(iRecorderScore, basestring):
                return {'message':None,'error': iRecorderScore}
            else:
                return {'message': iRecorderScore,'error':''}
        except:
            logger.error("iRecorderScore POST exception, see the traceback.log")
            #异常写入日志文件.
            f = open('Logs/traceback.txt','a')
            traceback.print_exc()
            traceback.print_exc(file = f)
            f.flush()
            f.close()

    def PUT(self):
        """
        PUT iRecorderScore资源
        author: J.Wong
        return: JSON
        """
        try:
            logger = getLogger()
            logger.debug("start iRecorderScore PUT response")

            webData = web.data()
            iRecorderScoreJson = json.loads(webData)

            logicObj = iRecorderScoreLogicObj()

            iRecorderScore = logicObj.putiRecorderScoreByJson(iRecorderScoreJson)

            if isinstance(iRecorderScore, basestring):
                return {'message':None,'error': iRecorderScore}
            else:
                return {'message': iRecorderScore,'error':''}
        except:
            logger.error("iRecorderScore PUT exception, see the traceback.log")
            #异常写入日志文件.
            f = open('Logs/traceback.txt','a')
            traceback.print_exc()
            traceback.print_exc(file = f)
            f.flush()
            f.close()

class iRecorderQuestion:
    """
    录音打分系统-问卷
    author:J.Wong
    """
    @mimerender(
        default = 'json',
        html = render_html,
        xml  = render_xml,
        json = render_json,
        txt  = render_txt
    )
    def GET(self):
        """
        Get iRecorderQuestion资源
        author: J.Wong
        return: JSON
        """
        try:
            logger = getLogger()
            logger.debug("start iRecorderQuestion GET response")

            #获取queryString
            params  = web.input()

            logicObj = iRecorderQuestionLogicObj()
            if "fid" in params.keys() and params["fid"] is not None:
                #根据文件名精确查询
                iRecorderQuestionList = logicObj.getiRecorderQuestionByFileFid(params["fid"]);
                if isinstance(iRecorderQuestionList, basestring):
                    return {'message':None,'error': iRecorderQuestionList}
                else:
                    return {'message': iRecorderQuestionList,'error':''}

            return  {'message':None,'error': 'Must set the value of fid.'}
        except:
            logger.error("iRecorderQuestion GET exception, see the traceback.log")
            #异常写入日志文件.
            f = open('Logs/traceback.txt','a')
            traceback.print_exc()
            traceback.print_exc(file = f)
            f.flush()
            f.close()

class iRecorderListCount:
    """
    录音打分系统-录音列表计数
    author:J.Wong
    """
    @mimerender(
        default = 'json',
        html = render_html,
        xml  = render_xml,
        json = render_json,
        txt  = render_txt
    )
    def GET(self):
        """
        Get login资源
        author: J.Wong
        return: JSON
        """
        try:
            logger = getLogger()
            logger.debug("start iRecorderListCount GET response")

            #获取queryString
            params  = web.input()

            conn = msSqlConnect()
            cur = conn.cursor()
            sqlstr =  "SELECT COUNT(*) as TOTALCOUNT"\
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

            cur.execute(sqlstr)
            row = cur.fetchone()
            logger.info("sql:"+str(sqlstr))
            if row:
                return {'message':str(row["TOTALCOUNT"]),'error': ''}
            else:
                return {'message':None,'error': 'No data match.'}
        except:
            logger.error("iRecorderListCount GET exception, see the traceback.log")
            logger.error("sql:"+str(sqlstr))
            #异常写入日志文件.
            f = open('Logs/traceback.txt','a')
            traceback.print_exc()
            traceback.print_exc(file = f)
            f.flush()
            f.close()
        finally:
            if conn is not None:
                conn.close()

class login:
    """
    录音打分系统-登录
    author:J.Wong
    """
    @mimerender(
        default = 'json',
        html = render_html,
        xml  = render_xml,
        json = render_json,
        txt  = render_txt
    )
    def GET(self):
        """
        Get login资源
        author: J.Wong
        return: JSON
        """
        try:
            logger = getLogger()
            logger.debug("start login GET response")

            #获取queryString
            params  = web.input()

            if "id" not in params.keys() or "pwd" not in params.keys() or params["id"] is None or params["pwd"] is None:
                return  {'message':None,'error': 'Must set the value of id and pwd.'}
            conn = msSqlConnect()
            cur = conn.cursor()
            sqlstr = "SELECT [LOGINID]"\
                    ",[PASSWORD]"\
                    ",[FID]"\
                    " FROM [T_USER]"\
                    " LEFT JOIN [TRQ_USRFRM]"\
                    " ON [T_USER].[LOGINID] = [TRQ_USRFRM].[USRID]"\
                    " WHERE [FID] = 'CEM'"\
                    " AND [LOGINID] = '"+str(params["id"])+"'"\
                    " AND [PASSWORD] = '"+str(params["pwd"])+"'"
            cur.execute(sqlstr)
            row = cur.fetchone()
            logger.info("sql:"+str(sqlstr))
            if row:
                return {'message':True,'error': ''}
            else:
                return {'message':False,'error': 'No data match.'}
        except:
            logger.error("login GET exception, see the traceback.log")
            logger.error("sql:"+str(sqlstr))
            #异常写入日志文件.
            f = open('Logs/traceback.txt','a')
            traceback.print_exc()
            traceback.print_exc(file = f)
            f.flush()
            f.close()
        finally:
            if conn is not None:
                conn.close()

class report:
    """
    录音打分系统-报表
    author: J.Wong
    """
    @mimerender(
        default = 'json',
        html = render_html_report,
        xml  = render_xml_report,
        json = render_json_report,
        txt  = render_txt_report
    )
    def GET(self):
        """
        Get report资源
        author: J.Wong
        return: JSON
        """
        try:
            logger = getLogger()
            logger.debug("start report GET response")

            #获取queryString
            params  = web.input()

            iRecorderReportObj = iRecorderReport()
            iReportReturn = iRecorderReportObj.exportReport(params)
            if isinstance(iReportReturn['result'], basestring):
                return {'message':None,'error':iReportReturn['result'],'filename':str(iReportReturn['filename'])}
            else:
                return{'message':iReportReturn['result'],'error':'','filename':str(iReportReturn['filename'])}
        except:
            logger.error("report GET exception, see the traceback.log")
            #异常写入日志文件.
            f = open('Logs/traceback.txt','a')
            traceback.print_exc()
            traceback.print_exc(file = f)
            f.flush()
            f.close()


if __name__ == "__main__":
    app.run()