''' given a sequence of brackets, how will you identify if it's valid or not. Every opening has a closing bracket'''

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

# Bad Input 
print(is_valid(_[]))