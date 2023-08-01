
#SIMPLE COMPLEXITY - O(1) - the best
#LINEAR COMPLEXITY - O(n) - fair complexity - (diagonal 45 degrees line on the graph)

# def linear_algo(items:list):
#     for item in items: #loop
#         print(item)
        
# a_list = [1,2,3,4]

# linear_algo(a_list)


# QUADRATIC COMPLEXITY O(n^2) - bad - (almost vertical line on the graph)

# def quadratic_algo(items:list):
#     for item in items: #loop inside loop
#         for item2 in items:
#             print(item, '', item2)

# a_list = [1,2,3,4]
# quadratic_algo(a_list)


# LIFO - LAST IN FIRST OUT - the rule for working with STACK - 
# when we know that we need to deal only with the recent last data

# a_stack = []

# a_stack.append(1)
# a_stack.append(2)
# a_stack.append(3) #Last in

# a_stack.pop() #First out


# DEQUE
# when you start with the first data
# from collections import deque

# my_queue = deque(['one', 2, 'three', 4])

# my_queue.pop() #O(1) deque(['one', 2, 'three'])
# my_queue.popleft() #O(1) <--- deque([2, 'three'])

# print(my_queue)

# when you're working with data, you need to start from the first thing


#DOUBLE LINKED LIST
#interested on the double edges of the list


# def subsetsum(numbers: list, target: int) -> bool:
#     hashtable = set({}) #O(1)

#     for num in numbers: # +n = O(n)
#         nto_find = target - num
#         if nto_find in hashtable:
#             print(True, nto_find, num)
#             return True
#         hashtable.add(num)

# 12 + x = 2
# X = 2 - 10
# X = -10

    # print(False)
    # return False

    
# nums = [12, -7, 20, 1, 4, -10, -1]
# subsetsum(nums, 1)
# subsetsum(nums, 2)
# subsetsum(nums, 3)
# subsetsum(nums, 4)
# subsetsum(nums, 1) # False
# subsetsum(nums, 2) # True: 12,  -10
# subsetsum(nums, 3) # True: 4,  -1
# subsetsum(nums, 4) # False #


# RECURSION 
# is a method for solving problems 
# involves a function that calls itself
# is not faster than itteration

#conditions for doing a recursion:
# A - function needs to return some kind of result, which is the product of itself
# B - function needs to have a base case - it should stop

# factorial of 5 is 5 + 4 + 3 + 2 + 1
# factorial function is recursive  -   5 + factorial(5 - 1)
                                    #  4 + factorial(4 - 1)
                                    #  3 + factorial(3 - 1)
                                    #  2 + factorial(2 - 1)
                                    #  stop at 1
                                    
# A CALL STACK is a bit of memory where temporary data of function (function call) operations is stored untill
# function stops recurring - metaphor is digging, reaching the bottom, putting earth back

# def factorial(n):
#     #define base case
#     if n == 1:
#         return n
#     else:
#         return n + factorial(n - 1)  #RECURSIVE CALL

# print(factorial(5))

# dig in
# call 1 5 + factorial(5)
# call 2 4 + factorial(4)
# call 3 3 + factorial(3)
# call 4 2 + factorial(2)
# call 5 1 + factorial(1)

# dig out
# ---> 15

# books = [ 'book1', 'book2','book3','book4','book5']

# books[1:] #the argument to the next recursive function
# len(books) == 0   #condition to stop

# def count_books(book_list):
#     #define base case 
#     if len(book_list) == 0:
#         return 0
#     else:
#         return 1 + count_books(book_list[1:]) #slice remove from the list
    
# print(count_books(books))

# EXERCISES EXAMPLES

# def count_num(number_list):
#     if not number_list: 
#         return 0
#     else:
#         return number_list[0] + count_num(number_list[1:])
    
# numbers = [2, 4, 5, 6, 7]

# print(count_num(numbers))


# def reverse(sentence: str) -> str:
#     if len(sentence) == 0:
#         return sentence
#     else:
#         # return reverse(sentence[1:]) + sentence[0] 
#         return sentence[-1] + reverse(sentence[:-1])

# my_sentence = 'Hello World'
# print(reverse(my_sentence))


# def exponent(base, exp):
#     if exp == 0:
#         return 1
#     else:
#         return base * exponent(base, exp - 1)
    
# print(exponent(2, 3))