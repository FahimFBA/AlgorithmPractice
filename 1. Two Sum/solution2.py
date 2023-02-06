# Time = O(n^2) and Space = O(1)
# Using sorting

def twoNumberSum(array, targetSum):
    for i in range(len(array) - 1):
        firstNum = array[i]
        for j in range(i + 1, len(array)):
            secondNum = array[j]
            if firstNum + secondNum == targetSum:
                return [firstNum, secondNum]
    return []

# driver code
array = [3, 5, -4, 8, 11, 1, -1, 6]
targetSum = 19
print(twoNumberSum(array, targetSum))