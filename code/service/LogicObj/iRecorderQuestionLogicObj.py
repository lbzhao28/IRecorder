__author__ = 'Administrator'
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
        args: fid,string 录音文件名
        return: iRecorderList,list 对应的录音资源list
        """
        logger = getLogger()
        logger.debug("start iRecordeQuestionLogicObj.getiRecorderQuestionByFileFid")
        moduleObj = iRecorderQuestionModuleObj()
        iRecorderQuestionDicList = moduleObj.getiRecorderQuestionByFid(fid)
        if iRecorderQuestionDicList is None:
            return None;
        iRecorderQuestionList = [];
        for iRecorderQuestionDic in iRecorderQuestionDicList:
            iRecorderQuestion = self.__iRecorderQuestionDic2Json(iRecorderQuestionDic)
            iRecorderQuestion["questionCount"] = moduleObj.getQuestionCount(iRecorderQuestionDic["ITEMID"])
            iRecorderQuestionList.append(iRecorderQuestion)
        return  iRecorderQuestionList

    def __iRecorderQuestionDic2Json(self,iRecorderQuestionDic):
        return {
            'fid':iRecorderQuestionDic['FID'],
            'itemID':iRecorderQuestionDic['ITEMID'],
            'itemDesc':unicode(iRecorderQuestionDic['ITEMDESC'],"cp936"),
            'itemPerc':iRecorderQuestionDic['ITEMPERC'],
            'hasRemark':iRecorderQuestionDic['HASREMARK']
        }