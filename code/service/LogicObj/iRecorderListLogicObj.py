__author__ = 'JohannWong'
#coding=UTF-8
import sys
import os
sys.path.append(os.getcwd()+'\\ModuleObj')
from ModuleObj.iRecorderListModuleObj import iRecorderListModuleObj
from logHelper import getLogger

class iRecorderListLogicObj:
    """

    """
    def getiRecorderListByFileName(self,filename):
        logger = getLogger()
        logger.debug("start iRecorderListLogicObj.getiRecorderListByFileName")
        moduleObj = iRecorderListModuleObj()
        iRecorderDicList = moduleObj.getiRecorderListByFileName(filename)
        if iRecorderDicList is None:
            return None;
        iRecorderList = [];
        for iRecorderDic in iRecorderDicList:
            iRecorder = self.__iRecorderDB2JSON(iRecorderDic)
            iRecorderList.append(iRecorder)
        return  iRecorderList

    def getiRecorderListByParams(self,params):
        logger = getLogger()
        logger.debug("start iRecorderListLogicObj.getiRecorderListByParams")
        moduleObj = iRecorderListModuleObj()
        iRecorderDicList = moduleObj.getiRecorderListByParams(params)
        if iRecorderDicList is None:
            return None;
        iRecorderList = [];
        for iRecorderDic in iRecorderDicList:
            iRecorder = self.__iRecorderDB2JSON(iRecorderDic)
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