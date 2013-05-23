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
        if iRecorderScoreDicList == None:
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
        if filename == None or len(filename) <= 0:
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
            'scrvals':iRecorderJson['SCRVALS'],
            'scrval0':iRecorderJson['SCRVAL0'],
            'scrval1':iRecorderJson['SCRVAL1'],
            'scrval2':iRecorderJson['SCRVAL2'],
            'scrval3':iRecorderJson['SCRVAL3'],
            'scrval4':iRecorderJson['SCRVAL4'],
            'scrval5':iRecorderJson['SCRVAL5'],
            'scrval6':iRecorderJson['SCRVAL6'],
            'scrval7':iRecorderJson['SCRVAL7'],
            'scrval8':iRecorderJson['SCRVAL8'],
            'scrval9':iRecorderJson['SCRVAL9'],
            'scrval10':iRecorderJson['SCRVAL10'],
            'scrval11':iRecorderJson['SCRVAL11'],
            'scrval12':iRecorderJson['SCRVAL12'],
            'scrval13':iRecorderJson['SCRVAL13'],
            'scrval14':iRecorderJson['SCRVAL14'],
            'scrval15':iRecorderJson['SCRVAL15']
        }