__author__ = 'JohannWong'
#coding=UTF-8
import sys
import os
sys.path.append(os.getcwd()+'\\ModuleObj')
from ModuleObj.iRecorderScoreModuleObj import iRecorderScoreModuleObj
from logHelper import getLogger

class iRecorderScoreLogicObj:
    """

    """
    def getiRecorderScoreByFileName(self,filename):
        logger = getLogger()
        logger.debug("start iRecordeScoreLogicObj.getiRecordeScoreByFileName")
        moduleObj = iRecordeScoreLogicModuleObj()
        iRecorderScoreDicList = moduleObj.getiRecordeScoreByFileName(filename)
        if iRecorderScoreDicList is None:
            return None;
        iRecorderScoreList = [];
        for iRecorderScoreDic in iRecorderScoreDicList:
            iRecorderScore = self.__iRecorderScoreDic2Json(iRecorderScoreDic)
            iRecorderScoreList.append(iRecorderScore)
        return  iRecorderScoreList

    def postiRecorderScoreByJson(self,scoreJson):
        logger = getLogger()
        logger.debug("start iRecordeScoreLogicObj.postiRecorderScoreByJson")
        moduleObj = iRecordeScoreLogicModuleObj()
        scoreDic = self.__iRecorderScoreJson2Dic(scoreJson)
        filename = moduleObj.postiRecorderScoreByJson(scoreDic)
        if filename is None or len(filename) <= 0:
            return None
        iRecorderScoreList = self.getiRecorderScoreByFileName(filename)
        return iRecorderScoreList

    def __iRecorderScoreDic2Json(self,iRecorderDic):
        return {
            'fileName':iRecorderDic['RECKEY'],
            'raters':iRecorderDic['RATERS'],
            'total':iRecorderDic['TOTAL'],
            'reterTime':iRecorderDic['UPDT'],
            'remark':iRecorderDic['REMARK'],
            'scrvals':iRecorderDic['SCRVALS'],
            'scrval0':iRecorderDic['SCRVAL0'],
            'scrval1':iRecorderDic['SCRVAL1'],
            'scrval2':iRecorderDic['SCRVAL2'],
            'scrval3':iRecorderDic['SCRVAL3'],
            'scrval4':iRecorderDic['SCRVAL4'],
            'scrval5':iRecorderDic['SCRVAL5'],
            'scrval6':iRecorderDic['SCRVAL6'],
            'scrval7':iRecorderDic['SCRVAL7'],
            'scrval8':iRecorderDic['SCRVAL8'],
            'scrval9':iRecorderDic['SCRVAL9'],
            'scrval10':iRecorderDic['SCRVAL10'],
            'scrval11':iRecorderDic['SCRVAL11'],
            'scrval12':iRecorderDic['SCRVAL12'],
            'scrval13':iRecorderDic['SCRVAL13'],
            'scrval14':iRecorderDic['SCRVAL14'],
            'scrval15':iRecorderDic['SCRVAL15']
        }

    def __iRecorderScoreJson2Dic(self,iRecorderJson):
        return {
            'RECKEY':iRecorderJson['fileName'],
            'RATERS':iRecorderJson['raters'],
            'TOTAL':iRecorderJson['total'],
            'UPDT':iRecorderJson['reterTime'],
            'REMARK':iRecorderJson['remark'],
            'SCRVALS':iRecorderJson['scrvals'],
            'SCRVAL0':iRecorderJson['scrval0'],
            'SCRVAL1':iRecorderJson['scrval1'],
            'SCRVAL2':iRecorderJson['scrval2'],
            'SCRVAL3':iRecorderJson['scrval3'],
            'SCRVAL4':iRecorderJson['scrval4'],
            'SCRVAL5':iRecorderJson['scrval5'],
            'SCRVAL6':iRecorderJson['scrval6'],
            'SCRVAL7':iRecorderJson['scrval7'],
            'SCRVAL8':iRecorderJson['scrval8'],
            'SCRVAL9':iRecorderJson['scrval9'],
            'SCRVAL10':iRecorderJson['scrval10'],
            'SCRVAL11':iRecorderJson['scrval11'],
            'SCRVAL12':iRecorderJson['scrval12'],
            'SCRVAL13':iRecorderJson['scrval13'],
            'SCRVAL14':iRecorderJson['scrval14'],
            'SCRVAL15':iRecorderJson['scrval15']
        }