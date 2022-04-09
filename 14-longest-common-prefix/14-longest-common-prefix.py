class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 1:
            return strs[0]
        smallest_string_lexographic = min(strs)
        largest_string_lexographic = max(strs)
        
        # longest common prefix of strs -> common prefix of smallest_string_lexographic and largest_string_lexographic
        min_length = min(len(smallest_string_lexographic), len(largest_string_lexographic))
        if min_length == 0:
            return ''
        common_prefix = ''
        for i in range(min_length):
            if smallest_string_lexographic[i] == largest_string_lexographic[i]:
                common_prefix +=  smallest_string_lexographic[i]
            else:
                return common_prefix
        return common_prefix
            
        