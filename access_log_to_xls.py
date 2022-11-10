import re
import xlwt
#  access.log path
PATH = r"C:\Users\YanC\PycharmProjects\机考\access.log-20221027"
#  output file name
FILENAME = 'Nginx_log'

#  正则表达式匹配
a = re.compile(r'(?P<ip>.*?)- - \[(?P<time>.*?)\] "(?P<request>.*?)" (?P<status>.*?) (?P<bytes>.*?) "(?P<referer>.*?)" "(?P<ua>.*?)"')


def load_log(path):  # 定义加载函数
    lst = []
    i = 0  # 日志记录数量
    with open(path, mode="r", encoding="utf-8") as f:
        for line in f:
            dic = parse(line)
            if dic:
                lst.append(dic)
            i += 1
    print("成功加载日志条目量{}".format(i))
    return lst


def parse(line):  # 每一行解析
    try:
        result = a.match(line)
        return result.groups()
    finally:
        pass


def to_xls(log, filename='Nginx_log'):  # 写入工作簿
    data_length = len(log)  # 数据的长度
    workbook = xlwt.Workbook()  # 新建工作簿
    work_sheet = workbook.add_sheet('log')  # 新建工作簿
    head = ["ip", "time", "request", "status", "bytes", "referer", "ua"]  # 表头
    for i in range(7):  # 写入内容
        work_sheet.write(0, i, head[i])
    for i in range(data_length):
        for j in range(7):
            work_sheet.write(i + 1, j, log[i][j])
    work_sheet.col(0).width = 4000  # set width
    work_sheet.col(1).width = 6500
    work_sheet.col(2).width = 4000
    work_sheet.col(6).width = 30000
    try:
        workbook.save('{}.xls'.format(filename))
    finally:
        pass


data = load_log(PATH)
to_xls(data, filename=FILENAME)


