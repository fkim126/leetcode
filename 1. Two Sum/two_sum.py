"""
Given an array of integers nums and an integer target, return indices of the
two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not
use the same element twice.

You can return the answer in any order.

Example:
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
"""

# 1. Brute force method - checking for every possible elements in the list for
# two values that equal the target value. NOTE: This time complexity would be
# O(n^2) as we have two for loops.
def solution(some_list, target):

    # First iteration of list of numbers
    for i in range(len(some_list)):

        # Second iteration of list of numbers
        for j in range(i+1, len(some_list)):

            if some_list[i] + some_list[j] == target:
                
                # If the two values equals the target, return the index
                # positions.
                return [i, j]
    
    # After looping all numbers of the list and not finding a pair,
    # we return the value None
    return None

my_list = [2, 7, 11, 15]
print(solution(my_list, 9))

# 2. Using a dictionary - checking for the complementary value (difference of
# target - number) if it's in the dictionary. If it is, return the two values,
# as those two numbers equals the target. This time complexity would be O(n).
def solution_2(some_list, target):

    # Creating empty dictionary
    seen = {}

    # Iterate through list of numbers
    # NOTE: enumerate() allows us to receive the index and the value of the
    # element
    for index, number in enumerate(some_list):
        
        # Check if the number that we need to add to the current number to get
        # the target
        complementary = target - number 
        if complementary in seen:

            # If the complementary value is in the dictionary, we return the
            # two indices which sums equal the target
            return [seen[complementary], index]

        # If the complementary is not in the dictionary, we add the value and
        # the corresponding index to the dictionary
        seen[number] = index
    
    # After looping through the list and no pairs sum equals the target value,
    # we return None
    return None

my_list = [2, 7, 11, 15]
print(solution_2(my_list, 9))