#LOOPS-> for , while
#dry principle
# for i in range(1,11):
#     print("hello")
#starting=0
# for i in range(5):
#     print(i)

# 10-20 elements sum
# sum=0
# for i in range(10,21):
#     sum=sum+i
#     print(sum)
#MODULE OPERATOR->allow remainder print krana(== for check value)(=assignment operator->for give value )
# if 8%2==0:
#     print("num is even")
# sum=0
# for i in range(0,31):
#     if i%2==0:
#         sum=sum+i
# print(sum)

#no.of steps

# sum=0
# for i in range(0,31,2):
#     if i%2==0:
#         sum=sum+i
# print(sum)

#OPERATOR
#->comparison(==,>=,<=)
#->logical operator(AND,OR,NOT)

# if (5>=4 and 2%2==0):
#     print("both condition are true")
# if (5>=4 or 3%2==0):
#     print("both condition are true")
# 1-100 5,2,3
# for i in range(101):
#     if i%5==0 and i%2==0 and i%3==0:
#         print(i)

#not logical operator->boolean reverse(true/false)
#truthy value->all numbers string,boolean (true)except zero
#falsy value-> 0,false,"",None

# print(not 10)
# print(not 0)
# val=not((10 and 5) or (5 or 10))
# print(val)

#SHORT CIRCUITING-> value return jispe ans depend krta hai
# val=((10 and 5) or (5 or 10))
# print(val)
# print(10 and 0 and 1)
# print(0 or not(5) or False)
# print((((0 or (not(4)))) or ("hello" and "kashish")) and (5.6 and False))

# #for loop
# for i in range(0,10,3):
#     print(i)

#outer loop-> no. of rows
#inner loop-> no. of column

#1 1 1
#2 2 2
#3 3 3

# for i in range(1,4):
#     for j in range(1,4):
#         print(i,end=" ")            #block printing
#     print()                        #->for row change print()    

# 1 2 3 
# 4 5 6
# 7 8 9

# num=1
# for i in range(1,4) :
#     for j in range(1,4):
#         print(num,end="")    
#         num+=1
#     print()

#1 3 5
#7 9 11
#13 15 17
# n=3
# v1=2
# count=1
# for i in range(n):
#     for j in range(n):
#         print((n*count)-v1,end="")
#         count+=1
#         v1+=1
#     print()
        
#1
#1 1
#1 1 1
#1 1 1 1

# for i in range(1,5):
#     for j in range(i+1):
#         print(1,end="")
#     print()

#1
#2 3
#4 5 6
#7 8 9 10
# n=1
# for i in range(1,5):
#     for j in range(i):
#         print(n,end="")
#         n+=1
#     print()

#WHILE LOOP
# num=int(input("enter a num"))
# print(num)

# while(num>=0):
#     print(num)
#     num-=1
# while(num<100):
#     print(num)
#     num+=1
# num=2
# sum=0

# while(num<=100):
#     sum+=num
#     num+=2
# print(sum)

#functions-> reusuability
# built-in function
# custom fuction

# def fn():
#     print("hello world")
# fn()
# def sum(a,b):
#      print(a+b)
# sum(10,20)

# def product(a,b):
#     print(a*b)       
# product(2,3)

# def power(a,b):
#     print(a**b)   # 3^4
# power(3,4)

# age=int(input("enter your age"))
# print(age)

# if (age>=18):
#     print("applicable for vote")
      
# else:
#     print("not applicable")

#perfect number-> 6(1,2,3,6) exclude itself sum of its factor(self)






