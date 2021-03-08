#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan  5 14:14:21 2021

@author: lilagravellier
"""


def convert_punctuation(filename_punct, word):
    file_punct=open(filename_punct, "r")
    lines=file_punct.readlines()
    file_punct.close()
    
    
    prob_nothing=[]
    prob_period=[]
    prob_comma=[]
    
    
    
    for i in range(0,2):
        prob_nothing.append(1)
        prob_period.append(0)
        prob_comma.append(0)
    j=0
    
    l_exception=["%", '"',"-", "[","]","«","»"]
    for i in range(0,len(lines)):
        if word[j+2] in l_exception:
            prob_nothing.append(0)
            prob_period.append(0)
            prob_comma.append(0)
            j+=1
            print("exception")

        l=lines[i].replace("\n", "")
        l=l.split(" ")
        prob_nothing.append(l[1])
        prob_period.append(l[2])
        prob_comma.append(l[3])
        i+=1
        j+=1
                
            
    # for line in lines:
    #     l=line.replace("\n", "")
    #     l=l.split(" ")
        
    #     prob_nothing.append(l[1])
    #     prob_period.append(l[2])
    #     prob_comma.append(l[3])

    
    for i in range(0,2):
        prob_nothing.append(1)
        prob_period.append(0)
        prob_comma.append(0)
    
    
    prob_nothing_bef=[0]+prob_nothing[:-1]
    prob_period_bef=[0]+prob_period[:-1]
    prob_comma_bef=[0]+prob_comma[:-1]
    
    
    if len(prob_nothing_bef)!=len(word):
        print("ERROR : list lengths do not match")
    
    return prob_nothing, prob_period, prob_comma, prob_nothing_bef, prob_period_bef, prob_comma_bef
