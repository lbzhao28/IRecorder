__author__ = 'stone'
#encoding:utf-8
#File:RecorderScore.py
import web
from web.contrib.template import render_mako

import globalDefine
import traceback
import configData
from configData import getConfig
from logHelper import getLogger
import RacorderClient



import base64
import json
import configData

import urlparse
import OrderDomainHandler

web.config.debug = False

urls = (
        '/rqscoscr/(.*)','rqscoscr',
        '/Saverqscoscr/(.*)','RacorderClient.RacorderSave'
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

class rqscoscr():
        def POST(self,filename):
            pass

        def GET(self,filename):
            try:
                logger = getLogger()
                logger.debug("start rqscoscr Page GET response")

                globalDefine.globalOrderInfoErrorlog = "No Error"

                #import  db
                #userdb = db.database(dbn = "mssql", db = 'RaRecorder_CEM', user ='sa' ,pw ='sa.rayda',host='192.168.1.186',charset="utf8")

                #str_query="select * from T_USER";
                #returnjson=[]
                #dic_result=userdb.query(str_query);
                #print dic_result;



#TODO: open the auth in future.also need purview.
                #            authreq = checkUserAuth(web)
                #
                #            if authreq:
                #                web.header('WWW-Authenticate','Basic realm="Auth example"')
                #                web.ctx.status = '401 Unauthorized'
                #                logger.debug("no right HTTP_AUTHORIZATION")
                #                return render.error(error = web.ctx.status)

                #TODO: when None happen?
                if filename is None:
                    return render.error(error = 'no filename')
                else:
                    return render.rqsco_stone(outdicrqscoscr=getTestData())

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


def getTestData():
    subitem = [{"subitemname":"1","subitemvalue":"1"},{"subitemname":"2","subitemvalue":"2"},{"subitemname":"3","subitemvalue":"3"}]
    dicrqscoscr = []
    recordequestion = {"itemID":"1","itemDesc":"开场白(真诚问候，专业身份与多美滋的关系 15%)","itemPerc":"10","subitems":subitem}

    dicrqscoscr.append(recordequestion)

    recordequestion = {"itemID":"2","itemDesc":"建议（评估结果 40%）","itemPerc":"10","subitems":subitem}
    dicrqscoscr.append(recordequestion)

    recordequestion = {"itemID":"3","itemDesc":"开场白,(表达同理心,对妈妈/孕妇的关心 自然真诚 15%)","itemPerc":"10","subitems":subitem}

    dicrqscoscr.append(recordequestion)
    recordequestion = {"itemID":"4","itemDesc":"开场白,(告之目的和利益，明确告知致电的目的或利益 2，并确认生日，预产期15%)","itemPerc":"10","subitems":subitem}
    dicrqscoscr.append(recordequestion)

    recordequestion = {"itemID":"5","itemDesc":"开场白(真诚问候，专业身份与多美滋的关系 15%)","itemPerc":"10","subitems":subitem}
    dicrqscoscr.append(recordequestion)

    recordequestion = {"itemID":"6","itemDesc":"建议（评估结果 40%）","itemPerc":"10","subitems":subitem}
    dicrqscoscr.append(recordequestion)

    recordequestion = {"itemID":"7","itemDesc":"开场白,(表达同理心,对妈妈/孕妇的关心 自然真诚 15%)","itemPerc":"10","subitems":subitem}

    dicrqscoscr.append(recordequestion)
    recordequestion = {"itemID":"8","itemDesc":"开场白,(告之目的和利益，明确告知致电的目的或利益 2，并确认生日，预产期15%)","itemPerc":"10","subitems":subitem}
    dicrqscoscr.append(recordequestion)

    recordequestion = {"itemID":"9","itemDesc":"开场白(真诚问候，专业身份与多美滋的关系 15%)","itemPerc":"10","subitems":subitem}

    dicrqscoscr.append(recordequestion)

    recordequestion = {"itemID":"10","itemDesc":"建议（评估结果 40%）","itemPerc":"10","subitems":subitem}
    dicrqscoscr.append(recordequestion)

    recordequestion = {"itemID":"11","itemDesc":"开场白,(表达同理心,对妈妈/孕妇的关心 自然真诚 15%)","itemPerc":"10","subitems":subitem}

    dicrqscoscr.append(recordequestion)
    recordequestion = {"itemID":"12","itemDesc":"开场白,(告之目的和利益，明确告知致电的目的或利益 2，并确认生日，预产期15%)","itemPerc":"10","subitems":subitem}
    dicrqscoscr.append(recordequestion)

    dicrqscoscrS = json.dumps(dicrqscoscr)

    return dicrqscoscrS

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
