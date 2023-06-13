def validate(str):
    stack = []
    for brace in str:
        if brace == "(" or  brace == "[" or  brace == "{":
            stack.append(brace)
    print(stack)

str = "[{("
validate(str)

dict = {}