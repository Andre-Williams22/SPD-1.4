# is_valid_parenthesis Leetcode solution
def valid(s):
  stack = []
  pairs = {'[':']', '{':'}', '(':')'}
  for item in s:
    if item in pairs:
      stack.append(pairs[item])
      print(stack)
    else:
      if len(stack)==0 or stack.pop() != item:
        return False

  print(stack)
  return len(stack) == 0

print(valid('[]{)}'))



# Variable Table

# Variables  Contents
# stack        []
# pairs       {'[':']', '{':'}', '(':')'}
# s            '[]{)}'
# item         []{)}

