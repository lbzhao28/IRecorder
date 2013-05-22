__author__ = 'JohannWong'
#coding=UTF-8
from iRecordeScoreModuleObj import iRecordeScoreModuleObj
from logHelper import getLogger
"""

"""
class iRecordeScoreLogicObj:
    def getiRecordeScoreByFileName(self,filename):
        logger = getLogger()
        logger.debug("start iRecordeScoreLogicObj.getiRecordeScoreByFileName")
        iRecorderScoreDicList = iRecordeScoreLogicModuleObj.getiRecordeScoreByFileName(filename)
        iRecorderScoreList = [];
        for iRecorderScoreDic in iRecorderScoreDicList:
            iRecorderScore = self.__iRecorderScoreDic2Json(iRecorderScoreDic)
            iRecorderScoreList.append(iRecorderScore)
        return  iRecorderScoreList

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