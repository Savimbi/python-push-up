#Two number sum question
#O(n*2) time and O(1) space as we don't need additional memory but double loops.
def twoNumberSum1(array, targetSum):
    for i in range(len(array) - 1):
        firstNum = array[i]
        for j in range(i+1, len(array)):
            secondNumber = array[j]

            if firstNum + secondNumber == targetSum:
                return [firstNum, secondNumber]

    return []

#We may solve it again by using hash map and solve eq x+y=targetSum, where x is an integer in our array
#This algo will evaluated as O(n) time as we will pass through to the whole array, and O(n) space 
def twoNumberSum2(array, targetSum):
    numMap = {}
    for num in array:
        potentialMatch = targetSum - num
        if potentialMatch in numMap:
            return [targetSum-num, num]
        else:
            numMap[num]= True
    return []


# We can also solve this by sorting our array fiest them we add two numbers left right side
#As we expect python to use an algo to sort array in O(nlog n), we evaluate this algo as O(nlog n)time| O(1) space
def twoNumberSum3(array, targetSum):
    array.sort()
    left = 0
    right = len(array) - 1

    while right < left :
        currentSum = array[right] + array[left]

        if currentSum == targetSum:
            return [ array[right] + array[left] ]

        elif currentSum < targetSum:
            right += 1;
        elif currentSum > targetSum:
            left -= 1;
    return []


