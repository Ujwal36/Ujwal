def parenthesisbalanced(string):
    dict = {'(':')', '{':'}','[':']'}
    stack = []
    for x in string:
        if x in dict.keys() :
            stack.append(x)
        elif x in dict.values():
            if len(stack) == 0:
                return False
            p = stack.pop()
            if dict.get(p) != x:
                return False
    print(stack)
    if len(stack) != 0:
        return False
    return True

string = "[{[{}]"
print(parenthesisbalanced(string))