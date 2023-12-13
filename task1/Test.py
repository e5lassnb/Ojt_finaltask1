from Task1 import checktheage
import unittest


class Testing(unittest.TestCase):


    def test_checktheage(self):
        result = checktheage(24,'ekhlass')
        str="hi ekhlass you are a Adult."
        self.assertEqual(result,str)

    def test_checktheage2(self):
        result = checktheage(1,'ekhlass')
        str="hi ekhlass you are a child."
        self.assertEqual(result,str)


    def test_checktheage3(self):
        result = checktheage(15,'ekhlass')
        str="hi ekhlass you are a Teenager."
        self.assertEqual(result,str)

    def test_checktheage(self):
        result = checktheage(24, 'ekhlass')
        str = "hi ekhlass you are a Adult."
        self.assertEqual(result, str)
    # def test_isnumber(self):
    #     result = main()
    #     str = "hi ekhlass you are a Adult."
    #     self.assertEqual(result, str)



if __name__ == '__main__':
    unittest.main()
