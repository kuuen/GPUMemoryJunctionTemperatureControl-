# coding: utf-8

import sys

def is_integer(n):
    try:
        float(n)
    except ValueError:
        return False
    else:
        return True

# 引数取得
args = sys.argv

powerLimit = 31

# 引数をうまく取得できない場合
if len(args) != 2 or is_integer(args[1]) == False :
  # 無条件で31にする
  powerLimit = 31
else :
  powerLimit = args[1]

file = open('C:/xxx/xxx/aaaa/PowerLimitValue.txt', 'w')
file.writelines(powerLimit)
#file.writelines('')
file.close()
