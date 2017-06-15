def readNumber(line, index):
    number = 0
    while index < len(line) and line[index].isdigit():
        number = number * 10 + int(line[index])
        index += 1
    if index < len(line) and line[index] == '.':
        index += 1
        keta = 0.1
        while index < len(line) and line[index].isdigit():
            number += int(line[index]) * keta
            keta *= 0.1
            index += 1
    token = {'type': 'NUMBER', 'number': number}
    return token, index

def readOperator(line, index, op):
    if op == 'PLUS':
        token = {'type': 'PLUS'}
    elif op == 'TIMES':
        token = {'type': 'TIMES'}
    elif op == 'MINUS':
        token = {'type': 'MINUS'}
    elif op == 'DIVIDE':
        token = {'type': 'DIVIDE'}
    elif op == 'L_PAREN':
        token = {'type': 'L_PAREN'}
    elif op == 'R_PAREN':
        token = {'type': 'R_PAREN'}
    else:
        print('unknown operator?') # unused pattern
        exit(1)
    return (token, index + 1)

def tokenize(line):
    tokens = []
    index = 0
    while index < len(line):
        if line[index].isdigit():
            (token, index) = readNumber(line, index)
        elif line[index] == '+':
            (token, index) = readOperator(line, index, 'PLUS')
        elif line[index] == '-':
            (token, index) = readOperator(line, index, 'MINUS')
        elif line[index] == '*':
            (token, index) = readOperator(line, index, 'TIMES')
        elif line[index] == '/':
            (token, index) = readOperator(line, index, 'DIVIDE')
        elif line[index] == '(':
            (token, index) = readOperator(line, index, 'L_PAREN')
        elif line[index] == ')':
            (token, index) = readOperator(line, index, 'R_PAREN')
        else:
            print ('Invalid character found: ' + line[index])
            exit(1)
        tokens.append(token)
    return tokens

def check_syntax (tokens):
    # parentheses
    index = 0
    flag_paren = 0
    while index < len(tokens):
        if tokens[index]['type'] == 'L_PAREN':
            flag_paren += 1
        elif tokens[index]['type'] == 'R_PAREN':
            flag_paren -= 1
        index += 1
    if flag_paren != 0:
        print('Invalid syntax : unmatched parentheses')
        exit(1)
    # numbers & operators
    flag_op = 0
    operators = ['PLUS', 'MINUS', 'TIMES', 'DIVIDE']
    if tokens[0]['type'] in ['PLUS', 'MINUS']:
        index = 1 
    else:
        index = 0
    while index < len(tokens): 
        if flag_op != 2 and flag_op != -1:
            if tokens[index]['type'] == 'NUMBER':
                flag_op += 1
            elif tokens[index]['type'] in operators:
                flag_op -= 1
        else:
            print('invalid syntax : operators in a row')
            exit(1)
        index += 1
    if flag_op != 1: # (the number of num) should be ((the number of operators) + 1)
        print('Invalid syntax : too many operators')
        exit(1)   

def is_times_divide_in (tokens):
    index = 0
    flag = False
    while index < len(tokens):
        if tokens[index]['type'] in ['TIMES', 'DIVIDE']:
            flag = True
        index += 1
    return flag

def eval_times_divide (tokens):
    tokens.insert(0, {'type': 'PLUS'}) # Insert a dummy '+' token
    while len(tokens) >= 3: # final form should be like [Sign, Number]
        index = 1
        if not (is_times_divide_in (tokens)): # finish if there are no '*'s or '/'s
            break
        while index < len(tokens):
            if tokens[index]['type'] == 'NUMBER' and index > 2:
                if tokens[index - 1]['type'] == 'PLUS':
                    tokens # skip!
                elif tokens[index - 1]['type'] == 'MINUS':
                    tokens # skip!
                elif tokens[index - 1]['type'] == 'TIMES':
                    tmp_ans = tokens[index - 2]['number'] * tokens[index]['number']
                    for x in range(3):
                        del tokens[index - 2]
                    tokens.insert(index - 2, {'type': 'NUMBER', 'number': tmp_ans})
                elif tokens[index - 1]['type'] == 'DIVIDE':
                    tmp_ans = tokens[index - 2]['number'] / tokens[index]['number']
                    for x in range(3):
                        del tokens[index - 2]
                    tokens.insert(index - 2, {'type': 'NUMBER', 'number': tmp_ans})
                else:
                    print ('Invalid syntax') # unused
            index += 1
            print(tokens)
    return tokens

def eval_plus_minus (tokens):
    while len(tokens) >= 3: # final form should be like [Sign, Number]
        index = 1
        while index < len(tokens):
            if tokens[index]['type'] == 'NUMBER' and index > 2:
                if tokens[index - 1]['type'] == 'PLUS':
                    tmp_ans = tokens[index - 2]['number'] + tokens[index]['number']
                    for x in range(3):
                        del tokens[index - 2]
                    tokens.insert(index - 2, {'type': 'NUMBER', 'number': tmp_ans})
                elif tokens[index - 1]['type'] == 'MINUS':
                    tmp_ans = tokens[index - 2]['number'] - tokens[index]['number']
                    for x in range(3):
                        del tokens[index - 2]
                    tokens.insert(index - 2, {'type': 'NUMBER', 'number': tmp_ans})
                else:
                    print ('Invalid syntax') # unused
                    exit(1)
            index += 1
            print(tokens)
    return tokens

while True:
    print ('> ', end='')
    line = input()
    tokens = tokenize(line)
    check_syntax(tokens)
    tokens = eval_times_divide(tokens)
    print('TIMES & DIVIDE HAS SUCCESSFULLY ENDED!')
    tokens = eval_plus_minus(tokens)
    print('PLUS & MINUS HAS SUCCESSFULLY ENDED! YAY!')
    # answer = evaluate(tokens)
    # print ('answer = %f\n' % answer)