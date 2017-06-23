# pages.txt の形式のファイルを読み込み、隣接リストを作る
# pages.txt はページ順に並んでいることを想定している

def make_adj(lst):
    n = lst[-1][0]     # lst の一番最後の要素のページ番号
    adjacent = []
    for i in range(n+1):
        print(i)
        links = []
        counter = 0
        for item in lst:
            if item[0] == i:
                links.append(item[1])
            elif item[0] == (i+1):
                break
            counter += 1
        # print(lst[counter])
        adjacent.append(links)
    # print(adjacent)
    return adjacent

if __name__ == '__main__':
    # use tiny data
    file1 = open('../wiki/test-links.txt', 'r')
    # file1 = open('../wiki/links.txt', 'r') # huge!
    links = []
    for line in file1:
        item = [int(i) for i in line[:-1].split('\t')]
        links.append(item)
    print(links)
    file1.close()
    print('file1 closed.')
    
    file2 = open('../wiki/test-pages.txt', 'r')
    # file2 = open('../wiki/pages.txt', 'r') # huge!
    pages = []
    for line in file2:
        item = line[:-1].split('\t')
        pages.append(item)
    print(pages)
    file2.close()
    print('file2 closed.')
    
    assert make_adj(links) == [[], [5, 4, 7], [3, 4, 6, 7, 8, 9],
                               [1, 7], [2, 5, 6, 7], [1, 3, 4, 7],
                               [2, 3, 4, 5, 7], [2, 4, 6, 8], [1], [3, 4, 5]]

