# Write a Python function called max_num()to find the maximum of three numbers.

def max_num(a,b,c):
    return max([a,b,c])

print(max_num(1,2,3))
print(max_num(4,8,12))
print(max_num(347825646, 392487652348975, 44))


# Write a Python function called mult_list() to multiply all the numbers in a list.

def mult_list(numbers):

  if len(numbers) == 0:
    return 0

  prod = numbers[0]


  if len(numbers) > 1:
    for i in numbers[1:]:
      prod = prod * i

  return prod
    
print(mult_list([1,2,3]))
print(mult_list([]))
print(mult_list([15]))



# Write a Python function called rev_string() to reverse a string.

def rev_string(my_str):
    return my_str[::-1]

print(rev_string(""))
print(rev_string("no"))
print(rev_string("reverse the string!"))


# Write a Python function called num_within() to check whether a number falls in a given range.

def num_within(i,a,b):
    return i in range(a,b+1)
     
print(num_within(4,5,6))     
print(num_within(4,0,4))     
print(num_within(24,2,6))



# Write a Python function called pascal() that prints out the first n rows of Pascal's triangle.

def pascal(num):
    if num < 1:
        print("invalid number of rows")
       



# triangle = [[1],[1,1]]
# def pascal(n):
#   #base case
#   if n < 1:
#     print("invalid number of rows")
#   elif n == 1:
#     print(triangle[0])
#   else:
#     row_number = 2
#     #fill up correct number of rows in triangle
#     while len(triangle) < n:
#       row = []
#       row_prev = triangle[row_number - 1]
#       #create correct row, then add to triangle (this row will be 1 longer than row before it)
#       length = len(row_prev)+1
#       for i in range(length):
#         #first number is 1
#         if i == 0:
#           row.append(1)
#         #intermediate numbers get added from previous rows
#         elif i > 0 and i < length-1:
#           row.append(triangle[row_number-1][i-1]+triangle[row_number-1][i])
#         #last number is 1
#         else:
#           row.append(1)
#       triangle.append(row)
#       row_number += 1

#     #print triangle
#     for row in triangle:
#       print(row)

# pascal(2)
# pascal(5)