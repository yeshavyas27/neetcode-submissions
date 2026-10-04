class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sorted_strs = {}
        for value in strs: 
            if ''.join(sorted(value)) in sorted_strs:
                sorted_strs[''.join(sorted(value))].append(value)
            else:
                sorted_strs[''.join(sorted(value))] = [value]
        return list(sorted_strs.values())
        