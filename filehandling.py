#file handling->automation(31 march,1 april)
#a,r,w
# a->add
#w->add,overwrite(previous data remove new data reflect only)
# file=open("data.txt","r")
# data=file.read()
# print(data)

# file=open("data.txt","w")    
# file.write("hello dice")    #overwrite
# file.close()           
# file2=open("data.txt","r")
# data=file2.read()
# print(data)

# file=open("data.txt","a")   
# file.write("\n hello analytics")
# file.close()           
# file2=open("data.txt","r")
# data=file2.read()
# print(data)

# for line in data:
#     # print(line)
#     # print("next line")
#     print(line)
#     print("next line-----")

# with open("data.txt","r") as file:
#     for i in file:
#         print(i)
#         print("next--")

#1->file create
#name?
#file m add
#file wo add krdenge
#read krni h
#han krni h ,krao

#"w"
import os
path="."
files=os.listdir(path)

def createFile():
    print("creating a file...")
    print("please choose a name not in-:,files")
    name=input("enter a name for your file")
    for i in files:
        if name==i:
            print("operation not allowed ,same file name used")
            return
    file=open(name,"w")
    file.close()
    text=input("what do you want to write in th file")
    file=open(name,"a")
    file.write(text)
    file.close()
    file=open(name,"r")
    data=file.read()
    print("file is successfully created with data-:")
def writeFile():
    print(files)
    file=input("enter the name of the file")
    isAvailable=False
    for i in files:
        if i==file:
            isAvailable=True
        if isAvailable:
            print("1 for appending data")
            print("2 for overwriting the data")
            userInput=int(input("enter your input"))
            text= input("enter the data")
            if userInput==1:
            
                filee=open(file,"a")
                filee.write(text)
                filee.close()
                print("\ndata is appended successfully!!")
            elif userInput==2:
                filee=open(file,"w")
                filee.write(text)
                filee.close()
                print("new data is added")
            else:
                print("invalid input")
                return
    else:
            print("file does not exist",files)
def readFile():
    print(files)
    file=input("enter a file to read")
    isAvailable=False
    for i in files:
        if i==file:
            isAvailable=True
    if isAvailable:
            filee=open(file,"r")
            print(filee.read())
            filee.close()
        
    else:
            print("file does not exist")
            return
def deletefile():
     print(files)
     userInput=input("enter the name of the file")
     os.remove(userInput)
     print("file deleted successfully")

def fileoperations():
    print(files)
    print("1 creating a file")
    print("2 for writing data in any existing file")
    print("3 for reading existing the file")
    print("4 for deleting existing file")
    userInput= int(input("enter your input"))
    if(userInput==1):
        createFile()
    elif(userInput==2):
        writeFile()
    elif userInput==3:
        
        readFile()
    else:
         deletefile()
        
fileoperations()







