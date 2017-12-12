"""
下面的文件将会从csv文件中读取读取短信与电话记录，
你将在以后的课程中了解更多有关读取文件的知识。
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)


"""
任务1：
短信和通话记录中一共有多少电话号码？每个号码只统计一次。
输出信息：
"There are <count> different telephone numbers in the records."""
#定义telephone_number函数，列出texts和call列表中电话号码
def telephone_number(list):
	telephones = []
	for index in range(len(list)):
		telephones.append(list[index][0])
		telephones.append(list[index][1])
	return telephones

#texts和calls列表中所不重复的电话号码,并统计数量
total_telephones = set(telephone_number(texts) + telephone_number(calls))
total_telephones_count = len(total_telephones)

print("There are {} different telephone numbers in the records.".format(total_telephones_count))