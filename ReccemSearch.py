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
            dic = [{"hostName": "1111", "fileName": "aaaa", "channelNO": "1111", "startTime": "111", "channelDN": "111",
                    "telDNIS": "11", "callID": "222",
                    "spendTime": "222", "available": "1", "agentID": "11", "filePath": "11", "callType": "11",
                    "telNO": "11", "endTime": "11", "total": "11"},
                    {"hostName": "1111", "fileName": "aaaa", "channelNO": "1111", "startTime": "111", "channelDN": "111"
                    , "telDNIS": "11", "callID": "222",
                     "spendTime": "222", "available": "1", "agentID": "11", "filePath": "11", "callType": "11",
                     "telNO": "11", "endTime": "11", "total": "11"},
                    {"hostName": "1111", "fileName": "aaaa", "channelNO": "1111", "startTime": "111", "channelDN": "111"
                    , "telDNIS": "11", "callID": "222",
                     "spendTime": "222", "available": "1", "agentID": "11", "filePath": "11", "callType": "11",
                     "telNO": "11", "endTime": "11", "total": "11"},
            ]
            print dic
            return render.ReccemSearch(outdic=dic);
        if(op == '1'):
            cemList = web.input();
            time1 = cemList["StrTime"];
            time2 = cemList["EndTime"];
            print time1 + time2
            dic = [{"hostName": "AAA", "fileName": "aaaa", "channelNO": "1111", "startTime": "111", "channelDN": "111",
                    "telDNIS": "11", "callID": "222",
                    "spendTime": "222", "available": "1", "agentID": "11", "filePath": "11", "callType": "11",
                    "telNO": "11", "endTime": "11", "total": "11"},
                    {"hostName": "ZZZ", "fileName": "aaaa", "channelNO": "1111", "startTime": "111", "channelDN": "111",
                     "telDNIS": "11", "callID": "222",
                     "spendTime": "222", "available": "1", "agentID": "11", "filePath": "11", "callType": "11",
                     "telNO": "11", "endTime": "11", "total": "11"},
                    {"hostName": "XXX", "fileName": "aaaa", "channelNO": "1111", "startTime": "111", "channelDN": "111",
                     "telDNIS": "11", "callID": "222",
                     "spendTime": "222", "available": "1", "agentID": "11", "filePath": "11", "callType": "11",
                     "telNO": "11", "endTime": "11", "total": "11"},
            ]
            print dic
            return render.ReccemSearch(outdic=dic);
