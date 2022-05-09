class Solution:
    def isValid(self, s: str) -> bool:
        array = []
        for el in s:
            if (el == '['): 
                array.append(']')
            elif (el == '('): 
                array.append(')')
            elif (el == '{'): 
                array.append('}')
            else:
                if len(array) > 0:
                    popped_el = array.pop()
                    if popped_el != el:
                        return False
                else:
                    return False
        return array == []
        