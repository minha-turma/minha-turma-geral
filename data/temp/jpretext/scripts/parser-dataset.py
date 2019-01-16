# -*- coding: utf-8 -*-

# this script reads the dataset and writes each document
# corresponding to its title + description.

doc = 1

with open('dataset.txt', 'rb') as dataset:
    for i in dataset.readlines():
        i = i.split(';')
        name = str(doc) + '.txt'
        f = open(name, 'w')
        f.write(i[3] + ' ' + i[4]) # title + description
    	f.close()
    	int(doc)
    	doc += 1