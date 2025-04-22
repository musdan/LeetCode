# Given an array of strings strs, group the

# together. You can return the answer in any order.

 

# Example 1:

# Input: strs = ["eat","tea","tan","ate","nat","bat"]

# Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

# Explanation:

#     There is no string in strs that can be rearranged to form "bat".
#     The strings "nat" and "tan" are anagrams as they can be rearranged to form each other.
#     The strings "ate", "eat", and "tea" are anagrams as they can be rearranged to form each other.

# Example 2:

# Input: strs = [""]

# Output: [[""]]

# Example 3:

# Input: strs = ["a"]

# Output: [["a"]]

 

# Constraints:

#     1 <= strs.length <= 104
#     0 <= strs[i].length <= 100
#     strs[i] consists of lowercase English letters.

from collections import defaultdict

def groupAnagrams(strs):
    # create a hash map of all anagrams by using the sored string
    # as the index and the value is the number of anagrams
    # ex: abc and cba will have a map(dict) index like:
    # ['abc'] = 2 as they are two instances of the anagram
    

    smap = defaultdict(list)
    
    for i in strs:
        k = ''.join(sorted(i))
        smap[k].append(i)
    
    ll = list(smap.values())
    return ll      
    

strs = ["eat","tea","tan","ate","nat","bat"]

# s = "abdefg"
# ss = ''.join(sorted(s))
# print(ss)
sr = groupAnagrams(strs)
print(sr)