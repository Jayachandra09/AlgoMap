class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        min_length = float('inf')
        res = ""
        for i in strs:
            if len(i)<min_length:
                min_length = len(i)
                min_arr = i
        i = 0
        while(i<min_length):
            count = 0 
            for j in strs:
                if j[i]!=min_arr[i]:
                    return min_arr[:i]
            i+=1
        return min_arr[:i]


        #Second Approach

        min_length = float('inf')
        for i in strs:
            if len(i)<min_length:
                min_length = len(i)
        i = 0 
        while(i<min_length):
            for j in strs:
                if j[i]!=strs[0][i]:
                    return strs[0][:i]
            i+=1
        return strs[0][:i]


#AlgoMap Approach:
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        min_length = float('inf')

        for s in strs:
            if len(s) < min_length:
                min_length = len(s)

        while i < min_length:
            for s in strs:
                if s[i] != strs[0][i]:
                    return s[:i]
            i += 1
        return strs[0][:i]
        # Time: O(n * m) where n is the number of strings, m is the min word length
        # Space: O(1)

#Problem link : https://leetcode.com/problems/longest-common-prefix/description/
