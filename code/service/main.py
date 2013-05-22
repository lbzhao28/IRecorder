__author__ = 'JohannWong'
#coding=UTF-8
import web
import json
import mimerender
import globalDefine
import traceback
from logHelper import getLogger

from iRecorderListLogicObj import iRecorderListLogicObj

render_xml =  lambda ret:'<ret>%s</ret>'%ret
render_json = lambda **args:json.dumps(args)
render_html = lambda ret:'<html><body>ret is:%s<body></html>'%ret
render_txt =  lambda ret:ret

urls = (
    "/irecorderservice/irecordelist(.+)","iRecordeList",
    "/irecorderservice/irecordescore(.+)","iRecordeScore",
    "/irecorderservice/irecordequestion(.+)","iRecordeQuestion",
    )
app = web.application(urls,globals())
"""

"""
class iRecordeList:
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
            logger.debug("start iRecordeList GET response")

            globalDefine.globaliRecordeListErrorlog = "No Error"
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
            logger.error("iRecordeList GET exception, see the traceback.log")
            #异常写入日志文件.
            f = open('traceback.txt','a')
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

            globalDefine.globaliRecordeScoreErrorlog = "No Error"
            #获取queryString
            params  = web.input(filename=None)

            logicObj = iRecordeScoreLogicObj()
            if params["filename"] != None :
                #根据文件名精确查询
                iRecordeScore = logicObj.getiRecordeScoreByFileName(params["filename"]);

            if iRecordeScore == None:
                pass
            else:
                return iRecordeScore
        except:
            logger.error("iRecordeScore GET exception, see the traceback.log")
            #异常写入日志文件.
            f = open('traceback.txt','a')
            traceback.print_exc()
            traceback.print_exc(file = f)
            f.flush()
            f.close()

if __name__ == "__main__":
    app.run()