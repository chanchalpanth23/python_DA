# x="phython"
# print(type(x))

# list=[x*x for x  in range(1,5)]
# print(list)

# list=[7,3,9,3,2]
# print(list)

# list.append(1)
# print(list)

# list.insert(2,4)
# print(list)

# list.remove(3)
# print(list)

# print(len(list))

# max=list[0]
# for i in range(1,len(list)):
#     if(list[i]>max):
#         max=list[i]
#         print(max)

# min=list[0]
# for i in range(1,len(list)):
#     if(list[i]<min):
#         max=list[i]
#         print(min)

# print(list.count(3))

# list=[12,5,3,8]
# sum=0
# for i in list:
#     sum+=i
# print(sum)

# list=[x for x in range(1,21) if x%2==0]
# print(list)
# a=[2,5,3]
# b=[1,3,2]
# print(list(set(a) & set(b)))

# list=[x for x in list if x >=0]
# print(list)
# list=[2,4,6,4,9,2]
# print(list.index(4))

# def fn(a):
#     print("phython")
#     return chanchal
# b=fn(3)
# print(b)

# # list=[2,4,51,8]
# # print(list[-6])

# def fn():
#     a= "chanchal"
#     return 22
# b=12
# print(b)

# import os
# path="."
# files=os.listdir(path)
# def createfile():
#     print("creating a file")
#     print("please choose a name not in -:",files)
#     name=input("enter a name of your file")
#     for i in files:
#         if name==i:
#             print("operation not allowed, same file name used")
#             return
#         file=open(name,"w")

# word="charu"
# for i in range(len(word) -1,-1,-1):
#     print(word[i],end=" ")

# faboniacci sequence
# a=0
# b=1

# for i in range(10):
#     next_term=a+b
#     print(next_term,end=" ")
#     a,b=b,next_term

#count of occurence of each character

# word="electonics"
# count={}
# for char in word:
#     if char in count:
#         count[char]+=1
#     else:
#         count[char]=1
#     print(count)

# characters="chanchal"
# vowels="aeiou"
# count=0
# for i in characters:
#     if i in vowels:
#         count+=1
#         print(count)

# sentence=input("enter a sentence=")
# word=sentence.split()
# for word in word:
#     print(word,"->",len(word))

# multiple=3
# count=1
# while count<=5:
#      print(multiple,end=" ")
#      multiple+=3
#      count+=1

# base=3
# power=4
# result=base**power
# print(result)

# num=int(input("enter a number to check="))
# i=1
# is_perfect_square =False
# while i*i<=num:
#     if i*i==num:
#         is_perfect_square= True
#         break
#     i+=1

#     if is_perfect_square:
#         print("num is perfect square")
#     else:
#         print("not a perfect square")

# character=input("enter a string=")
# count=0
# for i in range(0,len(character)):
#     count+=1
#     print(count)

# nestedlist=[
#     [1,4,5],
#     [4,8,9],
#     [0,2,3]
# ]
# print(nestedlist[1][2])

# tuple=(6,3,4,5)
# a,b,c,d=tuple
# print(a,b,c,d)
# print(type(tuple))

# tuple=(2,5,1,4)
# # tuple[4][1]=4
# # print(tuple)
# print(max(tuple))

# tuple=(
#     (3,6,4),
#     (6,2,9),
#     (4,6,7)
# )
# print(tuple[2][0])

# tuple=(11,5,9)
# print(sum(tuple))
# class camera:
#     def __init__(self,photosclick):
#         self.photosclick=photosclick
# c1=camera("photosclick")
# # c1.camera()
# print(camera.mro())
# class phone(camera):
#     def __init__(self,photosclick,calling):
#         super().__init__(photosclick)
#         self.calling=calling
# print(phone.mro())
# class smartphone(phone):
#     def __init__(self,photosclick,calling,apps):
#         super().__init__(photosclick,calling)
#         self.apps=apps
# print(smartphone.mro())

# class Atm():
#     def __init__(self):
#         self.pin= "" 
#         self.balance=0

# def menu(self):
#     user_Input=input("""
# Hi how can I help you?
# 1. press 1 to create pin
# 2. press 2 to change pin
# 3. press 3 to check balance
# 4. press 4 to withdraw
# 5. Anything else to exist
# """)
#     if user_Input==1:
#         #create pin
#         self.create_pin()
#     elif user_Input==2:
#         #change pin
#         pass
#     elif user_Input==3:
#         #check balance
#         pass
#     elif user_Input==4:
#         #withdraw
#         pass
#     else:
#         exit()
# def create_pin(self):
#     user_pin=input("enter your pin")
#     self.pin=user_pin
#     user_balance=int(input("enter your balance"))
#     print("pin created successfully")
#     self.menu()



# obj=Atm()

# import os
# path="."
# files=os.listdir(path)
# def createfile():
#     print("creating a file....")
#     print("please choose a name not in-:,files")
#     name=input("enter a name of your file")
#     for i in files:
#         if name==i:
#             print("operation not allowed,same file name used")
#             return
#         file=open(name,"w")
#         file.close()
#         text=input("what o you want to write in the file")
#         file.write(text)
#         file.close(name,"r")
#         data=file.read()
#         print("file is created with data-:data")
# def writefile():
#     pass
# def readfile():
#     pass
# def fileoperations():
#     print(files)
#     print("1 for creating a file")
#     print("2 for writing data in any existing file")
#     print("3for reading existing file")
#     user_input=int(input("enter your input"))
#     if user_input==1:
#         createfile()
#     elif(user_input==2):
#         writefile()
#     else:
#         readfile()

# fileoperations()



   

        


    
# obj=Atm()

# print(not 10)
num=1
for i in range(1,4):
    for j in range(1,4):
        print(i,end="")
        num=+1
    print()
        









   








    
    
