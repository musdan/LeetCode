# 11. Container With Most Water
# Medium
# Topics
# Companies
# Hint

# You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

# Find two lines that together with the x-axis form a container, such that the container contains the most water.

# Return the maximum amount of water a container can store.

# Notice that you may not slant the container.

 

# Example 1:

# Input: height = [1,8,6,2,5,4,8,3,7]
# Output: 49
# Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.

# Example 2:

# Input: height = [1,1]
# Output: 1

 

# Constraints:

#     n == height.length
#     2 <= n <= 105
#     0 <= height[i] <= 104

def maxArea(heights):
    
    # calculate the widht of each rectanble made of the lower of
    # the two heights..
    mA = 0
    for h in range(len(heights)):
        for w in range(h+1, len(heights)):
            width = w - h
            cA = min(heights[h], heights[w]) * width
            mA = max(mA,cA )
    return mA

def maxAreaO(heights):
    
    mA = 0
    left = 0
    right = len(heights)-1
    while left < right:
        width = right - left
        cA = min(heights[left], heights[right]) * width
        mA = max(mA, cA)
        if heights[left] <= heights[right]:
            left+=1
        else:
            right-=1
    return mA
    
a = [1,8,6,2,5,4,8,3,7]

x = maxAreaO(a)
print(x)