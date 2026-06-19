# decorator-> modify or extend the behaviour of a function without changing its actual code.(kisifn ko intactrkhna  )
# argument meijo (raw function or  usme extra  functionality add karke return karte hai.
# def  decoratorFn(a):
#     def modified():
#         print("loop has started")
#         a()
#         print("loop has ended")
#     return modified

# @decoratorFn
# def printHello():
#     for i in range(1,6):
#         print("hello")
# fn=decoratorFn(printHello)
# fn()

# def decoratorFn(a):
#     def modified(*args):
#         print("Hi how are you?")
#         a(*args)
#         print("I am good.")
#     return modified
# @decoratorFn
# def printmultiply(a,b):
#     print(a*b)
    
    
# printmultiply(2,4)

#iterator- access elements one by one.
# a= iter([10,2,3,4,5])
# print(next(a))
# print(next(a))
# print(next(a))
# print(next(a))
# print(next(a))

# for i in[10,2,3,4,5]:
#     print(i)

#generator=>value create krna without allocating permanent memory.






