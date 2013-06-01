__author__ = 'zhuangkun'

import pycurl
import cStringIO
import json

import traceback
from configData import getConfig
from logHelper import getLogger
import  web

def GetRaccemSearchUrl(instartdate, inenddate, incalltype, inagentid, intelno, inavailablein, totalmin, intotalmax,
                       inchanneldn, inteldnis, inpageno, inpagesize):
    """get the order info from REST """
    try:
        logger = getLogger()
        logger.debug("start GET RaccemSearch Info ")
        localURL = ''

        if instartdate is None:
            return None
        if instartdate != '':
            localURL = localURL + '&startdate=' + instartdate

        if inenddate is None:
            return None
        if inenddate != '':
            localURL = localURL + '&enddate=' + inenddate

        if inagentid is None:
            return None
        if inagentid != '':
            localURL = localURL + '&agentid=' + inagentid

        if incalltype is None:
            return None
        if incalltype != '':
            localURL += '&calltype=' + incalltype
        if intelno is None:
            return None
        if intelno != '':
            localURL += '&telno=' + intelno
        if inavailablein is None:
            return None
        if inavailablein != '':
            localURL = localURL + '&available=' + inavailablein
        if totalmin is None:
            return None
        if totalmin != '':
            localURL = localURL + '&totalmin=' + totalmin
        if intotalmax is None:
            return None
        if intotalmax != '':
            localURL = localURL + '&intotalmax=' + intotalmax
        if inchanneldn is None:
            return None
        if inchanneldn != '':
            localURL = localURL + '&channeldn=' + inchanneldn
        if inteldnis is None:
            return None
        if inteldnis != '':
            localURL = localURL + '&teldnis=' + inteldnis
        if inpageno is None:
            return None
        if inpageno != '':
            localURL = localURL + '&pageno=' + inpageno
        if inpagesize is None:
            return None
        if inpagesize != '':
            localURL = localURL + '&pagesize=' + inpagesize

        buf = cStringIO.StringIO() #define in function.
        c = pycurl.Curl()
        if localURL != '':
            localURL = getConfig('RESTService', 'irecorderSearchListusr', 'str') + '?' + localURL
            print localURL
        else:
            localURL = getConfig('RESTService', 'irecorderSearchListusr', 'str')
        localURL = str(localURL)
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

        #we need change the data structure, so the html show simple.
        if localRecorderSearchlist is not None:
        #localRacorderQuestion = flatOrderInfoOrder(localRacorderQuestion)
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

