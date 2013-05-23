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

mimerender = mimerender.WebPyMimeRender()

render_xml = lambda message: '<message>%s</message>'%message
render_json = lambda**args: json.dumps(args)
render_html = lambda message: '<html><body>%s</body></html>'%message
render_txt = lambda message: message

urls = (
    "/irecorderservice/irecorderlist","iRecorderList",
    "/irecorderservice/irecorderscore","iRecorderScore",
    "/irecorderservice/irecorderquestion","iRecorderQuestion",
    )
app = web.application(urls,globals())
"""

"""
class iRecorderList:
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

            globalDefine.globaliRecorderListErrorlog = "No Error"
            #获取queryString
            params  = web.input(filename=None)

            logicObj = iRecorderListLogicObj()
            if params["filename"] == None :
                #各个查询字段精确查询
                iRecorderList = logicObj.getiRecorderListByParams(params);
            else:
                #根据文件名精确查询
                iRecorderList = logicObj.getiRecorderListByFileName(params["filename"]);

            if iRecorderList == None:
                pass
            else:
                return iRecorderList
        except:
            logger.error("iRecorderList GET exception, see the traceback.log")
            #异常写入日志文件.
            f = open('Logs/traceback.txt','a')
            traceback.print_exc()
            traceback.print_exc(file = f)
            f.flush()
            f.close()

class iRecordeScore:
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

            globalDefine.globaliRecordeScorerErrorlog = "No Error"
            #获取queryString
            params  = web.input(filename=None)

            logicObj = iRecorderScoreLogicObj()
            if params["filename"] != None :
                #根据文件名精确查询
                iRecorderScore = logicObj.getiRecorderScoreByFileName(params["filename"]);

            if iRecorderScore == None:
                pass
            else:
                return iRecorderScore
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
            logger.debug("start iRecordeScore POST response")

            globalDefine.globaliRecordeScorerErrorlog = "No Error"

            webData = web.data()
            iRecordeScoreJson = json.loads(webData)

            logicObj = iRecorderScoreLogicObj()

        except:
            logger.error("iRecorderScore POST exception, see the traceback.log")
            #异常写入日志文件.
            f = open('Logs/traceback.txt','a')
            traceback.print_exc()
            traceback.print_exc(file = f)
            f.flush()
            f.close()


if __name__ == "__main__":
    app.run()