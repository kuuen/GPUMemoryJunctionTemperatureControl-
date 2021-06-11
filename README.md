# GPUMemoryJunctionTemperatureControl-
GDDR6Xのメモリジャンクション温度の制御

## 用途
Nvidia GeForce RTX 3080,3090のMemory Junction Temperatureの値を制御する  
温度が設定温度以上に達するとPOWER LIMITの値を下げる。温度に余裕がある場合はPOWER LIMITの値を上げる

## 必要条件
Windows10,  以下のインストール.[HWiNFO64](https://www.hwinfo.com/),[nvidiaInspector](https://www.nvidiainspector.com/),python3

## インストール
### pythonファイルの編集
powerLimitControl.py

MemoryJunctionTemperatureの上限値(℃)を設定
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
各パラメータを設定。省略するとオーバークロック値がクリアされる（CoreClock、MemoryClockが0設定となる）  
setBaseClockOffset=コアクロック(例では-200MHz)  
setMemoryClockOffset=メモリクロック(例では990MHz)  
setTempTarget=温度上限(例では65℃)  
```
subprocess.call([nvidiaInspectorPath, "-setBaseClockOffset:0,0,-200", "-setMemoryClockOffset:0,0,990" ,"-setPowerTarget:0,%d" % (chengePower), "-setTempTarget:0,0,65"])
```


savePowerLimitValue.py
PowerLimitValue.txtの場所を指定
```
file = open('C:/xxx/xxx/aaaa/PowerLimitValue.txt', 'w')
```
### HWiNFO64の設定
#### 対象のGPU「GPU Memory Junction Temperature」のAlert Settingsを設定  
Enable Alerting を有効  
if value >= の内容を設定 30くらいにする  
Run a Programを有効 pythonw.exeを設定、Arguments:はpowerLimitControl.py、%vを指定  
例　Program
```
C:\Users\ユーザ名\AppData\Local\Programs\Python\Python39\pythonw.exe
```
例　Arguments
```
C:\Users\ユーザ名\Desktop\test\powerLimitControl.py %v
```

#### 対象のGPU「ToTal GPU Power「% of TDP」」のAlert Settingsを設定  
Enable Alerting を有効  
if value >= の内容を設定 10くらいにする  
Run a Programを有効 pythonw.exeを設定、Arguments:savePowerLimitValue.py、%vを指定  
例　Program
```
C:\Users\ユーザ名\AppData\Local\Programs\Python\Python39\pythonw.exe
```
例　Arguments
```
C:\Users\ユーザ名\Desktop\test\savePowerLimitValue.py %v
```

※無効にするには各Enable Alertingを無効にする
