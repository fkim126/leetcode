"""
Given an array of integers nums which is sorted in ascending order, and an
integer target, write a function to search target in nums. If target exists,
then return its index. Otherwise, return -1.

You must write an algorithm with O(log n) runtime complexity.

Example: 
Input: nums = [-1,0,3,5,9,12], target = 9
Output: 4
Explanation: 9 exists in nums and its index is 4
"""

# NOTE: Binary search can only be implemented if the list is sorted in
# ascending order
def binary_search(some_list, target):

    # Setting lower and upper bounds
    low = 0
    high = len(some_list) - 1

    # Continue searching while lower bound is less than or equal the higher
    # bound
    while low <= high:

        # Setting middle boundle
        mid = (high + low) // 2

        if target > some_list[mid]:
            
            # If the target value is greater than the mid value, we update the
            # lower bound to middle plus one
            low = mid + 1
        
        elif target < some_list[mid]:

            # Else if the target is less than the mid value, we update the
            # uppoer bound to middle minus one
            high = mid - 1
        
        else: 

            # If we found the target, we return the value of mid
            return mid
    
    # After looping through the list and if we do not find the target, we
    # return -1
    return -1

my_list = [-1, 0, 3, 5, 9, 12]
print(binary_search(my_list, 9))