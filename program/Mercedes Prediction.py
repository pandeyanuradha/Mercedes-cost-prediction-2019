#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)

from keras.preprocessing.image import ImageDataGenerator, load_img
from keras.utils import to_categorical
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
import random

import os


# In[2]:


train_df=pd.read_csv('train.csv')
test_df=pd.read_csv('test.csv')


# In[3]:


num_train = len(train_df)
y_train = train_df['y']
id_test = test_df['ID']


# In[4]:


train_df.drop(['ID', 'y'], axis=1, inplace=True)
test_df.drop(['ID'],axis=1, inplace=True)


# In[5]:


train_df.head()


# In[6]:


test_df.head()


# In[7]:


test_df.isnull().values.any()


# In[8]:


train_df.isnull().values.any()


# In[9]:


df_all = pd.concat([train_df, test_df])


# In[10]:


df_all.head()


# In[11]:


df_all = pd.get_dummies(df_all, drop_first=True)


# In[12]:


df_all.head()


# In[13]:


from sklearn.preprocessing import MinMaxScaler
scaler = MinMaxScaler()
df_all = scaler.fit_transform(df_all)

X_train = df_all[:num_train]
X_test = df_all[num_train:]


# In[14]:


y_train.shape


# In[15]:


X_train.shape


# In[16]:


X_test.shape


# In[17]:


from keras.models import Sequential
from keras.layers import Dense
NN_model = Sequential()

# The Input Layer :
NN_model.add(Dense(128,kernel_initializer='normal',input_dim =X_train.shape[1], activation='relu'))

# The Hidden Layers :
NN_model.add(Dense(256,activation='relu'))
NN_model.add(Dense(256,activation='relu'))

# The Output Layer :
NN_model.add(Dense(1,activation='linear'))

# Compile the network :
NN_model.compile(loss='mse', optimizer='adam', metrics=['mse','mae'])


# In[19]:


history=NN_model.fit(X_train, y_train, epochs=150, batch_size=32, validation_split=0.3)


# In[20]:


print(history.history.keys())
# "Loss"
plt.plot(history.history['loss'])
plt.plot(history.history['val_loss'])
plt.title('model loss')
plt.ylabel('loss')
plt.xlabel('epoch')
plt.legend(['train', 'validation'], loc='upper left')
plt.show()


# In[23]:


output=NN_model.predict(X_test)


# In[24]:


print(output)

