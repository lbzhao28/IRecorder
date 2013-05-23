__author__ = 'zhuangkun'
#encoding:utf-8
import web
import urls
import json
from web.contrib.template import render_mako

render = render_mako(
    directories=['templates'],
    input_encoding='utf-8',
    output_encoding='utf-8',
)

class SearchReccem():
    def GET(self):
        return render.ReccemSearch()

    def POST(self):
        pass


class ReccemSelect:
    def GET(self, op):
        if(op == '0'):
            dic = [{"Dnis": "1101", "TsrName": "60001", "StrTime": "2012-10-12 12:23:04", "CountTime": "329",
                    "Status": "111", "Score": "", "Zhu": "021-52808080", "Bei": ""},
                    {"Dnis": "1102", "TsrName": "60002", "StrTime": "2012-10-12 12:56:04", "CountTime": "128",
                     "Status": "222", "Score": "", "Zhu": "", "Bei": "13501916492"},
                    {"Dnis": "1103", "TsrName": "60004", "StrTime": "2012-10-12 13:06:04", "CountTime": "223",
                     "Status": "333", "Score": "", "Zhu": "", "Bei": "18017511892"},
                    {"Dnis": "1104", "TsrName": "60003", "StrTime": "2012-10-12 15:20:04", "CountTime": "112",
                     "Status": "444", "Score": "", "Zhu": "021-52808080", "Bei": ""}
            ]
            print json.dumps(dic)
            return  json.dumps(dic)
        if(op == '1'):
            dic = "1";
            print dic