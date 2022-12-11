# Time Complexity: O(n * k * log k)
# Space Complexity: max O(n), not count the result space
# where n is the length of strs, k is the longest length of a string in strs.
# And k * log k refers to the sort operation.

class Solution:

    def groupAnagrams(self, strs):
        result = []
        dict = {}

        for str in strs:
            sorted_str = ''.join(sorted(str))
            if sorted_str not in dict:
                dict[sorted_str] = len(dict)
                result.append([])
            result[dict[sorted_str]].append(str)

        return result

print(Solution().groupAnagrams(["eat","tea","tan","ate","nat","bat"]))
print(Solution().groupAnagrams([""]))
print(Solution().groupAnagrams(["a"]))
print(Solution().groupAnagrams(["ace","cia","cea","aic","beet","ebet","ica"]))