__author__ = 'JohannWong'
#coding=UTF-8
import sys
import os
sys.path.append(os.getcwd()+'\\ModuleObj')
from ModuleObj.iRecorderScoreModuleObj import iRecorderScoreModuleObj
from logHelper import getLogger

class iRecorderScoreLogicObj:
    """
    录音打分系统-打分资源逻辑业务处理类
    author:J.Wong
    """
    def getiRecorderScoreByFileName(self,filename):
        """
        通过filename查找到录音打分资源
        author: J.Wong
        args: fid,string 录音文件名
        return: iRecorderList,list 对应的录音资源list
        """
        logger = getLogger()
        logger.debug("start iRecordeScoreLogicObj.getiRecorderScoreByFileName")
        moduleObj = iRecorderScoreModuleObj()
        iRecorderScoreDic = moduleObj.getiRecorderScoreByFileName(filename)
        if iRecorderScoreDic is None:
            return None
        if isinstance(iRecorderScoreDic, basestring):
            return  iRecorderScoreDic

        iRecorderScore = self.__iRecorderScoreDic2Json(iRecorderScoreDic)
        return  iRecorderScore

    def postiRecorderScoreByJson(self,scoreJson):
        """
        通过JSON新增一条录音打分信息
        author: J.Wong
        args: scoreJson,dict 封装新录音打分信息的JSON，格式参见doc目录下“座席录音质检资源接口说明文档.xlsx”
        return: iRecorderScore,dict 插入成功时返回该数据查询结果的JSON
        """
        logger = getLogger()
        logger.debug("start iRecordeScoreLogicObj.postiRecorderScoreByJson")
        moduleObj = iRecorderScoreModuleObj()
        scoreDic = self.__iRecorderScoreJson2Dic(scoreJson)
        if  'fileName' in scoreJson.keys():
            filename = moduleObj.postiRecorderScoreByJson(scoreDic)
        else:
            return 'Must set the value of fileName.'
        if filename is None or len(filename) <= 0:
            return 'Post iRecorderScore failed.'
        if filename.find('wav'):
            iRecorderScore = self.getiRecorderScoreByFileName(filename)
        else:
            return filename
        return iRecorderScore

    def putiRecorderScoreByJson(self,scoreJson):
        """
        通过JSON更新一条录音打分信息
        author: J.Wong
        args: scoreJson,dict 封装新录音打分信息的JSON，格式参见doc目录下“座席录音质检资源接口说明文档.xlsx”
        return: iRecorderScore,dict 更新成功时返回该数据查询结果的JSON
        """
        logger = getLogger()
        logger.debug("start iRecordeScoreLogicObj.putiRecorderScoreByJson")
        moduleObj = iRecorderScoreModuleObj()
        scoreDic = self.__iRecorderScoreJson2Dic(scoreJson)
        if  'fileName' in scoreJson.keys():
            filename = moduleObj.putiRecorderScoreByJson(scoreDic)
        else:
            return 'Must set the value of fileName.'
        if filename is None or len(filename) <= 0:
            return 'Put iRecorderScore failed.'
        if filename.find('wav'):
            iRecorderScore = self.getiRecorderScoreByFileName(filename)
        else:
            return filename
        return iRecorderScore

    def __iRecorderScoreDic2Json(self,iRecorderScoreDic):
        """
        将数据库dict映射为JSON格式的dict，并转换部分字段为string以及中文转码
        author: J.Wong
        args: iRecorderScoreDic,dict 查询数据库后获得的单条数据的dict
        return: JSON,dict 对应资源说明文档之JSON格式的dict
        """
        return {
            'fileName':iRecorderScoreDic['RECKEY'],
            'raters':iRecorderScoreDic['RATERS'],
            'total':str(iRecorderScoreDic['TOTAL']),
            'reterTime':iRecorderScoreDic['UPDT'],
            'remark':iRecorderScoreDic['REMARK'],
            'scrvals':iRecorderScoreDic['SCRVALS'],
            'scrval0':iRecorderScoreDic['SCRVAL0'],
            'scrval1':iRecorderScoreDic['SCRVAL1'],
            'scrval2':iRecorderScoreDic['SCRVAL2'],
            'scrval3':iRecorderScoreDic['SCRVAL3'],
            'scrval4':iRecorderScoreDic['SCRVAL4'],
            'scrval5':iRecorderScoreDic['SCRVAL5'],
            'scrval6':iRecorderScoreDic['SCRVAL6'],
            'scrval7':iRecorderScoreDic['SCRVAL7'],
            'scrval8':iRecorderScoreDic['SCRVAL8'],
            'scrval9':iRecorderScoreDic['SCRVAL9'],
            'scrval10':iRecorderScoreDic['SCRVAL10'],
            'scrval11':iRecorderScoreDic['SCRVAL11'],
            'scrval12':iRecorderScoreDic['SCRVAL12'],
            'scrval13':iRecorderScoreDic['SCRVAL13'],
            'scrval14':iRecorderScoreDic['SCRVAL14'],
            'scrval15':iRecorderScoreDic['SCRVAL15']
        }

    def __iRecorderScoreJson2Dic(self,iRecorderJson):
        """
        将数据库dict映射为JSON格式的dict，并自动补足没有传递的key
        author: J.Wong
        args: iRecorderJson,dict 对应资源说明文档之JSON格式的dict
        return: JSON,dict 对应数据库命名的dict
        """
        if 'raters' not in iRecorderJson.keys():
            iRecorderJson['raters'] = ""
        if 'total' not in iRecorderJson.keys():
            iRecorderJson['total'] = ""
        if 'reterTime' not in iRecorderJson.keys():
            iRecorderJson['reterTime'] = ""
        if 'remark' not in iRecorderJson.keys():
            iRecorderJson['remark'] = ""
        if 'scrvals' not in iRecorderJson.keys():
            iRecorderJson['scrvals'] = ""
        if 'scrval0' not in iRecorderJson.keys():
            iRecorderJson['scrval0'] = ""
        if 'scrval1' not in iRecorderJson.keys():
            iRecorderJson['scrval1'] = ""
        if 'scrval2' not in iRecorderJson.keys():
            iRecorderJson['scrval2'] = ""
        if 'scrval3' not in iRecorderJson.keys():
            iRecorderJson['scrval3'] = ""
        if 'scrval4' not in iRecorderJson.keys():
            iRecorderJson['scrval4'] = ""
        if 'scrval5' not in iRecorderJson.keys():
            iRecorderJson['scrval5'] = ""
        if 'scrval6' not in iRecorderJson.keys():
            iRecorderJson['scrval6'] = ""
        if 'scrval7' not in iRecorderJson.keys():
            iRecorderJson['scrval7'] = ""
        if 'scrval8' not in iRecorderJson.keys():
            iRecorderJson['scrval8'] = ""
        if 'scrval9' not in iRecorderJson.keys():
            iRecorderJson['scrval9'] = ""
        if 'scrval10' not in iRecorderJson.keys():
            iRecorderJson['scrval10'] = ""
        if 'scrval11' not in iRecorderJson.keys():
            iRecorderJson['scrval11'] = ""
        if 'scrval12' not in iRecorderJson.keys():
            iRecorderJson['scrval12'] = ""
        if 'scrval13' not in iRecorderJson.keys():
            iRecorderJson['scrval13'] = ""
        if 'scrval14' not in iRecorderJson.keys():
            iRecorderJson['scrval14'] = ""
        if 'scrval15' not in iRecorderJson.keys():
            iRecorderJson['scrval15'] = ""

        return {
            'RECKEY':iRecorderJson['fileName'].encode('utf8'),
            'RATERS':iRecorderJson['raters'].encode('utf8'),
            'TOTAL':iRecorderJson['total'].encode('utf8'),
            'UPDT':iRecorderJson['reterTime'].encode('utf8'),
            'REMARK':iRecorderJson['remark'].encode('utf8'),
            'SCRVALS':iRecorderJson['scrvals'].encode('utf8'),
            'SCRVAL0':iRecorderJson['scrval0'].encode('utf8'),
            'SCRVAL1':iRecorderJson['scrval1'].encode('utf8'),
            'SCRVAL2':iRecorderJson['scrval2'].encode('utf8'),
            'SCRVAL3':iRecorderJson['scrval3'].encode('utf8'),
            'SCRVAL4':iRecorderJson['scrval4'].encode('utf8'),
            'SCRVAL5':iRecorderJson['scrval5'].encode('utf8'),
            'SCRVAL6':iRecorderJson['scrval6'].encode('utf8'),
            'SCRVAL7':iRecorderJson['scrval7'].encode('utf8'),
            'SCRVAL8':iRecorderJson['scrval8'].encode('utf8'),
            'SCRVAL9':iRecorderJson['scrval9'].encode('utf8'),
            'SCRVAL10':iRecorderJson['scrval10'].encode('utf8'),
            'SCRVAL11':iRecorderJson['scrval11'].encode('utf8'),
            'SCRVAL12':iRecorderJson['scrval12'].encode('utf8'),
            'SCRVAL13':iRecorderJson['scrval13'].encode('utf8'),
            'SCRVAL14':iRecorderJson['scrval14'].encode('utf8'),
            'SCRVAL15':iRecorderJson['scrval15'].encode('utf8')
        }