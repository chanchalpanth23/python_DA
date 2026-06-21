#dictionary(24 march)->key-value pair
#values->mutable
#keys->immutable
#does not allow duplicates
#keys->list,dict ke andar ke dict nhi ho skti
#keys->string,number,tuple
#values->any data type
#get(),setdefault,membership testing(if key in dict)

# dict1={
#     "name":"dice",
#     "age":10,
#     "prof":["coaching"]
# }
# # print(dict1)
# print(dict1["age"],dict1["name"])

#for value change
# dict1["name"]="dice academy"
# print(dict1)

#if exist then value change or if not then new key-value pair add ho jayega
# dict1["address"]="nirman vihar"
# print(dict1)

#get-> kisi particular key ki value lana
# print(dict1.get("name"))

#indexing is not followed,index key notation followed

#delete
# dict1={
#     "name":"dice",
#     "age":10,
#     "prof":["coaching","bfbf"],
#     (1,2):"hello"
# }
# del dict1[(1,2)]
# print(dict1)

# dict.keys()=["name","age","prof",(1,2)]
# print(dict1.keys())
# for i in dict1.keys():
#     print(i)
# ["dice",10,["coaching","bfbf"],"hello"]
# for i in dict1.values():
#     print(i)

#list convert into dict
# list1=[1,2,3,4]
# squares={
#     x:x**2 for x in list1}
# print(squares)

# list=[10,20,30]
# multiply={
#     x*2:x for x in list
# }
# print(multiply)

#dictionary merge->overiding(same key ko remove peehle vali ko remove krke)
# dict1={
#     "a":10,
#     "b":20
# }
# dict2={
#     "c":30,
#     "d":20,
#     "b":50
# }
#membership testing->kya is naam ki key  exist krti h
# if "b" in dict2:
#     print("a found")

# finaldict=dict1|dict2
# print(finaldict)

#nested dictionaries
# user={
#     "name":"chanchal",
#     "age":22,
#     "address":{
#         "street_num":30,
#         "city_name":"delhi",
#         "country":"India"
#     }
# }
# print(user["address"]["country"])

# dict1={
#     "a":10,
#     "b":20
# }
# print(dict1.get("c","c is not in the dict"))

# dict1={
#     "a":10,
#     "b":20
# }
# dict1.setdefault("c",0)
# print(dict1)
# print(dict1.get("c","c is not in the dict"))

# dict1={
#     "a":10,
#     "b":20,
#     "c":50
# }
# dict1.setdefault("c",0)
# print(dict1)

#items->every key-value pair ko tuple m convert kr deta
# for i in dict1.items():
#     print(i)