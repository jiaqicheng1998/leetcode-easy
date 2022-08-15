# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

# An input string is valid if:

# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.

# Example 1:

# Input: s = "()"
# Output: true
# Example 2:

# Input: s = "()[]{}"
# Output: true
# Example 3:

# Input: s = "(]"
# Output: false

# 还是要先明白题目的意思，如果有一个东西close不了就不行。。。
# def isValid(s): 
#     lst = [char for char in s]
#     while len(lst) > 1:
#         curr = lst.pop(0)
#         if curr == '(':
#             for i in range(len(lst)):
#                 if lst[i] == ')':
#                     del lst[i]
#                     break
#                 elif i == len(lst) - 1 and lst[i] != ')':
#                     return False
#         elif curr == '[':
#             for i in range(len(lst)):
#                 if lst[i] == ']':
#                     del lst[i]
#                     break
#                 elif i == len(lst) - 1 and lst[i] != ']':
#                     return False
#         elif curr == '{':
#             for i in range(len(lst)):
#                 if lst[i] == '}':
#                     del lst[i]
#                     break
#                 elif i == len(lst) - 1 and lst[i] != ']':
#                     return False

#     if len(lst) == 0:
#         return True
#     else:
#         return False

# print(isValid('()'))
# print(isValid('()[]{}'))


# def isValid(s):
#     lst = [char for char in s]
#     d = {
#         "(": ")",
#         "[": "]",
#         "{": "}"
#     }
#     while len(lst) > 1:
#         curr = lst.pop(0)
#         print(curr)
#         for i in range(len(lst)):
#             if lst[i] in d:
#                 continue
#             elif lst[i] == d[curr]:
#                 del lst[i]
#                 break
#             else:
#                 return False

#     if len(lst) == 0:
#         return True
#     else:
#         return False

#先一个一个的过，如果都是左半边的东西就他妈直接略过 所以是一个stack last in last out 左半边都去stack 右半边做匹配
#直到第一个右边的玩意，然后看左边的东西
#如果不配对直接报错
#如果是对stack上面的东西pop出来

def isValid(s):
    lst = [char for char in s]
    stack = []
    d = {
        "(": ")",
        "[": "]",
        "{": "}"
    }
    for i in range(len(lst)):
        if lst[i] in d:
            stack.append(lst[i])
        else:
            if len(stack) > 0: #如果第一个玩意就是右边的就直接报错
                if lst[i] != d[stack[-1]]:
                    return False
                else:
                    stack.pop()
            else:
                return False 

    if len(stack) > 0:
        return False 
    else:
        return True


print(isValid("]"))
