__author__ = 'JohannWong'
#coding=UTF-8
import web
import json
import mimerender

import globalDefine
import traceback
from logHelper import getLogger

from LogicObj.iRecorderListLogicObj import iRecorderListLogicObj
from LogicObj.iRecorderScoreLogicObj import iRecorderScoreLogicObj
from LogicObj.iRecorderQuestionLogicObj import iRecorderQuestionLogicObj

mimerender = mimerender.WebPyMimeRender()

render_xml = lambda message: '<message>%s</message>'%message
render_json = lambda **args: json.dumps(args)
render_html = lambda message: '<html><body>%s</body></html>'%message
render_txt = lambda message: message

urls = (
    "/irecorderservice/irecorderlist","iRecorderList",
    "/irecorderservice/irecorderscore","iRecorderScore",
    "/irecorderservice/irecorderquestion","iRecorderQuestion",
    )
app = web.application(urls,globals())

class iRecorderList:
    """

    """
    @mimerender(
        default = 'json',
        html = render_html,
        xml  = render_xml,
        json = render_json,
        txt  = render_txt
    )
    def GET(self):
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

            if iRecorderList is None:
                return {'message': None}
            else:
                return {'message':iRecorderList}
        except:
            logger.error("iRecorderList GET exception, see the traceback.log")
            #异常写入日志文件.
            f = open('Logs/traceback.txt','a')
            traceback.print_exc()
            traceback.print_exc(file = f)
            f.flush()
            f.close()

class iRecorderScore:
    @mimerender(
        default = 'json',
        html = render_html,
        xml  = render_xml,
        json = render_json,
        txt  = render_txt
    )
    def GET(self):
        try:
            logger = getLogger()
            logger.debug("start iRecordeScore GET response")
            #获取queryString
            params  = web.input()

            logicObj = iRecorderScoreLogicObj()
            if "filename" in params.keys() and params["filename"] is not None:
                #根据文件名精确查询
                iRecorderScore = logicObj.getiRecorderScoreByFileName(params["filename"])

            if iRecorderScore is None:
                return {'message': None}
            else:
                return {'message': iRecorderScore}
        except:
            logger.error("iRecorderScore GET exception, see the traceback.log")
            #异常写入日志文件.
            f = open('Logs/traceback.txt','a')
            traceback.print_exc()
            traceback.print_exc(file = f)
            f.flush()
            f.close()

    def POST(self):
        try:
            logger = getLogger()
            logger.debug("start iRecorderScore POST response")

            webData = web.data()
            iRecorderScoreJson = json.loads(webData)

            logicObj = iRecorderScoreLogicObj()

            iRecorderScore = logicObj.postiRecorderScoreByJson(iRecorderScoreJson)

            if iRecorderScore is None:
                return {'message': None}
            else:
                return {'message':iRecorderScore}
        except:
            logger.error("iRecorderScore POST exception, see the traceback.log")
            #异常写入日志文件.
            f = open('Logs/traceback.txt','a')
            traceback.print_exc()
            traceback.print_exc(file = f)
            f.flush()
            f.close()

    def PUT(self):
        try:
            logger = getLogger()
            logger.debug("start iRecorderScore PUT response")

            webData = web.data()
            iRecorderScoreJson = json.loads(webData)

            logicObj = iRecorderScoreLogicObj()

            iRecorderScore = logicObj.putiRecorderScoreByJson(iRecorderScoreJson)

            if iRecorderScore is None:
                return {'message': None}
            else:
                return {'message': iRecorderScore}
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

    """
    @mimerender(
        default = 'json',
        html = render_html,
        xml  = render_xml,
        json = render_json,
        txt  = render_txt
    )
    def GET(self):
        try:
            logger = getLogger()
            logger.debug("start iRecorderQuestion GET response")

            #获取queryString
            params  = web.input()

            logicObj = iRecorderQuestionLogicObj()
            if "fid" in params.keys() and params["fid"] is not None:
                #根据文件名精确查询
                iRecorderQuestionList = logicObj.getiRecorderListByFileFid(params["fid"]);

            if iRecorderQuestionList is None:
                return {'message': None}
            else:
                return {'message': iRecorderQuestionList}
        except:
            logger.error("iRecorderQuestion GET exception, see the traceback.log")
            #异常写入日志文件.
            f = open('Logs/traceback.txt','a')
            traceback.print_exc()
            traceback.print_exc(file = f)
            f.flush()
            f.close()

if __name__ == "__main__":
    app.run()