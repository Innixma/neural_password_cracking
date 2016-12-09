
from keras.models import Sequential
from keras.layers import Dense
import numpy as np

data_dir = 'passwordGen/passwordFiles/'

def import_data(filename):
    f = open(filename, 'r')
    data = f.read()
    f.close()
    data = data.split('\n')
    data = data[:-1]
    data = [list(i) for i in data]
    data = [[ord(j) for j in i] for i in data]
    data = np.array(data)
    return data
    
p_8type2 = import_data(data_dir+'8type2.txt')
# fix random seed for reproducibility
seed = 7
np.random.seed(seed)

total_val = 0
for i in p_8type2:
    total_val += np.sum(i)
    
mean_val = total_val/p_8type2.shape[0]

c_8type2 = np.zeros([p_8type2.shape[0]])
for i in range(p_8type2.shape[0]):
    if np.sum(p_8type2[i]) > mean_val:
        c_8type2[i] = 1
    else:
        c_8type2[i] = 0

# create model
model = Sequential()
model.add(Dense(12, input_dim=8, init='uniform', activation='relu'))
model.add(Dense(8, init='uniform', activation='relu'))
model.add(Dense(1, init='uniform', activation='sigmoid'))

# Compile model
model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])

# Fit the model
model.fit(p_8type2[:25000], c_8type2[:25000], nb_epoch=400, batch_size=1000)
# evaluate the model
scores = model.evaluate(p_8type2[25000:], c_8type2[25000:])
print("%s: %.2f%%" % (model.metrics_names[1], scores[1]*100))


















