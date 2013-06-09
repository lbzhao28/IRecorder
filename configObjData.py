__author__ = 'stone'
#coding=UTF-8
from logHelper import getLogger
from configobj import ConfigObj
import  RacorderClient
import  web;
import  json;
import os
import traceback

from web.contrib.template import render_mako

# input_encoding and output_encoding is important for unicode
# template file. Reference:
# http://www.makotemplates.org/docs/documentation.html#unicode
render = render_mako(
    directories = ['templates'],
    input_encoding = 'utf-8',
    output_encoding = 'utf-8',
)

def getConfigPage():
    configPage = ConfigObj('pagesConf.conf')
    return configPage

def getRecorderConfigPage(tRacorderQuestion):
    configPage = RecorderConfigPage(tRacorderQuestion);
    return configPage

# 创建录音打分的页面
def RecorderConfigPage(tRacorderQuestion):

    try:
        logger = getLogger();
        localtRacorderQuestion = {};


        #单条录音的文件的问题额答案
        if tRacorderQuestion is not None and len(tRacorderQuestion)>0 and tRacorderQuestion["message"] is not None:
            localtRacorderQuestion = tRacorderQuestion["message"];


        Recordertotal = 0;   #总分数
        RecorderscrvalsEval = [];  # 问题答案的json
        QuestionNote ="";          # 备注字段

        configPage = ConfigObj()


        #localtRacorderQuestion 问题答案信息
        if localtRacorderQuestion.keys() > 0 and len(localtRacorderQuestion)>0:
            Recordertotal = localtRacorderQuestion["total"];
            strRecorderscrvals = localtRacorderQuestion["scrvals"];
            Recorderscrvals =  strRecorderscrvals.replace("@","'");
            RecorderscrvalsEval = eval(Recorderscrvals);

        # 获取问卷信息
        tRacorderQuestionsMesage = RacorderClient.GetRacorderQuestionUrl("CEM");
        if tRacorderQuestionsMesage is None or len(tRacorderQuestionsMesage)==0 :
            logger.error("获取问卷失败：连接数据库失败")

        else:
            tRacorderQuestions = tRacorderQuestionsMesage["message"];
            web.ctx.session.tRacorderQuestions_count = len(tRacorderQuestions);
            logger.info("问题的个数：tRacorderQuestions_count:",  web.ctx.session.tRacorderQuestions_count)
            #return a config list
            SBaseName = 'Q' # 序号

            i = 0
            for item in tRacorderQuestions:     # 把问题的项绑定到config 中
                itemRadioAnswer = "";           # 单个radio 的答案值
                txtSCORE = "";                  # 单个备注
                txtNote = "";                   # 总备注
                itemDesc = item["itemDesc"];   # 问题描述
                itemPerc = item["itemPerc"];   # 问题百分比
                itemID = item["itemID"];        # 问题编号
                hasRemark = item["hasRemark"];  #问题类型

                RecorderQuestionAnswer = {};
                for localitem in  RecorderscrvalsEval:  # localitem 单个问题的答案
                    if localitem['questionID'] == str(itemID):
                        RecorderQuestionAnswer = localitem
                        break;

                if RecorderQuestionAnswer is not None and len(RecorderQuestionAnswer)>0:
                    itemRadioAnswer = RecorderQuestionAnswer["subitemAnswer"];
                    txtSCORE = RecorderQuestionAnswer["score"];
                    txtNote = RecorderQuestionAnswer["note"];


                # i 用于控制前台的 jquery 中获得的ID
                i=i+1

                Sname = SBaseName + str(i)

                configPage[Sname] = {}

                configPage[Sname]['sequence'] = {}
                configPage[Sname]['sequence']['controlText'] =i
                configPage[Sname]['sequence']['controlType'] = 'labelName'
                configPage[Sname]['sequence']['controlCss'] = 'label label-normal'
                #configPage[Sname]['sequence']['dataType'] = 'input'
                configPage[Sname]['sequence']['controlName'] = 'lblSEQUENCEName'
                configPage[Sname]['sequence']['controlID'] = 'lblSEQUENCEID'+str(i)
                configPage[Sname]['sequence']['mustHave'] = 'no'



                configPage[Sname]['question'] = {}
                configPage[Sname]['question']['controlText'] =itemDesc
                configPage[Sname]['question']['controlType'] = 'labelName'
                configPage[Sname]['question']['controlCss'] = 'label label-normal'
                #configPage[Sname]['question']['dataType'] = 'input'
                configPage[Sname]['question']['controlName'] = 'lblQUESTIONNAME'
                configPage[Sname]['question']['controlID'] = itemID
                configPage[Sname]['question']['mustHave'] = 'no'


                configPage[Sname]['pinji'] = {}
                configPage[Sname]["pinji"]['controlText'] ='评级'
                configPage[Sname]["pinji"]['controlType'] = 'label'
                configPage[Sname]["pinji"]['controlCss'] = 'label label-normal'
                configPage[Sname]["pinji"]['dataType'] = 'input'
                configPage[Sname]["pinji"]['controlName'] = 'lblPINJI'+str(i)
                configPage[Sname]["pinji"]['mustHave'] = 'no'


                configPage[Sname]['class'] = {}
                configPage[Sname]["class"]['controlType'] = 'input'
                configPage[Sname]["class"]['controlShowType'] = 'radio'
                configPage[Sname]["class"]['controlName'] = 'radioCLASS'+str(i)

                if itemRadioAnswer is not None and itemRadioAnswer.strip()!='':
                    configPage[Sname]['class']["hasRealDataValue"] = int(itemRadioAnswer)
                else:
                    configPage[Sname]['class']["hasRealDataValue"] = ""
                configPage[Sname]['class']["onClick"] = 'radioclick(this)'

                configPage[Sname]['class']['radio'] = {}
                questionCount = item["questionCount"];   #问题答案子类

                subitems = [];

                for jj in range(questionCount):
                    subitem = {"subitemname":jj,"subitemvalue":jj }
                    subitems.append(subitem)
                radioBaseName = 'radio'
                j = 0
                for itemj in subitems:
                    j=j+1;
                    text = itemj["subitemname"]  # 显示值
                    value = itemj["subitemvalue"] # value值
                    sectionRadio = {
                        'titleType': 'label',
                        'titleCss': 'radio inline',
                        'inDataType': 'label',
                        'inDataCss': 'label',
                        'inDataText':text,
                        'inDataValue': value,
                        'inDataID': 'rl_answer'+str(j),
                        }
                    radioName = radioBaseName + str(j)

                    configPage[Sname]['class']['radio'][radioName] = sectionRadio

                configPage[Sname]['zhanbi'] = {}
                configPage[Sname]['zhanbi']['controlText'] = '占比'
                configPage[Sname]['zhanbi']['controlType'] = 'label'
                configPage[Sname]['zhanbi']['controlCss'] = 'label label-normal'
                configPage[Sname]['zhanbi']['controlName'] = 'label label-normal'


                itemPerc = item["itemPerc"] #百分比
                configPage[Sname]['percent'] = {}
                configPage[Sname]['percent']['controlText'] = str(itemPerc) +"%"
                configPage[Sname]['percent']['controlType'] = 'labelName'
                configPage[Sname]['percent']['controlCss'] = 'label label-normal'
                configPage[Sname]['percent']['controlName'] = 'lblPERCENTName'+str(i)
                configPage[Sname]['percent']['controlID'] = 'lblPERCENTId'+str(i)



                configPage[Sname]['defen'] = {}
                configPage[Sname]['defen']['controlText'] = "得分"
                configPage[Sname]['defen']['controlType'] = 'labelName'
                configPage[Sname]['defen']['controlCss'] = 'label label-normal'
                configPage[Sname]['defen']['controlID'] = 'defen'+str(i)
                if not hasRemark is None:
                    configPage[Sname]['defen']['controlName'] = 'hasRemark'+str(hasRemark)
                else:
                    configPage[Sname]['defen']['controlName'] = 'hasRemark'




                configPage[Sname]['defen']['mustHave'] = 'no'

                configPage[Sname]['score'] = {}
                configPage[Sname]['score']['controlType'] = 'input'
                configPage[Sname]['score']['controlCss'] = 'input-mini'
                configPage[Sname]['score']['controlShowType'] = 'text'
                configPage[Sname]['score']['controlName'] = 'txtSCORE'
                configPage[Sname]['score']['controlID'] = 'idSCORE'+str(i)
                configPage[Sname]['score']['hasRealDataValue'] = txtSCORE

                configPage[Sname]['memo'] = {}
                configPage[Sname]['memo']['controlText'] = "备注"
                configPage[Sname]['memo']['controlType'] = 'label'
                configPage[Sname]['memo']['controlCss'] = 'label label-normal'
                configPage[Sname]['memo']['controlName'] = 'lblMEMO'+str(i)
                configPage[Sname]['memo']['mustHave'] = 'no'

                configPage[Sname]['memoText'] = {}
                configPage[Sname]['memoText']['controlType'] = 'input'
                configPage[Sname]['memoText']['controlCss'] = 'input-large'
                configPage[Sname]['memoText']['controlShowType'] = 'text'
                configPage[Sname]['memoText']['controlName'] = 'txtMemo'
                configPage[Sname]['memoText']['controlID'] = 'idMemo'+str(i)
                configPage[Sname]['memoText']['hasRealDataValue'] = txtNote;
                configPage[Sname]['memoText']['placeholder'] = '备注'               # 如果有这个属性则可以进行编辑
    except Exception,ex:
                logger.error("exception occur, see the traceback.log")
                logger.error("获取录音文件失败:"+ex.message)
                #异常写入日志文件.
                f = open('Logs/traceback.txt','a')
                traceback.print_exc()
                traceback.print_exc(file = f)
                f.flush()
                f.close()
                return None;
    finally:
        pass

    return configPage

def getConfigFile(inFileName):
    """get the Static config file"""

    configFile = ConfigObj(inFileName)
    return configFile

if __name__ == "__main__":
    getRecorderConfigPage()
