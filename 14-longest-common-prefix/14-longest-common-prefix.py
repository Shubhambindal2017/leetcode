class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        '''
        # case 1 - O(l * nlogn)
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
        '''
        # case 2 - O(l * n) - O(S)
        if len(strs) == 1:
            return strs[0]
        string1 = strs[0]
        for i in range(1, len(strs)):
            string2 = strs[i]
            min_length = min(len(string1), len(string2))
            common_prefix = ''
            for j in range(min_length):
                if string1[j] == string2[j]:
                    common_prefix += string1[j]
                else:
                    break
            if len(common_prefix) == 0:
                return ''
            else:
                string1 = common_prefix
        return common_prefix
        