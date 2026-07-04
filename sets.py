#sets->sets is a data structure that mainly provide features for duplicates remove

# sets={}
# print(type(sets))
# set1={1}
# print(type(set1))
#sets mei sirf immutable cheeze hi rkhenge list mutable hai to wo nhi
#duplicates remove
#indexing not allowed so location change ->reason(hashing)

# set1={1,2,1,2,1,1,"hello",(1,2)}
# print(type(set1),set1)
# set1={1,1}
#indexing allowed nhi h
# print(set1[0])
#set converted into list
# set1={1,2,3,3,(1,2),4,"hello",6}
# list1=list(set1)
# print(list1)
#set ko list m convert krke indexing notation pe rely kiya ja skta hai ya nhi->NO
#BCS of order change agr different data types hai to

#pop->random element ko remove kr deta h
# element=set1.pop()
# print(element)

# for i in set1:
#     print(i)

# set1.add(10)
# print(set1)

#remove vs discard

#remove->if value exist nhi krti to error aa jayega
# set1.remove(1)
# set1.remove(2)
# print(set1)

#discard->value exist nhi krti to bhi error nhi dega
# set1.discard(2)
# set1.discard(1)
# print(set1)

set1={1,2,3}
set2={2,4,5}
#union
# set3=set1|set2
# print(set3)

#intersection->common
# set3=set1&set2
# print(set3)

#set1-set2->jo set1 mai h set2 m nhi h
#set2-set1->set2 m h set1 m nhi h

# set3=set1-set2
# set4=set2-set1
# print(set3,set4)

#symmetric difference->dono ke unique(common ko hatake)
# print(set1^set2)
#print(set1.symmetric_difference(set2))

#supersets/subsets

# set1={1,2,9,6}
# set2={1,2}

#disjoint-> ek single  element bhi common na ho(true/false)
# print(set1.isdisjoint(set2))
#set1->superset
#set2->subset
# print(set2.issubset(set1))
# print(set1.issuperset(set2))

# list2=[1,2,5,4,1,5,5]
# set2 = set({x for x in list2 if list2.count(x)>1})
# print(set2)

# list2=[1,2,5,4,1,5,5]
# def fn(list2):
#     list1=list(set(list2))         #list to set dublicates remove
#     set2 = set({x for x in list2 if list2.count(x)>1})
#     list3=[list1,set2]
#     return tuple(list3)
# a=fn([1,4,3,4,3,4,6,7,5,5])
# print(a)

# {1,2,3,4} ,{
#1:4,
#2:3,
#3:2,
#4:8
#}

# def fn(dict):
#     list1=[]
#     for key, values in dict.items():
#         list1.extend([key]*values)          #square bracket m key ka mattlb ka key ke list bna li phir like or us list ko 4 baar replica kr liya
#     return list1
# print(fn({
# 1:4,
# 2:3,
# 3:2,
# 4:8
# }))
# print("2"*5)
#identation error
#syntax(,: ())
#typing error
#value error

#zerodivisionerror
# a=10
# b=0
# print(a/b)

#try expect
#value error
# b=int("a")
# print(b)
#type error
# print("2"/5)
# print("2"-5)
# print("2"+5)
#name error
# print(b)
# fn()
#index error
# li=[6,8,9]
# print(li[4])
#key error
# dict={
#     "name":"dice"
# }
# print(dict["age"])

#attribute error
# a="dice academy"
# a.append("!!")
# tupple=(1,2)
# tupple.append(10)

#try expect
#numbers, non integer,null
# def sum():
#     a=int(input("enter a num A-:"))
#     b=int(input("enter a num B-:"))
#     print(a+b)
# sum()

#TRY EXCEPT
# def sum():
#     a=input("enter a num A-:")
#     b=input("enter a num B-:")
#     try:
#      print(a+int(b))
#     except ValueError:
#        print("any of the values is not a")
#     except TypeError:
#        print("any of the value is not a integer")
#     except Exception as exp:
#        print("-------",exp)
       
# sum()


 




