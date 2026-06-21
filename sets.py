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

