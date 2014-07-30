import sys
import pickle

def list_pickler(path, my_list):
    f = open(path, 'wb')
    pickle.dump(my_list, f)
    f.close()

def unpickler(path):
    f = open(path, 'rb')
    my_list = pickle.load(f)
    f.close()
    return my_list