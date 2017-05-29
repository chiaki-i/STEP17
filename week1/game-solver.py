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
        word_abc = (''.join(sorted(word))).lower()
        # ''.join(リスト) で、リスト内の文字列を''を連結子として連結できる
        dict[word] = word_abc
        # 辞書の最後に新しい要素が追加されていくので結果的に昇順になる
    return dict

def exact_match (string, lst):
    '''
    入力された文字を順にリストに格納したものと、単語リストを与えると、
    あたえられた文字が全て入っているような単語のうち、辞書で一番最初に見つかったものを返す
    入力された文字に空白が含まれていても無視する。
    '''
    dict = dict_gen(lst) # あたえられた単語リストを辞書に直す
    str_abc = (''.join(sorted(string))).replace(' ', '') # 空白も無視する
    for key in dict:
        if str_abc == dict[key]:
            print('congrats! exact match with "' + string + '" is '+ key)
            return key
    print('No perfect match with "' + string + '"...')
    return ''

# あたえられた文字の一部しか入っていない単語を作る
# 辞書ではなく、tree にして保存したい

# が、とりあえず一番賢くないやりかた

def partial_match (string, lst):
    # あたえられた文字列の全ての組み合わせのリスト combi をつくる
    dict = dict_gen(lst)
    str_abc = (''.join(sorted(string))).replace(' ', '')
    combi = []
    for i in range(3, len(str_abc)+1):
        combi.extend(list(itertools.combinations(str_abc, i)))
    combi = sorted(list(set([(''.join(x)) for x in combi])))

    # combi の全てを辞書と比較して、答えを answer に追加する
    answer = []
    for word in combi:
        for key in dict:
            if word == dict[key]:
                print((key + ' '), end='')
                answer.append(key)
    print()
    return sorted(answer)

def select_best (lst):
    '''
    部分一致の回答の string list を受け取ったら、その中で最もスコアの高いものを返す
    一応、一番長い単語も出力している。
    (まだ Qu については考えていない)
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
        pts = (pts+1) ^ 2 # bonus included
        return pts # 計算あってる？
    score_list = [[word, calc(word), len(word)] for word in lst]
    score_list.sort(key=lambda x:x[1])
    score_list.reverse()
    # print(score_list)
    best = score_list[0][0]
    print('BEST : ' + best + ', ' + str(calc(best)) + 'pts.')
    score_list.sort(key=lambda x:x[2])
    score_list.reverse()
    longest = score_list[0][0]
    print('LONGEST : ' + longest )
    return best


# for test
tiny_list = sorted(['dog', 'cat', 'bear', 'rabbit', 'giraffe', 'camel'])

# use real dictionary
file = open('dictionary.txt', 'r')
dictionary = [(word.rstrip()).lower() for word in file.readlines()] # 内包表記
file.close()

# use testdict 
file = open('testdict.txt', 'r')
testdict = [(word.rstrip()).lower() for word in file.readlines()] # 内包表記
file.close()

if __name__ == '__main__': 
    """
    assert dict_gen(tiny_list) == {'bear': 'aber', 'camel': 'acelm', 'cat': 'act', 'dog': 'dgo', 'giraffe': 'aeffgir', 'rabbit':'abbirt'}
    assert exact_match('tac', tiny_list)          == 'cat'
    assert exact_match('trabbi', tiny_list)       == 'rabbit'
    assert exact_match('mlcae', dictionary)       == 'camel' 
    assert exact_match('zzzzz', dictionary)       == ''      # Not_found
    assert exact_match('apple ', dictionary)      == 'apple' # with space
    assert exact_match('moon starer', dictionary) == 'astronomer'
    """
    # assert partial_match ('cdogat', tiny_list)    == ['cat', 'dog']
    select_best(partial_match ('mdbigarnayprfchz', dictionary))
    # assert select_best (tiny_list)                == 'giraffe'
