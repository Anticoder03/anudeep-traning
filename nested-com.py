a = {
    'row1':{'a':1,'b':2},
    'row2':{'a':1,'b':2},
}

b = { 
     outer_key:{inner_key:innerval*2 for inner_key,innerval in outer.items()}
     for outer_key,outer in a.items()
     }
# print(a)
# print(b)

def num_gen():
    yield 1
    yield 2

obj = num_gen()

# print(next(obj))
# print(next(obj))

# print(next(obj))

g = tuple((x for x in range(10)))

# print(type(g))




# #? Generator function
# def divisible_by_five():
#     for i in range(5, 51):
#         if i % 5 == 0:
#             yield i

# #? Using the generator
# gen = divisible_by_five()

# for num in gen:
#     print(num)

def name(name):
    print(name)

def greet():
    print("hello, ")
    name("Ashish")
    print("bye.")
    
# greet()



# def teach():
#     print("teaching python")
    

# def punch():
#     print("punch in")
#     teach()
#     print("punch out")
    
# punch()

def punch(func):
    def wrapper():
        print("punch in")
        func()
        print("punch out")
    return wrapper


@punch
def teach():
    print("teaching python")


teach()
