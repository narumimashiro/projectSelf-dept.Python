# collect list and create unique list

# input function example
# str = input('enter : ')

# white True:
#     ans = input('')
#         if ans == "yes";

# f = open('filename.txt', "a", encoding='UTF-8')
# f.write('string')
# f.writelines('list')
# f.close()

# os.path.isfile(path)

# from dir import file

import os
import logging

# 入力データ定義
FILENAME = ''
OUTPUTFILENAME = 'output.txt'
KEYWORD = 'temp'

def isFileExist(path):
    return os.path.isfile(path)

def writeFile(wDataList):
    with open(OUTPUTFILENAME, 'a', encoding='UTF-8') as f:
        for word in wDataList:
            f.write(f'{word}\n')
        f.close()
        
def getList():
    with open(FILENAME) as f:
        readLine = f.readlines()
        pickUpLineList = [line for line in readLine if KEYWORD in line]
        deleteSpaceList = [line.split() for line in pickUpLineList]
        connectList = [''.join(word) for word in deleteSpaceList]
        preList = [line.replace(KEYWORD, f' {KEYWORD} ').split() for line in connectList]
        return [word[word.index(KEYWORD)+1] for word in preList]


# Main
while True:
    ans = input("Input enter text file name : ")
    FILENAME = f'./{ans}.txt' # 入力されたファイル名を定数に格納する
    if not isFileExist(FILENAME):
        print(FILENAME)
       # LOG_ASSERT('file not exist')
       # LOG_ASSERT('please check input file name')
    else:
        break
        
#LOG_INFO('start creating unique list')

getlist = getList()
# print(getlist) # fore debug
uniqueList = list(set(getlist))

writeFile(uniqueList)
  
print('Fin.')
    
# LOG_INFO('Fin.')