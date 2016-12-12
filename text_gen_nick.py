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

MAX_SIZE = 16
sentence_size = 12

#path = get_file('nietzsche.txt', origin="https://s3.amazonaws.com/text-datasets/nietzsche.txt")
orig_path = './passwordGen/passwordFiles/'
names = ['john.txt','myspace.txt']#, 'phpbb.txt', 'cain.txt'] #'john.txt', 'myspace.txt'

for name in names:
    path = orig_path + name
    
    
    text = open(path,'r',encoding='ascii',errors='ignore').read()#.lower()
    
    c = 0
    """
    data = np.array([])
    for line in file:
        c += 1
        try:
            data.append(line)
            
        except:
            continue
    """
    
    
    print('corpus length:', len(text))
    
    
    
    
    data = np.array(text.split('\n'))
    data = data[:-1]
    #data = data[:14000000]
    data = [line for line in data if len(line) <= MAX_SIZE]
            
    #data = data[:10000]
    
    chars = sorted(list(set(text)))
    chars.remove('\n')
    if '`' not in chars:
        chars.append('`')
    if '~' not in chars:    
        chars.append('~')
    print('total chars:', len(chars))
    char_indices = dict((c, i) for i, c in enumerate(chars))
    indices_char = dict((i, c) for i, c in enumerate(chars))
    
    
    #tmp = len(char_indices.keys())
    #char_indices[' '] = tmp
    #indices_char[tmp] = ' '
    
    maxlen = np.max([len(line) for line in data])
    
    for i, line in enumerate(data):
        size = len(line)
        data[i] = line + '`'*(maxlen-size)
        data[i] = '~'*(sentence_size)+data[i]
        
    maxlen = np.max([len(line) for line in data]) 
    print('maxlen:', maxlen)
    
    # cut the text in semi-redundant sequences of maxlen characters
    
    #a = bb
    
    step = 3
    
    sentences = []
    next_chars = []
    for i in range(0, len(data)):
        for j in range(0, len(data[i])-sentence_size-1):
            sentences.append(data[i][j:j+sentence_size])
            next_chars.append(data[i][j+sentence_size])
    """
    for i in range(0, len(text) - maxlen, step):
        sentences.append(text[i: i + maxlen])
        next_chars.append(text[i + maxlen])
    """
    print('nb sequences:', len(sentences))
    
    print('Vectorization...')
    X = np.zeros((len(sentences), maxlen, len(chars)), dtype=np.bool)
    y = np.zeros((len(sentences), len(chars)), dtype=np.bool)
    for i, sentence in enumerate(sentences):
        for t, char in enumerate(sentence):
            X[i, t, char_indices[char]] = 1
        y[i, char_indices[next_chars[i]]] = 1
    
    """
    # build the model: a single LSTM
    print('Build model...')
    model = Sequential()
    model.add(LSTM(128, input_shape=(maxlen, len(chars))))
    model.add(Dense(len(chars)))
    model.add(Activation('softmax'))
    
    optimizer = RMSprop(lr=0.01)
    model.compile(loss='categorical_crossentropy', optimizer=optimizer)
    
    
    def sample(preds, temperature=1.0):
        # helper function to sample an index from a probability array
        preds = np.asarray(preds).astype('float64')
        preds = np.log(preds) / temperature
        exp_preds = np.exp(preds)
        preds = exp_preds / np.sum(exp_preds)
        probas = np.random.multinomial(1, preds, 1)
        return np.argmax(probas)
    
    # train the model, output generated text after each iteration
    for iteration in range(1, 20):
        print()
        print('-' * 50)
        print('Iteration', iteration)
        model.fit(X, y, batch_size=5000, nb_epoch=10)
    
        start_index = random.randint(0, len(data)-1)
    
        for diversity in [0.2, 0.5, 1.0, 1.2]:
            print()
            print('----- diversity:', diversity)
    
            generated = ''
            #sentence = text[start_index: start_index + maxlen]
            orig_sentence = data[start_index][:sentence_size]
            generated += orig_sentence
            print('----- Generating with seed: "' + orig_sentence + '"')
            sys.stdout.write(generated)
    
            for k in range(1):
                sentence = orig_sentence
                for i in range(maxlen-sentence_size):
                    x = np.zeros((1, maxlen, len(chars)))
                    for t, char in enumerate(sentence):
                        x[0, t, char_indices[char]] = 1.
        
                    preds = model.predict(x, verbose=0)[0]
                    next_index = sample(preds, diversity)
                    next_char = indices_char[next_index]
        
                    generated += next_char
                    sentence = sentence[1:] + next_char
        
                    sys.stdout.write(next_char)
                    sys.stdout.flush()
                print()
                
        print("Saving Model...")
        model.save_weights("model_" + name.split('.')[0] + ".h5", overwrite=True)
        with open("model_" + name.split('.')[0] + ".json", "w") as outfile:
            json.dump(model.to_json(), outfile)
    """