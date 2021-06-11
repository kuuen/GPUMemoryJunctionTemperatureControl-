# coding: utf-8

import subprocess
import sys
import shutdownOs

# 限界温度
TMP_LIMIT = 80

# nvidiaInspector.exeがある場所を設定
nvidiaInspectorPath = "C:/Users/XXXX/Desktop/BBBBB/Nvidia_Inspector/nvidiaInspector.exe"

# 引数取得
args = sys.argv


#現在温度
temp = 0

print("args len " + str(len(args)))
print("args[1]" + args[1])

def is_integer(n):
    try:
        float(n)
    except ValueError:
        return False
    else:
        return True

# 引数をうまく取得できない場合
if len(args) != 2 or is_integer(args[1]) == False :
  # 無条件で110度にする
  temp = 110
else :
  temp = float(args[1])

print("temp = " + str(temp))

# GPUのPower
power = 0

try:
  # HWiNFO64のTotal GPU Powerで出力された内容を取得する
  f = open('C:/Users/XXXX/Desktop/BBBB/PowerLimitValue.txt', 'r')
  power = float(f.readline().replace(' /n', ''))

  print(power)
  
  if is_integer(power) == False:
    print("not int power")
    power = 30

except FileNotFoundError:
  # 取得できない場合30固定
  power = 30

print("power = " + str(power))

chengePower = power

if temp >= 110:
  # 110度の場合 マシンを落とすb
  shutdownOs.shutdown(["", "MemoryJunction", args[1]])
  quit()
# 温度が限界を超えている場合
elif temp >= TMP_LIMIT:
  # Powerを下げる
  chengePower = power - 3
  print("chengePower = power - 3")

# 温度に余裕がある場合 max 70%
elif temp <= (TMP_LIMIT - 3) and power <= 70:
  # Powerを上げる
  chengePower = power + 3
  print("chengePower = power + 3")
else :
  print("何もしない")

# PowerLimitを変更するかの判断
if chengePower != power:
  # Powerの変更
  #setMemoryClockOffset=メモリクロック, 
  #setPowerTarget=power limit 
  #setTempTarget=温度上限
  #setBaseClockOffset=コアクロック
  #setFanSpeed=ファンスピード(制御できず、変わらない)
  subprocess.call([nvidiaInspectorPath, "-setBaseClockOffset:0,0,-200", "-setMemoryClockOffset:0,0,990" ,"-setPowerTarget:0,%d" % (chengePower), "-setTempTarget:0,0,65"])

#  file = open("C:/Users/XXXX/Desktop/BBBB/PowerLimitValue.txt", "w", encoding = "utf_8")
#  file.writelines(str(chengePower))
##  file.writelines('')

#  print("-setPowerTarget:0,%d" % (chengePower))


