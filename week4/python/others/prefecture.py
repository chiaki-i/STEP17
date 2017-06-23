# 都道府県名のデータを使う
file = open('../wiki/prefecture.txt', 'r')
prefecture = [word.rstrip() for word in file.readlines()]
print(prefecture)

def is_digit_in (lst, dic):
    '''
    タイトルが数字を含んでいるかどうか
    '''
    return 0
    
if __name__ == '__main__':
    # use tiny data
    file1 = open('../wiki/test-links.txt', 'r')
    links = []
    for line in file1:
        item = [int(i) for i in line[:-1].split('\t')]
        links.append(item)
    # print(links)
    file1.close()
    
    file2 = open('../wiki/test-pages.txt', 'r')
    pages = []
    for line in file2:
        item = line[:-1].split('\t')
        pages.append(item)
    # print(pages)
    file2.close()
    
