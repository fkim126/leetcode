"""
Given an integer array nums, return true if any value appears at least twice
in the array, and return false if every element is distinct.

Example:
Input: nums = [1,2,3,1]
Output: true

Example 2:
Input: nums = [1,2,3,4]
Output: false
"""

# Solution using dictionary. Time complexity of O(n).
def contains_duplicate(some_list): 
    
    # Empty dictionary
    seen = {}

    # Iterating through list of numbers, while tracking the index/number
    for index, number in enumerate(some_list):

        if number in seen:
            
            # If the number has been seen in the dictionary, we return True
            return True
        
        # If we don't see the number, we add the number in the dictionary with
        # its corresponding index
        seen[number] = index
    
    # After looping through the list and we do not find the same number in the
    # dictionary, we return False
    return False

my_list = [1,2,3,1]
print(contains_duplicate(my_list))

# Solution using sets. Time complexity of O(n).
def contains_duplicate_2(some_list):

    # We first change the list to a set, then get the length of the set
    set_length = len(set(some_list))

    # If the set_length is equal to the length of the original list, we return
    # False as all elements in set are unique and cannot contain duplicates
    if (set_length == len(some_list)):
        return False

    # If the set_length is equal not equal to the length of the original list,
    # we return True as there are duplicate elements in the list
    else:
        return True

my_list = [1,2,3,1]
print(contains_duplicate_2(my_list))