#!/usr/bin/python
# program that returns the count of each word in the file
file = open("C:/Users/Allah/Desktop/tea.txt","r+")
wordcount={}
for word in file.read().split():
    if word not in wordcount:
        # print word
        wordcount[word] = 1
    else:
        wordcount[word] += 1
for key in wordcount.keys():
    print ("%s %s " % (key, wordcount[key]))

file.close();