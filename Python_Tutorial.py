#Reference : https://www.geeksforgeeks.org/getting-started-with-python-programming/?ref=lbp

# print("Hello world")

# name = "Jamal"

# print("Hello : "+ name)

#-------------------------------------------
# """ 
# Multiline Comment
# """
# # printing string with \
# sentence = "Tiger is a national animal of India\
#     It is Fearless in Nature. Its main food is Fats and Proteins."

# #printing numbers sum with \
# total = 1+2+456+4+56+\
#     +45+100
# print(sentence)

# print(total)

#------------------------------------------------

# numbers = [1,2,3,4,5,6]

# print(numbers)

# Getting input from user

# name = input("Enter your name")
# print(f"Hello :"+ name)

# x =5
# x = "Samantha"

# print(x)
#-----------------------------------------------------------
# # Typecast string to float
# num = float("23")
# print(num)


# Typecast int to string

# num = 10

# stringnum  = str(num)
# print(stringnum)

#-------------------------------------------------

# Check their datatypes

# myint = 10
# myfloat = 10.20
# mystring = "My string"
# myBool = True
# mylist = [1,2,3,4]
# mydict = {"a": "apple"}
# mytuple = ("jelly","gum","juice")
# myset = set(mydict)

# myset2 = {2,3,4,1,1,2}

# print(type(myint))
# print(type(myfloat))
# print(type(mystring))
# print(type(myBool))
# print(type(mydict))
# print(type(mylist))
# print(type(myset))
# print(type(mytuple))
# print(myset)
# print(myset2)

#------------------------------------------------
# Defining a function
# def printMyname(name):
#     print("Hello :"+name)


# printMyname("Jamal")

#------------------------------------------------------

#Delete a variable

# x = 10
# print(x)
# del x

# #------------------------------------------------------------

# #Swapping Variable

# a,b = 10,20
# a,b = b,a
# print(a,b)

#---------------------------------------------------------

# #Length of string

# word = "hello"
# size = len(word)

# print("length of word : ", size)
# #------------------------------------------------------------
# #python keywords
# import keyword

# print(keyword.kwlist)

#------------------------------------------------------
#boolean

# print(True == 1)
# print (True +True + True)

# print(True + False + True)
# print(None == 0)

# print(None == [])

#---------------------------------------------------------
#Logic Operators

# a = True
# b = False

# # And Needs both True for True
# print("and Logic", (a and b))

# # OR Needs one True for True
# print("or logic : ",(a or b))

# # not logic gives opposite given bool

# print(not a)

#---------------------------------------------------------------

#Membership Operator : in , is ,
# print(3 in [1,2,3,4])

# letter = 'a'
# if letter in 'string':
#     print(letter," is  present")
# else :
#     print(letter," is not present")

# a =2
# b =3
# print(a is b)

#------------------------------------
#Iteration keywords

# for i in range(20):
#     if i %2 ==0 :
#         continue
#     if i == 4:
#         break

#     print(i)



# count = 0
# while( count < 4):

#     print(count)
#     count += 1

# for i in range(5):
   
#     pass

#------------------------------------------------

#ERROR handling
# b =0
# try :
#     a = 2/b
#     print(a)
# except ArithmeticError:
#     print("Zero cant be divisor")
# finally:
#     print("This is always exectuted")

# assert b != 0 ,"Divide by 0 error"

# temp = "hello world"

# if (temp != "hello"):
#     raise TypeError ("Both are different strings")

#-----------------------------------------------------


#Class keyword:

# class Dog :
#     attr1 = "Mammal"
#     attr2 = "Dog"

#------------------------------------------------------

# return : This keyword is used to return from the function.
# yield : This keyword is used like return statement but is used to return a generator.

# def fun():
#     return 1+2

# print(fun())


# def fun():
#     yield 1

#     yield 2

# for value in fun():
#     print(value)

#----------------------------------------
#Lambda Function

# x = lambda a : a+a+a

# a = 10
# c = 2
# func = lambda b : b*b
# print(func(5))
# # print(x(2))


#----------------------------------------------
# Math module

# import math;

# n = math.factorial(3)
# print(n)

#---------------------------------------------------
# import asyncio
# async def say_hello():
#     print("Hello")
#     await asyncio.sleep(2)
#     print("Hi")

# asyncio.run(say_hello())

#Example for async and await:
# import asyncio

# async def task1():
#     print("Task1 line 1 is printed")
#     await asyncio.sleep(3)
#     print("Task1 line 2 is printed")

# async def task2():
#     print("Task2 line 2 is printed")
#     await asyncio.sleep(2)
#     print("Task2 line 2 is printed")

# async def taskmain():
#     await asyncio.gather(task1(),task2())

# asyncio.run(taskmain())


# with open('text.txt','w') as file:
#     file.write("Thank you!")

#--------------------------------------------------------
# Output Formatting

#1. formatting using .format

# name = "Jamal"
# age = 23
# city = "Chennai"

# print(name," - ",age," - ",city)

# amount = 120.95

# print("Amount is ${:.2f}".format(amount))

#2. using sep and end;

# print("a","2","d",sep="-")
# print("a","2","d",sep="@")
# print("a","2","d",sep="#")


# print("jamal",end="@")
# print("gmail.com")

#3. using f-string

# name = "Jamal"
# age =23

# print(f"{name} is {age} years old")

#4. using # operator

# %d –integer
# %f – float
# %s – string
# %x –hexadecimal
# %o – octal

# num = 23

# print("%d is odd number" %num)



#------------------------------------------------
#Taking multiple inputs in python

# x,y = input("Enter two values :").split()
# print(x," ",y)

#Conditional Inputs in Python

# age = int(input("Enter your age"))

# if (age < 0):
#     print("Enter the Valid age")

# elif (age < 18):
#     print("Youre a minor")

# elif (age > 18):
#     print("Youre an adult")

#-------------------------------------------------------
#Date : 28-02-25

# print(5/3)
# print(5//3)
# print(5**2)

# num = input("Enter the number")
# print(type(num))

# print("Geeks for Geeks",end="*")
# print("Hello")

# print("%.2f is float, %d is int" %(1,34))

#Formatting Output using The Format Method

# print("{0} is a number. {1} is float.".format(1,23.23))
# print("{0} is a person".format("Jamal"))


#-- # Mixing positional and named arguments
# string = "{0:10} is a person , {1} years old"
# print(string.format("Jamal",23))

# -- Format integers and floats with specified width and precision

# string1  = "{0:.4f} is a float".format(10)
# string2  = "{0:10.2f} is a precisioned value".format(10) 
# 0: (before : is denotes the position of element is given format)
# :10 (after : is denotes space width btwn float and word)
# .2f (.2 denotes precision. For ex: 13.45)
# f -> denotes float
# print(string1)
# print(string2)


# string3 = "{1:.2f} fahrenheit is a body's temperature. {0:d} is avg lifespan of indian ".format(72,98.7)
# print(string3)

# string4 = "{a} is a Dog which  is {b} years old".format(a="Sam",b=3)
# print(string4)

# string = "Hello Jamal"

# print("Left aligned")
# print(string.ljust(40,"#"))

# print("\nCenter aligned ")
# print(string.center(40,"!"))

# print("\nRight aligned ")
# print(string.rjust(40,"*"))

# mylist = list(input())

# print(mylist)

#-----------------------------------------------

#Set an Input Time Limit using the inputimeout module

# from inputimeout import inputimeout

# try :
#     name = inputimeout("Enter the name", timeout=10)

# except exception : 
#     timeover = "Entry time is over"
#     print(exception,timeover)

# print(name)

# print("hello")

#---------------------------------------------------------------------------------------------------------
#Set an Input Time Limit using the inputimeout module

# from threading import Timer

# inputtime = int(input("Enter the time in seconds"))

# t = Timer(inputtime, lambda : print("\nYour entry time is over"))

# t.start()

# print("Enter your pet animal")
# pet = input("Enter the pet name")
# print(pet)

# t.cancel()


#------------------------------------------

# try :
#     num = int(input("Enter the number"))
#     print(num)
# except ValueError:
#     print("Invalid Input, ENter the number")

#---------------------------------------------------

# name = input("Enter the name")
# print(name)
# print(type(name))

# x,y,z = input("Enter multiple inputs").split()
# print(x,y,z)

