# -*- coding: utf-8 -*-

temp = []

with open('dataset.txt', 'r') as dataset:
    for i in dataset.readlines():
        if len(i) > 2:
            temp.append(i.replace('\n', ''))

chunks = [temp[x:x+5] for x in xrange(0, len(temp), 5)]

new = open('dataset.txt', 'w')

for item_list in chunks:
    t = ''
    for item in item_list:
        t += item + ';'
    new.write(t[:-1] + '\n')

new.close()