# utf-8
import itertools

def dict_gen (lst) :
    '''
    昇順にソートされた単語のリストを受け取ったら、
        "もとの正しい並びの単語" : "アルファベット順にソートされた単語"
    という辞書に直して返す 
    '''
    dict = {}
    for word in lst:
        # ''.join(リスト) で、リスト内の文字列を''を連結子として連結できる
        word_abc = (''.join(sorted(word))).lower()
        dict[word] = word_abc
        # 辞書の最後に新しい要素が追加されていくので結果的に昇順になる
    return dict

def exact_match (string, lst):
    '''
    入力された文字を順にリストに格納したものと、単語リストを与えると、
    あたえられた文字が全て入っているような単語のうち、辞書で一番最初に見つかったものを返す
    入力された文字に空白が含まれていても無視する。
    '''
    dict = dict_gen(lst)
    str_abc = (''.join(sorted(string))).replace(' ', '')
    for key in dict:
        if str_abc == dict[key]:
            print('congrats! exact match with "' + string + '" is '+ key)
            return key
    print('No perfect match with "' + string + '"...')
    return ''

def unwise_search (dict, combi):
    '''
    辞書 dict と 文字列のリスト combi を与えられると、
    文字列リストの全ての要素が dict と一致するか全て試す。
    '''
    answer = []
    for word in combi:
        for key in dict:
            if word == dict[key]:
                print((key + ' '), end='')
                answer.append(key)
    print()
    return answer

def partial_match (string, lst):
    '''
    文字列 string と、単語のリスト lst (string list 型)が与えられると、
    string に含まれる文字からなる
    '''
    dict = dict_gen(lst)
    str_abc = (''.join(sorted(string))).replace(' ', '')
    combi = all_combinations(str_abc)
    answer = unwise_search(dict, combi)
    return sorted(answer)

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
tiny_list = sorted(['dog', 'cat', 'bear', 'rabbit', 'giraffe', 'camel'])
u_and_q   = sorted(['queen', 'Ukraine', 'quantum', 'vacuum', 'quit'])

# use real dictionary
file = open('dictionary.txt', 'r')
dictionary = [(word.rstrip()).lower() for word in file.readlines()] 
file.close()

# use small dictionary
file = open('testdict.txt', 'r')
testdict = [(word.rstrip()).lower() for word in file.readlines()]
file.close()

if __name__ == '__main__': 
    assert dict_gen(tiny_list) == {'bear': 'aber', 'camel': 'acelm', 'cat': 'act', 'dog': 'dgo', 'giraffe': 'aeffgir', 'rabbit':'abbirt'}
    assert exact_match('tac', tiny_list)          == 'cat'
    assert exact_match('trabbi', tiny_list)       == 'rabbit'
    assert exact_match('mlcae', dictionary)       == 'camel' 
    assert exact_match('zzzzz', dictionary)       == ''      # Not_found
    assert exact_match('apple ', dictionary)      == 'apple' # with space
    assert exact_match('moon starer', dictionary) == 'astronomer' #with space
    assert partial_match ('cdogat', tiny_list)    == ['cat', 'dog']
    assert partial_match ('qeen', u_and_q)        == ['queen']   # e < n < q < u
    assert partial_match ('qkraine', u_and_q)     == []          # cannot use u
    assert partial_match('qantum', u_and_q)       == ['quantum'] # q < t < u (double/redundancy) 
    assert partial_match ('qit', u_and_q)         == ['quit']    # q < t < u (single)
    # assert calc('cat') == 25
    # assert calc('garden') == 49   
    assert select_best (tiny_list)                == 'giraffe'
    assert select_best(partial_match('mdbigarn', dictionary))          == 'bridgman'
    # select_best(partial_match ('mdbigarnayprfchz', dictionary))

