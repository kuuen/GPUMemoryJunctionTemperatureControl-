# coding: utf-8

import subprocess
import sys

# 限界温度
TMP_LIMIT = 95

# nvidiaInspector.exeがある場所を設定
nvidiaInspectorPath = "C:/xxx/xxx/xxxx/Nvidia_Inspector/nvidiaInspector.exe"

PowerLimitValuePath = "C:/xxx/xxx/aaaa/PowerLimitValue.txt"

# 引数取得
args = sys.argv

#現在温度
temp = 0

def is_integer(n):
    try:
        float(n)
    except ValueError:
        return False
    else:
        return True

# 引数をうまく取得できない場合
if len(args) != 2 or is_integer(args[1]) == False :
  # 無条件で99度にする
  temp = 99
else :
  temp = float(args[1])

# GPUのPower
power = 0

try:
  # HWiNFO64のTotal GPU Powerで出力された内容を取得する
  f = open(PowerLimitValuePath, 'r')
  power = float(f.readline().replace(' /n', ''))

  
  if is_integer(power) == False:
    print("not int power")
    power = 30

except FileNotFoundError:
  # 取得できない場合30固定
  power = 30

chengePower = power
# 温度が限界を超えている場合
if temp >= TMP_LIMIT:
  # Powerを下げる
  chengePower = power - 3

# 温度に余裕がある場合
elif temp <= (TMP_LIMIT - 5):
  # Powerを上げる
  chengePower = power + 3

# PowerLimitを変更するかの判断
if chengePower != power:
  # Powerの変更
  #setMemoryClockOffset=メモリクロック, 
  #setPowerTarget=power limit 
  #setTempTarget=温度上限
  #setBaseClockOffset=コアクロック
  #setFanSpeed=ファンスピード(制御できず、変わらない)
  subprocess.call([nvidiaInspectorPath, "-setBaseClockOffset:0,0,-200", "-setMemoryClockOffset:0,0,990" ,"-setPowerTarget:0,%d" % (chengePower), "-setTempTarget:0,0,65"])

  file = open("C:/Users/arata/Desktop/0402/PowerLimitValue.txt", "w", encoding = "utf_8")
  file.writelines(str(chengePower))

