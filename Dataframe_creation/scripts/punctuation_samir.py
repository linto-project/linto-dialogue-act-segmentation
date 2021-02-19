#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 10 15:48:40 2021

@author: lilagravellier
"""



def punctuation_samir_extraction(file_punctuation, word):
    file_punct=open(file_punctuation, "r")
    lines=file_punct.readlines()
    file_punct.close()
    
    line=""
    for li in lines:
        li=li.replace("\n", " ")
        li=li.replace("'", "' ")
        li=li.replace("  ", " ")
        li=li.replace("aujourd' hui", "aujourd'hui")
        
        line+=li
    
    
    line=line.lower()
    
    l=line.split(" ")
    
    l=line.split(" ")
    if "." in l:
        l.remove(".")
    if "," in l:
        l.remove(",")
    
    punct=[]
    j=0
    i=0
    while i<len(word) and j<len(l):
        s=l[j].replace(",", "")
        s=s.replace(".", "")
        
        if word[i]!=s:
            if word[i] in s:
                #print(word[i], s)
                k=0
                w=word[i]
                while word[i+k] in s and w in s:
                    #print("b")
                    punct.append(0)
                    k+=1
                    w+=word[i+k]
                #print(k)
                if "." in l[j]:
                    del punct[-1]
                    punct.append(".")
                elif "," in l[j]:
                    del punct[-1]
                    punct.append(",")
                j+=1
                i+=k
            else:
                print("ERROR:",j, s,i, word[i])
                break
                i+=1
        else:
            if "." in l[j]:
                punct.append(".")
            elif "," in l[j]:
                punct.append(",")
            else:
                punct.append(0)
            j+=1
            i+=1
    
    if j<len(l):
        print("ERROR2")
    
    while i<len(word):
        punct.append(0)
        i+=1
            
    punct_bef=[0]+punct
    del punct_bef[-1]
    
    print(len(punct), len(punct_bef))
    return punct, punct_bef
    
            

        