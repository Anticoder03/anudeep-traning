# min max sum

# Sample Input

# 1 2 3 4 5
# Sample Output

# 10 14
# arr = [1,2,3,4,5]

# min_val = min(arr)
# max_val = max(arr)

# min_arr = [x for x in arr if x != max_val]
# max_arr = [x for x in arr if x != min_val]

# print(sum(min_arr))
# print(sum(max_arr))

# def miniMaxSum(arr):
#     total = sum(arr)
#     min_sum = total - max(arr)
#     max_sum = total - min(arr)

#     print(min_sum, max_sum)


# arr = [1, 2, 3, 4, 5]
# miniMaxSum(arr)



# for i in range(1,6):
#     for j in range(1,i+1):
#         print(i, end=" ")
#     print()
    

# for i in range(1,6):
#     for j in range(1,i+1):
#         if(j%2!=0):
#             print("1", end=" ")
#         else:
#             print("0", end=" ")
#     print()
    
# fibonachi series

series = [0, 1]
num = int(input("Enter the number of terms: "))

if num == 1:
    print(series[0])
elif num == 2:
    print(series)
else:
    for i in range(2, num):
        next_term = series[i-1] + series[i-2]
        series.append(next_term)
    print(series)