#!/usr/bin/python3
# Filename: pickling.py

import pickle

# the name of the file where we will store the object
shoplistfile = 'shoplist.data'
# the list of things to buy
shoplist = ['apple','mango','carrot']

# Write to the file
f = open(shoplistfile,'wb')
pickle.dump(shoplist,f) # dump the object to a file
f.close()

del shoplist # destroy the shoplist variable

# Read back from the storage
f = open(shoplistfile,'rb')
storelist = pickle.load(f) # load the object from the file
print(storelist)
