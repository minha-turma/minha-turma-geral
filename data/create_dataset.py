# -*- coding: utf-8 -*-
#!/usr/bin/python

# This script creates a dataset(.txt) in portuguese following the schema bellow:
# Main topic (more general)
# Subtopic
# Video's link
# Video's title
# Video's description

# working only for biology at this moment (15/01/2019)

import requests, json

import sys
reload(sys)
sys.setdefaultencoding('utf8')

url_mec = 'https://api.portalmec.c3sl.ufpr.br/v1/search?search_class=LearningObject&results_per_page=164&query=biologia&object_types[]=8&educational_stages[]=4&order=score'
url_khan = 'https://pt.khanacademy.org/api/v1/topictree?kind=video'
r = requests.get(url_mec).text

# dictionary
data = json.loads(r) 

test = ''
test2 = ''
test3 = ''
test4 = ''

f = open('dataset.txt', 'w')

for key1, value1 in data.items():
    if key1 == 'children':
        for i in data[key1]:
            for key2, value2 in i.items():
                if key2 == 'translated_title':
                        test = value2.encode('utf-8')
                elif key2 == 'children' and test == 'Ciências':
                    for j in i[key2]:
                        for key3, value3 in j.items():
                            if key3 == 'translated_title':
                                test2 = value3.encode('utf-8')
                            elif key3 == 'children' and test2 == 'Biologia':
                                for k in j[key3]:
                                    for key4, value4 in k.items():
                                        if key4 == 'translated_title':
                                            test4 = value4
                                        elif key4 == 'children':
                                            for l in k[key4]:
                                                for key5, value5 in l.items():
                                                    if key5 == 'translated_title':
                                                        test3 = value5
                                                    elif key5 == 'children':
                                                        for m in l[key5]:
                                                            for key6, value6 in m.items():
                                                                if key6 == 'ka_url':
                                                                    f.write(test4 + '\n')
                                                                    f.write(test3 + '\n')
                                                                    f.write(value6 + '\n')
                                                                elif key6 == 'title':
                                                                    f.write(value6 + '\n')
                                                                elif key6 == 'description':
                                                                    f.write(value6 + '\n-\n')

# used for collect data from MEC api
# for i in data: 
#     if i['link'] != None:
#         f.write(i['link'].encode('utf-8') + '\n')
#         f.write(i['name'].encode('utf-8') + '\n')
#         f.write(i['description'].encode('utf-8') + '\n-\n')

f.close()