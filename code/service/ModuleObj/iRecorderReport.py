__author__ = 'Johann Wong'
#encoding:utf-8
from xlwt import Workbook,easyxf
from dbConnection import msSqlConnectutf

class iRecorderReport:
    """
    录音打分系统报表导出
    author:J.Wong
    """
    def exportReport(self):
        """
        获取报表并导出至excel文档
        author: J.Wong
        """
        workbook = Workbook(encoding='utf-8')
        sheet1 = workbook.add_sheet('录音打分报表')
        row_head = sheet1.row(0)
        row_head.height = 7050

        row_head_style = easyxf(
            'font: name SimSun, bold true;'
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
        row_head.set_cell_text(13,'建议（建议选择方案30%）',row_head_style)
        row_head.set_cell_text(14,'建议（运用经验30%）',row_head_style)
        row_head.set_cell_text(15,'建议（介绍产品，自然过渡1，特点1，优势1，好处1 30%）',row_head_style)
        row_head.set_cell_text(16,'建议（评估结果 30%）',row_head_style)
        row_head.set_cell_text(17,'建议总分',row_head_style)
        row_head.set_cell_text(18,'结束（约定下次致电时间 5%）',row_head_style)
        row_head.set_cell_text(19,'结束总分',row_head_style)
        row_head.set_cell_text(20,'沟通技巧（语音2，语速2，语调2，理解4 15%）',row_head_style)
        row_head.set_cell_text(21,'沟通技巧（消费者反馈 5%）',row_head_style)
        row_head.set_cell_text(22,'沟通技巧总分',row_head_style)
        row_head.set_cell_text(23,'总分',row_head_style)
        row_head.set_cell_text(24,'评语1',row_head_style)
        row_head.set_cell_text(25,'评语2',row_head_style)
        row_head.set_cell_text(26,'评语3',row_head_style)
        row_head.set_cell_text(27,'评语4',row_head_style)
        row_head.set_cell_text(28,'评语5',row_head_style)
        row_head.set_cell_text(29,'评语6',row_head_style)
        row_head.set_cell_text(30,'评语7',row_head_style)
        row_head.set_cell_text(31,'评语8',row_head_style)
        row_head.set_cell_text(32,'评语9',row_head_style)
        row_head.set_cell_text(33,'评语10',row_head_style)
        row_head.set_cell_text(34,'评语11',row_head_style)
        row_head.set_cell_text(35,'评语12',row_head_style)
        row_head.set_cell_text(36,'评语13',row_head_style)
        row_head.set_cell_text(37,'评语14',row_head_style)
        row_head.set_cell_text(38,'评语15',row_head_style)
        row_head.set_cell_text(39,'总评',row_head_style)

        row_content_style = easyxf(
            'font: name SimSun, bold false;'
            'pattern: pattern solid, fore_colour white;'
        )

        conn = msSqlConnectutf()
        sqlstr = "SELECT [RECKEY]"\
                 ",[T_RECORDER].[AGENTID]"\
                 ",[T_RECORDER].[STARTTIME]"\
                 ",[RATERS]"\
                 ",[UPDT]"\
                 ",[TOTAL]"\
                 ",[SCRVALS]"\
                 " FROM [TRQ_SCORE]"\
                 " LEFT JOIN [T_RECORDER]"\
                 " ON [TRQ_SCORE].[RECKEY] = [T_RECORDER].[FILENAME]"\
                 " WHERE 1=1"

        workbook.save("write.xls")

if __name__ == "__main__":
    iRecorderReport().exportReport()