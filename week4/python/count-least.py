# 被参照数が 0 ではないページの中で、もっとも被参照数が低いものを2つ選ぶ

import adj
import bfs

def pair_lst (lst):
    '''
    リストの各要素を(ページ番号, リンクのリストの長さ, リンクのリスト)の形にする
    (こうすれば、リストの順番を崩してもOK)
    '''
    counter = 0
    adj_lst = []
    for item in lst:
        pair = (counter, len(item), item)
        adj_lst.append(pair)
        counter += 1
    # print(adj_lst)
    print('adj_lst success!')
    return adj_lst

def choose_least (lst):
    lst = sorted(lst, key=lambda x:x[1], reverse=False)
    least = []
    booby = []
    # counter = 0
    for i in range(len(lst)+1):
        if lst[i][1] != 0: # はじめてリンクの長さが0ではなくなったら
            least = lst[i]
            booby = lst[i+1]
            break
    if least == []:
        print('Cannot find any linked pages.')
        exit(1)
    elif booby == []:
        print('Cannot find booby.')
        exit(1)
    else:
        print('least : page no.' + str(least[0]))
        print('booby : page no.' + str(booby[0]))
    return (least, booby)

if __name__ == '__main__':
    # use tiny data
    file1 = open('../wiki/links.txt', 'r')
    links = []
    for line in file1:
        item = [int(i) for i in line[:-1].split('\t')]
        links.append(item)
    # print(links)
    file1.close()
    
    file2 = open('../wiki/pages.txt', 'r')
    pages = []
    for line in file2:
        item = line[:-1].split('\t')
        pages.append(item)
    # print(pages)
    file2.close()
    '''
    assert adj.make_adj(links) == [[], [5, 4, 7], [3, 4, 6, 7, 8, 9],
                                   [1, 7], [2, 5, 6, 7], [1, 3, 4, 7],
                                   [2, 3, 4, 5, 7], [2, 4, 6, 8],
                                   [1], [3, 4, 5]]
    adj = [[], [5, 4, 7], [3, 4, 6, 7, 8, 9],
           [1, 7], [2, 5, 6, 7], [1, 3, 4, 7],
           [2, 3, 4, 5, 7], [2, 4, 6, 8], [1], [3, 4, 5]]
    new_adj = pair_lst(adj)
    choose_least(new_adj)
    '''
    adj.make_adj(links)
    print('make_adj success!')
