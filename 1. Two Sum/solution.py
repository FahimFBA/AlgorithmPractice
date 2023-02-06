# Time = O(N) and Space = O(N)
# Using Hash Table

def twoNumberSum(array, targetSum):
    nums = {}
    for num in array:
        potentialMatch = targetSum - num
        if potentialMatch in nums:
            return [potentialMatch, num]
        else:
            nums[num] = True
    return []

# driver code
array = [3, 5, -4, 8, 11, 1, -1, 6]
targetSum = 19
print(twoNumberSum(array, targetSum))