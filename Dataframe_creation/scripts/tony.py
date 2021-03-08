#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 18 14:20:23 2020

@author: lilagravellier
"""

import os

def data_prep_tony(name, word, rank_turn, text_turn):
    name_tony=os.path.splitext(name)[0]
    name_tony2=os.path.basename(name_tony)
    file_tony=open(name_tony2+"_tony_prep.txt","w")
    cmpt=0
    for i in range(0,len(word)):
        if rank_turn==0:
            cmpt=0
            file_tony.write("\n")
            cmpt+=1
        if cmpt>230:
            file_tony.write("\n")
            cmpt=0
        file_tony.write(word[i]+" ")
        cmpt+=1
    file_tony.close()





def convert_tony_results(filename_tony, word):
    
    file_tony=open(filename_tony, "r")
    lines=file_tony.readlines()
    file_tony.close()
    
    tony_vect=[]
    word_tony_vect=[]
    compt_apos=0
    
    for i in range (0,len(lines)):
        if str(lines[i])!="\n":
            l=lines[i].replace("_	_	_	_	_	_	_	","")
            l=l.split("\t")
            #print(l)
            if l[0].isnumeric()==True:
                wrd=str(l[1])
                if "-" in wrd and wrd[0]!="-":
                    wrd2=wrd.split("-")
                    if "BeginSeg=Yes" in l[2]:
                        tony_vect.append(1)
                        word_tony_vect.append(wrd2[0])
                        for k in range(1,len(wrd2)):
                            tony_vect.append(0)
                            s="-"+str(wrd2[k])
                            word_tony_vect.append(s)
                    else:
                        tony_vect.append(0)
                        word_tony_vect.append(wrd2[0])
                        for k in range(1,len(wrd2)):
                            tony_vect.append(0)
                            s="-"+str(wrd2[k])
                            word_tony_vect.append(s)
                elif wrd=="'":
                    compt_apos+=1
                else:
                    word_tony_vect.append(wrd)
                    if "BeginSeg=Yes" in l[2]:
                        tony_vect.append(1)
                    else:
                        tony_vect.append(0)
   
    i=0
    while i<len(word):
        if "'" in word[i]:
            i+=1
        else:
            if word[i]!=word_tony_vect[i]:
                print(i,word[i],word_tony_vect[i])
                break
            i+=1

    return tony_vect 