# Assignment - 1
# num1 = int(input("Enter the number1"))
# num2 = int(input("Enter the number2"))
# sum=num1+num2
# print(sum)



# 2. Write a program that takes the length and width of a rectangle as input from the user and calculates its area.
# print("Give length & width of rectangle to find area")
# length = int(input("Enter the length: "))
# width = int(input("Enter the width :"))
# Area = length*width
# print(Area)
# print(f"area of rectangle: {Area}")

# 3.Write a program to convert temperature from Celsius to Fahrenheit. The formula is `F = (C * 9/5) + 32`.
# t=22
# c=19
# F = (c*9/5)+32
# print(F)


# 4.Write a program that takes the principal amount, rate of interest, and time in years as input and calculates the simple interest
# print("Enter data to calculate Principle simple intres ")
# # p*T*R/3
# Amount = int(input("Enter the Amount: "))
# Rate = int(input("Enter the Rate: "))
# Time = int(input("Enter the time: "))
# principle =(Amount*Rate*Time)/3
# print(f"the principle INTREST is{principle}")
# print(int(principle))


# 5.Write a program to take three numbers as input from the user and calculate their average.
# n1 = int(input("Enter the num1: "))
# n2 = int(input("Enter the num2: "))
# n3 = int(input("Enter the num3: "))
# Average = (n1+n2+n3)/3
# print(Average)

# 6.Write a program that takes the radius of a circle as input from the user and calculates its perimeter (circumference). The formula is `Perimeter = 2 * π * radius` (use 3.14159 for π)
# radius = int(input("Enter the radius of circle : "))
# perimeter = 2*3.142*radius
# print(perimeter)



# 7. Write a program that takes an integer input from the user and checks whether it is even or odd.
# intiger =int(input("Enter the number"))
# if intiger%2==0:
#     print("even",intiger)
# else:
#     print(" odd ",intiger)

# 8.Write a program that takes two numbers as input and swaps their values.
# A = int(input("Enter the value A :"))
# B =int(input("Enter the value B :"))
# temp = A
# A = B
# B = temp
# print(f"swapping {A,B}")



# 9.Write a program to take two numbers from the user and print their product.
# A = int(input("Enter the value A :"))
# B = int(input("Enter the value B :"))
# print(A*B)


# 10.Write a program that takes a time in minutes from the user and converts it to seconds.
# minetus = int(input("Enter the time in minutes"))
# input=minetus*60
# print(input) 

# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$  -----    END ------   $$$$$$$$$$$$$$$$$




# Assignment 2  

# 1.Write a Python program that checks whether a given number is positive, negative, or zero.
# n = int(input("Enter the number : "))
# if n>0:
#     print("number is positive")
# elif n<0: 
#     print("number is negative")
# else:  print("number is zero")
    
    
# 2.Write a Python program that takes an integer input from the user and checks whether the number is even or odd
# number = int(input("Enter the numer :"))
# if number %2==0:
#     print("even")
# else:
#     print("odd")

# 3 Write a Python program to determine if a given year is a leap year. A leap year is divisible by 4 but not by 100, except if it is also divisible by 400
# year = int(input("Enter year to check leap year"))
# if year%4==0 and year%100 !=0 or year%400==0:
#     print("Leap  year")
# else:
#     print("not a leap year")


# 4. Write a Python program that takes a student's score as input and prints the corresponding grade based on the following criteria:
#    - A: 90-100
#    - B: 80-89
#    - C: 70-79
#    - D: 60-69
#    - F: below 60

# Marks = int(input("Enter the marks to print the grades"))
# if Marks>=90 and Marks>=100:
#     print("A grade")
# elif Marks>=80 and Marks<=89:
#     print("B grade")
# elif Marks>=70 and Marks<=79:
#     print("c grade")
# elif Marks>=60 and Marks<=69:
#     print("c grade")
# elif Marks<=60 and Marks>=40:
#     print("F grade")
# else:
#     print("fail")


#  5.Write a Python program that takes three numbers as input and prints the largest of the three.
# A = int(input("Enter the value A :"))
# B =int(input("Enter the value B :"))
# C =int(input("Enter the value c :"))
# if A>=B and A>=C:
#     print (f"Greater value of A: {A}")
# elif B>=A and B>C:
#     print(f" greater value of B :{B}")
# else:
#     print(f"c is the greater no :{C}")


# 6.Write a Python program that takes a single character from the user and checks whether it is a vowel (a, e, i, o, u) or a consonant.

# vowels =input("enter a character to check vowels: ").lower()
# if vowels in ['a','e','i','o','u']:
#     print(f"it is an vowel{vowels}")
# else:
#     print(f"charter is not an Vowels{vowels}")




#  7.Write a Python program that takes the user's age as input and determines which age group they belong to:
#    - Child: 0-12 years
#    - Teenager: 13-19 years
#    - Adult: 20-64 years
#    - Senior: 65 years and above

# age =int(input("Enter ur age :"))
# if age>=0 and age<=12:
#     print("ur child ")
# elif age>=13 and age<=19:
#     print("ur Teenager ")

# elif age>=20 and age<=64:
#     print("ur Adult ")
        
# elif age>=65 and age<=125:
#     print("ur senior citizen ")
# else:
#     print("invalid age")

# 8.Write a Python program that checks if a given number is divisible by both 5 and 11.

# num = int(input("Enter the number for divisible : "))
# if num%5==0 and num%11==0:
#     print(f"The {num} divisible both 5 & 11")
# else:
#     print("the no is not divisible")


# 9. Write a Python program that takes an integer (1-7) as input and prints the corresponding day of the week (1 for Monday, 2 for Tuesday, ..., 7 for Sunday)

# Days = int(input("Enter the no. of days: "))
# if Days==1 :
#     print("Monday")
# elif Days==2 :
#     print("Tuesday")
# elif Days==3 :
#     print("wednesday")
# elif Days==4 :
#     print("Thursday")
# elif Days==5 :
#     print("Friday")
# elif Days==6 :
#     print("saturday")
# elif Days==7 :
#     print("sunday")
# else:
#     print("invalid data")

# 10.Write a Python program that takes a username and password as input and checks if they match predefined credentials. If they match, print "Access Granted"; otherwise, print "Access Denied"
# username = input("Enter uname : ")
# password = int(input("Enter password: "))
# if username == 'abu'and password==123:
#     print("Acess granted")
# else:
#     print("Acess Denied")


# $$$$$$$$$$$$$$$$$$$$$$$$$4---------------  Assignment 3   --------------- $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$

# 1.Write a Python program to print all numbers from 1 to 10 using a `for` loop.
# for i in range (1,11):
#     print(i) 

# 2.Write a Python program to print all even numbers between 10 and 30 using the `range` function and also using the while loop. 
# for i in range(10,30):
#     if i%2==0:
#         print(i)
        
# 3.Write a Python program to calculate the sum of all numbers from 1 to 100 using a `for` loop. 
# print(sum([i for i in range (1,101)]))

# 4.Write a Python program to find the first 5 numbers divisible by 3 using a `for` loop and the `break` statement.

        
# -Assignment 1---------

# 1)Write a program that takes two numbers as input from the user and prints their sum.

# num1 = int(input("Enter the num1 :"))
# num2 = int(input("Enter the num2 : "))
# sum = num1+num2
# print("Sum of n1 & n2 is :",sum)


# 2)Write a program that takes the length and width of a rectangle as input from the user and calculates its area.
# print("Give length and width of rectangle to find Aera")
# length = int(input("Enter the length "))
# width = int(input("Enter the width "))
# Area = length*width
# print("Area of rectangle:",Area)



# 3.Write a program to convert temperature from Celsius to Fahrenheit. The formula is `F = (C * 9/5) + 32`. 
# t = 22
# c = 19
# F = (c * 9/5) + 32
# print(F)

# 4.Write a program that takes the principal amount, rate of interest, and time in years as input and calculates the simple interest
# print("Enter data to calculate simple intrest")
# Amount = int(input("Enter the Amount "))
# Intrest = int(input("Enter the Intrest "))
# Time = int(input("Enter the Time : "))
# principle = (Amount*Intrest*Time)/3
# print("simple intrest is ",principle)


# 5.Write a program to take three numbers as input from the user and calculate their average. 
# print("Enter 3 nos to calculate its Average")
# n1 = int(input("Enter the number1"))
# n2 = int(input("Enter the number2"))
# n3 = int(input("Enter the number3"))
# Average = (n1+n2+n3)/3
# print(Average)

# 6.Write a program that takes the radius of a circle as input from the user and calculates its perimeter 
# (circumference). The formula is `Perimeter = 2 * π * radius` (use 3.14159 for π)

# radius = int(input("Enter radius of circle"))
# Perimeter = 2 * 3.142 * radius
# print(Perimeter)

# 7. Write a program that takes an integer input from the user and checks whether it is even or odd. 
# n1 = int(input("Enter the no to check odd or even : "))
# if n1%2==0:
#     print("Even",n1)
# else:
#     print("Odd",n1)

# 8.Write a program that takes two numbers as input and swaps their values. 
# n1 = int(input("Enter the no.1 :"))
# n2 = int(input("Enter the no.2 :"))
# temp = n1
# n1 = n2
# n2 = temp
# print("Swapping",n1 ,n2)

# 9.Write a program to take two numbers from the user and print their product. 
# n1 = int(input("Enter the number1: "))
# n2 = int(input("Enter the number2 :"))
# print("Prodoct of n1 & n2 ",n1*n2)

# 10.Write a program that takes a time in minutes from the user and converts it to seconds. 
# min = int(input("Enter the time in minitues "))
# input = min*60
# print(input)



#----------------***********   Assignment 2  ***********----------------
# 1.Write a Python program that checks whether a given number is positive, negative, or zero.

# num = int(input("Enter the number : "))
# if num %2==0:
#     print("number is even")
# else:
#    print("odd")



# 2.Write a Python program that takes an integer input from the user and checks whether the number is even or odd.

# num = int(input("Enter the number : "))
# if num %2==0:
#     print("number is even")
# else:
#    print("odd")


# 3.Write a Python program to determine if a given year is a leap year. A leap year is divisible by 4 but not 
# by 100, except if it is also divisible by 400

# yr = int(input("Enter the to check leap year : "))
# if yr%4==0 and yr%100 !=0 or yr%400==0:
#     print(yr,"is leap year")
# else: 
#     print("not a leap year")



#  4.Write a Python program that takes a student's score as input and prints the corresponding grade 
# based on the following criteria

# per = int(input("Enter the marks: "))
# if per<35:
#     print("fail")
# elif per>=35 and per <=50:
#     print("C grade")
# elif per>50 and per<=70:
#     print("B Grade")
# elif per>70 and per<=90:
#     print("A Grade")
# elif per>90 and per<=100:
#     print("A+ grade")
# else:
#     print("invalid marks")



#5.Write a Python program that takes three numbers as input and prints the largest of the three.

# A = int(input("Enter the 1st no."))
# B = int(input("Enter the 2nd no."))
# C = int(input("Enter the 3rd no."))
# if A>B and A>C :
#     print(A, "bigger than",B,C)
# elif B>A and B>C :
#     print(B, "bigger than ",A,C)
# else:
#     print(C,"is bigger than",A,B)



#  6.Write a Python program that takes a single character from the user and checks whether it is a vowel 
# (a, e, i, o, u) or a consonant.

# Alpha = str(input("Enter the a single Alphabet to check vowel: "))
# if Alpha.lower() in 'aeiou' or Alpha.upper() in 'aeiou':
#     print(Alpha,"is a vowel")
# else:
#     print(Alpha,"is not an voewl")
    
    

#  7.Write a Python program that takes the user's age as input and determines which age group they 
# belong to:
#    - Child: 0-12 years
#    - Teenager: 13-19 years
#    - Adult: 20-64 years

# Age = int(input("Enter ur aage : "))
# if Age <= 12:
#     print("Child")
# elif Age>= 13 and Age<=19:
#     print(Age,"Tenage")
# elif Age>=20 and Age<=64:
#     print(Age,"Adult")
# else:
#     print(Age,"Senior citizen")
    
    
    
    
    
    
# 8.Write a Python program that checks if a given number is divisible by both 5 and 11.
# num = int(input("Enter the number for divisible by 5 and 11 :"))
# if num % 5 == 0 and num % 11 == 0:
#     print(num,"yes divisible")
# else: 
#     print("not Divisible")


# Write a Python program that takes an integer (1-7) as input and prints the corresponding day of the 
# week (1 for Monday, 2 for Tuesday, ..., 7 for Sunday)

# D = int(input("Enter the no to ckeck specific day in week : "))
# if D==1:
#     print(D,"Monday")
# elif D==2:
#     print(D,"Tuesday")
# elif D==3:
#     print(D,"wednesday")
# elif D==4:
#     print(D,"Tursday")
# elif D==5:
#     print(D,"Friday")
# elif D==6:
#         print(D,"saturday")

# elif D==7:
#     print(D,"Sunday")
# else:
#     print("invalid data")
    

#  10.Write a Python program that takes a username and password as input and checks if they match pre
# defined credentials. If they match, print "Access Granted"; otherwise, print "Access Denied"

# uname = str(input("Enter user name : "))
# pwd = str(input("Enter the password : "))
# if uname =="admin" and pwd =="1234":
#     print("Acess Granted")
# else:
#     print("Access Denied")



# *************    ----------   Assignment 3  --------  ****************

# 1.Write a Python program to print all numbers from 1 to 10 using a `for` loop. 

# for i in range(1,10):
#     print(i+1)



# 2.Write a Python program to print all even numbers between 10 and 30 using the `range` 
# function and also using the while loop. 

# for i in range(10,30):
#     if i%2==0:
#      print(i) 


# 3.Write a Python program to calculate the sum of all numbers from 1 to 100 using a `for` loop. 
# print(sum([i for i in range (1,101)]))



# 4.Write a Python program to find the first 5 numbers divisible by 3 using a `for` loop and the `break` statement. 
# count = 0
# for i in range(1,5):
#     if i %3==0:
#         print(i,"divisible by 3")
#         count += 1
#     if count == 5:
#         break



# 5.Write a Python program to iterate over a string "Python" using a `for` loop and print each character. 
            
# for i in ('python'):
#     print(i)


# 6. Write a Python program using nested `for` loops to print a pattern of stars: 
# * 
# ** 
# *** 
# **** 
# ***** 
# **** 
# *** 
# ** 
# * 



# 7.Write a Python program to print numbers from 10 to 1 in descending order using the `range` 
# function and a `for` loop.

# for i in range(11,1,-1):
#     print(i-1)



# 8.Write a Python program to calculate the sum of squares of all numbers from 1 to 10 using the 
# `range` function and a `for` loop and.

# print(sum(i**2 for i in range(1,11)))



# 9.Write a Python program to check if a number (input by the user) is prime using a `for` loop and the `break` statement. 
# num = int(input("Enter the no to check : "))
# count = 0
# if num>1:
#     for i in range(1,num+1):
#         if(num%i)==0:
#             count=count+1
#     if count ==2:
#         print("number is prime")
#     else: 
#         print("not")
# else:
#     print("Snoop")

# 10.Write a Python program to print all numbers from 1 to 20 except multiples of 5 using a `for` 
# loop and the `continue` statement.


# -------- Assignment 10 --------------

#  1.Write a Python program that takes a sentence as input and splits it into individual words using the split 
# method. Print each word on a new line. 

# smt = input("Enter ur stmt: ")
# words= smt.split()
# print("words in sentence are .")
# for word in words:
#     print(word)


# 2.Write a Python program that takes a comma-separated string of numbers as input, splits it into 
# individual numbers, and converts them to a list of integers

# smt = input("Enter ur stmt: ")
# words= smt.split(',')
# print(words)
# for item in words:
#  words.strip(item)
#  print(item)

# 3)Write a Python program that takes an email address as input and extracts the domain name 
# using the `split` method






# from p1 import chaicode
# chaicode("ginger tea")


# for c  in "chai":
#     print(c)

# --------------  Advance topics python ------------
# Decorators,Generators,Iterators,Meta programing

# # time :2:13

# ltr  = input("Enter the letter to check: ")
# if (ltr in 'aeiou') or ('ltr in aeiou'):
#     print(" containing its ovwel")
# else:
#     print("not ovwel")



# num = int (input("Enter the num up to 5 digit"))
# if num >=0 and num<=9:
#     print("its single digit number:",num)
# elif num>=10 and num<=99:
#     print("its double digit number")
# else:
#     print("its higher than 2 digit number")



# ----------********* Loops *********---------
# 1) For loop
# 2)While loop
# 3)while True
# 4)Nested Loop


# ------------------  for loop ----------------------
# n=int(input("Enter the number to calculate: "))
# for i in range(1,11):
#     print(n,"*",i,"=",i*n)



# While  loop:while{conduction }:
# body of loop
# Condition

# n = 0
# while n<=50:
#     print(n)
#     n+=10

# n = int(input("Enter the no to print: "))
# a = 0
# while n<=10:
#     print(a,"x",n,"=",n*a)
#     n+=1
#     a+=1



#----------- While True ------------------ // infinite loop
# to break Ehile true break statement is used . 

# n=0
# while True :
#    n>=100
#    n+=1
#    print(n)
#    break 
#    print(n)

# while True:
#     num1=int(input("Enter the number :"))
#     num2=int(input("Enter the  another number :"))
     
#     print(num1+num2)
#     repeat=input("do u want to stop program:")
#     if repeat == 'yes':
#      break


# -------- Nested Loop ------------------ 
#  a loop inside a loop is called Nested loop

# for i in range(1,4+1):
#     for j in range(1,11):
#         print(j,end=" ")
#     print(i)

# pattern programing [Right Angle Triangle]

# for i in range(1,6):
#     for j in range(i+1):
#         print(j,end=" ")
#     print()


# ----------- for loop with Conditionl statement ----------------

# for i in range(1,11):
#     if i == 3:
#         print("Add this song to the fav")
#     else:
#         print(i)



# for i in range (1,101):
#     if i % 8 == 0 and i % 12 == 0:
#         print(i)

# n = 1
# while n<=10:
#     if n == 3:
#         print("add thsis to fav")
#     else:
#         print(n)
#     n += 1


#--- ***************** Break and Contine statement ************-----
# Contine Statmt: -> is used when u want to skip a perticular condition

# ex: -> 
# for i in range(1,11):
#     if i==5:
#         continue
#     else:
#         print(i)


# Break Stmt:->  is used when u want to destroy a loop at
# certain condition and come out of the loop

# ex->
# for i in range(1,11):
#     if i==7:
#        break
#     else:
#         print(i)
# print("Thank u")

# --------- practise Problems -------------
# sum of even
# sum = 0
# for i in range(1,51):
#     if  i%2==0:
#      sum +=i
# print("the sum of all even numbers is ",sum)




#numbers and their squared numbers
# for i in range(1,21):
#         print(i,i**2)


# sum of odd numbers useing while loop
# n = 0
# sum = 0
# while n<=20:
#  if(n%2!=0):
#      sum +=n
#  n+=1
# print(sum)
  
    
    

# timr: 3:
# multiple of 8 and 12
# for i in range(1,101):
#     if(i%8==0 and i%12==0):
#      print(i)
    
# write a prm billing stmt at supermarket

# name : (input)
# ttl =(0)
# while True:
#     print("enter the input")
#     qnt = int(input("enter the quantty ")) 
#     amt=int(input("Enter the amount"))
#     ttl +=amt*qnt
#     repeat = (input("do u want to repeat  "))
#     break 
# print("-"*40)
# print("Namme: ",name)
# print("Amount to b paid:", ttl)
# print("-"*40)
# print("Happy shopping")

# repeat1 = input("do want to repeat the coustomer")
# # def adding():
# #     num1=(int(input("Enter the no"))) 
#     print("Adding")





# -------Multithreading ---------------------
# def mul1():
#     for i in range(5):
#      print("hey guys!")
    
# def mul2():
#     for j in range(10):
#      print("bye")


# mul1()
# mul2()



# from threading import Thread
# def mul1():
#     for i in range(10):
#      print("hey guys")
    
# def mul2():
#     for j in range(10):
#      print(" bye")
    
# t1=Thread(target=mul1 )
# t1.start()
# t1.join()
# t1=Thread(target=mul)

# t2=Thread(target=mul2)
# t2.start()    
# t2.join()




# time3:48
# fabinaco series:- 

# a = 0
# b = 1
# n = int(input("Enter the number: " ))
# if n == 1:
#   print(1)
  
# else:
#  print(a)
#  print(b)
#  for i in range(2,n):
#     c= a+b
#     a = b
#     b = c
#     print(c)
    
    
# #---------------   prime no. or not----------
# # num = int(input("Enter the number: "))
# if num<= 1:
#     print("it is not a prime number: ")
# else:
#     for i in range(2,num):
#         if num%i==0:
#             print("number is not prime number")
#             break
#         else:
#             print("It is a prime numbr")
#             break


# ---------- Palindrome --------------------

# name = str(input("Enter the string to check palindrome or not: "))
# if name[::-1]==name:
#     print(name,"is palindrome")
# else:
#     print(name,"it is not palindrome")


# ------------- or ------------------

# name = int(input("Enter to check palindrome or not: "))
# temp = name
# rev = 0
# while name >0:
#     dig = name % 10
#     rev = rev*10+dig
#     name = name 
# if rev == temp:
#     print("it is an palindreome")
# else:
#     print("it is not palindrome")




# ----------- ************  String Manuplation **********----------------

# som Strings Methods
# 1 len() ,3)count(), 4 lower() , 5 index[], 10 center,
# 2 upper() 6 captilize, 7 casefold , 8 find , 9 format 
# etc


# a = "hello Guys!"
# b = "how r u  all {}.my age is {}"
# age = 24
# # print(len(a))
# # print(a.upper)
# # print(a.count)
# # print(a.index('o',1,11))
# # print(len(a))
# # print(a.casefold())
# # print(a.find("l",5,11))
# # print(b.format(a,age))

# print(a.center(20,"*"))
# print(a.split())



# ------------ String Functions ----------------------

# endswith()-> returns true if the string ends with the specified value
# startswith()-> returns true if the string starts with the specified value

#replace()-> replaces a string with another string
# a = "hello. my name is john"
# print(a.replace('john','abu'))

# strip()-> returns a trimmed version of the string

#split()-> splits is used to separate the string into a substring
# a = "hello. my name is john. iam 23 yrs old "
# print(a.split('.'))


#join()-> joins the elements of an iterable to the end of the string
# swapcase()-> swaps the case of the string lower to upper and upper to lower

# ljust()-> returns a left justified version of the string // its used to add at left side of string
# # a = "hello. my name is john"
# x=a.ljust(10)
# print(x,'and my favroite movie is avengers')

# rjust()-> returns a right justified version of the string

# rindex -> returns the highest index of the substring inside the string //
# the last position where it was found
# a = "hello. my name is john and iam 24 yrs old" 
# print(a.rindex('john'))

# rfind -> returns the range of highest index of the substring inside the string
# the last position where it was found 
# a = "hello. my name is john"
# print(a.find('i',1,20))





# isalnum()-> returns true if all the characters are alphanumeric
# isalpha()-> returns true if all the characters are in the alphabet
# isdigit()-> returns true if all the characters are digits
# islower()-> returns true if all the characters are in lower case
# isupper()-> returns true if all the characters are in upper case
# isspace()-> returns true if all the characters are whitespaces
# istitle()-> returns true if the string follows the rules of a title
# 




# ------------ Slicing of string ----------------
# a = "harry potter and the goblet of fire"
# b = "123456789"
# print(a)
# # print(b[::-1])
# # print(a[0:10])
# # print(a[-4:])
# # print(a[0:5])
# print(b[6::-1])



#--------- practise programs ------------
A = "Why fit in. when u are Born to Stand Out!" 
# print(len(A))
# print(A.count('o'))
# print(A.lower())
# print(A.upper())
# print(A.title())
print(A.find('fit in'))



















































