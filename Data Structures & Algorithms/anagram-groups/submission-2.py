class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sorted_strs = {}
        for value in strs: 
            sorted_value= ''.join(sorted(value))
            if sorted_value in sorted_strs:
                sorted_strs[sorted_value].append(value)
            else:
                sorted_strs[sorted_value] = [value]
        return list(sorted_strs.values())
        