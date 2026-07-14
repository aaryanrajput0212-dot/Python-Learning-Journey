#Write a program to check if we can vote
"""age=int(input("Enter age of person:"))
if(age>=18):
    print("Eligible to vote")"""

#Write a program to check if a student is pass or fail
"""marks=int(input("Enter the marks:"))
if(marks>=33):
    print("Student is pass")
else:
    print("Student is fail")"""

#Program to find shape is square or rectangle
"""
length=int(input("Enter length:"))
breadth=int (input("Enter breadth :"))
if(length==breadth):
    print("Square")
else:
    print("Rectangle")
"""
#Write a program to give bonus if year of service is greater than 5 year .
"""
Year=int(input("Enter year of service"))
salary=int(input("Enter salary of user"))
if(Year>5):
    print("Bonus:",salary*0.20)
else:
    print("Not eligible for bonus")
    """
#Program to check wheather a person is eligible for vote or not
"""age=int(input("Enter age of person:"))
if(age>=18):
    print("Eligible to vote")
else:
    print("Not Eligible for vote")"""
#check if no. is even or odd
"""Num1=int(input("Enter number:"))
if(Num1%2==0):
         print("Number is even")
else:
    print("Number is odd")"""
#check no. is divisible by seven or not
"""A=int(input("Enter no."))
if(A%7==0):
    print("Divisible by seven")
else:
    print("Not divisible by seven")"""
#Write a program to display"hello" if a number entered by user is a multiple of five,otherwise print"bye"
"""
A=int(input("Enter no."))
if(A%5==0):
    print("Hello")
else:
    print("Bye")
    """
#
"""if a=9
if(a>5 and a<=10):
    print("Hello")
else:
    print("Bye")"""
#check wheather a number is divisible by 2 and 3 both.
"""
N=int(input("Enter no:"))
if(N%2==0 and N%3==0):
    print("Divisible by both")
else:
    print("Not divisible by both")
    """
#Program to check if a no is positive,negative,or zero.
"""
N=int(input("Enter a no.:"))
if(N>0):
    print("No. is positive")
elif(N<0):
    print("No is Negative")
else:
    print("NO is zero")
    """
#Program of automatic grading system on the basis of marks.
"""
M=int(input("Enter marks:"))
if(M>=91 and M<=100):
    print("Grade A")
elif(M>=81 and M<=90):
    print("Grade B")
elif(M>=71 and M<=80):
    print("Grade C")
elif(M>=61 and M<=70):
    print("Grade D")
elif(M>=51 and M<=60):
    print("E")
else():
    print("Invalid Marks")
    """
#Program of Greater of two numbers.
"""
A=int(input("Enter no A:"))
B=int(input("Enter no B:"))
if(A>B):
    print("A is greater ")
else:
    print("B is greater")
    """
#Write a program of greater among three numbers.
"""
A=int(input("Enter no A:"))
B=int(input("Enter no B:"))
C=int(input("Enter no C:"))
if(A>B and A>C):
    print("A is greater among three numbers")
elif(B>C):
    print("B is greater among three numbers")
else:
    print("C is greater")
"""    
#Write a program to find the electric bill.
"""
A=int(input("enter no of unit:"))
if(A<=150):
    print("Total Bill:",660+(A*5.50))
elif(A>=150 and A<=250):
    print("Total Bill:",660+(150*5.5)+((A-150)*6.5)
else:
    print("Total bill:",660+(150*5.5)+(100*6.5)+((A-250)*7.5)
    """
#Program to find roots of quadratic eq.
"""
A=int(input("Enter Value of A:"))
B=int(input("Enter Value of B:"))
C=int(input("Enter Value of C:"))
D=B**2-(4*A*C)
if(D==0):
      print("Real and equal")
elif(D>0):
    print("Real and distict")
else:
    print("Imaginary")
    """
#Write a program to write days of week by using numbers(1-7).
"""
Num=int(input("Enter number between 1 to 7:"))
if(num==1):
    print("Monday")
elif(num==2 ):
    print("Tuesday")
elif(num==3 ):
    print("Wednesday")
elif(num==4 ):
    print("Thursday")
elif(num==5 ):
    print("Friday")
elif(num==6):
    print("Saturday")
else:
    print("Sunday")
    """
#Check wheather a alphabet is vowel or not.
"""
Ch=input("Enter a alphabet:").lower()
if(ch in "aeiou"):
    print("Alphabet is vowel")
else:
    print("Alphabet is consonant")
    """
#Program to find the quadrant by the value of x and y.
"""
X=int(input("Enter coordinate of X:"))
Y=int(input("Enter coordinate of Y:"))
if(X>0 and Y>0):
    print("First quadrant")
elif(X<0 and Y>0):
    print("Second Quadrant")
elif(X<0 and Y<0):
    print("Third quadrant")
else(X>0 and Y<0):
    print("Fourth quadrant")
    """
#Program to print the first 10 natural no.
"""
n=int(input("Enter a no."))
i=1
while(i<=n):
    print(i)
    i=i+1
    """
#output
"""
i=10
while(i>=1):
    print(i)
    i=i-1
    """
#Program to find sum of n number
"""
i=1
sum=0
n=int(input("Enter no.:"))
while(i<=n):
    sum=sum+i
    i=i+1
print(sum)
"""
#Program to find sum of square of number up to n.
"""
i=1
sum=0
n=int(input("Enter no.:"))
while(i<=n):
    sum=sum+i**2
    i=i+1
print(sum)
"""
#
"""
i=1
sum=0
while(i<=100):
    if(i%2==0):
        sum=sum+i
    print(i)
    i=i+1
    """
#sum of digit of number
"""
i=int(input("Enter the number:"))
sum=0
while(i>0):
    d=i%10
    sum=sum+d
    i=i//10
print(sum)
"""
#Reverse
"""
i=int(input("Enter a no.:"))
rev=0
while(i>0):
    d=i%10
    rev=(rev*10)+d
    i=i//10
print(rev)
"""
#palindrome
"""
i=int(input("Enter a no.:"))
x=i
rev=0
while(i>0):
    d=i%10
    rev=(rev*10)+d
    i=i//10
print(rev)
if(rev==x):
    print("palindrome")
else:
    print("Not palindrome")
    """
#Factorial
"""i=int(input("Enter a no:"))
fact=1
while(i>0):
          fact=fact*i
          i=i-1
print(fact)
"""
#Range fn
"""for i in range(1,11):
    print(i)
    """
#
"""for i in range(10,0,-1):
    print(i)
    """
#Table of no.
"""n=int(input("Enter a no:"))
for i in range(1,11):
    print(i*n)
    """
#Factorial by using for loop
"""
num=int(input("Enter a no."))
fact=1
for i in range(1,num+1):
    fact=fact*i
print(fact)
"""
#
"""for i in range(1,5):
    for j in range(i):
        print("*",end=" ")
    print()
    """
#Program of trafic signal by using conditional statement.
"""
color=input("Enter a color:").lower()
if(color=="green"):
    print("Light Green 'GO GO GO'")
elif(color=="yellow"):
    print("Be ready to go")
elif(color=="red"):
    print("Stop")
else:
    print("Trafic light is broken")
"""
#
"""
Difference between if and elif statement:In if statement all conditions should be
check and in elif statement if one condition is correct then others conditions after
that conditions are not check.Ex-
"""
#if statement over elif
"""
num=8
if(num>=2):
    print("num is greater than 2")
if(num>=5):
    print("num is greater than 5")
"""
#elif statement over if
"""
num=8
if(num>=2):
    print("num is greater than 2")
elif(num>=5):
    print("num is greater than 5")
"""
#In if-else statement or elif statement else can't contain any condition ,it only consist of print statement.
#Indentation contain space of one tab or we can say 4 spaces.
#Nesting statement
"""
percentage=int(input("Enter percentage of student:"))
if(percentage>=45):
    if(percentage>=75):
        print("Eligible for JEE counselling and all other counselling too")
    else:
        print("Only eligible for UPTAC counselling")
else:
    print("Not eligible for any counselling,\nBetter Luck next time")
"""
#Check if a year is a leap year
"""
year=int(input("Enter a year:"))
if((year%400==0)or(year%4==0 and year%100!=0)):
    print("Year is leap year")
else:
    print("Year is not leap year")
"""
# Simple calculator using if-elif-else
"""
import time
def slow_print(text):
    for char in text:
        print(char, end="", flush=True)
        time.sleep(0.02)
    print()
slow_print("** SIMPLE CALCULATOR **")

num1=int(input("Enter a first number:"))
num2=int(input("Enter a second number:"))
operator=input("Enter (+,-,*,/):")
if(operator=="+"):
    print("Result:",num1+num2)
elif(operator =="-"):
    print("Result:",num1-num2)
elif(operator =="*"):
    print("Result:",num1*num2)
elif(operator =="/"):
    if(num2!=0):
        print("Result:",num1/num2)
    else:
        print("Divisible by zero is not possible")
else:
    print("Invalid operator ")
"""
#. Write a program to categorize a person's age into child (0-12), teenager (13-19), 
# adult (20-59), and senior (60+).
"""
age=int(input("Enter a age of person:"))
if(age<=12):
    print("Person is child")
elif(age>13 and age<=19):
    print("Person is teenager")
elif(age>19 and age<=59):
    print("Person is adult")
elif(age>59):
    print("Person is senior citizen")
else:
    print("Wrong age")
"""
#Write a program to determine if a triangle is valid based on the lengths of its sides. 
"""
a=int(input("Enter side a:"))
b=int(input("Enter side b:"))
c=int(input("Enter side c:"))
if(a<=0 or b<=0 or c<=0):
    print("Invalid input,Side length must be positive")
else:
    if((a+b>c)and(a+c>b)and(c+a>b)):
        print("Triangle is valid")
    else:
        print("Triangle is not valid")
"""
#Nesting statement
"""
age=int(input("Enter age of Driver:"))
if(age>=18):
    if(age>=80):
        print("Cannot Drive\tTake rest")
    else:
        print("Can Drive")
else:
    print("Cannot Drive")
"""
# Program to print the sentence in slow motion.
"""
import time
def slow_time(text):
    for i in text:
        print(i,end="",flush=True)
        time.sleep(0.02)
slow_time("Hi,My name is Aaryan Rajput.what is your name")
"""
#Program to find the greater in four numbers.
"""
a=int(input("Enter the no. a:"))
b=int(input("Enter the no. b:"))
c=int(input("Enter the no. c:"))
d=int(input("Enter the no. d:"))
if(a>b and a>c and a>d):
            print("a is greater in all four numbers")
elif(b>c and b>d):
    print("b is greater in all four numbers")
elif(c>d):
    print("c is greater in all four numbers")
else:
    print("d is greater in all numbers")
"""
#List
#Basic of list
"""
list=[87,78.7,28,928,38,"Aaryan",True]
print(list)
print(len(list))
print(type(list))#class of list variable
print(list[1])
print(list[3])
list[4]="Rajput"
print(list)
"""
#String slicing
"""
A=[1,3,5,6,7,4,5,65,646,453,3554,353,45,35,3,535,3,53,355]
print(A[:18])#A[0:18]
print(A[0:])#A[0:len(A)]
print(A[0:len(A)])
print(A[3:9])
print(A[0:19])
print(A[0:18:2])
print(A[-18:-1])#Negative indexing
print(A[-5:-1])
"""
#List Function
"""
L=[1,3,4,2,56,78,45,3,67,45,90]
print(L.append(101))
List is a mutuable data type so,it make changes in existing list and print None if
implement function in print statement
"""
#List Functions
"""
L=[1,3,4,2,56,78,45,3,67,45,90]
L.append(101)#append is used to add single element at list.
print(L)
L.sort()#Sort the element of the list in ascending order.
print(L)
L.sort(reverse=True)
print(L)#Sort the element of the list in descending order.
L.reverse()
print(L)#Reverse all element of the list.
L.insert(5,1000)#Insert the element at specific index.
print(L)
L.remove(3)#remove the input element from the list.
print(L)
L.pop(8)#remove the element at specific index.
print(L)
"""
#Store one element in list
"""
L=[1]
print(L)
print(type(L))
"""
#Tuple
#Basic of tuple
"""
T=(1,2,3,4,5,6,7,8,9,10)
print(T)
print(type(T))
print(len(T))
print(T[4])
print(T[6])
T[1]=100#Make error because tuple is immutable (unchangable) data type.
"""
#Tuple slicing
"""
T=(1,2,3,4,5,6,7,8,9,10)
print(T[3:8])
print(T[0:8:2])
"""
#Tuple function
"""
T=(1,2,3,4,5,1,5)
print(T.index(5))
Note:-
In tuple we directly implement functions in print statement as tuple is immutable data
type ,it not show None.
"""
#count
"""
T=(1,2,3,4,5,1,5)
print(T.count(5))
"""
#WAP to ask the user to enter name of their 3 favourite movie and store them in a list.
"""
Movies=[]
Movie1=(input("Enter 1st favourite movie:"))
Movie2=(input("Enter 2nd favourite movie:"))
Movie3=(input("Enter 3rd favourite movie:"))
Movies.append(Movie1)
Movies.append(Movie2)
Movies.append(Movie3)
print(Movies)
"""
#WAP to check if a list contain a palindrome of a element.(Hint use copy() function)
"""
L=[1,2,3,4,5]
L_copy=L.copy()
L_copy.reverse()
if(L==L_copy):
    print("Palindrome")
else:
    print("Not palindrome")
 """
#WAP to count the number of student with the "A" grade in the following tuple ["C","D",A","A","B","B","A"]
"""
grade=("C","D","A","A","B","B","A")
print(grade.count("A"))
"""
#WAP to sort a list in ascending order.["C","D",A","A","B","B","A"]
"""
l=["C","D","A","A","B","B","A"]
l.sort()
print(l)
"""
#Dictionary
#WAP to create a dictionary of different datatype keys and print it.
"""
Dict={"name":"Aaryan","D.O.B":2007,"Address":"Bijnor","Marks":86.5,6:"Favourite No.",
      "Age":True}
print(Dict)
print(len(Dict))#Size is calculated by count keys of dictionary
print(type(Dict))
"""
#WAP to create dictionary ,access element by keys and add new element.
"""
Dict={"name":"Aaryan","D.O.B":2007,"Address":"Bijnor","Marks":86.5,6:"Favourite No.",
      "Age":True}
print(Dict["name"])
print(Dict["Marks"])
Dict["Surname"]="Rajput"
print(Dict)
"""
#Empty Dictionary
"""
A={}
A["Name"]="Aaryan"
A["Surname"]="Rajput"
print(A)
"""
#Nested Dictionary
"""
1Dict={"Name":"Aaryan Rajput","Subject":{"Phy":87,"DSA":91,"chem":32,"Maths":96},"Age":19}
print(Dict)
print(Dict["Subject"]["DSA"])
Dict["Address"]="Bijnor"
print(Dict)
"""
#Dictionary functions.
"""
Dict={"name":"Aaryan","D.O.B":2007,"Address":"Bijnor","Marks":86.5,6:"Favourite No.",
      "Age":True}
print(Dict.keys()) #Print list of all keys in dictionary
print(Dict.values()) #Print list of all value in dictionary
print(Dict.items()) #Print keys,values pairs of dictionary in a tuple
print(Dict.get("name")) #get is used to get the value by using key
Dict.update({"Surname":"Rajput"}) #Used to add new key,value pair in dictionary.
print(Dict)
"""
#Program of Accessing values of dictionary by normal method and .get method.
"""
Dict={"name":"Aaryan","D.O.B":2007,"Address":"Bijnor","Marks":86.5,6:"Favourite No.",
      "Age":True}
print(Dict["name"])
print(Dict.get("name"))
print(Dict.get("name2"))#When we find non existing key it return None.
print(Dict["name2"])#when we find non existing key it gives error.
"""
#Sets
#Write a program to create a set and print it.
"""
set={1,2,3,4,5,5,6,7,3,3,3,"Aaryan Rajput",(39.5,56.8,89.7),True,5.6}
print(set)
print(len(set))
"""
#Write a program to create a empty set.
"""
empty_set=set() #correct method
print(type(empty_set))
s={}
print(type(s)) #Dictionary not set
"""
#Set methods
"""
s={1,2,3,4,5,6,7,8,2,1,3,4}
s.add("Aaryan Rajput")
s.add(50.9)
print(s)
s.remove(3)
print(s)
print(s.pop())
print(s)
print(s.clear())
print(s)
"""
#Program of using union and intersection function in set.
"""
s1={1,2,3,4,5}
s2={4,5,6,7,8,}
print(s1.union(s2))
print(s1.intersection(s2))
"""
# WAP to store a word and there meaning in python and also store a word with two meaning.
"""
dict={"envy":("Jealousy","Angry with someone"),"Flock":"Group of animals"}
print(dict)
print(dict.get("envy"))
"""
#
"""
You are given a list of subjects for students.Assume one classroom is required for 1 subject
.How many classrooms are needed by all students.
"python","java","c++","python","javascript","java","python","java","c++","c"
"""
"""
S={"python","java","c++","python","javascript","java","python","java","c++","c"}
print("Classrooms required by all students:",len(S))
"""
#WAP to enter marks of 3 subjects from the user and store them in a dictionary.start with an empty
#dictionary & add one by one .Use subjects name as key & marks as value.
"""
result={}
x=int(input("Enter marks of DSA:"))
result.update({"DSA":x})
y=int(input("Enter marks of maths:"))
result.update({"Maths":y})
z=int(input("Enter marks of IOT:"))
result.update({"IOT":z})
print(result)
"""
# **IMPORTANT**
#Figure out a way to store 9 and 9.0 as separate values in the set.add(Hint:use built-in data types)
"""
s={9,"9.0"}
print(s)
a={("float",9.0),("int",9)}
print(a)
"""
# Nested loops to print a pattern.
"""
*
* *
* * *
* * * *
* * * * *
"""
"""
for i in range(1,6):
    for j in range(1,i+1):
        print("*",end=" ")#We use end To avoid print * in next line.
    print()
"""
# Nested loops to print a pattern.
"""
n=int(input("Enter number of row you want in pattern:"))
for i in range(1,n+1):
    for j in range(1,i+1):
        print("#",end=" ")
    print()
"""
#Nested loops to print a pattern.
"""
1
1 2
1 2 3
1 2 3 4
1 2 3 4 5
"""
"""
n=int(input("Enter number of row you want in pattern:"))
for i in range(1,n+1):
    for j in range(1,i+1):
        print(j,end=" ")
    print()
"""
#Nested loops to print a pattern.
"""
1
2 2
3 3 3
4 4 4 4
5 5 5 5 5
"""
"""
n=int(input("Enter number of row you want in pattern:"))
for i in range(1,n+1):
    for j in range(1,i+1):
        print(i,end=" ")
    print()
"""
#Nested loops to print a pattern.
"""
1
2 3
4 5 6
7 8 9 10
11 12 13 14 15
"""
"""
nums=int(input("Enter number of row you want in pattern:"))
n=1
for i in range(1,nums+1):
    for j in range(1,i+1):
        print(n,end=" ")
        n+=1
    print()
"""
#Nested loops to print a pattern.
"""
A
A B
A B C
A B C D
A B C D E
"""
"""
n=int(input("Enter number of row you want in pattern:"))
for i in range(1,n+1):
    for j in range(65,65+i):
        print(chr(j),end=" ")
    print()
"""
#Nested loops to print a pattern.
"""
* * * * *
* * * *
* * *
* *
*
"""
"""
n=int(input("Enter number of row you want in pattern:"))
for i in range(n,0,-1):
    for j in range(i):
        print("*",end=" ")
    print()
"""
#Nested loops to print a pattern.
"""
    *
   ***
  *****
 *******
*********
"""
"""
n=int(input("Enter number of rows:"))
for i in range(1,n+1):
    print(" "*(n-i)+"*"*(2*i-1))
"""
#Nested loops to print a pattern.
"""
*********
 *******
  *****
   ***
    *
"""
"""
n=int(input("Enter number of rows:"))
for i in range(n,0,-1):
    print(" "*(n-i)+"*"*(2*i-1))
"""
#Nested loops to print a pattern.
"""
    *
   ***
  *****
 *******
*********
*********
 *******
  *****
   ***
    *
"""
"""
n=int(input("Enter number of rows:"))
for i in range(1,n+1):
    print(" "*(n-i)+"*"*(2*i-1))
for i in range(n,0,-1):
    print(" "*(n-i)+"*"*(2*i-1))
"""
# Use break to terminate a loop when a condition is met.
"""
for i in range(10):
    if(i==7):
        break
    print(i)
"""
# Use continue to skip an iteration when a condition is met.
"""
i=1
while i<=15:
    if(i==6):
        i+=1
        continue
    print(i)
    i+=1
"""
#Use pass as a placeholder in a loop.
"""
for i in range(10):
    if i==2:
        pass
    print(i)
"""
#Check if a number is prime using a for loop and else.
"""
num=int(input("Enter a num:"))
if(num<=1):
    print(num,"is not a prime number")
else:
    prime=True
    for i in range(2,num):
        if(num%i==0):
            prime=False
            break
if prime:
    print(num,"is a prime number")
else:
    print(num,"is not a prime number")
"""
#.Print Fibonacci Series: 0, 1, 1, 2, 3, 5, 8, 13 . . . .
"""
n=int(input("Enter no of terms for the fibonacci series:"))
if(n<=0):
    print("Please enter a valid no of term")
else:
    a=0
    b=1
    for i in range(n):
        print(a,end=" ")
        c=a+b
        a=b
        b=c
"""
#Program to compute the factorial of a given number.
"""
n=int(input("Enter a no. to find factorial:"))
if(n<=0):
    print("Factorial is not defined for negative number")
elif(n==0):
    print("Factorial of 0 is 1")
else:
    fact=1
    for i in range(1,n+1):
        fact=fact*i
    print(f"Factorial of {n} is {fact}.")
"""
#Program to compute the sum of n natural numbers.
"""
n=int(input("Enter a number:"))
if(n<=0):
    print("Entered number is not a natural number")
else:
    sum=0
    for i in range(1,n+1):
        sum+=i
    print(f"Sum of natural number up to {n} is {sum}.")
"""
# Write a program to find the greatest of three numbers using Nested if without elif.
"""
a=int(input("Enter a number a:"))
b=int(input("Enter a number b:"))
c=int(input("Enter a number c:"))
if(a>b):
    if(a>c):
        print(f"{a} is greater in all number")
    else:
        print(f"{c} is greater in all number")
else:
    if(b>c):
        print(f"{b} is greater in all numbers")
    else:
        print(f"{c} is greater in all numbers")
"""
#Write a program to Add two Complex Numbers.
"""
a=complex(input("Enter first complex number:"))
b=complex(input("Enter second complex number:"))
sum=a+b
print("Sum of two complex number :",sum)
"""
#Write a program to print color names, if the user enters the first letter of the color name.
"""
ch=input("Enter a character:").lower()
if(ch=="w"):
    print("White color")
elif(ch=="r"):
    print("Red color")
elif(ch=="g"):
    print("Green color")
elif(ch=="y"):
    print("Yellow color")
elif(ch=="o"):
    print("Orange color")
elif(ch=="b"):
    print("Black color")
elif(ch=="p"):
    print("Pink color")
else:
    print("Invalid Input")
"""
# Arithmetic Calculator using match-case (Switch)
"""
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
op = input("Enter operator (+, -, *, /): ")
match op:
    case "+":
        print("Result =", num1 + num2)
    case "-":
        print("Result =", num1 - num2)
    case "*":
        print("Result =", num1 * num2)
    case "/":
        if num2 != 0:
            print("Result =", num1 / num2)
        else:
            print("Division by zero is not possible.")
    case _:
        print("Invalid Operator")
    """
#Write a menu driven program for calculating areas of different geometrical figures such 
#as circle, square, rectangle, and triangle.
"""
while True:
    print("=====MENU=====")
    print("1. Circle")
    print("2. square")
    print("3. rectangle")
    print("4. Triangle")
    print("5. Exit")
    choice=int(input("Enter a number to perform function:"))
    if(choice==1):
        pie=3.14
        r=float(input("Enter radius of circle:"))
        print("Area of circle:",pie*r*r)
    elif(choice==2):
        s=int(input("Enter side of square:"))
        print("Area of square:",s*s)
    elif(choice==3):
        l=int(input("Enter length of rectangle:"))
        b=int(input("Enter breadth of rectangle:"))
        print("Area of rectangle :",l*b)
    elif(choice==4):
        b=int(input("Enter base of triangle:"))
        h=int(input("Enter height of triangle"))
        print("Area of triangle:",0.5*b*h)
    elif(choice==5):
        break
    else:
        print("Invalid number")
"""
# Write a program to display all even numbers from 1 to 20.
"""
for i in range(21):
    if(i%2==0):
        print(i)
"""
# Write a program to display all odd numbers from 1 to 20.
"""
for i in range(21):
    if(i%2!=0):
        print(i)
"""
# Write a program to print all the Numbers Divisible by 7 from 1 to 100.
"""
for i in range(101):
    if(i%7==0):
        print(i)
"""
# Write a program to print table of any number.
"""
n=int(input("Enter a number:"))
for i in range(1,11):
    print(n*i)
"""
#Write a program to print table of 5 in following format. 
"""
5 X 1 = 5 
5 X 2 = 10 
5 X 3 = 15
"""
"""
n=int(input("Enter a no:"))
for i in range(1,11):
    print(f"{n} X {i} = {n*i}")
"""
#Write a program to find the sum of first 50 natural numbers using for loop.
"""
sum=0
for i in range(1,51):
    sum+=i
print("Sum of first 50 natural numbers:",sum)
"""
#Write a program to count the sum of digits in the entered no.
"""
num=int(input("Enter a number:"))
sum=0
while num>0:
    digit=num%10
    sum=sum+digit
    num=num//10
print("Sum of digits in the number:",sum)
"""
#Write a program to find the reverse of a given no.
"""
num=int(input("Enter a number:"))
reverse=0
while num>0:
    digit=num%10
    reverse=reverse*10+digit
    num=num//10
print("Reverse of a number is:",reverse)
"""
#Write a program to check wheather a given no is perfect no or not.
"""
num=int(input("Enter a number to check:"))
sum=0
for i in range(1,num):
    if num%i==0:
        sum=sum+i
if num==sum:
    print(num,"is perfect number")
else:
    print(num,"is not a  perfect no")
"""
#Write a program to print armstrong number from 1 to 1000.
"""
print("Armstrong number from 1 to 1000 are:")
for num in range(1,1001):
    temp=num
    sum=0
    while temp>0:
        digit=temp%10
        sum=sum+digit**3
        temp=temp//10
    if sum==num:
        print(num,"is armstrong number")
    else:
        print(num,"is not a armstrong number")
"""
#Write a program to print the value of X^N.
""""
X=int(input("Enter a value of X:"))
N=int(input("Enter a value of N:"))
result=X**N
print("Value of X^N:",result)
"""
#Write a program to calculate the value of nCr.
"""
n=int(input("Enter a value of n:"))
r=int(input("Enter a value of r:"))
fact_n=1
fact_r=1
fact_nr=1
for i in range(1,n+1):
    fact_n=fact_n*i
for i in range(1,r+1):
    fact_r=fact_r*i
for i in range(1,(n-r)+1):
    fact_nr=fact_nr*i
nCr=fact_n//(fact_r*fact_nr)
print("Value of nCr:",nCr)
"""
#Write a program to print first 10 natural numbers.
"""
for i in range(1,11):
    print(i,end=" ")
"""
#Write a program to check wheather a number is palindrome number or not.
"""
num=int(input("Enter a number to check wheather a number is palindrome or not:"))
temp=num
reverse=0
while temp>0:
    digits=temp%10
    reverse=reverse*10+digits
    temp = temp//10
if num==reverse:
    print(num,"is a palindrome number")
else:
    print(num,"is not a palindrome number")
"""
#Write a program to print all prime numbers from 50 to 500.
"""
print("Prime numbers from 50 to 500")
for num in range(50,501):
    is_prime=True
    for i in range(2,num):
        if num%i==0:
            is_prime=False
            break
    if is_prime:
        print(num,end=" ")
"""
#Write a program to find the sum of all prime numbers from 1-1000.
"""
sum=0
for num in range(1,1001):
    is_prime=True
    for i in range(2,num):
        if num%i==0:
            is_prime=False
            break
    if is_prime:
        sum=sum+num
print("Sum of all prime numbers from 1 to 1000:",sum)
"""
#Write a program to print the following sequence 0,5,10,15,20.
for i in range(0,21,5):
    print(i,end=" ")
        
            


    









    



               

    



    
    


    

      

















            

        


    
    


















    
