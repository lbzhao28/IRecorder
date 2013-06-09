__author__ = 'stone'
#encoding:utf-8
import web
from web.contrib.template import render_mako

import globalDefine
import traceback
import configData
from configData import getConfig
from logHelper import getLogger
import RacorderClient
import Login



import base64
import json
import configData

import urlparse
import OrderDomainHandler
import configData
from configData import getConfig
import configObjData
from configObjData import getRecorderConfigPage

web.config.debug = False

urls = (
        '/rqscoscr/(.*)','rqscoscr',
        '/Saverqscoscr/(.*)','RacorderClient.RacorderSave',
        '/login', 'Login.Login',
        '/RecSearch/(.*)', 'RecSearch.RecSelect',
        '/ReportExport/(.*)', 'RacorderClient.ReportExport',
    )

app = web.application(urls,globals(),autoreload=True)
session = web.session.Session(app,web.session.DiskStore('sessions'),
initializer={'session_grpid':'','session_usrid':'','session_loginned':'','session_pwd':''})

def session_hook():
    web.ctx.session = session

app.add_processor(web.loadhook(session_hook))

allowed = (
    (getConfig('allowedUser1','UserName','str'),getConfig('allowedUser1','Password','str')),
    (getConfig('allowedUser2','UserName','str'),getConfig('allowedUser2','Password','str'))
    )

# input_encoding and output_encoding is important for unicode
# template file. Reference:
# http://www.makotemplates.org/docs/documentation.html#unicode
render = render_mako(
        directories = ['templates'],
        input_encoding = 'utf-8',
        output_encoding = 'utf-8',
        )

# 问题页面
class rqscoscr():
        def POST(self,filename):
            pass

        def GET(self,filename):
            try:

                logger = getLogger()
                logger.debug("start rqscoscr Page GET response")

                globalDefine.globalOrderInfoErrorlog = "No Error"

                #TODO: when None happen?
                if filename is None or filename.strip() == '':
                    return render.error(error = 'no filename')
                else:
                    tRacorderQuestion = RacorderClient.GetRacorderQuestionByfilename(filename);
                    configPage = getRecorderConfigPage(tRacorderQuestion)    # 创建页面控件 configPage
                    #tRacorderQuestion = web.ctx.session.session_tRacorderQuestion; #取得缓存里面录音的质检结果 如果没有质检过则为 None

                    flag = "add";         # falg 用于在前台判断质检结果 是否新增
                    QuestionNote = "";
                    print tRacorderQuestion
                    if tRacorderQuestion is not None and len(tRacorderQuestion)>0 and tRacorderQuestion["message"] is not None:
                        localtRacorderQuestion = tRacorderQuestion["message"];
                        flag = "edit";
                        QuestionNote = localtRacorderQuestion["remark"];
                    return render.rqsco_stone(outfilename =filename,configPage = configPage,QuestionNote = QuestionNote,flag = flag);

            except :
                logger.error("exception occur, see the traceback.log")
                #异常写入日志文件.
                f = open('traceback.txt','a')
                traceback.print_exc()
                traceback.print_exc(file = f)
                f.flush()
                f.close()
            else:
                pass
            finally:
                pass


def checkUserAuth(inWeb):
    logger = getLogger()
    auth = inWeb.ctx.env.get('HTTP_AUTHORIZATION')
    authreq = False
    if auth is None:
        authreq = True
    else:
        auth = re.sub('^Basic ','',auth)
        username,password = base64.decodestring(auth).split(':')
        if (username,password) in allowed:
            logger.debug("has right HTTP_AUTHORIZATION")
            pass
        else:
            authreq = True
    return authreq

if __name__ == "__main__":
    app.run()
