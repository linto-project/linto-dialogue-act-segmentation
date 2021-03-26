#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 26 10:35:07 2021

@author: lilagravellier


Utils 
needed functions for the labeling function creation in Snorkel LinTo

get_word_context : return the previous word and the next word in text according
to the position of the current word.

set_first_marker: given lists of discursive markers, return 1 if the current word 
is an isolated marker or the first of a series of markers

set_after_marker : given lists of markers, return 1 if the current word follows a 
serie of markers or an isolated one

get_dictionary_spacy_audio : return the needed dictionary of spacy information combined to 
audio informatio

P = previous , C = Current, N = Next
e = energy
p = pitch
dep = dependency
pos = part-of-speech
headpos = part-of-speech of the headin dependency

example : 
PCe = Previous + Current energy 

"""

import numpy as np

def get_word_context(text_list, position):
    
    if position<len(text_list)-1 and position>0:
        word_bef = text_list[position-1]
        word_aft = text_list[position+1]
    elif position==0 and position<len(text_list)-1:
        word_bef = np.nan
        word_aft= text_list[position+1]
    elif position==len(text_list)-1 and position==0:
        word_aft = np.nan
        word_bef = text_list[position-1]
    else:
        word_aft = np.nan
        word_bef = np.nan
        
    return word_bef, word_aft


def set_first_marker(couple_markers, single_markers, text_list, position, word):
    m=0
    if position!=len(text_list)-1:
        word_aft=str(text_list[position+1])
        if word in single_markers or ((word in couple_markers.keys()) and (word_aft in couple_markers[word])):
            if position==0:
                m=1
            else:
                word_bef=str(text_list[position-1])
                if word_bef in single_markers:
                    m=0
                else:
                    if position==1:
                        m=1
                    else:
                        word_bef_bef=str(text_list[position-2])
                        if word_bef_bef in couple_markers.keys() and word_bef in couple_markers[word_bef_bef]:
                            m=0
                        else:
                            m=1
    return m


def set_after_marker(couple_markers, single_markers, text_list, position, word):
    bef=0
    after_mark=0
    if position>0:
        word_bef=str(text_list[position-1])
        for k in couple_markers.keys():
            if word_bef in couple_markers[k]:
                bef=1

        if word_bef in single_markers or bef==1:
            if word not in single_markers and word not in couple_markers.keys():
                after_mark=1
            else:
                after_mark=0
        else:
            after_mark=0
    
    return after_mark



def get_dictionaries_spacy_audio():
    
    dict_PC_PCe=dict(NOUN_PRON=["DU", "DS", "US"],
                    NOUN_CCONJ=["DD", "DU", "DS", "UD", "UU", "US", "SD", "SU"],
                    NOUN_ADV=["DD"],
                    ADJ_PRON=["DU", "DS"],
                    ADJ_CCONJ=["DD", "DU", "DS", "UU"],
                    NOUN_SCONJ=["DD", "DS"],
                    PROPN_PRON=["DU", "DS", "UD", "UU"],
                    ADV_CCONJ=["DD", "DU", "UD"],
                    VERB_CCONJ=["DD"]
                    )


    dict_PC_PCp=dict(NOUN_PRON=["US", "DK", "UD", "SD", "UK"],
                    NOUN_CCONJ=["SS","DD", "SK","UD", "SD", "KS", "UK"],
                    NOUN_ADV=["UD", "KS", "US", "UU"],
                    ADJ_PRON=["SK", "DK","UD","UK"],
                    ADJ_CCONJ=["SS","DD", "US", "DK", "UD", "SD"],
                    NOUN_SCONJ=["DD","SK", "UK"],
                    ADJ_ADV=["US","UD"],
                    PROPN_PRON=["SS"],
                    ADJ_SCONJ=["SS","DD", "DK", "UD"]
                    )


    dict_PC_PCpe=dict(NOUN_PRON=["DK_DS", "SK_DS", "US_DU", "UK_DS", "UD_DU", "SD_DU", "UK_DU", "DK_DU"],
                    NOUN_CCONJ=["SS_DU", "UD_DU", "SK_DU"],
                    NOUN_ADV=["SS_DD", "UD_DD", "US_DD"]
                     )
        

    
    dict_PC_Cdep=dict(NOUN_PRON=["nsubj", "obj", "nmod"],
                    NOUN_CCONJ=["cc"],
                    NOUN_ADV=["advmod"],
                    NOUN_SCONJ=["mark"],
                    ADJ_ADV=["advmod"],
                    PROPN_PRON=["nsubj"],
                    ADV_CCONJ=["cc"],
                    VERB_CCONJ=["cc"]
                    )


    dict_PC_Cheadpos=dict(NOUN_PRON=["ADJ","PRON","AUX"],
                        NOUN_CCONJ=["VERB","NOUN", "ADJ", "ADV", "PRON"],
                        ADJ_PRON=["VERB"],
                        ADJ_CCONJ=["VERB","NOUN", "ADJ", "ADV"],
                        NOUN_SCONJ=["VERB"],
                        PROPN_PRON=["VERB","NOUN"],
                        ADV_CCONJ=["VERB","NOUN"],
                        VERB_CCONJ=["VERB","NOUN", "ADV"]
                        )



    dict_PC_Pheadpos=dict(NOUN_PRON=["VERB", "ADJ", "PRON"],
                        NOUN_CCONJ=["VERB", "NOUN", "ADJ", "ADV"],
                        ADJ_PRON=["NOUN"],
                        ADJ_CCONJ=["VERB", "NOUN", "ADJ", "ADV"],
                        NOUN_SCONJ=["NOUN"],
                        ADJ_ADV=["NOUN"],
                        PROPN_PRON=["VERB", "NOUN"],
                        ADV_CCONJ=["VERB", "NOUN"],
                        VERB_CCONJ=["VERB"]
                        )

    dict_PC_Pdep=dict(NOUN_PRON=["nomd", "obj", "obl:arg", "dep", "ccomp"],
                    NOUN_CCONJ=["nmod", "obj", "amod", "obj:mod", "obl:arg"],
                    NOUN_ADV=["nmod"],
                    ADJ_PRON=["amod", "xcomp"],
                    VERB_ADV=["nmod", "obj", "dep"],
                    NOUN_SCONJ=["nmod"],
                    ADV_CCONJ=["advmod"], 
                    VERB_CCONJ=["xcomp"]
                     )
    
    
    
    return dict_PC_PCe,dict_PC_PCp,dict_PC_PCpe,dict_PC_Cdep,dict_PC_Cheadpos,dict_PC_Pheadpos, dict_PC_Pdep
    
    
    

    
    