__author__ = 'JohannWong'
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

mimerender = mimerender.WebPyMimeRender()

render_xml = lambda message,error: '<message>%s</message><error>%s</error>'%(message,error)
render_json = lambda **args: json.dumps(args)
render_html = lambda message,error: '<html><body>Message:%s<br />Error:%s</body></html>'%(message,error)
render_txt = lambda message,error: message+error

urls = (
    "/irecorderservice/irecorderlist","iRecorderList",
    "/irecorderservice/irecorderscore","iRecorderScore",
    "/irecorderservice/irecorderquestion","iRecorderQuestion",
    "/irecorderservice/login","login",
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

class login:
    """
    录音打分系统-登录
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
            logger.error("iRecorderQuestion GET exception, see the traceback.log")
            logger.error("sql:"+str(sqlstr))
            #异常写入日志文件.
            f = open('Logs/traceback.txt','a')
            traceback.print_exc()
            traceback.print_exc(file = f)
            f.flush()
            f.close()
        finally:
            conn.close()

if __name__ == "__main__":
    app.run()