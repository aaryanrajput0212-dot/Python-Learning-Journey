#print("Hello")

#print("Aaryan","Rajput")

#print("Aaryan",end="016")

#print('123')

#print("Aaryan","Rajput",end="@@",sep="&&")

#
'''
a=5
b=5
print(a,id(a))
print(b,id(b))
'''
#
"""
Age=18
Name="Aaryan rajput"
print("My name is",Name)
print("And age is",Age)
"""
#
"""
Age=18
Name="Aaryan rajput"
print("My name is",Name,type(Name))
print("And age is",Age,type(Age))
"""
#Program to add two numbers
"""
num1=int(input("Enter first no:"))
num2=int(input("Enter second no:"))
sum=num1+num2
print("Sum of numbers:",sum)
"""

#Invalid keyword
"""
def=5
print(def)
"""
#
"""
import keyword
print(keyword.Kwlist)
"""
#Program to print the area of scalene triangle or by using heron's formula.
"""
A=int(input("Enter Side A:"))
B=int(input("Enter side B:"))
C=int(input("Enter side c:"))
s=(A+B+C)/2
Area=(s*(s-A)*(s-B)*(s-C))**(1/2)
print("Area of triangle:",Area)
"""
#Program to print Surface area of cylinder
"""
R=float(input("Enter Radius of cylinder:"))
H=float(input("Enter height of cylinder:"))
Pie=3.14
Area=Pie*R*R*H
print("Surface area of cylinder:",Area)
"""
#Program to perform all Bitwise operators
"""a=92
b=14
print(a&b)
print(a|b)
print(a^b)
print(a<<1)
print(a>>1)
print(a>>3)
print(a<<3)
"""
#Program to swap two values with the help of third variable.
"""
a=9
b=8
print("a:",a,"b:",b)
c=a
a=b
b=c
print("a:",a,"b:",b)
"""
#Program to swap to number without using third no.
"""
a=int(input("Enter value of a:"))
b=int(input("Enter value of b"))
a=a+b
b=a-b
a=a-b
print("Value of a after swap:",a)
print("Value of b after swap:",b)
"""
#Print complex no.
"""a=complex(3,4)
print(a)
print(type(a))
"""
#Index
"""
x="I read Python Book"
print(x[5])
print(x[6:14])
print(x[0:15:2])
print(x[ :7])
print(x[9: ])
print(x[-5])
print(x[-8:-2])
print(x[ :-7])
print(x[-4: ])
print(x[0])
print(x*2)
print(x+"2")
"""
#list
"""
x=[1,32.4,"Ravi"]
print(x)
print(type(x))
print(sizeof(x))
"""
#Tuple
"""y=(1,32.4,"Ravi")
print(y)
print(type(y))
print(y[2])
print(sizeof(y))"""
#Write a program to check if we can vote
"""
age=int(input("Enter age of person:"))
if(age>=18):
    print("Eligible to vote")
"""

#Write a program to check if a student is pass or fail
"""
marks=int(input("Enter the marks:"))
if(marks>=33):
    print("Student is pass")
else:
    print("Student is fail")
   """ 
#Write a program to swap two no. with the help of using XOR operator.
"""
a=int(input("Enter no a:"))
b=int(input("Enter no b:"))
print("Before Swapping")
print("a:",a)
print("b:",b)
a=a^b
b=a^b
a=a^b
print("After swapping")
print("a:",a)
print("b:",b)
"""
#Size of list
"""
import sys
x = [1, 32.4, "Ravi"]
print(x)
print(type(x))
print(sys.getsizeof(x))
"""
#Size of tuple(Advantage over list,Tuple take less memory)
"""
import sys
y=(1,32.4,"Ravi")
print(y)
print(type(y))
print(y[2])
print(sys.getsizeof(y))
"""
#Program to calculate the perimeter and semi-perimeter of triangle .
"""
A=int(input("Enter side A:"))
B=int(input("Enter side B:"))
C=int(input("Enter sidec:"))
Perimeter=A+B+C
Semi_perimeter=Perimeter/2
print("Perimeter of triangle:",Perimeter)
print("Semi perimeter of triangle:",Semi_perimeter)
"""
#Program to convert Fahrenheit to Celsius .
"""
F=float(input("Enter temperature in Fahrenheit:"))
C=(F-32)*(5/9)
print("Temperature in Celsius is :",C)
print("Temperature in Celsius is :", round(C, 2))#Round of to 2 decimal digit
"""
# Program to Calculate Simple Interest
"""
P=float(input("Enter principal amount:"))
R=float(input("Enter rate of interest in (%):"))
T=float(input("Enter time in years:"))
Si=(P*R*T)/100
print("Simple interest of principal amount:",Si)
print("Total amount:",P+Si)
"""
#Program to Calculate the Hypotenuse of a Right-Angled Triangle
"""
Base=float(input("Enter a length of Base:"))
Height=float(input("Enter a Height:"))
Hypotenuse=(Base**2+Height**2)**(1/2)
print("Hypotenuse of a Right-Angle Triangle:",round(Hypotenuse,4))
"""
#Program to calculate the compound Intereset.
"""
P=int(input("Enter the principal amount:"))
R=int(input("Enter the rate of interset in (%):"))
T=int(input("Enter the time in years:"))
A=P*(1+(R/100))**T
Ci=A-P
print("Total amount:",round(A,2))
print("Compound Interset :",round(Ci,2))
"""
#Program of logical operator.
"""a=5
b=0
c=10
d=15
print(a and b)#In AND gate if value is false(0) then output is 0,else output is last term of expression.
print(a and c)
print(b and c)
print(c and d)
print(a and b and c and d)
print(a and c and d)
print(a or b)
print(a or b or c or d)
print(d or c)#In OR gate first term of experssion is output
"""
#Program of identity operator
"""
a=10
b=5
c=10
d=a
print(a is b)
print(a is c)
print(a is d)
print(a is not b)
print(a is not c)
"""
#Program of Membership operator.
"""
fruits = ["apple", "banana", "cherry"]  
print("apple" in fruits)  
print("grape" not in fruits)
"""
#Convert a string to uppercase and lowercase
"""
A="My name is Aaryan Rajput.I am from Bijnor"
print(A.lower())# .lower()
print(A.upper())# .upper()
"""
#Find the number of occurrences of a substring.
"""
A="My name is Aaryan Rajput"
print(A.count("a"))
print(A.count("n"))
"""
#Check if a string starts and ends with a specific substring
"""
A="Hello Everyone,My name is Aaryan Rajput"
print(A.startswith("Hello"))
print(A.endswith("Aaryan Rajput"))
"""
#Check if a string starts and ends with a word.
"""
A="Excellent"
print(A.startswith("E"))
print(A.endswith("y"))
"""
#Extracting initials from a full name.
"""
Name=input("Enter name of person:")
word=Name.split()
for i in word:
    print(i[0],end=" ")
"""
#Count vowels in a string.
"""
s=input("Enter a string:")
count=0
for i in s:
    if i.lower() in "aeiou":
        count+=1
print("Total vowel in a string :",count)
"""
#Reverse words in a sentence.
"""
sentence=input("Enter a sentence:")
word=sentence.split()
reverse_words=" ".join(word[ : :-1])
print(reverse_words)
"""
#Reverse the characters instead of the words.
"""
sentence=input("Enter a sentence:")
reverse_word=sentence[ : :-1]
print(reverse_word)
"""
#Replace spaces with hyphens in a string.
"""
Word=input("Enter a word:")
print(Word.replace("a","*"))
"""
#Check if a string is a palindrome.
"""
s=input("Enter a string:")
if(s==s[ : :-1]):
    print("String is palindrome")
else:
    print("String is not palindrome")
"""
#Check if a string is a palindrome using loop.
"""
s = input("Enter a string: ")
rev = ""
for ch in s:
    rev = ch + rev
if s == rev:
    print("Palindrome")
else:
    print("Not a Palindrome")
"""
#Write a program to Find the Average of Three Numbers.
"""
A=int(input("Enter a no. A:"))
B=int(input("Enter a no. B:"))
C=int(input("Enter a no. C:"))
Average=(A+B+C)/3
print("Average of three number:",round(Average,2))
"""
#Write a program to Calculate Sum of 5 Subjects and Find Percentage.
"""
S1=56
S2=89
S3=98
S4=81
S5=76
sum=S1+S2+S3+S4+S5
Percentage=(sum/500)*100
print("Sum of five subject:",sum)
print("Percentage of five subejct:",Percentage)
"""
#Write a program to find gross salary.
"""
Basic=int(input("Enter basic salary:"))
HRA=0.20*Basic
DA=0.80*Basic
gross_salary=Basic+HRA+DA
print("Gross salary of employe:",gross_salary)
"""
#Write a program to Calculate Area of Circle.
"""
Radius=float(input("Enter a radius of circle:"))
pie=3.14
Area=pie*Radius*Radius
print("Area of circle:",Area)
"""
#Write a program to find the volume and surface area of cuboids.
"""
length=float(input("Enter length of a cuboid:"))
breadth=float(input("Enter breadth of cuboid:"))
height=float(input("Enter height of cuboid:"))
volume=length*breadth*height
Surface_area=2*(length*breadth+breadth*height+height*length)
print("Volume of cuboid:",volume)
print("Surface area of cuboid:",Surface_area)
"""
#Write a program to convert the string from upper case to lower case.
"""
A="AARYAN RAJPUT"
print(A.lower())
"""
#Write a program to convert the string from lower case to upper case.
"""
A="aaryan rajput"
print(A.upper())
"""
#Write a program to delete the all consonants from given string.
"""
s=input("Enter a string:")
result=""
for i in s:
    if i.lower() in "aeiou" or i==" ":
        result+=i
print("String without consonant:",result)
"""
#Write a program to count the different types of characters in given string.
"""
s=input("Enter a string:")
alphabet=0
digit=0
space=0
special=0
for i in s:
    if i.isalpha():
        alphabet+=1
    elif i.isdigit():
        digit+=1
    elif i.isspace():
        space+=1
    else:
        special+=1
print("Alphabets:",alphabet)
print("Digits:",digit)
print("Space:",space)
print("Special symbol:",special)
"""
#Count() is used to count how many time a value appear and len() functionis used to find the length of a string .
#Difference count() counts a how many time a same value or symbol repeat in string.

#Write a program to count number of words in a multi word string.
"""
s=input("Enter a string:")
print(len(s))
"""
#Write a program to sort the characters of a string.
"""
s = input("Enter a string: ")
chars = list(s)
chars.sort()
print("Sorted string:", "".join(chars))
"""
#Write a program for concatenation two strings.
"""
str1=input("Enter a string 1:")
str2=input("Enter a string 2:")
c=str1+str2
print("Concatenation of two string is:",c)
"""
#Write a program to find the length of a string.
"""
s=input("Enter:")
print(len(s))
"""
#Write a program to find the length of a string without using string function.
"""
s=input("Enter a string:")
count=0
for i in s:
    count+=1
print("Length of string :",count)
"""
#Write a program which prints initial of any name (print RAM for RAM KUMAR).
"""
name=input("Enter a name:")
A=name.split()
print("Initial word:",A[0])
"""
#Write a program to sort given names in Lexicographical sorting (Dictionary order)
"""
names = input("Enter names separated by spaces: ").split()
names.sort()
print(names) #Dictionary order
print("Names in Lexicographical Order:")
for name in names:
    print(name)
"""
#slow_print
"""
import time
def slow_print(text):
    for char in text:
        print(char, end="", flush=True)
        time.sleep(0.02)
    print()
slow_print("Write a program to sort given names in Lexicographical sorting")
"""
#Escape sequence character
"""
A="I am Aaryan Rajput.\nI want to crack GATE" #NEWLINE
print(A)
B="I am Aaryan Rajput.\t I want to crack GATE exam \t Because i want to study in IIT bombay."
print(B)
"""
#String slicing
"""
st="I like reading Books"
print(st[ :10])
print(st[0: ])
print(st[3:19])
print(st[-1:1])
print(st[-18:-1])
print(st[0:18:2])
print(st[ : :-1])
"""
#string functions
"""
A="I love studing"
print(A.startswith("I"))
print(A.endswith("studing"))
print(A.capitalize())
print(A.replace("love","like"))
print(A.replace("v","a"))
print(A.find("love"))
print(A.find("s"))
print(A.count("u"))
print(A.count("Q"))

"""
#WAP to input user's first name and print its length.
"""
name=input("Enter First name of user:")
len1=len(name)
print("Length of user's first name :",len1)
"""
#WAP to find the occurence of $ in a string.
"""
st=input("Enter a string:")
count=st.count("$")
print("Occurence of $ in string is:",count)
"""






















    






 
      

























