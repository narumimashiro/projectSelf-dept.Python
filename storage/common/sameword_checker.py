# 特定のKeywordの後ろに付く単語に同名がないかチェックしたい場面があった。

import collections

# 出力文字色を変更する
GREEN = '\033[32m'
COLOREND = '\033[0m'

KEYWORD = 'keyword'

def getCheckList(path):
    with open(path) as f:
        # ファイルを1行ずつ読み込む
        read_lines = f.readlines()
        # keywordの単語が入っている行だけ取り出す
        lines = [line for line in read_lines if KEYWORD in line]
        # 単語で分割する
        words = [word.replace(KEYWORD, f' {KEYWORD} ').split() for word in lines]
        # keywordの次の単語だけを配列にまとめる
        check_list = [word[word.index(KEYWORD)+1] for word in words]
        return check_list

def isExistSameWord(check_list):
    # 集合型に変換して同じ要素を排除し、ユニークなリストを生成する
    uni_list = list(set(check_list))
    # 長さが違うときは同名要素が存在している
    return len(uni_list) != len(check_list)

def outputSameWord(word_list):
    # 要素をkey、その要素数をvalueに整形し、valueが1より多いものをリストアップ
    same_list = [key for key, value in collections.Counter(word_list).items() if value > 1]
    for word in same_list:
        print(GREEN,'same word exist : ',COLOREND, word)

# main
print('Check Start')
check_list = getCheckList('sample.txt')
if isExistSameWord(check_list):
    outputSameWord(check_list)

print('Fin.')