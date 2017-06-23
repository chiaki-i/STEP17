'''連番のページを探してくるプログラム'''

import re
import csv

def read_file(file):
    '''
    pages.txtの形式のファイルを読み込んで、ページのタイトルだけのリストを作る
    '''
    lst = []
    for line in file:
        pagename = (line[:-1].split('\t'))[1] # 1行読むと(num, pagename)となる
        lst.append(pagename)
    return lst

def judge_string(letters):
    '''
    文字列を受け取って、
    [非数字][数字][非数字][任意の文字列]
    という格好になっていれば、それを
    [数字より前][数字][数字よりあと] に分解する
    '''
    exp = (re.compile('[^0-9]+([0-9]+([^0-9]+.*))')).match(letters)
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
    collectionsにitem1, item2の組み合わせのものが含まれているかどうか調べる
    booleanを返す
    '''
    flag = False
    for elem in collections:
        if elem[0] == item1 and elem[1] == item2:
            flag = True
        else:
            continue
    return flag

def printlst(lst, string):
    '''リストを指定した場所(指定したファイル名、または標準出力)に書き出す'''
    if string == 'stdout':
        for item in lst:
            print(item)
    else:
        with open(string + '.txt', 'w') as file_out:
            writer = csv.writer(file_out)
            writer.writerows(lst)
    return None

def lst_sort(lst):
    '''
    collections の形をしたリストを受け取ったら、各要素内の番号のリストの長さが
    3以上のものに対して、長さの情報を付け加え、長い順に並べる
    '''
    result = []
    for item in lst:
        temp_len = len(item[2])
        if temp_len < 3:
            continue
        else:
            result.append([item[0], item[1], temp_len])
    result.sort(key=lambda x: x[2], reverse=True)
    return result

if __name__ == '__main__':
    # use tiny data (contains pagenames only)
    FILE = open('../wiki/serial.txt', 'r')
    SERIAL = [word.rstrip() for word in FILE.readlines()]
    FILE.close()
    print(SERIAL)
    LIST = judge_stringlist(SERIAL)
    COLLECTIONS = collect_serial(LIST)
    printlst(LIST, 'stdout')
    printlst(COLLECTIONS, 'stdout')

    # use 'pages.txt'
    # if you want to try tiny version, see '../wiki/test-pages-serial.txt'
    FILE = open('../wiki/pages.txt', 'r')
    SERIAL = read_file(FILE)
    FILE.close()
    LIST = judge_stringlist(SERIAL)
    COLLECTIONS = collect_serial(LIST)
    SORTED = lst_sort(COLLECTIONS)
    printlst(SORTED, 'sorted-result')

    # user input
    # exit program if 'q'
    while True:
        print('>>> ', end='')
        LINE = input()
        if LINE == 'q':
            print('bye')
            exit(1)
        else:
            print(judge_string(LINE))
