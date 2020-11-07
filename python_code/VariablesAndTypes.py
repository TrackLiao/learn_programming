#!/usr/bin/env python
# coding=utf-8
print("Int section")
myint = 7
print(myint)

print("float section")
myfloat = 7.0
print(myfloat)
myfloat = float(7)
print(myfloat)

print("String section")
mystring = 'hello'
print(mystring)
mystring = "hello"
print(mystring)

# The difference between the two is that using double quotes makes it easy to include apostrophes 
#(whereas these would terminate the string if using single quotes)

mystring = "Don't worry about apostrophes"
print(mystring)

print("Simple operators on numbers and strings")
one = 1
two = 2
three = one + 2
print(three)

hello = "hello"
world = "world"
helloworld = hello + " " + world
print(helloworld)

# assignments can be done on more than one variable "simultaneously"
a, b = 3, 4
print(a, b)

# mixing operators between numbers and strings is not supported
# this will not work!
one = 1
two = 2
hello = "hello"

# print(one + two + hello)

# Exercise

mystring = "hello"
myfloat = 10.0
myint = 20

# test the code
if mystring == "hello":
    print("String: %s" % mystring)
if isinstance(myfloat, float) and myfloat == 10.0:
    print("Float: %f" % myfloat)
if isinstance(myint, int) and myint == 20:
    print("Integer: %d" % myint)




