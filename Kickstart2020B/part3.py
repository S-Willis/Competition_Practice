testCases = int(input())
strings = [input() for x in range(testCases)]


for case in range(testCases):
    string = strings[case]
    w = 1 # east is positive
    h = 1 # south is positive
    stack = [1]
    multiplier = 1

    for char in string:
        if(char.isnumeric()):
            stack.append(int(char))
            multiplier = multiplier*int(char)
        elif(char == ')'):
            multiplier = multiplier/stack[-1]
            stack.pop()
        elif(char.isalpha()):
            if(char == 'W'):
                w = w - 1*multiplier
            if(char == 'E'):
                w = w + 1*multiplier
            if(char == 'N'):
                h = h - 1*multiplier
            if(char == 'S'):
                h = h + 1*multiplier

    if(w<=0):
        w = 1000000000+w
    if(w>=1000000001):
        w = w - 1000000000

    if(h<=0):
        h = 1000000000+h
    if(h>=1000000001):
        h = h - 1000000000

    w = int(w)
    h = int(h)

    print('Case #' + str(case+1) + ': ' + str(w) + ' ' + str(h))
