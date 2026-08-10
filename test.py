# a = int(input("Enter a number: "))
# if a%2 == 0:
#     print("The number is even.")
# else:
#     print("The number is odd.")
    
# my_set = {1, 2, 3}

# my_set.discard(2)   # Removes 2
# my_set.discard(5)   # No error, even though 5 is not in the set

# print(my_set)
# Output: {1, 3}

# A = {1, 2, 3} 
# B = {4, 5, 6, 7, 8} 
# result = A - B 
# print(result)

# my_set = {1, 2, 3}
# my_set.pop()
# print(my_set)
# my_set = set()
# my_set.add(10)
# my_set.add(20)
# my_set.clear()
# print(my_set)


# set1 = {1, 2, 3}
# set2 = {1, 2}

# result = set1.issubset(set2)
# print(result)

# set1 = {1, 2, 3}
# set2 = {4, 5, 6}

# print(set1.isdisjoint(set2))

# set1 = {1, 2, 3}
# set2 = {3, 4, 5}

# result = set1 ^ set2
# print(result)


# set1 = {1, 2, 3}
# set1.update({4, 5, 6})
# print(set1)
# set1.pop()

# a = [y + x for x in range(2) for y in range(2)]x
# print(a)



# even_numbers = [x for x in range(1,51) if x %2 == 0]
# print(even_numbers)

def check_prime(num):
    if num < 0:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

prime_numbers = [i for i in range(0,51) if check_prime(i)]
print(prime_numbers)


