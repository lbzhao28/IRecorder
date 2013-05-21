__author__ = 'stone'
#coding=UTF-8

from configobj import ConfigObj
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
    configPage = ConfigObj()

    #
    configPage['hasShowScore'] = 'yes'
    #
    configPage['recorderScore'] = {}
    configPage['recorderScore']['rowNumber'] = '1'
    configPage['recorderScore']['itemCount'] = '4'

    qBaseName = 'Q'
    for i in range(4):
        qName = qBaseName + str(i)
        configPage['recorderScore'][qName] = {}
        configPage['recorderScore'][qName]['titleText'] = '开场白(真诚问候，专业身份与多美滋的关系 15%)' + str(i)
        configPage['recorderScore'][qName]['titleType'] = 'label'
        configPage['recorderScore'][qName]['titleCss'] = 'label label-normal'
        configPage['recorderScore'][qName]['dataType'] = 'input'
        configPage['recorderScore'][qName]['dataShowType'] = 'radio'
        configPage['recorderScore'][qName]['dataName'] = 'POLICYHOLDER_USR_SEX'+str(i)
        configPage['recorderScore'][qName]['mustHave'] = 'no'

        configPage['recorderScore'][qName]['radio'] = {}

        radioBaseName = 'radio'
        for j in range(i+1):
            sectionRadio = {
                'titleType': 'label',
                'titleCss': 'radio inline',
                'inDataType': 'label',
                'inDataCss': 'label',
                'inDataText': str(j),
                'inDataValue': str(j),
                'inDataID': 'PolicyInformation_txtSexMan'+str(j),
            }
            radioName = radioBaseName + str(j)
            configPage['recorderScore'][qName]['radio'][radioName] = sectionRadio

            #another write.
            #configPage['recorderScore'][qName]['radio']['radio1'] = {}
            #configPage['recorderScore'][qName]['radio']['radio1']['titleType'] = 'label'
            #configPage['recorderScore'][qName]['radio']['radio1']['titleCss'] = 'radio inline'
            #configPage['recorderScore'][qName]['radio']['radio1']['inDataType'] = 'label'
            #configPage['recorderScore'][qName]['radio']['radio1']['inDataCss'] = 'label'
            #configPage['recorderScore'][qName]['radio']['radio1']['inDataText'] = '1'
            #configPage['recorderScore'][qName]['radio']['radio1']['inDataValue'] = '0'
            #configPage['recorderScore'][qName]['radio']['radio1']['inDataID'] = 'PolicyInformation_txtSexMan'

    return configPage

def getTestData():
    subitem = [{"subitemname":"1","subitemvalue":"1"},{"subitemname":"2","subitemvalue":"2"},{"subitemname":"3","subitemvalue":"3"}]
    dicrqscoscr = []
    recordequestion = {"itemID":"1","itemDesc":"开场白(真诚问候，专业身份与多美滋的关系 15%)","itemPerc":"10","subitems":subitem}

    dicrqscoscr.append(recordequestion)

    recordequestion = {"itemID":"2","itemDesc":"建议（评估结果 40%）","itemPerc":"10","subitems":subitem}
    dicrqscoscr.append(recordequestion)

    recordequestion = {"itemID":"3","itemDesc":"开场白,(表达同理心,对妈妈/孕妇的关心 自然真诚 15%)","itemPerc":"10","subitems":subitem}

    dicrqscoscr.append(recordequestion)
    recordequestion = {"itemID":"4","itemDesc":"开场白,(告之目的和利益，明确告知致电的目的或利益 2，并确认生日，预产期15%)","itemPerc":"10","subitems":subitem}
    dicrqscoscr.append(recordequestion)


    recordequestion = {"itemID":"5","itemDesc":"开场白(真诚问候，专业身份与多美滋的关系 15%)","itemPerc":"10","subitems":subitem}

    dicrqscoscr.append(recordequestion)

    recordequestion = {"itemID":"6","itemDesc":"建议（评估结果 40%）","itemPerc":"10","subitems":subitem}
    dicrqscoscr.append(recordequestion)

    recordequestion = {"itemID":"7","itemDesc":"开场白,(表达同理心,对妈妈/孕妇的关心 自然真诚 15%)","itemPerc":"10","subitems":subitem}

    dicrqscoscr.append(recordequestion)
    recordequestion = {"itemID":"8","itemDesc":"开场白,(告之目的和利益，明确告知致电的目的或利益 2，并确认生日，预产期15%)","itemPerc":"10","subitems":subitem}
    dicrqscoscr.append(recordequestion)

    recordequestion = {"itemID":"9","itemDesc":"开场白(真诚问候，专业身份与多美滋的关系 15%)","itemPerc":"10","subitems":subitem}

    dicrqscoscr.append(recordequestion)

    recordequestion = {"itemID":"10","itemDesc":"建议（评估结果 40%）","itemPerc":"10","subitems":subitem}
    dicrqscoscr.append(recordequestion)

    recordequestion = {"itemID":"11","itemDesc":"开场白,(表达同理心,对妈妈/孕妇的关心 自然真诚 15%)","itemPerc":"10","subitems":subitem}

    dicrqscoscr.append(recordequestion)
    recordequestion = {"itemID":"12","itemDesc":"开场白,(告之目的和利益，明确告知致电的目的或利益 2，并确认生日，预产期15%)","itemPerc":"10","subitems":subitem}
    dicrqscoscr.append(recordequestion)

    dicrqscoscrS = json.dumps(dicrqscoscr)

    return dicrqscoscrS

def getConfigFile(inFileName):
    """get the Static config file"""

    configFile = ConfigObj(inFileName)
    return configFile

if __name__ == "__main__":
    getRecorderConfigPage()
