'''Example script to generate text from Nietzsche's writings.

At least 20 epochs are required before the generated text
starts sounding coherent.

It is recommended to run this script on GPU, as recurrent
networks are quite computationally intensive.

If you try this script on new data, make sure your corpus
has at least ~100k characters. ~1M is better.
'''

from __future__ import print_function
from keras.models import Sequential
from keras.layers import Dense, Activation, Dropout
from keras.layers import LSTM
from keras.optimizers import RMSprop
from keras.utils.data_utils import get_file
import numpy as np
import random
import sys
import json
import math

import graphHelper

['FourType500','bookWordsFirstLetter','8type3','16type3', 'cain']


john_on_john = ['john_on_john', 73, 'john']
myspace_on_john = ['myspace_on_john', 94, 'myspace']

john_on_myspace = ['john_on_myspace', 73, 'john']
myspace_on_myspace = ['myspace_on_myspace', 94, 'myspace']

john_on_ThreeType500 = ['john_on_ThreeType500', 73, 'john']
myspace_on_ThreeType500 = ['myspace_on_ThreeType500', 94, 'myspace']

john_on_phpbb = ['john_on_phpbb', 73, 'john']
myspace_on_phpbb = ['myspace_on_phpbb', 94, 'myspace']

john_on_FourType500 = ['john_on_FourType500', 73, 'john']
myspace_on_FourType500 = ['myspace_on_FourType500', 94, 'myspace']



john_on_bookWordsFirstLetter = ['john_on_bookWordsFirstLetter', 73, 'john']
myspace_on_bookWordsFirstLetter = ['myspace_on_bookWordsFirstLetter', 94, 'myspace']

john_on_8type3 = ['john_on_8type3', 73, 'john']
myspace_on_8type3= ['myspace_on_8type3', 94, 'myspace']

john_on_16type3 = ['john_on_16type3', 73, 'john']
myspace_on_16type3 = ['myspace_on_16type3', 94, 'myspace']

john_on_cain = ['john_on_cain', 73, 'john']
myspace_on_cain = ['myspace_on_cain', 94, 'myspace']


john_sets = ['john', 73, [john_on_john, myspace_on_john]]
myspace_sets = ['myspace', 94, [john_on_myspace, myspace_on_myspace]]
ThreeType500_sets = ['ThreeType500', 73, [john_on_ThreeType500, myspace_on_ThreeType500]]
phpbb_sets = ['phpbb', 94, [john_on_phpbb, myspace_on_phpbb]]

FourType500_sets = ['FourType500', 94, [john_on_FourType500, myspace_on_FourType500]]
bookWordsFirstLetter_sets = ['bookWordsFirstLetter', 94, [john_on_bookWordsFirstLetter, myspace_on_bookWordsFirstLetter]]
_8type3_sets = ['8type3', 94, [john_on_8type3, myspace_on_8type3]]
_16type3_sets = ['16type3', 94, [john_on_16type3, myspace_on_16type3]]
cain_sets = ['cain', 94, [john_on_cain, myspace_on_cain]]


data_sets = [john_sets, myspace_sets, ThreeType500_sets, phpbb_sets,FourType500_sets,bookWordsFirstLetter_sets,_8type3_sets,_16type3_sets,cain_sets]

for word_set in data_sets:
    namesList = []
    percentiles = []
    words_name = word_set[0]
    chars = word_set[1]     

    for filename,chars_subset,true_name in word_set[2]:
        orig_data = open(filename+'.txt','r').read().split('\n')
        data = []
        brute = []
        for i in range(len(orig_data)):
            a,b = orig_data[i].split('\t')
            b = float(b)
            data.append(b)
            brute.append(math.pow(chars,len(a)))
            
        data.sort()
        dataLen = len(data)
        brute.sort()
        
        percentileCur = []
        
        for i in range(0,96):
            percentileCur.append(data[int(dataLen*i/100)])
            
        percentiles.append(percentileCur)
        
        namesList.append(true_name + ' RNN')
        
        
    percentileBrute = []
    for i in range(0,96):
        percentileBrute.append(brute[int(dataLen*i/100)])
    percentiles.append(percentileBrute)
    namesList.append('Brute Force')
    xList = [np.arange(0,96)]*len(percentiles)
    yList = percentiles
    title = words_name + ' dataset'
    ylabel = 'Guesses'
    xlabel = 'Percent Cracked'
    savefigName = 'results_' + words_name
    print('hey')
    graphHelper.graphSimple(xList, yList, namesList, title, ylabel, xlabel, savefigName)
    print('there')