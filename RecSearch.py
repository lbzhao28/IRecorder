__author__ = 'zhuangkun'
#encoding:utf-8
import web
import urls
import json
import ReccemClient;
from web.contrib.template import render_mako

render = render_mako(
    directories=['templates'],
    input_encoding='utf-8',
    output_encoding='utf-8',
)

class SearchRec():
    def GET(self):
        return  render.RecSearch();

    def POST(self):
        pass


class RecSelect:
    def GET(self, op):
        if(op == 'select'):
            dic = []
            return render.RecSearch(outdic=dic);
        if(op == 'Search'):
            ReccemList = web.input()
            startdate = ReccemList['startdate']
            enddate = ReccemList['enddate']
            calltype = ReccemList['calltype']
            agentid = ReccemList['agentid']
            telno = ReccemList['telno']
            available = ReccemList['available']
            totalmin = ReccemList['totalmin']
            totalmax = ReccemList['totalmax']
            channeldn = ReccemList['channeldn']
            teldnis = ReccemList['teldnis']
            pageno = ReccemList['pageno']
            pagesize = ReccemList['pagesize']
            SearchList = ReccemClient.GetRaccemSearchUrl(startdate, enddate, calltype, agentid, telno, available,
                totalmin, totalmax, channeldn, teldnis, pageno, pagesize)
            dic = SearchList["message"]
            return render.RecSearch(outdic=dic);
