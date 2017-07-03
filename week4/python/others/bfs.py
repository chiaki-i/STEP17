# 隣接リストをもとに幅優先探索をする
# 隣接リストは adj.py で作成する

import adj

def bfs(start, goal, lst):
    '''
    start と goal のページ番号を与えられたら、隣接リストから経路を求める
    '''
    q = [[start]]                        # 初期化
    answer = []
    path = []
    while not(len(q) == 0):        
        path = q.pop(0)                  # dequeue
        n = path[len(path) - 1]
        if n == goal:
            break
            # print(path)                  # 経路を表示
            answer.append(path)
        else:
            for x in lst[n]:
                if x not in path:
                    new_path = path[:] 
                    new_path.append(x) 
                    q.append(new_path)   # enqueue
    # print(path)
    return path

def search(start, goal, pages, links):
    '''
    ページの名前が与えられたら、pages でページ番号を調べて bfs で探索する
    '''
    (ans_start, ans_goal) = ('', '')
    for i in pages:
        if i[1] == start:
            ans_start = int(i[0])
        elif i[1] == goal:
            ans_goal = int(i[0])
    if ans_start == '':
        print('No such pages: ' + start + '\n' + 'Stop BFS.')
        exit(1)
    elif ans_goal == '':
        print('No such pages: ' + goal + '\n' + 'Stop BFS.')
        exit(1)
    else:
        answer = bfs(ans_start, ans_goal, links)
    return answer
    

if __name__ == '__main__':
    adjacent = [[1, 2],    # page 0
                [0, 2, 3], # page 1
                [0, 1, 4], # page 2
                [1, 4, 5], # page 3
                [2, 3, 6], # page 4
                [3],       # page 5
                [1]]       # page 6
    name = [['0', 'a'], ['1', 'p'], ['2', 'q'], ['3', 'r'],
            ['4', 's'], ['5', 't'], ['6', 'z']]
    
    assert bfs (0, 6, adjacent)             == [[0, 2, 4, 6],
                                                [0, 1, 2, 4, 6],
                                                [0, 1, 3, 4, 6],
                                                [0, 2, 1, 3, 4, 6]]
    assert bfs (1, 9, adjacent)             == []
    assert search('a', 'z', name, adjacent) == [[0, 2, 4, 6],
                                                [0, 1, 2, 4, 6],
                                                [0, 1, 3, 4, 6],
                                                [0, 2, 1, 3, 4, 6]]
    
    # search('b', 'z', name, adjacent)
    # No such pages: b. Stop BFS. と表示され終了する
    
    # use tiny data
    file1 = open('../../wiki/test-links.txt', 'r')
    links = []
    for line in file1:
        item = [int(i) for i in line[:-1].split('\t')]
        links.append(item)
    # print(links)
    file1.close()
    
    file2 = open('../../wiki/test-pages.txt', 'r')
    pages = []
    for line in file2:
        item = line[:-1].split('\t')
        pages.append(item)
    print(pages)
    file2.close()

    adjacent = adj.make_adj(links)
    test = search('a', 'b', pages, adjacent)

    
