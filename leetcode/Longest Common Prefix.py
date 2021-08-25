'''
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

 

Example 1:

Input: strs = ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
 

Constraints:

1 <= strs.length <= 200
0 <= strs[i].length <= 200
strs[i] consists of only lower-case English letters.
'''

class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        list1 = ""
        x = len(strs[0])
        for i in range(len(strs)):
            if len(strs[i])< x :
                x = len(strs[i])
        new = strs[0][0:x]
        for i in range(x):
            for j in range(1,len(strs)):
                if strs[j][i] != new[i]:
                       return list1
            list1 +=new[i]
        return list1
        
