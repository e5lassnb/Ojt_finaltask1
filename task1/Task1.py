
import unittest


#the main function that take the input and call checktheage
def main():
  name, age = input("Enter your name and your age: ").split()

  x = age.isnumeric()
  # print(int(x))

  if x==True:
      x = True
     # print(checktheage(age,name))
     # print(int(x))

  else:
        print("hi " + name + " please write your age.")
        while x==False:
         ag=input()
         x = ag.isnumeric()
         if x == False:
          print("hi " + name + " please write your age.")
          age2=input()
          x=age2.isnumeric()
          age=x
  print(checktheage(age,name))


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

