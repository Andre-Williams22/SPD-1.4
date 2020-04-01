''' problem: implement a function that takes a string and returns a character that only appears once. 
Return the first unique character in the string. If there is no unique item retrun None.''' 


# Clarifying Questions: is the function taking 1 word at a time? What does the function return? Can there be two characters that appear once?
# Assumptions: The inputs are strings only, the function returns the unique character.
# Possible Solutions: A hashtable that stores the values and a list that keeps track of all unique characters


def non_repeating(string):
  hashtable = {}
  nums = []
  for item in string:
    if item in hashtable:
      hashtable[item] += 1
    else:
      hashtable[item] = 1
  
  for item in hashtable:
    if hashtable[item] == 1:
      nums.append(item)
    
  if len(nums) == 0:
    return None

  return nums[0]



word = 'aabbdbc'
word2 = 'xxbyzb'
print(non_repeating(word))
print(non_repeating(word2))