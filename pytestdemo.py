import unittest

class Demo(unittest.TestCase):
    '''test the add method'''
    def testAdd(self):
        self.assertEquals((1+4),5)
        
if __name__ == '__main__' :
    unittest.main() 
