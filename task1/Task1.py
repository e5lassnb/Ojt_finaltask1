
import unittest


#the main function that take the input and call checktheage
def main():
  name, age = input("Enter your name and your age: ").split()

  x = age.isnumeric()

  if x==True:
     print(checktheage(x,name))
  else:
    # if age=="":
    #     print("hi please write your age.")

    print("hi " + name + " please write your age.")
    while x==False:
     ag=input()
     x = ag.isnumeric()
     if x == False:
         print("hi " + name + " please write your age.")
  print(checktheage(x,name))


#print the write massege if the user inter the name and the write age
def checktheage(c,name):
    if int(c) > -1 and int(c) < 13:
        return ("hi " + name + " you are a child.")
    elif int(c) > 12 and int(c) < 18:
        return ("hi " + name + " you are a Teenager.")
    elif int(c) > 17:
        return ("hi " + name + " you are a Adult.")



if __name__ == '__main__':
    main()

# class Testing(unittest.TestCase):
#
#
#     def test_checktheage(self):
#         result = checktheage(24,'ekhlass')
#         str="hi ekhlass you are a Adult."
#         self.assertEqual(result,str)
#
#     def test_checktheage2(self):
#         result = checktheage(1,'ekhlass')
#         str="hi ekhlass you are a child."
#         self.assertEqual(result,str)
#
#
#     def test_checktheage3(self):
#         result = checktheage(15,'ekhlass')
#         str="hi ekhlass you are a Teenager."
#         self.assertEqual(result,str)
#

    # def test_main1(self):
    #     result = main()
    #     str="hi ekhlass you are a Teenager."
    #     self.assertEqual(result,str)
    #



#
# if __name__ == '__main__':
#     unittest.main()
