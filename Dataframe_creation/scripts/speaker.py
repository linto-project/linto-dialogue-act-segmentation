#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan  4 10:08:14 2021

@author: lilagravellier
"""


def get_sec(time_str):
	# BONJOUR JE MAPPELLE LILA
    h, m, s = time_str.split(':')
    return float(h) * 3600 + float(m) * 60 + float(s)


def read_change_spk(filename_change_spk_detection):
    file=open(filename_change_spk_detection,"r")
    lines=file.readlines()
    file.close()
    
    beg_chg_spk=[]
    end_chg_spk=[]
    
    remove_strings=["[ ","]","-->"]
    for line in lines:
        for ch in remove_strings:
            line=line.replace(ch,"")
        #line=line.replace("[","")
        # to do : ajuster au format de base de sortie de pyannote
        line=line.replace("\n","")
        line=line.replace("   "," ")
        l=line.split(" ")

        #print(l)
        beg_chg_spk.append(round(get_sec(l[0]),3))
        end_chg_spk.append(round(get_sec(l[1]),3))
        
    return beg_chg_spk, end_chg_spk





def round_extraction(word, beg_word, end_word, beg_chg_spk, end_chg_spk):
    n=0
    w=0

    n_round=[]
    beg_round=[]
    end_round=[]
    rank_round=[]
    text_round=[]
    
    while n<len(beg_chg_spk):
        i=0
        text_round_list=[]
        
        while w<len(word) and beg_word[w]<=end_chg_spk[n]:
            
            n_round.append(n)
            beg_round.append(beg_chg_spk[n])
            end_round.append(end_chg_spk[n])
            text_round_list.append(word[w])
            rank_round.append(i)
            i+=1
            w+=1
            #print(len(beg_chg_spk), n, w, i, len(word))
        n+=1
        text_round_unit=" ".join(text_round_list)
        text_round+=[text_round_unit]*len(text_round_list)
    
        
    #print(word[-1],text_round[0], text_round[-1])
    return n_round, beg_round, end_round, rank_round, text_round


