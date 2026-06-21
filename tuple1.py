#TUPLES->immutable,little fast,(),use it when changes cannot be done
#list->mutable,little slow,[],use it when changes need to be done
#both are allowed dublicates entries
#negative indexing->start from back

# tuple=()
#tuple=(1)->string
# tuple=(1,)
# print(type(tuple))
# tuple=(1,2,3)
# print(tuple)
# tuple2=(1,"hello",True)
# print(tuple2[-1])

#tuple unpacking
# tuple1=(1,2,3,4)
# a,b,c,d=tuple1
# print(a,b,c,d)

# tuple=(1,2,3,4,[1,2,3])
# tuple[4][0]=10
# print(tuple)
# instances of (list and integer) ko hum sath m likhke max nhi nikal skte

# tuple=(5,24,2,6)
# print(max(tuple))
# print(min(tuple))

#nested tuple
# nestedtuple=(
#     (4,2,6),
#     (1,2,4),
#     (6,2,1)
# )
# print(nestedtuple[0][1])

# tuple=(2,3,4,1,2)
# print(tuple.count(2))
# print(tuple.index(2))

#TUPLE SLICING
# tuple1=((1,2),(3,4),(7,9))
# print(tuple1[2][0])
#SUM OF TUPLE
# tuple=(1,6,3)
# print(sum(tuple))


#list-> mutability,iterate,comp fn
#tuple->(1)->string,(1,)->tuple,mutable,count,index