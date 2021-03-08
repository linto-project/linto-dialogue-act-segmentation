#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 18 14:20:23 2020

@author: lilagravellier
"""


def alignments_word_extraction(filename_alignments):
    #lecture fichier
    file=open(filename_alignments, "r")
    lines=file.readlines()
    file.close()
    
    #extraction des informations des colonnes
    word_list=[]
    beg_word=[]
    end_word=[]
    
    for line in lines:
        l=line.split(" ")
        word=str(l[3])
        word=word.replace('"', "")
        word_list.append(word)
        beg_word.append(float(l[1]))
        end_word.append(float(l[2]))
    
    
    return  word_list, beg_word, end_word

# ne fonctionne que pour les alignements générés à partir de Jtrans.
def alignments_real_turn_extraction(filename_alignments):
    #lecture fichier
    file=open(filename_alignments, "r")
    lines=file.readlines()
    file.close()
    
    text_turn=[]
    beg_turn=[]
    end_turn=[]
    n_turn=[]
    rank_turn=[]
    loc=[]

    l=lines[0].split(" ")
    l_tamp=str(l[4])
    rnd=[]
  
    cmpt=0
    beg=float(l[1])
    n=0
    for i in range(0,len(lines)):
        l=lines[i].split(" ")
        l_comp=str(l[4]) 
        loc.append(l[4].replace("\n",""))
        word=str(l[3])

        
        if l_comp!=l_tamp:
            n+=1
            n_turn.append(n)
            rnd_str=" ".join(rnd)
            
            beg_turn+=[beg]*len(rnd)
            end_turn+=[float(l[1])]*len(rnd)
            beg=float(l[1])
            text_turn+=[rnd_str]*len(rnd)
            l_tamp=l_comp
            rnd=[]
            rnd.append(word)

            cmpt=0
            rank_turn.append(cmpt)

            cmpt+=1
        else:
            rnd.append(word)
            rank_turn.append(cmpt)
            cmpt+=1
            n_turn.append(n)
            



    rnd_str=" ".join(rnd)
    
    beg_turn+=[beg]*len(rnd)
    end_turn+=[float(l[2])]*len(rnd)
    text_turn+=[rnd_str]*len(rnd)

    print(len(n_turn), len(beg_turn), len(end_turn), len(rank_turn), len(text_turn))
    
    return n_turn, beg_turn, end_turn, rank_turn, text_turn, loc
