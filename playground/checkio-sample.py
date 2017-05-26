# coding utf-8

# 4.13 復習課題
########################
# 4-1
# 変数 guess_me に 7 を代入し、guess_me が 7 よりも小さければ 'too low'
#                                               大きければ 'too high'
#                                               等しければ 'just right
# と表示する条件テストを書く。
########################
'''
def make_a_guess ():
    guess_me = input().rstrip().
    if guess_me < 7:
        print ('too low')
    elif guess_me < 7: 
        print ('too high')
    else :
        print('just right')
make_a_guess ()
'''
dic = {"1000":'M', "900":"CM", "500":'D', "400":"CD", "100":'C', "90":"XC", "50":'L', "40":"XL", "10":'X', "9":"IX", "5":'V', "4":"IV", "1":'I'}
def checkio(data):
    lst = list(str(data))
    place = 0
    string = ''
    for i in lst:
        if   int(i) == 4: 
            if len(lst) - place == 1:
                string += dic["4"]
            elif len(lst) - place == 2:
                string += dic["40"]
            elif len(lst) - place == 3:
                string += dic["400"]
            else:
                print("ERROR: CASE 4.")
                return 0
        elif int(i) == 9:
            if len(lst) - place == 1:
                string += dic["9"]
            elif len(lst) - place == 2:
                string += dic["90"]
            elif len(lst) - place == 3:
                string += dic["900"]
            else:
                print("ERROR: CASE 9.")
                return 0
        elif int(i) >= 5: # q = 5,6,7,8
            if len(lst) - place == 1:
                string += dic["5"]
            elif len(lst) - place == 2:
                string += dic["50"]
            elif len(lst) - place == 3:
                string += dic["500"]
            else:
                print("ERROR: CASE 5.")
                return 0
            i = str(int(i) - 5)
        if int(i) == 1 or int(i) == 2 or int(i) == 3:             # q = 1,2,3
            for _ in range(int(i)):
                if len(lst) - place == 1:
                    string += dic["1"]
                elif len(lst) - place == 2:
                    string += dic["10"]
                elif len(lst) - place == 3:
                    string += dic["100"]
                elif len(lst) - place == 4:
                    string += dic["1000"]
                else:
                    print("ERROR: CASE 1.")
                    return 0
        place += 1
    print(string)
    return string

def checkio2(words):
    ''' checkio2 は、スペースで区切られた単語数を数え、3語ならtrueを返す'''
    lst = words.split(" ")
    counter = 0
    for item in lst:
        if item.isdigit() == True: # こういうのは docstring に
            counter = 0
        else:
            counter += 1
        if counter >= 3:
            print(True)
            return True
    print(False)
    return False

# assert 文の基本的な使い方は、プログラムの任意の場所に
#「その場所で成立していることが期待される条件式」を記述するというものです。
# メッセージは省略することができます。
#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    # コマンド実行すると、__name__ に __main__ が代入されるため、その時だけ以下が実行される
    # import など、そうでない場合には実行されない
    assert checkio(6) == 'VI', '6'
    assert checkio(76) == 'LXXVI', '76'
    assert checkio(499) == 'CDXCIX', '499'
    assert checkio(3888) == 'MMMDCCCLXXXVIII', '3888'
    assert checkio2("Hello World hello") == True, "Hello"
    assert checkio2("He is 123 man") == False, "123 man"
    assert checkio2("1 2 3 4") == False, "Digits"
    assert checkio2("bla bla bla bla") == True, "Bla Bla"
    assert checkio2("Hi") == False, "Hi"


