# -*- coding: utf-8 -*-import twitter_config
import os,fnmatch,codecs


counter = 0
wordcount={}

for dirpath, dirs, files in os.walk('step2'):
    for filename in fnmatch.filter(files, '*.txt'):
        with codecs.open(os.path.join(dirpath, filename),'r',encoding="utf-8") as file:

            for word in file.read().split():

                if word not in wordcount:
                    wordcount[word] = 1
                else:
                    wordcount[word] += 1

f=open("step3/word-frequency.txt", 'w', encoding="utf-8")

for k,v in wordcount.items():
      #print (k,v)
        my_string = u"{key}:{value} ".format(key=k, value=v)
        print(my_string)
        f.write(my_string+"\n")
f.close();
file.close();

# with codecs.open("step3/word-frequency.txt", 'a+', encoding="utf-8") as f:
