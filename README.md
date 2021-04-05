# GPUMemoryJunctionTemperatureControl-
GDDR6Xのメモリジャンクション温度の制御

## 用途
Nvidia GeForce RTX 3080,3090のMemoryJunctionTemperatureの値を制御する  
温度が設定温度以上に達するとPOWER LIMITの値を下げる。温度に余裕がある場合はPOWER LIMITの値を上げる

## 必要条件
Windows10,  [HWiNFO64](https://www.hwinfo.com/),[nvidiaInspector](https://www.nvidiainspector.com/),python3

## インストール
### pythonファイルの編集
powerLimitControl.py

MemoryJunctionTemperatureの上限値を設定
```
TMP_LIMIT = 95
```
nvidiaInspectorのインストール場所を指定
```
nvidiaInspectorPath = "C:/xxx/xxx/xxxx/Nvidia_Inspector/nvidiaInspector.exe"
```
PowerLimitValue.txtの場所を指定
```
PowerLimitValuePath = "C:/xxx/xxx/aaaa/PowerLimitValue.txt"
```
nvidiaInspectorコマンド発行
```
subprocess.call([nvidiaInspectorPath, "-setBaseClockOffset:0,0,-200", "-setMemoryClockOffset:0,0,990" ,"-setPowerTarget:0,%d" % (chengePower), "-setTempTarget:0,0,65"])
```
