__author__ = 'Administrator'
#coding=UTF-8
import sys
import os
sys.path.append(os.getcwd()+'\\ModuleObj')
from ModuleObj.iRecorderQuestionModuleObj import iRecorderQuestionModuleObj
from logHelper import getLogger

class iRecorderQuestionLogicObj:
    """

    """
    def getiRecorderListByFileFid(self,fid):
        logger = getLogger()
        logger.debug("start iRecordeQuestionLogicObj.getiRecorderListByFileFid")
        moduleObj = iRecorderQuestionModuleObj()
        iRecorderQuestionDicList = moduleObj.getiRecorderQuestionByFid(fid)
        if iRecorderQuestionDicList is None:
            return None;
        iRecorderQuestionList = [];
        for iRecorderQuestionDic in iRecorderQuestionDicList:
            iRecorderQuestion = self.__iRecorderQuestionDic2Json(iRecorderQuestionDic)
            iRecorderQuestion["questionCount"] = moduleObj.getQuestionCount(iRecorderQuestion["ITEMID"])
            iRecorderQuestionList.append(iRecorderQuestion)
        return  iRecorderQuestionList

    def __iRecorderQuestionDic2Json(self,iRecorderQuestionDic):
        return {
            'fid':iRecorderQuestionDic['FID'],
            'itemID':iRecorderQuestionDic['ITEMID'],
            'itemDesc':iRecorderQuestionDic['ITEMDESC'],
            'itemPerc':iRecorderQuestionDic['ITEMPERC'],
            'hasRemark':iRecorderQuestionDic['HASREMARK']
        }