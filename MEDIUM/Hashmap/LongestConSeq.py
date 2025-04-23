
# 128. Longest Consecutive Sequence
# Medium
# Topics
# Companies

# Given an unsorted array of integers nums, return the length of the 
# longest consecutive elements sequence.

# You must write an algorithm that runs in O(n) time.

 

# Example 1:

# Input: nums = [100,4,200,1,3,2]
# Output: 4
# Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. 
# Therefore its length is 4.

# Example 2:

# Input: nums = [0,3,7,2,5,8,4,6,0,1]
# Output: 9

# Example 3:

# Input: nums = [1,0,1,2]
# Output: 3

 

# Constraints:

#     0 <= nums.length <= 105
#     -109 <= nums[i] <= 109
  
                    
                    
# l = [ 1, 2, 3, 4, 100, 10]


# Simplest brute force solution.,

def longestConsecSeqBF(nums):
    
    longest_seq = 0
    for i in nums:
        curr_seq = 1 # we start from 1 as we care considering i+1 seq.
        while i+1 in nums:
            curr_seq +=1
            i +=1
        longest_seq = max(longest_seq, curr_seq)
    
    return longest_seq

# Sorting the array solution

def longestConsSeqSort(nums):
    nums.sort()
    curr_seq = 1
    longest_seq = 1
    
    for i in range(1, len(nums)):
    
        if nums[i] != nums[i-1]:        # only if the next number is not same as previous
            if nums[i] == nums[i-1] +1 :
                curr_seq +=1
            else:
                longest_seq = max(longest_seq, curr_seq)
                curr_seq =1 
                
    
    return max(longest_seq, curr_seq)
        

def longestConsecSeqHashMap(nums):
    nums_set = set()
    max_seq = 0
    for v in nums:
        nums_set.add(v)
    
    for n in nums:
        if n in nums_set and (n-1) not in nums_set:
            cur_seq = n
            cur_seq_count = 0
            while cur_seq in nums_set:
                nums_set.remove(cur_seq)
                cur_seq_count +=1
                cur_seq +=1
            max_seq = max(max_seq, cur_seq_count)
    return max_seq             
            
    
    
    
    
    
    
nums = [100,4,200,1,3,2, 7, 101, 102, 11, 103, 104, 5, 6] 
# Ans: 7

# nums = [0,3,7,2,5,8,4,6,0,1]
# Ans: 9

# s = longestConsecSeqBF(nums)

# print(longestConsSeqSort(nums))

m = longestConsecSeqHashMap(nums)


print(m)



# print("Longest seq lenght: ", s)
