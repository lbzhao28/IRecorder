__author__ = 'stone'
#coding=UTF-8

import pycurl
import cStringIO
import json

import traceback
from configData import getConfig
from logHelper import getLogger
import  web

# 根据条件查询录音
def GetRaccemSearchUrl(instartdate, inenddate, incalltype, inagentid, intelno, inavailablein, totalmin, intotalmax,
                       inchanneldn, inteldnis,inpageno, inpagesize,spendmin,spendmax):
    """get the order info from REST """
    try:
        logger = getLogger()
        logger.debug("start GET RaccemSearch Info ")
        localURL = ""

        if instartdate is not None and instartdate != '':
            localURL = localURL + '&startdate=' + instartdate

        if inenddate is not None and inenddate != '':
            localURL = localURL + '&enddate=' + inenddate

        if  inagentid is not None and inagentid != '':
            localURL = localURL + '&agentid=' + inagentid

        if incalltype is not None and incalltype != '':
            localURL += '&calltype=' + incalltype

        if intelno is not None and intelno != '':
            localURL += '&telno=' + intelno

        if  inavailablein is not None and inavailablein != '':
            localURL = localURL + '&available=' + inavailablein

        if totalmin is not None and totalmin != '':
            localURL = localURL + '&totalmin=' + totalmin

        if intotalmax is not None and intotalmax != '':
            localURL = localURL + '&totalmax=' + intotalmax

        if inchanneldn is not None and inchanneldn != '':
            localURL = localURL + '&channeldn=' + inchanneldn

        if inteldnis is not None and inteldnis != '':
            localURL = localURL + '&teldnis=' + inteldnis


        if inpageno is not None and inpageno != '':
            localURL = localURL + '&pageno=' + inpageno

        if inpagesize is not None and inpagesize != '':
            localURL = localURL + '&pagesize=' + inpagesize


        if spendmin is not None and spendmin != '':
            localURL = localURL + '&spendmin=' + spendmin

        if spendmax is not None and spendmax != '':
            localURL = localURL + '&spendmax=' + spendmax
        print localURL;
        buf = cStringIO.StringIO() #define in function.
        c = pycurl.Curl()
        if localURL != '':
            localURL = getConfig('RESTService', 'irecorderSearchList', 'str') + '?' + localURL
           # localURL = "http://127.0.0.1:8088/irecorderservice/irecorderlist?&pageno=1&pagesize=10"
            localURL = str(localURL)
            print localURL
            c.setopt(pycurl.URL, localURL)
            c.setopt(c.WRITEFUNCTION, buf.write)
            c.setopt(c.VERBOSE, True)
            c.setopt(pycurl.USERPWD,
                getConfig('allowedUser1', 'UserName', 'str') + ':' + getConfig('allowedUser1', 'Password', 'str'))
            c.perform()

            http_code = c.getinfo(pycurl.HTTP_CODE)
            #judge get success.
            if http_code != 200:
                return None

            #get the data from json.
            if (len(buf.getvalue()) > 0):
                s = buf.getvalue()
                localRecorderSearchlist = json.loads(buf.getvalue())
            else:
                localRecorderSearchlist = None
            buf.close()
            c.close()
            logger.debug("get localOrderInfo success.")
            print localURL
        else:
            localRecorderSearchlist = None

        return localRecorderSearchlist
    except pycurl.error, error:
        logger.error("exception occur, see the traceback.log")

        f = open('traceback.txt', 'a')
        traceback.print_exc()
        traceback.print_exc(file=f)
        f.flush()
        f.close()

        errno, errstr = error
        print 'An error occurred: ', errstr
    else:
        pass
    finally:
        pass


#数据录音查询有多少条数据
def GetRaccemSearchUrlcount(instartdate, inenddate, incalltype, inagentid, intelno, inavailablein, totalmin, intotalmax,
                       inchanneldn, inteldnis,spendmin,spendmax):
    """get the GetRaccemSearchUrlcount info from REST """
    try:
        logger = getLogger()
        logger.debug("start GET RaccemSearch Info ")
        localURL = ""

        if instartdate is not None and instartdate != '':
            localURL = localURL + '&startdate=' + instartdate

        if inenddate is not None and inenddate != '':
            localURL = localURL + '&enddate=' + inenddate

        if  inagentid is not None and inagentid != '':
            localURL = localURL + '&agentid=' + inagentid

        if incalltype is not None and incalltype != '':
            localURL += '&calltype=' + incalltype

        if intelno is not None and intelno != '':
            localURL += '&telno=' + intelno

        if  inavailablein is not None and inavailablein != '':
            localURL = localURL + '&available=' + inavailablein

        if totalmin is not None and totalmin != '':
            localURL = localURL + '&totalmin=' + totalmin

        if intotalmax is not None and intotalmax != '':
            localURL = localURL + '&intotalmax=' + intotalmax

        if spendmin is not None and spendmin != '':
            localURL = localURL + '&spendmin=' + spendmin

        if spendmax is not None and spendmax != '':
            localURL = localURL + '&spendmax=' + spendmax

        if inchanneldn is not None and inchanneldn != '':
            localURL = localURL + '&channeldn=' + inchanneldn

        if inteldnis is not None and inteldnis != '':
            localURL = localURL + '&teldnis=' + inteldnis

        print localURL;
        buf = cStringIO.StringIO() #define in function.
        c = pycurl.Curl()
        if localURL != '':
            localURL = getConfig('RESTService', 'irecorderSearchListCount', 'str') + '?' + localURL
            # localURL = "http://127.0.0.1:8088/irecorderservice/irecorderlist?&pageno=1&pagesize=10"
            localURL = str(localURL)
            print localURL
            c.setopt(pycurl.URL, localURL)
            c.setopt(c.WRITEFUNCTION, buf.write)
            c.setopt(c.VERBOSE, True)
            c.setopt(pycurl.USERPWD,
                getConfig('allowedUser1', 'UserName', 'str') + ':' + getConfig('allowedUser1', 'Password', 'str'))
            c.perform()

            http_code = c.getinfo(pycurl.HTTP_CODE)
            #judge get success.
            if http_code != 200:
                return None

            #get the data from json.
            if (len(buf.getvalue()) > 0):
                s = buf.getvalue()
                localRecorderSearchlistCount = json.loads(buf.getvalue())
            else:
                localRecorderSearchlistCount = None
            buf.close()
            c.close()
            logger.debug("get GetRaccemSearchUrlcount success.")
            print localURL
        else:
            localRecorderSearchlistCount = None

        return localRecorderSearchlistCount
    except pycurl.error, error:
        logger.error("exception occur, see the traceback.log")

        f = open('traceback.txt', 'a')
        traceback.print_exc()
        traceback.print_exc(file=f)
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

        logger.debug("get GetRacorderQuestionUrl success.")

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

        logger.debug("get GetRacorderQuestionUrl success.")

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

#录音问题保存
def RacorderQuestionContact(storageData,retPost):
    try:
        logger = getLogger()
        logger.debug("start POST RacorderQuestionContact Info according contact id.")

        jsonData = storageData;

        print  jsonData;
        #print jsonData

        buf = cStringIO.StringIO()
        c = pycurl.Curl()
        localURL = getConfig('RESTService','irecorderscoreUrl','str')
        localURL = str(localURL)
        c.setopt(pycurl.URL,localURL)
        c.setopt(pycurl.HTTPHEADER,['Content-Type: application/json','Content-Length: '+str(len(jsonData))])
        c.setopt(c.VERBOSE, True)
        c.setopt(pycurl.CUSTOMREQUEST,retPost)
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

        logger.debug("RacorderQuestionContact success.")
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

def Login(username,password):
    ret = False
    try:
        logger = getLogger()
        logger.debug("start GET RacorderQuestion Info according fid id.")

        if username is not None and username != '':
            localURL = '&id=' + username

        if password is not None and password != '':
            localURL = localURL + '&pwd=' + password

        buf = cStringIO.StringIO() #define in function.
        c = pycurl.Curl()
        localURL = getConfig('RESTService','irecorderloginUrl','str')+"?"+localURL
        localURL = str(localURL)
        print localURL
        c.setopt(pycurl.URL,localURL)
        c.setopt(c.WRITEFUNCTION,buf.write)
        c.setopt(c.VERBOSE, True)
        c.setopt(pycurl.USERPWD,getConfig('allowedUser1','UserName','str')+':'+getConfig('allowedUser1','Password','str'))
        c.perform()

        http_code = c.getinfo(pycurl.HTTP_CODE)
        #judge get success.
        if http_code != 200:
            return False

        #get the data from json.
        if (len(buf.getvalue())>0):
            s = buf.getvalue()
            localRacorderQuestion = json.loads(buf.getvalue())
        buf.close()
        c.close()
        logger.debug("get GetRacorderQuestionUrl success.")
        #we need change the data structure, so the html show simple.
        if localRacorderQuestion is not None:
        #localRacorderQuestion = flatOrderInfoOrder(localRacorderQuestion)
            ret = localRacorderQuestion["message"]
    except pycurl.error, error:
        logger.error("exception occur, see the traceback.log")

        #异常写入日志文件.
        f = open('traceback.txt','a')
        traceback.print_exc()
        traceback.print_exc(file = f)
        f.flush()
        f.close()

        ret = False;
        print 'An error occurred: ', "login"
    else:
        return ret
    finally:
        return ret;

#录音质检进行保存的动作
class RacorderSave:
    def POST(self,retPost):
        if retPost is not None and str(retPost).strip() !="":
            strPost = str(retPost)
            #传入参数
            data = web.data();
            #retStr 返回值
            retStr= RacorderQuestionContact(data,strPost)
            if retStr is not None and len(retStr)>0:
                retStrJson = eval(retStr)
                retStrJson = retStrJson["message"]
                retStrJson["fileNameNo"] = str(retStrJson["fileName"]).replace(".","").replace("_","")
                print retStrJson
                retStrJson = json.dumps(retStrJson)
                web.header('Content-Type', 'application/json')
                print retStrJson
                return retStrJson;
            else:
                return None;
        else:
            return None;

    def GET(self,filename):
        pass

class ReportExport:
    def POST(self,retPost):
        localwebs = web.input();
        #startdate enddate agentid totalmin totalmax rater

        startdate = str(localwebs["startdate"]);
        enddate =  str(localwebs["enddate"]);
        agentid = str(localwebs["agentid"]);
        totalmin =  str(localwebs["totalmin"]);
        totalmax = str(localwebs["totalmax"]);
        rater = str(localwebs["rater"]);

        localURL = "";
        if startdate is not None and startdate != '':
            localURL = localURL + '&startdate=' + startdate

        if enddate is not None and enddate != '':
            localURL = localURL + '&enddate=' + enddate

        if  agentid is not None and agentid != '':
            localURL = localURL + '&agentid=' + agentid

        if totalmin is not None and totalmin != '':
            localURL += '&totalmin=' + totalmin

        if totalmax is not None and totalmax != '':
            localURL += '&totalmax=' + totalmax

        if  rater is not None and rater != '':
            localURL = localURL + '&rater=' + rater

        try:
            logger = getLogger()
            logger.debug("start POST RacorderQuestionContact Info according contact id.")

            #print jsonData
            buf = cStringIO.StringIO() #define in function.
            c = pycurl.Curl()
            localURL = getConfig('RESTService','irecorderReportExportUrl','str')+"?"+localURL
            localURL = str(localURL)
            print localURL
            c.setopt(pycurl.URL,localURL)
            c.setopt(c.WRITEFUNCTION,buf.write)
            c.setopt(c.VERBOSE, True)
            c.setopt(pycurl.USERPWD,getConfig('allowedUser1','UserName','str')+':'+getConfig('allowedUser1','Password','str'))
            c.perform()
            #TODO: how to show succes code? 200 or OK?
            http_code = c.getinfo(pycurl.HTTP_CODE)
            #judge post success.
            if http_code != 200:
                return None

            retStr = json.loads(buf.getvalue())
            #retStrData = eval(retStr);

            buf.close()
            c.close()

            logger.debug("RacorderQuestionContact success.")
            retStr = json.dumps(retStr)

            web.header('Content-Type', 'application/json')
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
    def GET(self,retPost):
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




