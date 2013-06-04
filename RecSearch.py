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
        try:
            logger = getLogger()  #初始化日志对象

            filename = None;
            webs = web.input();   # 获得前台传入进来的参数

            isbofang = "N";      # 变量用于控制前台是否播放

            if "filename" in webs:  #文件名
                filename = webs["filename"];

            if "isbofang" in webs:
                isbofang = webs["isbofang"];

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


            #pageSession 是否需要将用Session缓存起来
            pageSession = {"startdate":"","enddate":"","calltype":"","agentid":"","telno":"",
                           "vailabl":"","totalmin":"","totalmax":"","channeldn":"","teldnis":"",
                           "pageno":"","pagesize":"","available":""};

            if "startdate" in webs:
                startdate = webs['startdate']
                pageSession["startdate"] =str(startdate)
            else:
                startdatetime = str(time.strftime('%Y-%m-%d',time.localtime(time.time())))+" 00:00:00"
                pageSession["startdate"] = startdatetime

            if "enddate" in webs:
                enddate = webs['enddate']
                pageSession["enddate"] = str(enddate)
            else:
                enddate =  str(time.strftime('%Y-%m-%d',time.localtime(time.time())))+" 23:59:59"
                pageSession["enddate"] = str(enddate)

            if "channeldn" in webs:
                channeldn = webs['channeldn']
                pageSession["channeldn"] = str(channeldn)
            if "teldnis" in webs:
                teldnis = webs['teldnis']
                pageSession["teldnis"] =str(teldnis)
            if "totalmax" in webs:
                totalmax = webs['totalmax']
                pageSession[""] = str(totalmax)
            if "totalmin" in webs:
                totalmin = webs['totalmin']
                pageSession["totalmin"] = str(totalmin)
            if "available" in webs:
                available = webs['available']
                pageSession["available"] =str(available)
            if telno in webs:
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
                pageSession["pagesize"] =str(pagesize)

            if "pageno" in webs:
                pageno = webs['pageno']
                pageSession["pageno"] =str(pageno)


            print pageSession
            SearchList = RacorderClient.GetRaccemSearchUrl(startdate, enddate, calltype, agentid, telno, available, totalmin, totalmax, channeldn, teldnis, pageno, pagesize)
            localdic = [];
            if SearchList is not None and "message" in SearchList and len(SearchList["message"])>0:
                localdic = SearchList["message"]

            return render.RecSearch(outdic=localdic,outfilename=filename,configPage=configPage,QuestionNote=QuestionNote,
                flag=flag, isbofang=isbofang,pageSession=pageSession);

        except:

            logger.error("exception occur, see the traceback.log")
            #异常写入日志文件.
            f = open('traceback.txt', 'a')
            traceback.print_exc()
            traceback.print_exc(file=f)
            f.flush()
            f.close()

        finally:
            pass


def POST(self, op):
    pass
