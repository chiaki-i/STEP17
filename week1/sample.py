# 木構造のプログラム http://www.geocities.jp/m_hiroi/light/pyalgo03.html
# graphviz の話 http://qiita.com/shimo_t/items/b761973805f2cf0b2967

from graphviz import Digraph

class Node:
    def __init__(self, str):
        '''
        left が左側の子、right が右側の子を表す
        子を持たない場合は、連結リストと同様に None をセットする
        '''
        self.data  = str
        self.left  = None
        self.right = None

# 大文字小文字の区別?
# とりあえず小文字だけ考えている
two = ['c', 'f', 'h', 'l', 'm', 'p', 'v', 'w', 'y']
three = ['j', 'k', 'q', 'x', 'z']
def pts(x):
    if x in three: return 3
    elif x in two: return 2
    else : return 1

def search(node, str):
    while node:
        if node.data == str: return True
        if str < node.data:
            node = node.left
        else:
            node = node.right
    return False

def insert(node, str):
    if node is None: return Node(str)
    elif str == node.data: return node
    elif str < node.data:
        node.left = insert(node.left, str)
    else:
        node.right = insert(node.right, str)
    return node

def insert_abc(node, str):
    for i in list(str.replace(' ', '')):
        if node is None: node = Node(i)
        elif i == node.data: node
        elif i < node.data:
            node.left = insert(node.left, i)
        else:
            node.right = insert(node.right, i)
    return node

def insert_lst(node, lst):
    for word in lst:
        node = insert_abc(node, word)
    return node

def traverse(func, node):
    '''Tree.mapだと思っていい'''
    if node:
        traverse(func, node.left)
        func(node.data)
        traverse(func, node.right)

if __name__ == '__main__' :
    # sample tree
    print('-------tree0-------')
    tree0 = None
    tree0 = insert(tree0, 'bear')
    tree0 = insert(tree0, 'apple')
    tree0 = insert(tree0, 'cat')
    print(tree0.right.data)
    print(tree0.left.data)  
    print(tree0.data)  
    #            bear
    #            /  \
    #        apple  cat

    # small test
    print('-------tree1-------')
    tree1 = None 
    tree1 = insert_abc(tree1, 'be ar')
    print(tree1.data)
    print(tree1.right.data)
    print(tree1.right.right.data)
    print(tree1.left.data)  
    #        b       
    #       / \
    #      a   e
    #           \
    #            r

    # use testdict
    print('-------tree2-------')
    file = open('testdict.txt', 'r')
    dictionary = [word.rstrip().lower() for word in file.readlines()] # 内包表記
    # print(dictionary)
    file.close()

    tree2 = None
    tree2 = insert_lst(tree2, dictionary)
    print('top : ' + tree2.data)
    print('r   : ' + tree2.right.data)
    print('r-r : ' + tree2.right.right.data)
    print('r-l : ' + tree2.right.left.data)
    print('l   : ' + tree2.left.data)
    print('l-r : ' + tree2.left.right.data)
    print('l-l : ' + tree2.left.left.data)
    # moon,bear, ...
    #            m
    #          /   \
    #         b     o
    #        / \   / \
    #       a   e n   r




