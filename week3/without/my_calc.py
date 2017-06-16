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
    return tokens

def check_paren (tokens):
    '''
    左の括弧と右の括弧が対応しているか、括弧の数でチェックする。
    '''
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

def check_operators (tokens):
    '''
    括弧の含まれない tokens を受け取ってきたら、
        ・演算子が連続していないか
        ・式の最後に演算子が来ていないか
    をチェックする。正しければ tokens を返し、正しくなければ exit する。
    tokens は括弧が含まれていてはいけないので、eval_paren の中でだけ使われる。
    '''
    flag_op = 0
    operators = ['PLUS', 'MINUS', 'TIMES', 'DIVIDE']
    if tokens[0]['type'] in ['PLUS', 'MINUS']:
        index = 0
        tokens = remove_unary_operator_from(tokens)
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
    return tokens
    
def remove_unary_operator_from (tokens):
    '''
    単項演算子があったら、[符号, 数字]を[負の数字]に置き換えた tokens を返す
    '''
    if len(tokens) == 3 and tokens[1]['type'] in ['PLUS', 'MINUS']:
        del tokens[0]
    if tokens[1]['type'] != 'NUMBER': # unused pattern
        print('Invalid syntax : unary error') 
        exit(1)
    sign = 0
    if tokens[0]['type'] == 'PLUS':
        sign = 1
    elif tokens[0]['type'] == 'MINUS':
        sign = -1
    simple_number = tokens[1]['number'] * sign
    for i in range(2):
        del tokens[0]
    tokens.insert(0, {'type': 'NUMBER', 'number' : simple_number})
    # print(tokens)
    return tokens

def is_times_divide_in (tokens):
    index = 0
    flag = False
    while index < len(tokens):
        if tokens[index]['type'] in ['TIMES', 'DIVIDE']:
            flag = True
        index += 1
    return flag

def eval_times_divide (tokens):
    '''
    括弧も乗除算も含まない tokens について、和差算をしてその結果の tokens を返す
    '''
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
    '''
    [符号, 数字]の形になった tokens から、答えの数字を取り出す。
    '''
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
    return answer

def eval_plus_minus (tokens):
    '''
    括弧を含まない tokens を受け取ったら、和差算をスキップして乗除算だけ計算して tokens を返す。
    '''
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
    '''
    tokens 内に括弧がある場合、最も内側の括弧を計算して、括弧の部分をその計算結果で置き換える。
    これを、tokensから括弧がなくなるまで続け、なくなったら残りの計算をして、answer を返す。
    '''
    while True:
        if not (is_paren_in (tokens)): 
            break
        else:
            check_paren(tokens)
        start = 0
        end = 0
        for index in range(len(tokens)): # 一周するだけ
            if tokens[index]['type'] == 'LPAREN':
                start = index + 1 # after paren starts
                # print('start from ' + str(start))
            elif tokens[index]['type'] == 'RPAREN':
                if end == 0:
                    end = index - 1 # before paren ends
                else:
                    end
                # print('end ' + str(end))
        tmp = []
        for i in range(start, end + 1):
            tmp.append(tokens[i])
        tmp_ans = evaluate(tmp)
        for token in range(start - 1, end + 2):
            del tokens[start - 1]
        tokens.insert(start - 1, {'type': 'NUMBER', 'number': tmp_ans})
    answer = evaluate(tokens)
    return answer

def evaluate (tokens):
    '''
    括弧の含まれない tokens を計算し、答えを返す。
    '''
    check_operators(tokens)
    tokens.insert(0, {'type': 'PLUS'})
    tokens = eval_times_divide(tokens)
    tokens = eval_plus_minus(tokens)
    answer = pick_answer_from(tokens)
    return answer

def test(line, expectedAnswer):
    tokens = tokenize(line)
    actualAnswer = eval_paren(tokens)
    if abs(actualAnswer - expectedAnswer) < 1e-8:
        print ('PASS! (%s = %f)' % (line, expectedAnswer))
    else:
        print ('FAIL! (%s should be %f but was %f)' % (line, expectedAnswer, actualAnswer))


# Add more tests to this function :)
def runTest():
    print ('==== Test started! =====')
    # 単純な四則演算
    test('1+2', 3)
    test('1-3', -2)
    test('1*3', 3)
    test('4/5', 0.8)
    # 整数・小数混合
    test('1.0+2.1-3', 0.1)
    # 単項演算子
    test('-1', -1)
    test('(-100)', -100)
    test('+1', 1)
    test('(+3)', 3)
    # 括弧 (+ 単項演算子)
    test('(1+(2+(3+4)*2)*3)', 49)
    test('((-1)+2)*3', 3) 
    test('(1+(+2))', 3)
    # スペース
    test('(1 + (3 + 4) / 2) * 3', 13.5)
    print ('==== Test finished! ====')


runTest()

while True:
    print ('> ', end='')
    line = input()
    tokens = tokenize(line)
    answer = eval_paren(tokens)
    print ('answer = ' + str(answer))