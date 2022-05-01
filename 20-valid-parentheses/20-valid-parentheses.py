class Solution:
    def isValid(self, s: str) -> bool:
        array = [0] * (10**4)
        current_index = 0
        for el in s:
            if el == '[':
                array[current_index] = ']'
                current_index += 1
            elif el == '{':
                array[current_index] = '}'
                current_index += 1
            elif el == '(':
                array[current_index] = ')'
                current_index += 1
            else:
                if array[current_index-1] != el:
                    return False
                else:
                    current_index -= 1
        return True if current_index == 0 else False
        