# utf-8

def dict_gen (lst) :
    '''
    昇順にソートされた単語のリストを受け取ったら、
        "もとの正しい並びの単語" : "アルファベット順にソートされた単語"
    という辞書に直して返す 
    '''
    dict = {}
    for word in lst:
        word_abc = ''.join(sorted(word)) # ''.join(リスト) で、リスト内の文字列を''を連結子として連結できる
        dict[word] = word_abc # 辞書の最後に新しい要素が追加されていくので結果的に昇順になる
    return dict

def exact_match (str, lst):
    '''
    入力された文字を順にリストに格納したものと、単語リストを与えると、
    あたえられた文字が全て入っているような単語を作って返す
    '''
    dict = dict_gen(lst) # あたえられた単語リストを辞書に直す
    str_abc = ''.join(sorted(str))
    for key in dict:
        if str_abc == dict[key]:
            print('congrats! exact match for "' + str + '" is : '+ key)
            return key
    print('No perfect match for "' + str + '"...')
    return ''

# for test
tiny_list = sorted(['dog', 'cat', 'bear', 'rabbit', 'giraffe', 'camel'])

# use real dictionary
file = open('dictionary.txt', 'r')
dictionary = [word.rstrip() for word in file.readlines()] # 内包表記
file.close()


if __name__ == '__main__': 
    assert dict_gen(tiny_list) == {'bear': 'aber', 'camel': 'acelm', 'cat': 'act', 'dog': 'dgo', 'giraffe': 'aeffgir', 'rabbit':'abbirt'}
    assert exact_match('tac', tiny_list) == 'cat'
    assert exact_match('trabbi', tiny_list) == 'rabbit'
    assert exact_match('mlcae', dictionary) == 'camel'
    assert exact_match('moonstarer', dictionary) == 'astronomer'