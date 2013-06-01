__author__ = 'stone'
#coding=UTF-8

from configobj import ConfigObj
import  RacorderClient
import  web;
import  json;
import os

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
    """get the page config file"""


    #print os.getcwd()
    #os.chdir('..')
    #os.chdir('D:\Stone\Python\Python_Insurance')
    #print os.getcwd()

    configPage = ConfigObj('pagesConf.conf')

    #configPagePolicyHolder_Usr = configPage['PolicyHolder_Usr']
    #dictFirst = configPagePolicyHolder_Usr.dict()
    #print dictFirst
    #j = 2
    #for j in range(j):
    #    for member in dictFirst:
    #        if 'titleText' in dictFirst[member]:
    #            print member
    #            dictSecond = dictFirst[member]
    #            print dictSecond
    #            break
    #    dictFirst.pop(member)
            #i = i+1
            #print i
        #for item in configPagePolicyHolder_Usr[member]:
        #    print configPagePolicyHolder_Usr[member][item]
        #for item in member:
        #    print member[item]
    #print configPage
    #print configPagePolicyHolder_Usr
    #configPagePolicyHolder_Usr = configPage['PolicyHolder_Usr']
    #print configPagePolicyHolder_Usr

    #print configPagePolicyHolder_Usr.as_int( 'rowNumber')
    #print configPage.as_bool("hasPolicyHolder_Usr")
    return configPage

def getRecorderConfigPage(filename):
    configPage = RecorderConfigPage(filename);
    return configPage

# 创建录音打分的页面
def RecorderConfigPage(filename):

    #从Session 中取得filename 名字
    localtRacorderQuestion = {};

    if filename is not None or filename.strip != '':
        #单条录音的文件的问题额答案
        tRacorderQuestion = RacorderClient.GetRacorderQuestionByfilename(filename);
        if tRacorderQuestion is not None and len(tRacorderQuestion)>0 and tRacorderQuestion["message"] is not None:
            localtRacorderQuestion = tRacorderQuestion["message"];


    Recordertotal = 0;   #总分数
    RecorderscrvalsEval = [];  # 问题答案的json
    QuestionNote ="";          # 备注字段

    print localtRacorderQuestion;
    configPage = ConfigObj()

    web.ctx.session.session_QuestionNote = ""; #首先清空Session

    if localtRacorderQuestion.keys() > 0 and len(localtRacorderQuestion)>0:
        Recordertotal = localtRacorderQuestion["total"];
        strRecorderscrvals = localtRacorderQuestion["scrvals"];
        Recorderscrvals =  strRecorderscrvals.replace("@","'");
        RecorderscrvalsEval = eval(Recorderscrvals);
        QuestionNote =localtRacorderQuestion["remark"]

        web.ctx.session.session_QuestionNote =  QuestionNote # 将Note 用Sesssion 保存起来





    # 获取问卷信息
    tRacorderQuestionsMesage = RacorderClient.GetRacorderQuestionUrl("CEM");
    if tRacorderQuestionsMesage is None or len(tRacorderQuestionsMesage)==0 :
        return render.error(error = '连接数据库失败')
    else:
        tRacorderQuestions = tRacorderQuestionsMesage["message"];
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





    return configPage

def getConfigFile(inFileName):
    """get the Static config file"""

    configFile = ConfigObj(inFileName)
    return configFile

if __name__ == "__main__":
    getRecorderConfigPage()
