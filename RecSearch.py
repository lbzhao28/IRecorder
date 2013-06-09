__author__ = 'zhuangkun'
#encoding:utf-8
import web
import urls
import json
import ReccemClient;
import time

from configObjData import getRecorderConfigPage
from web.contrib.template import render_mako

import globalDefine
import traceback
import configData
from configData import getConfig
from logHelper import getLogger
import RacorderClient


render = render_mako(
    directories=['templates'],
    input_encoding='utf-8',
    output_encoding='utf-8',
)

class RecSelect:
    def GET(self, op):

        if "user_UserName" not in web.ctx.session:

            web.seeother('/RecSearch/')
        else:
            UserName = str(web.ctx.session.user_UserName);
            logger = getLogger()  #初始化日志对象

            filename = None;
            webs = web.input();   # 获得前台传入进来的参数

            isbofang = "N";      # 变量用于控制前台是否播放
            filePath = "";

            if "filename" in webs:  #文件名
                filename = webs["filename"];

            if "isbofang" in webs:
                isbofang = webs["isbofang"];

            if  "filePath" in webs:
                filePath = webs["filePath"];
                #filePath = str(filePath)[-11,0][:-1];

            flag = "add";         # falg 用于在前台判断质检结果 是否新增
            QuestionNote = "";    # QuestionNote 前台备注字段

            if filename is None or filename.strip() == '':  # filename如果为空，则创建问卷 ，则从web中间的session取
                logger.debug("filename is None")
                if "session_tRecorderConfigPage" in web.ctx.session:
                    configPage = web.ctx.session.session_tRecorderConfigPage;
                else:
                    tRacorderQuestion = None;
                    configPage = getRecorderConfigPage(tRacorderQuestion)    # 创建问卷页面控件 configPage
                    web.ctx.session.session_tRecorderConfigPage = configPage; # session 缓存起来
                    #return render.error(error = 'no filename')
            else:
                #web.ctx.session.session_tRecorderConfigPage = None;
                tRacorderQuestion = RacorderClient.GetRacorderQuestionByfilename(filename);

                if tRacorderQuestion is not None and len(tRacorderQuestion) > 0 and tRacorderQuestion[
                                                                                    "message"] is not None:
                    localtRacorderQuestion = tRacorderQuestion["message"];
                    flag = "edit";
                    QuestionNote = localtRacorderQuestion["remark"]
                    configPage = getRecorderConfigPage(tRacorderQuestion)             # 创建问卷页面控件 configPage
                else:
                    if "session_tRecorderConfigPage" in web.ctx.session:
                        configPage = web.ctx.session.session_tRecorderConfigPage;
                    else:
                        tRacorderQuestion = None;
                        configPage = getRecorderConfigPage(tRacorderQuestion)    # 创建问卷页面控件 configPage
                        web.ctx.session.session_tRecorderConfigPage = configPage; # session 缓存起来

            startdate = "";
            enddate = "";
            calltype = "";
            agentid = "";
            telno = "";
            vailabl = ""
            totalmin = ""
            totalmax = ""
            channeldn = ""
            teldnis = ""
            pageno = ""
            pagesize = ""
            available = ""

            tRacorderQuestions_count = 0
            #取得session 变量，读取题目是江count 保存起来的
            if "tRacorderQuestions_count" in web.ctx.session:
                tRacorderQuestions_count = web.ctx.session.tRacorderQuestions_count;
                #pageSession 是否需要将用Session缓存起来
            pageSession = {"startdate": "", "enddate": "", "calltype": "", "agentid": "", "telno": "",
                           "vailabl": "", "totalmin": "", "totalmax": "", "channeldn": "", "teldnis": "",
                           "pageno": "1", "pagesize": "10", "available": "", "pagecount": "0", "rowcount": "0",
                           "tRacorderQuestions_count": tRacorderQuestions_count,"UserName":UserName};

            if "startdate" in webs:
                startdate = webs['startdate']
                pageSession["startdate"] = str(startdate)
            else:
                localstartdate = str(time.strftime('%Y-%m-%d', time.localtime(time.time())))
                pageSession["startdate"] = localstartdate

            if "enddate" in webs:
                enddate = webs['enddate']
                pageSession["enddate"] = str(enddate)
            else:
                localenddate = str(time.strftime('%Y-%m-%d', time.localtime(time.time())))
                pageSession["enddate"] = str(localenddate)

            if "channeldn" in webs:
                channeldn = webs['channeldn']
                pageSession["channeldn"] = str(channeldn)
            if "teldnis" in webs:
                teldnis = webs['teldnis']
                pageSession["teldnis"] = str(teldnis)
            if "totalmax" in webs:
                totalmax = webs['totalmax']
                pageSession["totalmax"] = str(totalmax)
            if "totalmin" in webs:
                totalmin = webs['totalmin']
                pageSession["totalmin"] = str(totalmin)
            if "status" in webs:
                available = webs['status']
                pageSession["status"] = str(available)
            if "telno" in webs:
                telno = webs['telno']
                pageSession["telno"] = str(telno)
            if "agentid" in webs:
                agentid = webs['agentid']
                pageSession["agentid"] = str(agentid)
            if "calltype" in webs:
                calltype = webs['calltype']
                pageSession["calltype"] = str(calltype)

            if "pagesize" in webs:
                pagesize = webs['pagesize']
                pageSession["pagesize"] = str(pagesize)
            else:
                pageSession["pagesize"] = 10;

            if "pageno" in webs:
                pageno = webs['pageno']
                pageSession["pageno"] = str(pageno)
            else:
                pageSession["pageno"] = 1;


                # 根据条件返回数据的条数
            localdic = [];      # 录音的list 集合
            SearchListMessage = RacorderClient.GetRaccemSearchUrlcount(startdate, enddate, calltype, agentid, telno,
                available, totalmin, totalmax, channeldn, teldnis)

            if SearchListMessage is not None and "message" in SearchListMessage and len(SearchListMessage["message"]) > 0:
                SearchListMessageCount = int(SearchListMessage["message"]);
                varPagesize = int(pageSession["pagesize"]);
                pagecount = 0;
                pagecount = int(SearchListMessageCount / varPagesize)
                if(SearchListMessageCount % varPagesize > 0):
                    pagecount = pagecount + 1;
                pageSession["pagecount"] = pagecount;
                pageSession["rowcount"] = int(SearchListMessageCount)

                SearchList = RacorderClient.GetRaccemSearchUrl(startdate, enddate, calltype, agentid, telno, available,
                    totalmin, totalmax, channeldn, teldnis, pageno, pagesize)
                if SearchList is not None and "message" in SearchList and len(SearchList["message"]) > 0:
                    localdics = SearchList["message"]
                    print localdics
                    for item in localdics:
                        item["fileNameNo"] = str(item["fileName"]).replace(".", "").replace("_", "")
                        localfilePath = str(item["filePath"])
                        filePathNo = localfilePath[-11:][:-1];
                        item["filePathNo"] = filePathNo;
                        localdic.append(item);

            return render.RecSearch(outdic=localdic, outfilename=filename, configPage=configPage, QuestionNote=QuestionNote,
                flag=flag, isbofang=isbofang, pageSession=pageSession, filePath=filePath);


def POST(self, op):
    pass
