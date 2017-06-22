'''続き物を探してくるプログラム'''

import re

def judge_string(letters):
    '''
    文字列を受け取って、
    [任意の文字列][非数字][数字][非数字][任意の文字列]
    という格好になっていれば、それを
    [数字より前][数字][数字よりあと] に分解する
    '''
    exp = (re.compile('.*[^0-9]+([0-9]+([^0-9]+.*))')).match(letters)
    if exp is None:        # None との比較には is を使う
        answer = []
    else:
        third = exp.group(2)
        second = re.sub(third, '', exp.group(1))
        first = re.sub(exp.group(1), '', exp.group(0))
        answer = [first, second, third]
    return answer

def judge_stringlist(lst):
    '''
    リストの各要素に対して judge_string をおこなう
    judge_stringに通ったものだけを集めたリストを作って返す
    '''
    result = []
    for item in lst:
        temp = judge_string(item)
        if temp == []:
            continue
        else:
            result.append(temp)
    return result

def collect_serial(lst):
    '''
    [[first, second, third] ...]の形をしているリスト
    続き物を発見したら、リストに入れる
    '''
    collections = []
    for item in lst:
        temp0 = item[0]
        temp2 = item[2]
        if not is_in_collections(collections, temp0, temp2):
            collections.append([temp0, temp2, []])
            for elem in lst:
                if elem[0] == temp0 and elem[2] == temp2:
                    (collections[-1][2]).append(elem[1])
                else:
                    continue
    return collections

def is_in_collections(collections, item1, item2):
    '''
    collectionsにitem1, item2の組み合わせのものがすでに含まれているかどうか調べる
    booleanを返す
    '''
    flag = False
    for elem in collections:
        if elem[0] == item1 and elem[1] == item2:
            flag = True
        else:
            continue
    return flag

def printlst(lst):
    '''ただprintするだけ'''
    for item in lst:
        print(item)
    return None

if __name__ == '__main__':
    FILE = open('../wiki/serial.txt', 'r')
    SERIAL = [word.rstrip() for word in FILE.readlines()]
    print(SERIAL)
    LIST = judge_stringlist(SERIAL)
    COLLECTIONS = collect_serial(LIST)
    printlst(LIST)
    printlst(COLLECTIONS)
    while True:
        print('>>> ', end='')
        LINE = input()
        if LINE is 'q':
            print('bye')
            exit(1)
        else:
            print(judge_string(LINE))
