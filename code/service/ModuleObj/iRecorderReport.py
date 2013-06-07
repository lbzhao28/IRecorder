__author__ = 'Johann Wong'
#encoding:utf-8
from xlwt import Workbook,easyxf
from dbConnection import msSqlConnectutf
from logHelper import getLogger
import traceback
import time

class iRecorderReport:
    """
    录音打分系统报表导出
    author:J.Wong
    args: params,string 查询报表的querystring
    return: iRecorderReportList,list 对应的录音报表
    """
    def exportReport(self,params):
        """
        获取报表并导出至excel文档
        author: J.Wong
        """
        try:
            logger = getLogger()
            logger.debug("start iRecorderReport.exportReport")
            workbook = Workbook(encoding='utf-8')
            sheet1 = workbook.add_sheet('录音打分报表')
            row_head = sheet1.row(0)
            row_head.height = 7050

            row_head_style = easyxf(
                'font: name SimSun, bold true;'
                'borders: left thin, right thin, top thin, bottom thin;'
                'alignment: wrap true;'
                'pattern: pattern solid, fore_colour white;'
            )

            row_head.set_cell_text(0,'员工ID',row_head_style)
            row_head.set_cell_text(1,'录音时间',row_head_style)
            row_head.set_cell_text(2,'打分人ID',row_head_style)
            row_head.set_cell_text(3,'打分时间',row_head_style)
            row_head.set_cell_text(4,'开场白(真诚问候，专业身份与多美滋的关系 15%)',row_head_style)
            row_head.set_cell_text(5,'开场白,(表达同理心,对妈妈/孕妇的关心 自然真诚 15%)',row_head_style)
            row_head.set_cell_text(6,'开场白,(告之目的和利益，明确告知致电的目的或利益 2，并确认生日，预产期15%)',row_head_style)
            row_head.set_cell_text(7,'开场白,(征得同意，得到“许可”的意思才可以继续 15%）',row_head_style)
            row_head.set_cell_text(8,'开场白总分',row_head_style)
            row_head.set_cell_text(9,'提问（目的性提问30%）',row_head_style)
            row_head.set_cell_text(10,'提问（优阶及100日概念30%）',row_head_style)
            row_head.set_cell_text(11,'提问（分析了解客户相关状况30%）',row_head_style)
            row_head.set_cell_text(12,'提问（总结关键信息30%）',row_head_style)
            row_head.set_cell_text(13,'提问总分',row_head_style)
            row_head.set_cell_text(14,'建议（建议选择方案30%）',row_head_style)
            row_head.set_cell_text(15,'建议（运用经验30%）',row_head_style)
            row_head.set_cell_text(16,'建议（介绍产品，自然过渡1，特点1，优势1，好处1 30%）',row_head_style)
            row_head.set_cell_text(17,'建议（评估结果 30%）',row_head_style)
            row_head.set_cell_text(18,'建议总分',row_head_style)
            row_head.set_cell_text(19,'结束（约定下次致电时间 5%）',row_head_style)
            row_head.set_cell_text(20,'结束总分',row_head_style)
            row_head.set_cell_text(21,'沟通技巧（语音2，语速2，语调2，理解4 15%）',row_head_style)
            row_head.set_cell_text(22,'沟通技巧（消费者反馈 5%）',row_head_style)
            row_head.set_cell_text(23,'沟通技巧总分',row_head_style)
            row_head.set_cell_text(24,'总分',row_head_style)
            row_head.set_cell_text(25,'评语1',row_head_style)
            row_head.set_cell_text(26,'评语2',row_head_style)
            row_head.set_cell_text(27,'评语3',row_head_style)
            row_head.set_cell_text(28,'评语4',row_head_style)
            row_head.set_cell_text(29,'评语5',row_head_style)
            row_head.set_cell_text(30,'评语6',row_head_style)
            row_head.set_cell_text(31,'评语7',row_head_style)
            row_head.set_cell_text(32,'评语8',row_head_style)
            row_head.set_cell_text(33,'评语9',row_head_style)
            row_head.set_cell_text(34,'评语10',row_head_style)
            row_head.set_cell_text(35,'评语11',row_head_style)
            row_head.set_cell_text(36,'评语12',row_head_style)
            row_head.set_cell_text(37,'评语13',row_head_style)
            row_head.set_cell_text(38,'评语14',row_head_style)
            row_head.set_cell_text(39,'评语15',row_head_style)
            row_head.set_cell_text(40,'总评',row_head_style)

            row_content_style = easyxf(
                'font: name SimSun, bold false;'
                'borders: left thin, right thin, top thin, bottom thin;'
                'alignment: wrap true;'
                'pattern: pattern solid, fore_colour white;'
            )

            conn = msSqlConnectutf()
            cur = conn.cursor()
            sqlstr = "SELECT [RECKEY]"\
                     ",[T_RECORDER].[AGENTID]"\
                     ",[T_RECORDER].[STARTTIME]"\
                     ",[RATERS]"\
                     ",[UPDT]"\
                     ",[TOTAL]"\
                     ",[REMARK]"\
                     ",[SCRVALS]"\
                     " FROM [TRQ_SCORE]"\
                     " LEFT JOIN [T_RECORDER]"\
                     " ON [TRQ_SCORE].[RECKEY] = [T_RECORDER].[FILENAME]"\
                     " WHERE 1=1"
            if "startdate" in params.keys() and params["startdate"] is not None:
                sqlstr += " AND [T_RECORDER].[STARTTIME] >= '"+params["startdate"]+"'"
            if "agentid" in params.keys() and params["agentid"] is not None:
                sqlstr += " AND [T_RECORDER].[AGENTID] = '"+params["agentid"]+"'"
            if "totalmin" in params.keys() and params["totalmin"] is not None:
                sqlstr += " AND [TRQ_SCORE].[TOTAL] >= '"+params["totalmin"]+"'"
            if "totalmax" in params.keys() and params["totalmax"] is not None:
                sqlstr += " AND [TRQ_SCORE].[TOTAL] <= '"+params["totalmax"]+"'"
            if "rater" in params.keys() and params["rater"] is not None:
                sqlstr += " AND [T_RECORDER].[RATERS] = '"+params["rater"]+"'"
            sqlstr += " ORDER BY [TRQ_SCORE].[UPDT]"

            cur.execute(sqlstr)
            logger.info("sql:"+str(sqlstr))
            result = []
            i=1

            for row in cur:
                result.append(row)
                row_report = sheet1.row(i)
                row_report.set_cell_text(0,str(row["AGENTID"]),row_content_style)
                row_report.set_cell_text(1,str(row["STARTTIME"]),row_content_style)
                row_report.set_cell_text(2,str(row["RATERS"]),row_content_style)
                row_report.set_cell_text(3,str(row["UPDT"]),row_content_style)
                row_report.set_cell_text(24,str(row["TOTAL"]),row_content_style)
                row_report.set_cell_text(40,str(row["REMARK"]),row_content_style)
                scrstr = row["SCRVALS"]
                scrstr = scrstr.replace("@","'")
                scrvals = eval(scrstr)

                scoreFirst = 0 #开场白总分
                scoreQuestion = 0 #提问总分
                scoreSuggestion = 0 #建议总分
                scoreEnd = 0 #结束总分
                scoreTech = 0 #沟通技巧总分

                for scrval in scrvals:
                    if str(scrval["questionID"]) == 'C001':
                        scoreFirst += float(scrval["score"])
                        row_report.set_cell_number(4,str(scrval["score"]),row_content_style)
                        row_report.set_cell_text(25,str(scrval["note"]),row_content_style)
                    elif str(scrval["questionID"]) == 'C002':
                        scoreFirst += float(scrval["score"])
                        row_report.set_cell_number(5,str(scrval["score"]),row_content_style)
                        row_report.set_cell_text(26,str(scrval["note"]),row_content_style)
                    elif str(scrval["questionID"]) == 'C003':
                        scoreFirst += float(scrval["score"])
                        row_report.set_cell_number(6,str(scrval["score"]),row_content_style)
                        row_report.set_cell_text(27,str(scrval["note"]),row_content_style)
                    elif str(scrval["questionID"]) == 'C004':
                        scoreFirst += float(scrval["score"])
                        row_report.set_cell_number(7,str(scrval["score"]),row_content_style)
                        row_report.set_cell_text(28,str(scrval["note"]),row_content_style)
                    elif str(scrval["questionID"]) == 'C005':
                        scoreQuestion += float(scrval["score"])
                        row_report.set_cell_number(9,str(scrval["score"]),row_content_style)
                        row_report.set_cell_text(29,str(scrval["note"]),row_content_style)
                    elif str(scrval["questionID"]) == 'C006':
                        scoreQuestion += float(scrval["score"])
                        row_report.set_cell_number(10,str(scrval["score"]),row_content_style)
                        row_report.set_cell_text(30,str(scrval["note"]),row_content_style)
                    elif str(scrval["questionID"]) == 'C007':
                        scoreQuestion += float(scrval["score"])
                        row_report.set_cell_number(11,str(scrval["score"]),row_content_style)
                        row_report.set_cell_text(31,str(scrval["note"]),row_content_style)
                    elif str(scrval["questionID"]) == 'C008':
                        scoreQuestion += float(scrval["score"])
                        row_report.set_cell_number(12,str(scrval["score"]),row_content_style)
                        row_report.set_cell_text(32,str(scrval["note"]),row_content_style)
                    elif str(scrval["questionID"]) == 'C009':
                        scoreSuggestion += float(scrval["score"])
                        row_report.set_cell_number(14,str(scrval["score"]),row_content_style)
                        row_report.set_cell_text(33,str(scrval["note"]),row_content_style)
                    elif str(scrval["questionID"]) == 'C010':
                        scoreSuggestion += float(scrval["score"])
                        row_report.set_cell_number(15,str(scrval["score"]),row_content_style)
                        row_report.set_cell_text(34,str(scrval["note"]),row_content_style)
                    elif str(scrval["questionID"]) == 'C011':
                        scoreSuggestion += float(scrval["score"])
                        row_report.set_cell_number(16,str(scrval["score"]),row_content_style)
                        row_report.set_cell_text(35,str(scrval["note"]),row_content_style)
                    elif str(scrval["questionID"]) == 'C012':
                        scoreSuggestion += float(scrval["score"])
                        row_report.set_cell_number(17,str(scrval["score"]),row_content_style)
                        row_report.set_cell_text(36,str(scrval["note"]),row_content_style)
                    elif str(scrval["questionID"]) == 'C013':
                        scoreEnd += float(scrval["score"])
                        row_report.set_cell_number(19,str(scrval["score"]),row_content_style)
                        row_report.set_cell_text(37,str(scrval["note"]),row_content_style)
                    elif str(scrval["questionID"]) == 'C014':
                        scoreTech += float(scrval["score"])
                        row_report.set_cell_number(21,str(scrval["score"]),row_content_style)
                        row_report.set_cell_text(38,str(scrval["note"]),row_content_style)
                    elif str(scrval["questionID"]) == 'C015':
                        scoreTech += float(scrval["score"])
                        row_report.set_cell_number(22,str(scrval["score"]),row_content_style)
                        row_report.set_cell_text(39,str(scrval["note"]),row_content_style)

                row_report.set_cell_number(8,str(scoreFirst),row_content_style)
                row_report.set_cell_number(13,str(scoreQuestion),row_content_style)
                row_report.set_cell_number(18,str(scoreSuggestion),row_content_style)
                row_report.set_cell_number(20,str(scoreEnd),row_content_style)
                row_report.set_cell_number(23,str(scoreTech),row_content_style)
                i += 1

            for j in range(0,40):
                sheet1.col(j).width = 5000
            return result
        except Exception,ex:
            logger.error("exception occur, see the traceback.log")
            logger.error("sql:"+str(sqlstr))
            #异常写入日志文件.
            f = open('Logs/traceback.txt','a')
            traceback.print_exc()
            traceback.print_exc(file = f)
            f.flush()
            f.close()
            return ex.message
        else:
            pass
        finally:
            workbook.save(time.strftime('%Y-%m-%d-%H-%M-%S',time.localtime(time.time()))+".xls")
            conn.close()

if __name__ == "__main__":
    iRecorderReport().exportReport(dict())