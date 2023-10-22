'''
Binary Search
-------------------------------------------------------------
given a list of numbers find the given target number and return the index. 
The list of number are ordered
EXAMPLE: 
nums = [1,2,3,4,5,6], target = 3
answer = 2 
(3 is at the index 2 in the list)
lalala
'''

nums = [1, 2, 3, 4, 5, 6]
target = 3



def find_target(nums, target):

    # write code below, please use google for help
    for num in nums:
        if num == target:
            index = nums.index(num)
            print(index)
         
find_target([4,5,6,7,8,9,10],8)

# USE BINARY SEARCH TO FIND THE TARGET
def binary_search(numbers, target):
    # find midpoint of list

    left = 0
    right = len(numbers)

    while left < right:
        mid = (left + right)//2
        if numbers[mid] < target:
            left = mid + 1
        else:
            right = mid 
    return left
ans = binary_search(nums,target)
print(ans)



