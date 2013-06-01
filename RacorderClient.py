__author__ = 'stone'
#coding=UTF-8

import pycurl
import cStringIO
import json

import traceback
from configData import getConfig
from logHelper import getLogger
import  web



def getOrderInfoOrder(inOrderid):
    """get the order info from REST """
    try:
        logger = getLogger()
        logger.debug("start GET Order Info according order id.")

        if inOrderid is None:
            return None

        buf = cStringIO.StringIO() #define in function.
        c = pycurl.Curl()


        localURL = getConfig('RESTService','orderInfoOrderidUrl','str')+inOrderid
        localURL = str(localURL)
        c.setopt(pycurl.URL,localURL)
        c.setopt(c.WRITEFUNCTION,buf.write)
        c.setopt(c.VERBOSE, True)
        c.setopt(pycurl.USERPWD,getConfig('allowedUser1','UserName','str')+':'+getConfig('allowedUser1','Password','str'))
        c.perform()

        http_code = c.getinfo(pycurl.HTTP_CODE)
        #judge get success.
        if http_code != 200:
            return None

        #get the data from json.
        if (len(buf.getvalue())>0):
            s = buf.getvalue()
            localOrderInfo = json.loads(buf.getvalue())
        else:
            localOrderInfo =  None
        buf.close()
        c.close()

        logger.debug("get localOrderInfo success.")

        #we need change the data structure, so the html show simple.
        if localOrderInfo is not None:
            localOrderInfo = flatOrderInfoOrder(localOrderInfo)

            print localOrderInfo
        return localOrderInfo
    except pycurl.error, error:
        logger.error("exception occur, see the traceback.log")

        #异常写入日志文件.
        f = open('traceback.txt','a')
        traceback.print_exc()
        traceback.print_exc(file = f)
        f.flush()
        f.close()

        errno, errstr = error
        print 'An error occurred: ', errstr
    else:
        pass
    finally:
        pass


# 获取CEM问题所有的问题
def GetRacorderQuestionUrl(fid):
    """get the order info from REST """
    try:
        logger = getLogger()
        logger.debug("start GET RacorderQuestion Info according fid id.")

        if fid is None:
            return None

        buf = cStringIO.StringIO() #define in function.
        c = pycurl.Curl()
        localURL = getConfig('RESTService','irecorderQuestionUrl','str')+fid
        localURL = str(localURL)
        c.setopt(pycurl.URL,localURL)
        c.setopt(c.WRITEFUNCTION,buf.write)
        c.setopt(c.VERBOSE, True)
        c.setopt(pycurl.USERPWD,getConfig('allowedUser1','UserName','str')+':'+getConfig('allowedUser1','Password','str'))
        c.perform()

        http_code = c.getinfo(pycurl.HTTP_CODE)
        #judge get success.
        if http_code != 200:
            return None

        #get the data from json.
        if (len(buf.getvalue())>0):
            s = buf.getvalue()
            localRacorderQuestion = json.loads(buf.getvalue())
        else:
            localRacorderQuestion=  None
        buf.close()
        c.close()

        logger.debug("get localOrderInfo success.")

        #we need change the data structure, so the html show simple.
        if localRacorderQuestion is not None:
            #localRacorderQuestion = flatOrderInfoOrder(localRacorderQuestion)
             return localRacorderQuestion
    except pycurl.error, error:
        logger.error("exception occur, see the traceback.log")

        #异常写入日志文件.
        f = open('traceback.txt','a')
        traceback.print_exc()
        traceback.print_exc(file = f)
        f.flush()
        f.close()

        errno, errstr = error
        print 'An error occurred: ', errstr
    else:
        pass
    finally:
        pass

#获取单个录音的问题
def GetRacorderQuestionByfilename(filename):
    """get the order info from REST """
    try:
        logger = getLogger()
        logger.debug("start GET RacorderQuestion Info according fid id.")

        if filename is None:
            return None

        buf = cStringIO.StringIO() #define in function.
        c = pycurl.Curl()
        localURL = getConfig('RESTService','irecorderscoreUrl','str')+"?filename="+filename
        localURL = str(localURL)
        c.setopt(pycurl.URL,localURL)
        c.setopt(c.WRITEFUNCTION,buf.write)
        c.setopt(c.VERBOSE, True)
        c.setopt(pycurl.USERPWD,getConfig('allowedUser1','UserName','str')+':'+getConfig('allowedUser1','Password','str'))
        c.perform()

        http_code = c.getinfo(pycurl.HTTP_CODE)
        #judge get success.
        if http_code != 200:
            return None

        #get the data from json.
        if (len(buf.getvalue())>0):
            s = buf.getvalue()
            localRacorderQuestion = json.loads(buf.getvalue())
        else:
            localRacorderQuestion=  None
        buf.close()
        c.close()

        logger.debug("get localOrderInfo success.")

        #we need change the data structure, so the html show simple.
        if localRacorderQuestion is not None:
        #localRacorderQuestion = flatOrderInfoOrder(localRacorderQuestion)
            return localRacorderQuestion
    except pycurl.error, error:
        logger.error("exception occur, see the traceback.log")

        #异常写入日志文件.
        f = open('traceback.txt','a')
        traceback.print_exc()
        traceback.print_exc(file = f)
        f.flush()
        f.close()

        errno, errstr = error
        print 'An error occurred: ', errstr
    else:
        pass
    finally:
        pass

#录音问题Post
def postRacorderQuestionContact(storageData):
    try:
        logger = getLogger()
        logger.debug("start POST Order Info according contact id.")

        jsonData = storageData;
        #print storageData
        #dictData = json.loads(storageData)
        #jsonData =  json.dumps(dictData)



        #jsonData =  eval(jsonData)
        #jsonData =  json.dumps(jsonData)



        print  jsonData;
        #print jsonData

        buf = cStringIO.StringIO()
        c = pycurl.Curl()
        localURL = getConfig('RESTService','irecorderscoreUrl','str')
        localURL = str(localURL)
        c.setopt(pycurl.URL,localURL)
        c.setopt(pycurl.HTTPHEADER,['Content-Type: application/json','Content-Length: '+str(len(jsonData))])
        c.setopt(c.VERBOSE, True)
        c.setopt(pycurl.CUSTOMREQUEST,"POST")
        c.setopt(pycurl.POSTFIELDS,jsonData)
        c.setopt(c.WRITEFUNCTION,buf.write)
        c.setopt(pycurl.USERPWD,getConfig('allowedUser1','UserName','str')+':'+getConfig('allowedUser1','Password','str'))
        c.perform()

        #TODO: how to show succes code? 200 or OK?
        http_code = c.getinfo(pycurl.HTTP_CODE)
        #judge post success.
        if http_code != 200:
            return None

        logger.debug(buf.getvalue())
        retStr = buf.getvalue()

        buf.close()
        c.close()

        logger.debug("post OrderInfo success.")
        return retStr

    except pycurl.error, error:
        logger.error("exception occur, see the traceback.log")

        #异常写入日志文件.
        f = open('traceback.txt','a')
        traceback.print_exc()
        traceback.print_exc(file = f)
        f.flush()
        f.close()

        errno, errstr = error
        print 'An error occurred: ', errstr
    else:
        pass
    finally:
        pass
# 进行保存的动作
class RacorderSave:
    def POST(self,filename):

        #传入参数
        data = web.data();
        #retStr 返回值
        retStr= postRacorderQuestionContact(data);
        print retStr;
        return retStr;

    def GET(self,filename):
        pass


#ToDo:从Service 调出录音问题的所有的题目
#现在用的是默认的集合值
def GetRacorderQuestion():
    subitem = [{"subitemname":"0","subitemvalue":"0"},{"subitemname":"1","subitemvalue":"1"},{"subitemname":"2","subitemvalue":"2"}]
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


    return dicrqscoscr




