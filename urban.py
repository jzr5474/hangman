import urllib.request
import urllib
import re

def urban1(user_define_input):
    srch = str(user_define_input)
    a = list(srch)
    for index in range(len(a)):
        if a[index] == " ":
            a[index] = "+"
    srch = "".join(a)
    output_word=urllib.request.urlopen("http://www.urbandictionary.com/define.php?term="+srch)
    output_word=output_word.read()
    output_word = output_word.decode()
    lst = output_word.splitlines()
    for index in range(len(lst)):
        if lst[index]=="<div class='meaning'>":
            return(lst[index+1])
    else:
        print ("Word not found!")

def urban(s):
    y = urban1(s)
    bad = "<p>There aren't any definitions for <i>"+s+"</i> yet.</p>"
    if bad in y:
        return("This word isn't funny")
    quotes = "&quot;"
    link ="/define.php?term="
    x = list(y)
    index = 1
    while link in y:
        if index >= len(x):
            index = 0
            continue
        if x[index]=="a" and x[index-1]=="<" and x[index+6]=="=":
            for i in range(26):
                x.pop(index-1)
        else:
            index += 1
            continue
        return "".join(x)
    index = 1
    while quotes in y:
##        print(index,len(x),end=" | ")
        if index >= len(x):
            index = 0
            continue
        if x[index]=="q" and x[index-1]=="&":
            for i in range(6):
                x.pop(index-1)
            x.insert(index-1,""" " """)
        else:
            index += 1
            if index >= len(x):
                break
    index = 0
    while "&#39;" in y:
        if x[index]=="#" and x[index-1]=="&":
            for i in range(5):
                x.pop(index-1)
            x.insert(index-1,"'")
        else:
            index += 1
            if index == len(x):
                break
    y = "".join(x)
    return y

