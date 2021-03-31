# DialogueActsSegmentation_Linto


This work was done in the framework of the LinTo project https://linto.ai/fr/ .
The objective is to segment French spontaneous speech into dialogue acts. 
For this purpose, a corpus of Linagora meetings has been designed. 
We decided to automatically annotate the corpus using the Snorkel tool: https://www.snorkel.org/.  
The output files are the labeleled data which can be used to train a machine learning model (for example ToNy)
This directory contains all the data that were used to annotate the corpus with Snorkel, as well as the jupyter notebooks for processing the data and generating the labels. 

## Getting Started

You need to download the directory and unzip the two data.zip .
Then the jupyter notebooks decribe each step in the process so let them guide you. 

### Prerequisites

Specific Python packages needed to use jupyter notebooks : 
* spacy : _conda install -c conda-forge spacy_ and _python -m spacy download fr_core_news_sm_
* snorkel : _pip install snorkel_



### Description of repo

The DialogueActsSegmentation_linto repository contains 2 directories.

Dataframe_creation/ :
* data.zip
* Dataframe_creation_dialogue_act.ipynb
* scripts/

```
The Dataframe_creation_dialogue_act notebook takes all the data on the LinTo Corpus from data/ 
and converts it into one dataframe of features usable in the Snorkel_Linto notebook.
It's a preparation for the task of segmentation into dialogue acts. 
The output file of Dataframe_creation_dialogue_act is a DataFrame which has to go to the Snorkel_work/data/ directory. 
```

Snorkel_work/ :
* data.zip
* Snorkel_Linto.ipynb
* utils/

```
The Snorkel_Linto notebook takes the features from the previously created dataframe, to make vote heuristic rules. 
These votes will allow the generation of labels on an unannotated corpus. 
All the steps of creation and evaluation of the rules as well as the creation of the generative model annotating the corpus 
are performed step by step in this notebook.
```
## Authors

* **Lila Gravellier** - *Initial work* 



