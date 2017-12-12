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
任务4:
电话公司希望辨认出可能正在用于进行电话推销的电话号码。
找出所有可能的电话推销员:
这样的电话总是向其他人拨出电话，
但从来不发短信、接收短信或是收到来电


请输出如下内容
"These numbers could be telemarketers: "
<list of numbers>
电话号码不能重复，每行打印一条，按字母顺序输出。
"""
#发送或接收短信的电话号码列表和收到来电的号码集合
phone_total = []
for element in texts:
	phone_total.append(element[0])
	phone_total.append(element[1])
for element in calls:
	phone_total.append(element[1])
phone_total_set = set(phone_total)
#生成没有发送过短信,接受短信或收到来电的电话号码列表集合
telemarketers_phone = []
for element in calls:
	if element[0] not in phone_total_set:
		telemarketers_phone.append(element[0])
telemarketers_phone_set = sorted(set(telemarketers_phone))
print("These numbers could be telemarketers: \n{}".format('\n'.join(telemarketers_phone_set)))
