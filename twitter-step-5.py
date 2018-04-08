# -*- coding: utf-8 -*-import twitter_config
import operator
import os, fnmatch, codecs
import re
import pathlib

counter = 0
inverted_indext = {}
for dirpath, dirs, files in os.walk('nlp/step2'):
    for filename in fnmatch.filter(files, '*.txt'):
        with codecs.open(os.path.join(dirpath, filename), 'r', encoding="utf-8")as f:

            for word in f.read().split():
                if word not in inverted_indext:
                    list = []
                    list.append(str(filename).replace(".txt" , ""))
                    data = {"c" : 1 , "l" : list}
                    inverted_indext[word] = data

                else:
                    list = []
                    inverted_indext[word]["c"] += 1
                    for a in inverted_indext[word]["l"]:
                        list.append(a)

                    list.append(str(filename).replace(".txt" , ""))
                    inverted_indext[word]["l"] = list;


            f.close();


twitter_nlp = 'nlp/step5/'
pathlib.Path(twitter_nlp).mkdir(parents=True, exist_ok=True)
f = codecs.open(os.path.join(twitter_nlp, "inverted-index.txt"), 'w', encoding="utf-8")
for x in inverted_indext:
    f.write(x + "," +  str(inverted_indext[x]["c"]))
    for a in inverted_indext[x]["l"]:
        f.write(str(a) + ",")
    f.write("\n")

