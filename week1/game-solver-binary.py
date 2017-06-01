# utf-8
import itertools

def dict_list_gen (lst):
    '''
    昇順にソートされた単語のリストを受け取ったら、
        [元の正しい並びの単語, アルファベット順にソートされた単語]
    というリストのリストにして返す
    '''
    dict = []
    dict = [[word, (''.join(sorted(word))).lower()] for word in lst]
    return dict

def all_combinations (string):
    '''
    文字列 string を与えられると、string に含まれる文字の全ての3文字以上の組み合わせを考える。
    string に q が含まれているならば、u も追加しておく。
    (なぜなら、q を含む単語は、必ず qu という形で出現するから。)
    '''
    if 'q' in string:
        flag = True
    else:
        flag = False
    combi = []
    for i in range(3, len(string)+1): # 3文字以下は考えない
        combi.extend(itertools.combinations(string, i))
        combi = [list(x) for x in combi] # tuple : immutable
        if flag:
            for x in combi:
                if 'q' in x:
                    x.remove('q')
                    x.append('tmp')
            for x in combi:
                if 'tmp' in x:
                    x.remove('tmp')
                    x.append('q')
                    x.append('u')
    combi = [sorted(x) for x in combi]
    # 一旦setにしてlistにすることで重複を削除
    combi = list(set([''.join(x) for x in combi])) 
    return combi

def binary_search(dict, combi):
    '''
    辞書 dict と 文字列のリスト lst を与えられると、
    文字列リストの全ての要素が dict と一致するか二分探索を用いて探す。
    '''
    answer = []
    for target in combi:
        target = (''.join(sorted(target))).replace(' ', '')
        low = 0
        high = len(dict) - 1
        flag = True
        while low <= high and flag:
            mid = (low + high) // 2
            if dict[mid][1] == target:
                answer.append(dict[mid][0])
                # print(dict[mid][0] + ' ', end='')
                flag = False
            elif dict[mid][1] < target:
                low = mid + 1
            else:
                high = mid - 1
    if answer != []:
        for i in answer:
            print(i + ' ', end='')
        print('')
    else: print('Not Found.')
    return answer

def partial_match_dict_list (string, lst):
    '''
    文字列 string と、単語のリスト lst (string list 型)が与えられると、
    string に含まれる文字からなる
    '''
    dict = dict_list_gen(lst)
    dict.sort(key=lambda x: x[1])
    str_abc = (''.join(sorted(string))).replace(' ', '')
    combi = all_combinations(str_abc)
    answer = binary_search(dict, combi)
    return sorted(answer)

def select_best (lst):
    '''
    部分一致の回答 lst (string list 型) を受け取ったら、その中で最もスコアの高いものを返す。
    スコアが高い単語と一番長い単語は一致しないこともある。
    '''
    two = ['c', 'f', 'h', 'l', 'm', 'p', 'v', 'w', 'y']
    three = ['j', 'k', 'q', 'x', 'z']
    def pts_data (x):
        if x in three: return 3
        elif x in two: return 2
        else : return 1
    def calc (word):
        pts = 0
        for i in sorted(word):
            pts = pts + pts_data(i)
        pts = (pts + 1) ** 2 # bonus included
        return pts
    score_list = [[word, calc(word), len(word)] for word in lst]
    score_list.sort(key=lambda x:x[1])
    score_list.reverse()
    best = score_list[0][0]
    print('BEST : ' + best + ', ' + str(calc(best)) + 'pts.')
    score_list.sort(key=lambda x:x[2])
    score_list.reverse()
    longest = score_list[0][0]
    print('LONGEST : ' + longest )
    return best

# for test
tiny_list      = sorted(['ant', 'cat', 'dog', 'bear', 'rabbit', 'giraffe', 'camel'])
tiny_dict      = {'bear': 'aber', 'camel': 'acelm', 'cat': 'act', 'dog': 'dgo', 'giraffe': 'aeffgir', 'rabbit':'abbirt'}
u_and_q        = sorted(['queen', 'Ukraine', 'quantum', 'vacuum', 'quit'])

# use real dictionary
file = open('dictionary.txt', 'r')
dictionary = [(word.rstrip()).lower() for word in file.readlines()] 
file.close()

# use small dictionary
file = open('testdict.txt', 'r')
testdict = [(word.rstrip()).lower() for word in file.readlines()]
file.close()

if __name__ == '__main__':   
    assert select_best (tiny_list)                == 'giraffe'
    assert partial_match_dict_list('rabbit', tiny_list)                          == ['rabbit']
    assert partial_match_dict_list('dog', tiny_dict)                             == ['dog']
    assert partial_match_dict_list('qeen', u_and_q)                              == ['queen']
    assert select_best(partial_match_dict_list ('mdbigarnayprfchz', dictionary)) == 'pharmacy'


while __name__ == '__main__':
    line = input('enter your input >>> ')
    select_best(partial_match_dict_list(line, dictionary))