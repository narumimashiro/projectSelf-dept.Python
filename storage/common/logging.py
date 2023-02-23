# for DebugLog

# 出力文字色を変更する
RED = '\033[30m'
GREEN = '\033[32m'
YELLOW = '\033[33m'
COLOREND = '\033[0m'


def LOG_ASSERT(errorLog):
    print(RED, 'Error : ', errorLog, COLOREND)
    b 
def LOG_WARNING(warningLog):
    print(YELLOW, 'Warning : ', warningLog, COLOREND)
    
def LOG_INFO(infoLog):
    print(GREEN, 'Infomation : ', infoLog, COLOREND)