__author__ = 'stone'
#coding=UTF-8

from configobj import ConfigObj
import  RacorderClient
import os

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

def getRecorderConfigPage():
    """get the recorder page config file"""

    #just return json.
    #configPage = ConfigObj('recorderPagesConf.conf')

    #return a config list
    #configPage = ConfigObj()
    configPage = RecorderConfigPage();
#
#    #
#    configPage['hasShowScore'] = 'yes'
#    #
#    configPage['recorderScore'] = {}
#    configPage['recorderScore']['rowNumber'] = '1'
#    configPage['recorderScore']['itemCount'] = '4'
#
#    qBaseName = 'Q'
#    for i in range(4):
#        qName = qBaseName + str(i)
#        configPage['recorderScore'][qName] = {}
#        configPage['recorderScore'][qName]['titleText'] = '开场白(真诚问候，专业身份与多美滋的关系 15%)' + str(i)
#        configPage['recorderScore'][qName]['titleType'] = 'label'
#        configPage['recorderScore'][qName]['titleCss'] = 'label label-normal'
#        configPage['recorderScore'][qName]['dataType'] = 'input'
#        configPage['recorderScore'][qName]['dataShowType'] = 'radio'
#        configPage['recorderScore'][qName]['dataName'] = 'POLICYHOLDER_USR_SEX'+str(i)
#        configPage['recorderScore'][qName]['mustHave'] = 'no'
#
#        configPage['recorderScore'][qName]['radio'] = {}
#
#        radioBaseName = 'radio'
#        for j in range(i+1):
#            sectionRadio = {
#                'titleType': 'label',
#                'titleCss': 'radio inline',
#                'inDataType': 'label',
#                'inDataCss': 'label',
#                'inDataText': str(j),
#                'inDataValue': str(j),
#                'inDataID': 'PolicyInformation_txtSexMan'+str(j),
#            }
#            radioName = radioBaseName + str(j)
#            configPage['recorderScore'][qName]['radio'][radioName] = sectionRadio
#
#            #another write.
#            #configPage['recorderScore'][qName]['radio']['radio1'] = {}
#            #configPage['recorderScore'][qName]['radio']['radio1']['titleType'] = 'label'
#            #configPage['recorderScore'][qName]['radio']['radio1']['titleCss'] = 'radio inline'
#            #configPage['recorderScore'][qName]['radio']['radio1']['inDataType'] = 'label'
#            #configPage['recorderScore'][qName]['radio']['radio1']['inDataCss'] = 'label'
#            #configPage['recorderScore'][qName]['radio']['radio1']['inDataText'] = '1'
#            #configPage['recorderScore'][qName]['radio']['radio1']['inDataValue'] = '0'
#            #configPage['recorderScore'][qName]['radio']['radio1']['inDataID'] = 'PolicyInformation_txtSexMan'

    return configPage

# 创建录音打分的页面
def RecorderConfigPage():
    tRacorderQuestions = RacorderClient.GetRacorderQuestion();
    if tRacorderQuestions is None or len(tRacorderQuestions)==0 :
        return render.error(error = 'no filename')
    else:
    #return a config list
        configPage = ConfigObj()



        SBaseName = 'Q' # 序号

        i = 0
        for item in tRacorderQuestions:
            itemDesc = item["itemDesc"];   # 问题描述
            itemPerc = item["itemPerc"];   # 问题百分比
            itemID = item["itemID"];
            txtSCORE =(float(itemPerc) * 2)/100;
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
            configPage[Sname]['class']["hasRealDataValue"] = '2'
            configPage[Sname]['class']["onClick"] = 'radioclick(this)'





            configPage[Sname]['class']['radio'] = {}
            subitems = item["subitems"];   #问题答案子类
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
            configPage[Sname]['percent']['controlText'] = itemPerc +"%"
            configPage[Sname]['percent']['controlType'] = 'labelName'
            configPage[Sname]['percent']['controlCss'] = 'label label-normal'
            configPage[Sname]['percent']['controlName'] = 'lblPERCENTName'+str(i)
            configPage[Sname]['percent']['controlID'] = 'lblPERCENTId'+str(i)



            configPage[Sname]['defen'] = {}
            configPage[Sname]['defen']['controlText'] = "得分"
            configPage[Sname]['defen']['controlType'] = 'label'
            configPage[Sname]['defen']['controlCss'] = 'label label-normal'
            configPage[Sname]['defen']['controlName'] = 'lblDEFEN'+str(i)
            configPage[Sname]['defen']['mustHave'] = 'no'

            configPage[Sname]['score'] = {}
            configPage[Sname]['score']['controlType'] = 'input'
            configPage[Sname]['score']['controlCss'] = 'input-mini'
            configPage[Sname]['score']['controlShowType'] = 'text'
            configPage[Sname]['score']['controlName'] = 'txtSCORE'
            configPage[Sname]['score']['controlID'] = 'idSCORE'+str(i)
            configPage[Sname]['score']['placeholder'] = '得分'
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
            configPage[Sname]['memoText']['hasRealDataValue'] = ''
            configPage[Sname]['memoText']['placeholder'] = '备注'


        print configPage

    return configPage





def getConfigFile(inFileName):
    """get the Static config file"""

    configFile = ConfigObj(inFileName)
    return configFile

if __name__ == "__main__":
    getRecorderConfigPage()
