# Problem: Write a function to determine if a string is a palindrome or not

# Clarifying Questions: is the function taking 1 word at a time? What does the function return? string or boolean  
# Assumptions: The inputs are strings only, the function returns a boolean
# Possible Solutions: String slicing on both ends of the string to see if they match, pointers on each end to check similarities, 
# using sets to see what the elements have in commmon 



def palindrome(string):
  for i in range(0, len(string)//2):
    if string[i] != string[len(string)-i-1]:
      return False
  return True

print(palindrome('cat'))
print(palindrome('alla'))
print(palindrome('ot to'))