import unittest

class Test(unittest.TestCase):
    def testSomething(self):
        self.assertEqual(2+2, 4)
if __name__ == '__main__':
    unittest.main()