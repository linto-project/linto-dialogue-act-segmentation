#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 18 14:20:23 2020

@author: lilagravellier
"""


def convert_gold(filename_gold):
    file_gold=open(filename_gold, "r")
    lines=file_gold.readlines()
    file_gold.close()
    
    
    # conversion du fichier gold en vecteur 1 et 0
    
    gold_vect=[]
    word_gold_vect=[]
    
    for i in range (1,len(lines)):
        if str(lines[i])!="\n":
            l=lines[i].split(" ")
            
            if l[0].isnumeric()==False:
                j=0
                while j<len(l):
                    if "-" in str(l[j]) and l[j][0]!="-":
                        l2=l[j].split("-")
                        del l[j]
                        for k in range(0,len(l2)):
                            if k==0:
                                l.insert(j,str(l2[k]))
                            else:
                                s="-"+str(l2[k])
                                l.insert(j+k,s)
                    
                    if str(l[j])=="|" and j<len(l)-1:
                        word_gold_vect.append(str(l[j+1]))
                        gold_vect.append(1)
                        j+=2
                    elif "|" not in str(l[j]): 
                        gold_vect.append(0)
                        word_gold_vect.append(str(l[j]))
                        j+=1
                    else:
                        j+=1


    return gold_vect
