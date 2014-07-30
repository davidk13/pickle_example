import unittest, os, shutil
import time
from pickler import list_pickler, unpickler

class PickleTests(unittest.TestCase):

    def setUp(self):  # setUp gets run before all the tests.
                      # here, it's being used to create a temp folder to hold our 
                      # pickled list
        self.my_list = [1,2,3,'a','b','c']
        self.path = './pickle_temp'
        os.makedirs(self.path)  #os.makedirs() creates a directory
        self.file = os.path.join(self.path, 'list.pkl')

    def test_original_and_unpickled_list_same(self):
        list_pickler(self.file, self.my_list)
        unpickled_list = unpickler(self.file)
        self.assertEqual(self.my_list, unpickled_list)

    def tearDown(self):  # tearDown gets run after the tests have been run,
                         # whether they fail or pass. In this case, we're
                         # using tear down to delete our temp folder and its
                         # contents
        shutil.rmtree(self.path) #shutil.rmtree deletes a directory and all its contents