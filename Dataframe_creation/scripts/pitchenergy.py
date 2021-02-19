#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 27 17:36:04 2021

@author: lilagravellier
"""


#filename_pitchenergy="audio/Linagora_A1_pitchenergy.txt"

def audio_features_extraction(filename_pitchenergy, word):
    file=open(filename_pitchenergy, "r")
    lines=file.readlines()
    file.close()
    
    
    #les deux premières valeurs n'existe pas donc on les met à 0 
    # ( utilisation de trigrams)
    pitch=[0,0]
    energy=[0,0]
    
    l=lines[0].split("(")
    
    l_exception=["%", '"',"-", "[","]","«","»"]
    j=0
    for line in lines:
        if word[j+2] in l_exception:
            pitch.append(0)
            energy.append(0)
            j+=1
            print("exception_a")
        l=line.split("(")
        lp=lp=l[2][11]
        le=l[3][11]
        pitch.append(lp)
        energy.append(le)
        j+=1


    
    # pareil pour les deux derniers mots 
    pitch+=[0,0]
    energy+=[0,0]

    pitch_bef=list(pitch)
    energy_bef=list(energy)

    del pitch_bef[-1]
    del energy_bef[-1]

    pitch_bef.insert(2,0)
    energy_bef.insert(2,0)

    print(len(pitch), len(pitch_bef) ,len(energy), len(energy_bef))

    return pitch, pitch_bef, energy, energy_bef