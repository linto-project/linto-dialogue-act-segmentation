#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 18 14:20:23 2020

@author: lilagravellier
"""


def extract_silences_positions(filename_silences):
    file=open(filename_silences, "r")
    lines=file.readlines()
    file.close()
    
    
    beg_sil=[]
    end_sil=[]
    dur_sil=[]
    mid_sil=[]
    
    for line in lines[1:]:
        l=line.split(" ")
        beg_sil.append(float(l[0]))
        end_sil.append(float(l[1]))
        dur_sil.append(float(l[2]))
        mid=float(l[0])+(float(l[2]))/2
        mid_sil.append(mid)
    
    
    return beg_sil, end_sil, dur_sil, mid_sil





def silences_word_position(word, beg_word, end_word, beg_sil, end_sil, dur_sil, mid_sil):

    sil_aft=[]
    sil_bef=[]
    flag=0
    flag2=0

    for i in range(0,len(beg_word)):
        dur_word=abs(end_word[i]-beg_word[i])
        for j in range(0,len(beg_sil)):
            if i==0:
                if mid_sil[j]>=beg_word[i]+dur_word/2 and mid_sil[j]<=beg_word[i+1] and flag==0:
                    sil_aft.append(dur_sil[j])
                    flag=1
                elif mid_sil[j]<=beg_word[i]+dur_word/2 and mid_sil[j]>=0 and flag2==0:
                    sil_bef.append(dur_sil[j])
                    flag2=1
                    
            elif i==len(beg_word)-1:
                if mid_sil[j]>=beg_word[i]+dur_word/2 and flag==0:
                    sil_aft.append(dur_sil[j])
                    flag=1
                elif mid_sil[j]<=beg_word[i]+dur_word/2 and mid_sil[j]>=0 and flag2==0:
                    sil_bef.append(dur_sil[j])
                    flag2=1
            else:
                if mid_sil[j]>=beg_word[i]+dur_word/2 and mid_sil[j]<=beg_word[i+1] and flag==0:
                    sil_aft.append(dur_sil[j])
                    flag=1
                elif mid_sil[j]<=beg_word[i]+dur_word/2 and mid_sil[j]>=end_word[i-1] and flag2==0:
                    sil_bef.append(dur_sil[j])
                    flag2=1
        if flag==0:
            sil_aft.append(0)
        if flag2==0:
            sil_bef.append(0)
        flag=0
        flag2=0
        
                

    return sil_bef,sil_aft