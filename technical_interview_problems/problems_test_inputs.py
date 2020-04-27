''' given a sequence of brackets, how will you identify if it's valid or not. Every opening has a closing bracket'''

# Question 1 

def is_valid(string):
  stack = []
  hashtable = {'(':')', '[':']', '{':'}'}
  for item in string:
    if item in hashtable:
      stack.append(hashtable[item])
    else:
      if len(stack) ==0 or stack.pop() != item:
        return False

  return True
  
 # Good Normal Input 
print(is_valid('[{}]'))
print(is_valid('(['))

# Bad Input Cases 
# print(is_valid(_[]))
# print(is_valid(' '))



# Question 2 

def element_mult_add(x, y):
  ''' calculate the product of two list and then find the sum of the numbers in the list'''
  n = [i*j for i,j in zip(x,y)]
  count = 0
  for item in n:
    count += item
  return count 


x = [1, 2, 3]
y = [10, 15, 20]

# good test case input 
print(element_mult_add(x, y))
print(element_mult_add([3,5,6], [2,7,9]))

# # bad test case input 
# hashtable = {3:3, 2:6, 1:8}
# hashtable2 = {9:2, 1:7, 13:8}
# print(element_mult_add(+,-))
# print(element_mult_add(hashtable, hashtable2))
