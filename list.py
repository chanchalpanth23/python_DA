#LIST(17 march)
#-> mutable,duplicates allow,heterogenous(diff data types ko bhi store(int,float,string,list,tuple,dict,fn))
# list=["a","b","c",10]
# print(list)
# print(list[2])
#iteration

#length
# for i in range(len(list)):
#     print(list[i])
#direct access of value
# for j in list:
#     print(j)
#brute force->built method ko khud ko solve kro bnao

# list=[1,2,3,4,5,5,3]
# max=list[0]
# for i in range(1,len(list)):
#     if(list[i]>max):
#         max=list[i]
# print(max)

# list=[1,2,3,4,5,5,3]
# min=list[0]
# for i in range(1,len(list)):
#     if(list[i]<min):
#         min=list[i]
# print(min)
# list=[3,4,2,4,3,5,1,4]
# list[6]=7
# print(list)

# list.append(8)
# list.insert(1,9)
# list.pop()
# list.pop(4)
# list.remove(3)
# print(list.count(4))
# list.extend([1,2,3])
# print(list[1:5])
# print(list[:])
# print(list[3::2]) # ::2 hr second element ko lega(1 step remove)
# print(list[:5]) 
# print(list[:3]) 
# print(list)

# list[:]
# list[1:5]
# list[1::2]
# list[:5]
# list[:5:2]
# list[::2]

#19 march
# list=[10,6,8,9,2,0]
# listcopied=list.copy()
# print(list,listcopied)

# list.sort()
# list.reverse()
# print(list)

#COMPREHENSION FUNCTION in list->list copy but with modified values

# list=[10,6,8,9,2,0]
# newlist=[x*2 for x in list]
# print(newlist)
# newlist=[x**2 for x in list if x%3==0]
# print(newlist)
# nestedlist=[
#     [1,2,3],
#     [4,5,6],
#     [7,8,9]
# ]
# print(nestedlist[1][2])
