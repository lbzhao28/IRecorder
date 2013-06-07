__author__ = 'Johann Wong'
#coding=UTF-8
import sys
import os
sys.path.append(os.getcwd()+'\\ModuleObj')
from ModuleObj.iRecorderQuestionModuleObj import iRecorderQuestionModuleObj
from logHelper import getLogger

class iRecorderQuestionLogicObj:
    """
    录音打分系统-录音问卷问题资源逻辑业务处理类
    author:J.Wong
    """
    def getiRecorderQuestionByFileFid(self,fid):
        """
        通过fid查找到录音问题资源
        author: J.Wong
        args: fid,string 问卷ID
        return: iRecorderList,list 对应的录音资源list
        """
        logger = getLogger()
        logger.debug("start iRecordeQuestionLogicObj.getiRecorderQuestionByFileFid")
        moduleObj = iRecorderQuestionModuleObj()
        iRecorderQuestionDicList = moduleObj.getiRecorderQuestionByFid(fid)
        if iRecorderQuestionDicList is None:
            return None
        if isinstance(iRecorderQuestionDicList, basestring):
            return  iRecorderQuestionDicList
        iRecorderQuestionList = []
        for iRecorderQuestionDic in iRecorderQuestionDicList:
            iRecorderQuestion = self.__iRecorderQuestionDic2Json(iRecorderQuestionDic)
            iRecorderQuestion["questionCount"] = moduleObj.getQuestionCount(iRecorderQuestionDic["ITEMID"])
            iRecorderQuestionList.append(iRecorderQuestion)
        return  iRecorderQuestionList

    def __iRecorderQuestionDic2Json(self,iRecorderQuestionDic):
        """
        将数据库dict映射为JSON格式的dict，并转换部分字段为string以及中文转码
        author: J.Wong
        args: iRecorderQuestionDic,dict 查询数据库后获得的单条数据的dict
        return: JSON,dict 对应资源说明文档之JSON格式的dict
        """
        return {
            'fid':iRecorderQuestionDic['FID'],
            'itemID':iRecorderQuestionDic['ITEMID'],
            'itemDesc':iRecorderQuestionDic['ITEMDESC'].decode('gbk').encode('utf8'),
            'itemPerc':iRecorderQuestionDic['ITEMPERC'],
            'hasRemark':iRecorderQuestionDic['HASREMARK']
        }