i = 1
# while i<=10:
#     if i%2==1:
#         print(i)
#     i += 1
    
# while i<=1000:
#     print(f"{i}: Ashish")
#     i+=1
    
    
# num = int(input("Enter a number: "))
# fact = 1
# while num > 0:
#     fact *= num
#     num -=1 
# print("The factorial is:", fact)

# Step-by-step calculation:
# f    n
# 1    5
# 5    4
# 20   3
# 60   2
# 120  1

# nums = []

# while True:
#     num = int(input("Enter a number (or -1 to exit): "))
#     if num == -1:
#         break
#     else:
#         nums.append(num)
        
# print("The numbers entered are:", nums)

# sum = 0
# for i in nums:
#     sum += i
# print("The sum of the numbers is:", sum)



# sum   nums
# 0     1
# 1     2
# 3     3
# 6     4
# 10


sum = 0
for i in range(3,31,3):
    print(i)
    sum += i
    
print("\nSum is: ",sum)