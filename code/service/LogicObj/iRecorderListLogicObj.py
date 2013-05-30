__author__ = 'JohannWong'
#coding=UTF-8
import sys
import os
sys.path.append(os.getcwd()+'\\ModuleObj')
from ModuleObj.iRecorderListModuleObj import iRecorderListModuleObj
from logHelper import getLogger

class iRecorderListLogicObj:
    """
    录音打分系统-录音资源逻辑业务处理类
    author:J.Wong
    """
    def getiRecorderListByFileName(self,filename):
        """
        通过录音文件名查找到录音资源
        author: J.Wong
        args: filename,string 录音文件名
        return: iRecorderList,list 对应的录音资源list
        """
        logger = getLogger()
        logger.debug("start iRecorderListLogicObj.getiRecorderListByFileName")
        moduleObj = iRecorderListModuleObj()
        iRecorderDicList = moduleObj.getiRecorderListByFileName(filename)
        if iRecorderDicList is None:
            return None
        if isinstance(iRecorderDicList, basestring):
            return  iRecorderDicList
        iRecorderList = []
        for iRecorderDic in iRecorderDicList:
            iRecorder = self.__iRecorderDB2JSON(iRecorderDic)
            iRecorderList.append(iRecorder)
        return  iRecorderList

    def getiRecorderListByParams(self,params):
        """
        通过其他查询条件查找到录音资源
        author: J.Wong
        args: params,string 查询录音的querystring，格式参见doc目录下“座席录音资源接口说明文档.xlsx”
        return: iRecorderList,list 对应的录音资源list
        """
        logger = getLogger()
        logger.debug("start iRecorderListLogicObj.getiRecorderListByParams")
        moduleObj = iRecorderListModuleObj()
        iRecorderDicList = moduleObj.getiRecorderListByParams(params)
        if iRecorderDicList is None:
            return None
        if isinstance(iRecorderDicList, basestring):
            return  iRecorderDicList
        iRecorderList = []
        for iRecorderDic in iRecorderDicList:
            iRecorder = self.__iRecorderDB2JSON(iRecorderDic)
            iRecorderList.append(iRecorder)
        return  iRecorderList

    def __iRecorderDB2JSON(self,iRecorderDic):
        """
        将数据库dict映射为JSON格式的dict，并转换部分字段为string
        author: J.Wong
        args: iRecorderDic,dict 查询数据库后获得的单条数据的dict
        return: JSON,dict 对应资源说明文档之JSON格式的dict
        """
        return {
            'hostName':iRecorderDic['HOSTNAME'],
            'fileName':iRecorderDic['FILENAME'],
            'channelNO':iRecorderDic['CHANNELNO'],
            'startTime':iRecorderDic['STARTTIME'].strftime('%Y-%m-%d %H:%M:%S'),
            'spendTime':iRecorderDic['SPENDTIME'],
            'available':iRecorderDic['AVAILABLE'],
            'agentID':iRecorderDic['AGENTID'],
            'filePath':iRecorderDic['FILEPATH'],
            'callType':iRecorderDic['CALLTYPE'],
            'telNO':iRecorderDic['TELNO'],
            'channelDN':iRecorderDic['CHANNELDN'],
            'telDNIS':iRecorderDic['TELDNIS'],
            'callID':iRecorderDic['CALLID'],
            'endTime':iRecorderDic['ENDTIME'].strftime('%Y-%m-%d %H:%M:%S'),
            'total':str(iRecorderDic['TOTAL'])
        }