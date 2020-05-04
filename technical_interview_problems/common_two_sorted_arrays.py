# Problem: Given two ascending order arrays, print out the elements they have in common.
# Example 
# input:
# a = [1, 4, 5, 6, 7, 9]
# b = [1, 2, 4, 8, 9, 10]
# Output:
# c = [1, 4, 9]

def common_elements(list1, list2): # O(max(list1,list2))
    new_list = [] # O(n) space complexity
    p1 = 0
    p2 = 0 
    # for i in range(0, len(list1)-1): #O(n)
    while p1 < len(list1) and p2 < len(list2): #O(list1*list2) time complexity
        if list1[p1] == list2[p2]: # O(1)
            new_list.append(list1[p1]) # O(1)
            p1+=1 # O(1)
            p2+=1 # O(1)
        elif list1[p1] > list2[p2]: # O(1)
            p2+=1 # O(1) 
        else: # O(1)
            p1+=1 # O(1)

    return new_list

list1 = [1, 3, 6, 7, 10]
list2 = [3, 4, 5, 9, 10]
print(common_elements(list1, list2))
