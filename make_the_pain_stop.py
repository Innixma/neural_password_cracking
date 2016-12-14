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

john_char_indices = {'9': 16, 'Q': 35, '6': 13, '~': 72, '7': 14, 'E': 23, 'h': 52, 'b': 46, '2': 9, '1': 8, ';': 17, 'y': 69, 'I': 27, '$': 2, 'o': 59, 'e': 49, 'F': 24, 'O': 33, 'B': 20, 'q': 61, 'w': 67, 'v': 66, 'U': 39, '5': 12, 'A': 19, 'S': 37, 'x': 68, 'p': 60, '`': 71, '8': 15, '#': 1, 'J': 28, 'm': 57, 'i': 53, 'V': 40, '*': 5, 'n': 58, 'j': 54, 'R': 36, 'K': 29, 'N': 32, 'f': 50, 's': 63, 'c': 47, '0': 7, 'z': 70, 't': 64, 'l': 56, 'C': 21, '-': 6, 'k': 55, 'Y': 42, 'M': 31, 'g': 51, 'd': 48, 'D': 22, '4': 11, 'P': 34, 'u': 65, 'H': 26, 'r': 62, 'W': 41, 'G': 25, '^': 44, '&': 4, 'L': 30, 'T': 38, 'Z': 43, '%': 3, '!': 0, '@': 18, 'a': 45, '3': 10}
myspace_char_indices = {'9': 25, ')': 9, "'": 7, 'G': 37, '7': 23, 'E': 35, 'F': 36, '+': 11, '2': 18, ';': 26, 'I': 39, '$': 4, 'o': 77, 'D': 34, 'x': 86, 'B': 32, 'w': 85, 'U': 51, '5': 21, 'J': 40, 'a': 63, '\\': 58, '`': 62, '8': 24, '~': 91, 'm': 75, '/': 15, 'Q': 47, '*': 10, 'j': 72, 'R': 48, 'K': 41, ' ': 0, 'z': 88, '(': 8, 'C': 33, '-': 13, 'k': 73, 'M': 43, 'u': 83, 'H': 38, 'r': 80, '^': 60, '&': 6, '"': 2, 'L': 42, 'T': 50, 'l': 74, 'X': 54, '@': 30, 'c': 65, '3': 19, 'N': 44, '{': 89, '6': 22, 'y': 87, 'h': 70, ']': 59, 'b': 64, '1': 17, '?': 29, 'e': 67, 'Z': 56, '[': 57, '%': 5, 'q': 79, 'v': 84, 'd': 66, '}': 90, 'A': 31, 'S': 49, ',': 12, 'O': 45, '#': 3, 'i': 71, '.': 14, 'V': 52, 'p': 78, 'n': 76, '4': 20, '>': 28, 'f': 68, 't': 82, 'Y': 55, 'g': 69, '!': 1, 'P': 46, 'W': 53, 's': 81, '_': 61, '0': 16, '=': 27}

john_data = ['john', 25, 73, john_char_indices]
myspace_data = ['myspace', 28, 94, myspace_char_indices]

test_sets = []

for i in ['500','1000','1500','2000']:
    for j in ['FourType', 'ThreeType', 'FirstThreeChar']:
        name = j + i
        test_sets.append(name)

#
data_sets = [myspace_data, john_data]

#test_sets = test_sets + ['myspace', 'phpbb', 'john', 'cain']
#test_sets = test_sets + ['bookWordsFirstLetter','8type3','16type3']
             
             
             
#MAX_SIZE = 16
sentence_size = 12
orig_path = './passwordGen/passwordFiles/'




for i in range(len(data_sets)):
    name = data_sets[i][0]
    maxlen = data_sets[i][1]
    chars = data_sets[i][2]
    char_indices = data_sets[i][3]

    model = Sequential()
    model.add(LSTM(128, input_shape=(maxlen, chars)))
    model.add(Dense(chars))
    model.add(Activation('softmax'))
    optimizer = RMSprop(lr=0.01)
    model.compile(loss='categorical_crossentropy', optimizer=optimizer)
    model.load_weights("model_" + str(name) + ".h5")
    model.compile(loss='categorical_crossentropy', optimizer=optimizer)
    print(model.summary())
    
    for testname in test_sets:
        path = orig_path + testname + '.txt'
        
        
        
        
        text = open(path,'r',encoding='ascii',errors='ignore').read()#.lower()
        data = np.array(text.split('\n'))
        data = data[:-1]
        #data = data[:14000000]
        data = np.array([line for line in data if len(line) <= 32])
        
        if len(data) > 500:
            data = np.random.choice(data, 500, replace=False)
                
        fullInfo = []
        sentenceBase = np.array([char_indices['~']]*12)
        for passCount, password_orig in enumerate(data):
            if passCount % 100 == 0:
                print(passCount, '/', len(data))
            # Calc prob
            sentence = sentenceBase

            passlen = len(password_orig)
            password = [char_indices[c] for c in password_orig if c in char_indices]
            if passlen != len(password):
                continue
            
            password.append(char_indices['`'])
            passlen = passlen+1
            passProb = 1
            for i in range(passlen-1):
                #print(i)
                x = np.zeros((1, maxlen, chars))
                
                np.delete(sentence,0)
                np.append(sentence, password[i])
                #print(sentence[0])
                for t, char in enumerate(sentence):
                    x[0, t, char] = 1.
                
                #sentence = sentence[1:] + [password[i]]
                preds = model.predict(x, verbose=0)[0]

                if i < passlen-2:
                    passProb = passProb * preds[password[i+1]]
                #z = model.predict(curArray)
            passGuessCount = 1/passProb
            #print(password[:-1], '\t', passGuessCount, '\n')
            fullInfo.append([passGuessCount, password_orig])
            
            
        fullInfo.sort()
        #fullInfo.reverse()
        fullString = [d[1] + '\t' + str(d[0]) for d in fullInfo]
        fullString = '\n'.join(fullString)
        saveFileName = name + '_on_' + testname + '.txt'
        saveFile = open(saveFileName, 'w')
        saveFile.write(fullString)
        saveFile.close()
        
        
            
            