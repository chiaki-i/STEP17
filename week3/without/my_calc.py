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
    elif op == 'LPAREN':
        token = {'type': 'LPAREN'}
    elif op == 'RPAREN':
        token = {'type': 'RPAREN'}
    else:
        print('unknown operator?') # unused pattern
        exit(1)
    return (token, index + 1)

def tokenize(line):
    tokens = []
    index = 0
    while index < len(line):
        if line[index] == ' ':
            index += 1
            continue # skip spaces
        elif line[index].isdigit():
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
            (token, index) = readOperator(line, index, 'LPAREN')
        elif line[index] == ')':
            (token, index) = readOperator(line, index, 'RPAREN')
        else:
            print ('Invalid character found: ' + line[index])
            exit(1)
        tokens.append(token)
    print(tokens)
    return tokens

def check_syntax (tokens):
    # parentheses
    index = 0
    flag_paren = 0
    while index < len(tokens):
        if tokens[index]['type'] == 'LPAREN':
            flag_paren += 1
        elif tokens[index]['type'] == 'RPAREN':
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
    return tokens

def is_paren_in (tokens):
    index = 0
    flag = False
    while index < len(tokens):
        if tokens[index]['type'] in ['LPAREN', 'RPAREN']:
            flag = True
        index += 1
    return flag

def pick_answer_from (tokens):
    answer = 0
    sign = 0
    if len(tokens) == 2:
        if tokens[0]['type'] == 'PLUS':
            sign = 1
        elif tokens[0]['type'] == 'MINUS':
            sign = -1
        answer = sign * tokens[1]['number']
    elif len(tokens) == 1 and tokens[0]['type'] == 'NUMBER':
        answer = tokens[0]['number']
    else: 
        print('too many tokens!')
        exit(1)
    print(answer)
    return answer

def eval_plus_minus (tokens):
    while len(tokens) >= 3: # final form should be like [Sign, Number]
        index = 1
        if len(tokens) == 3 and tokens[1]['type'] in ['PLUS', 'MINUS']:
            del tokens[0]
            break
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
    return tokens

def eval_paren (tokens):
    tokens.insert(0, {'type': 'PLUS'}) # Insert a dummy '+' token
    while True:
        if not (is_paren_in (tokens)): 
            # print('no parentheses.')
            break
        start = 0
        end = 0
        for index in range(len(tokens)): # 一周するだけ
            if tokens[index]['type'] == 'LPAREN':
                start = index + 1 # after paren starts
                print('start from ' + str(start))
            elif tokens[index]['type'] == 'RPAREN':
                if end == 0:
                    end = index - 1 # before paren ends
                else:
                    end
                print('end ' + str(end))
        tmp = []
        for i in range(start, end + 1):
            tmp.append(tokens[i])
        tmp.insert(0, {'type': 'PLUS'})
        tmp = eval_times_divide(tmp)
        tmp = eval_plus_minus(tmp)
        tmp_ans = pick_answer_from(tmp)
        for token in range(start - 1, end + 2):
            del tokens[start - 1]
        tokens.insert(start - 1, {'type': 'NUMBER', 'number': tmp_ans})
    return tokens

def evaluate (tokens):
    check_syntax(tokens)

    tokens = eval_paren(tokens)
    # print('===== PARENTHESES DISSAPEARED! =====')
    # print(tokens)

    tokens = eval_times_divide(tokens)
    # print('===== TIMES & DIVIDE SUCCEEDED! ====')
    # print(tokens)

    tokens = eval_plus_minus(tokens)
    # print('===== PLUS & MINUS SUCCEEDED! ======')
    # print(tokens)

    answer = pick_answer_from(tokens)
    return answer

def test(line, expectedAnswer):
    tokens = tokenize(line)
    actualAnswer = evaluate(tokens)
    if abs(actualAnswer - expectedAnswer) < 1e-8:
        print ('PASS! (%s = %f)' % (line, expectedAnswer))
    else:
        print ('FAIL! (%s should be %f but was %f)' % (line, expectedAnswer, actualAnswer))


# Add more tests to this function :)
def runTest():
    print ('==== Test started! =====')
    test('1+2', 3)
    test('1.0+2.1-3', 0.1)
    print ('==== Test finished! ====')


runTest()
while True:
    print ('> ', end='')
    line = input()
    tokens = tokenize(line)
    answer = evaluate(tokens)
    print ('answer = ' + str(answer))