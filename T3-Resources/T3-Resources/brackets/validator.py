'''
checks to see if a set of brackets are valid

By Aidan Lalonde-Novales
'''

def isvalid(string):
    stack = []
    # appends opening brackets immediately for checking
    for bracket in string:
        if bracket in "({[":
            stack.append(bracket)
        # checks to see if the previous bracket matches the closing bracket
        # if not, return false
        elif bracket in ")}]":
            # need to check if the stack is empty to prevent program
            # from crashing by accessing a non-existant index (-1)
            if len(stack) == 0:
                return False
            elif bracket == ")" and stack[-1] != "(":
                return False
            elif bracket == "}" and stack[-1] != "{":
                return False
            elif bracket == "]" and stack[-1] != "[":
                return False
            else:
                # remove opening bracket as it is now verified
                stack.pop()
    # returns true if the stack is empty, which it should be if all brackets
    # match up, as the correct brackets are popped from the stack
    if len(stack) == 0:
        return True
    else:
        return False


def femboys_r_hot(string):
# initialize the stack
    stack = []
    # iterate through the string
    for char in string:
        # if the character is an opening bracket, add it to the stack
        if char in "([{":
            stack.append(char)
        # if the character is a closing bracket, check if it matches the last opening bracket
        elif char in ")]}":
            # if the stack is empty, return False
            if len(stack) == 0:
                return False
            # if the last opening bracket is not the same type as the closing bracket, return False
            if stack[-1] == "(" and char != ")":
                return False
            elif stack[-1] == "[" and char != "]":
                return False
            elif stack[-1] == "{" and char != "}":
                return False
            # if the last opening bracket is the same type as the closing bracket, remove it from the stack
            stack.pop()
    # if the stack is empty, return True
    if len(stack) == 0:
        return True
    # if the stack is not empty, return False
    else:
        return False