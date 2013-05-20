__author__ = 'JohannWong'
#coding=UTF-8
import web
import json
import mimerender
import globalDefine
import traceback
import re
import base64

render_xml =  lambda ret:'<ret>%s</ret>'%ret
render_json = lambda **args:json.dumps(args)
render_html = lambda ret:'<html><body>ret is:%s<body></html>'%ret
render_txt =  lambda ret:ret

urls = (
    "/irecorderservice/irecordelist/(.+)","iRecordeList",
    "/irecorderservice/irecordescore/(.+)","iRecordeScore",
    "/irecorderservice/irecordequestion/(.+)","iRecordeQuestion",
    )
app = web.application(urls,globals())

if __name__ == "__main__":
    app.run()