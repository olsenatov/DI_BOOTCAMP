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


def subsetsum(numbers: list, target: int) -> bool:
    hashtable = set({}) #O(1)

    for num in numbers: # +n = O(n)
        nto_find = target - num
        if nto_find in hashtable:
            print(True, nto_find, num)
            return True
        hashtable.add(num)

# 12 + x = 2
# X = 2 - 10
# X = -10

    print(False)
    return False

    
nums = [12, -7, 20, 1, 4, -10, -1]
subsetsum(nums, 1)
subsetsum(nums, 2)
subsetsum(nums, 3)
subsetsum(nums, 4)
# subsetsum(nums, 1) # False
# subsetsum(nums, 2) # True: 12,  -10
# subsetsum(nums, 3) # True: 4,  -1
# subsetsum(nums, 4) # False #