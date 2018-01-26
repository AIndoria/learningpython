import random
import sys
import os

# Find the largest palindrome made from the product of two 3-digit numbers.

l3number=999*999
print("Largest no. made from multiplication of two 3-digit numbers:", l3number)
for x in range(10000, l3number):
    l3num=str(x)
    if l3num[0]==l3num[-1] and l3num[1]==l3num[-2] and l3num[2]==l3num[-3]:
        palindrome=1
        if palindrome==1:
            largest_palindrome_number=x
print("Largest Palindrome made from the product of two 3-digit numbers:", largest_palindrome_number)
