#!/usr/bin/env python
# coding:utf8
# 

word = []
num = {}
book = open('xyj.txt','rb')
for line in book:
	line = line.strip().decode('utf-8')
	if len(line) == 0:
		continue
	for x in range(0, len(line)):
		if line[x] in [' ', '，' ,'。', '“', '”', '：', '　', '！', '？']:
			continue
		if not line[x] in word:
			word.append(line[x])
		if not line[x] in num:
			num[line[x]] = 0
		num[line[x]] += 1

num = sorted(num.items(), key=lambda d:d[1], reverse=True)
result = open('result.txt', 'w+')
result.write('《西游记》小说汉字使用频率排行：\n')
for x in range(0,20):
	result.write(str(num[x][0]) + ' ' + str(num[x][1]) + '\n')
book.close()
result.close()