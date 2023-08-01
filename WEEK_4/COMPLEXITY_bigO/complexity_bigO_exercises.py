# the smallest complexity there is (straight horizontal line on the graph): 
# CONSTANT COMPLEXITY -  O(1):

# def  constant_algo(items:list):
#     result = items[0] * items[0]    #1 simple operation
#     print(result) #2 simple operation
    
# constant_algo([1,2,3]) # only one operation = complexity is 2 - the highest speed of performance


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


# LIFO - LAST IN FIRST OUT - the rule for working with Stack
# a_stack = []

# a_stack.append(1)
# a_stack.append(2)
# a_stack.append(3) #Last in

# a_stack.pop() #First out

from collections import deque

my_queue = deque(['one', 2, 'three', 4])

my_queue.pop()
print(my_queue)