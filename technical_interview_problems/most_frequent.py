# Most Frequently Occuring Item in Array 
#Example: list1 = [1, 3, 1, 2, 3, 1]
# Output: => 1 

def most_frequent(given_list):
    hashtable = {} # O(n) Space Complexity
    max_num = 0 # O(1) space => tracks the most occuring number 
    max_count = 0  # O(1) space => tracks num of times number appears

    for i in given_list: #O(n) time
        if i in hashtable: # O(1) time
            hashtable[i] += 1  # O(1) time
        else:
            hashtable[i] = 1  # O(1) time
        if hashtable[i] > max_num: # O(1) time
            max_num = i #  grabs key  
            max_count = hashtable[i] # grabs value
    return max_num, max_count 

    # for item in hashtable.values():
    #     if item > max_num:
    #         max_num = item 
    #return max_num

array = [2, 5, 6, 3, 3, 5, 7, 5]

print(most_frequent(array))