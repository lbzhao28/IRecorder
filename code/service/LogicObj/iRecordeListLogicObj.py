__author__ = 'JohannWong'
#coding=UTF-8
from iRecorderListModuleObj import iRecorderListModuleObj
from logHelper import getLogger
"""

"""
class iRecorderListLogicObj:
    def getiRecorderListByFileName(self,filename):
        logger = getLogger()
        logger.debug("start iRecorderListLogicObj.getiRecorderListByFileName")
        iRecorderDicList = iRecorderListModuleObj.getiRecorderListByFileName(filename)
        iRecorderList = [];
        for iRecorderDic in iRecorderDicList:
            iRecorder = self.__iRecorderDic2Json(iRecorderDic)
            iRecorderList.append(iRecorder)
        return  iRecorderList

    def getiRecorderListByParams(self,params):
        logger = getLogger()
        logger.debug("start iRecorderListLogicObj.getiRecorderListByParams")
        iRecorderDicList = iRecorderListModuleObj.getiRecorderListByFileName(params)
        iRecorderList = [];
        for iRecorderDic in iRecorderDicList:
            iRecorder = self.__iRecorderDic2Json(iRecorderDic)
            iRecorderList.append(iRecorder)
        return  iRecorderList

    def __iRecorderDB2JSON(self,iRecorderDic):
        return {
            'hostName':iRecorderDic['HOSTNAME'],
            'fileName':iRecorderDic['FILENAME'],
            'channelNO':iRecorderDic['CHANNELNO'],
            'startTime':iRecorderDic['STARTTIME'],
            'spendTime':iRecorderDic['SPENDTIME'],
            'available':iRecorderDic['AVAILABLE'],
            'agentID':iRecorderDic['AGENTID'],
            'filePath':iRecorderDic['FILEPATH'],
            'callType':iRecorderDic['CALLTYPE'],
            'telNO':iRecorderDic['TELNO'],
            'channelDN':iRecorderDic['CHANNELDN'],
            'telDNIS':iRecorderDic['TELDNIS'],
            'callID':iRecorderDic['CALLID'],
            'endTime':iRecorderDic['ENDTIME'],
            'total':iRecorderDic['TOTAL']
        }