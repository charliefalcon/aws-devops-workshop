class Solution:
    # @return a boolean
    def isValid(s):
        stack = []
        br_dict = {"]":"[", "}":"{", ")":"("}
        for char in s:
            if char in br_dict.values():
                stack.append(char)
            elif char in br_dict.keys():
                if stack == [] or br_dict[char] != stack.pop():
                    return False
            else:
                return False
        return stack == []

s = ""
print (Solution.isValid(s))