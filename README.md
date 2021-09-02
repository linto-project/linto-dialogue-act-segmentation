# DialogueActsSegmentation_Linto


This work was done in the framework of the LinTo project https://linto.ai/fr/ .
The objective is to segment French spontaneous speech into dialogue acts. 
For this purpose, a corpus of Linagora meetings has been designed. 
We decided to automatically annotate the corpus using the Snorkel tool: https://www.snorkel.org/.  
The output files are the labeled data which can be used to train a machine learning model (for example ToNy  https://zenodo.org/record/4235850#.YTC-et86-w4 , https://gitlab.inria.fr/andiamo/tony)
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


## Usage 

### Get labeled data from the generative model using pre-processed data from LinTo

To obtain the predictions of the generative model from the pre-processed data of the LinTo corpus, the following steps must be followed: 

1. Unzip the _data.zip_ into _Snorkel_work/_
2. Open and run the cells of the jupyter notebook called _Snorkel_Linto.ipynb_ and check that the right file is called in the section **data loading** :
```
df_linto = pd.read_csv("../data/df_all_final_LinTo_23032021.csv")
```
3. Get the files generated at the end of the notebook : they contain the automatically labeled data separated in train/dev/test.

The steps for the creation of this generative model are well separated in this notebook, the rules used for Snorkel are written in the notebook directly, and for some of them are to be completed from the scripts in _Snorkel_work/utils/utils_snorkel_linto.py_
The generative model's performances are calculated inside the notebook.

At the end of the notebook, some files are generated : they contain all the data automatically labeled by Snorkel thanks to the written rules. They are under a format suited for training, fine-tuning and testing of the written discourse segmenter **ToNy** https://gitlab.inria.fr/andiamo/tony.

### Preprocessing task

To generate the table needed for the training and testing of the generative model, one must use the jupyter notebook _Dataframe_creation_dialogue_act.ipynb_ in the folder _Dataframe_creation/_. At the beginning of this notebook there is an inventory of all the necessary files and their formats for the creation of the final table.
Once you get the final table, you can use the notebook _Snorkel_Linto.ipynb_ as explained above. 

1. Unzip the _data.zip_ into _Dataframe_creation/_
2. Run the cells of the _Dataframe_creation_dialogue_act.ipynb_
3. Get the table generated at the end of the notebook, it contains all information needed for the training of the generative model.

## Authors

* **Lila Gravellier** - *Initial work* 



