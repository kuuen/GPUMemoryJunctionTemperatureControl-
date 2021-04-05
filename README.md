# GPUMemoryJunctionTemperatureControl-
GDDR6Xのメモリジャンクション温度の制御

## 用途
Nvidia GeForce RTX 3080,3090に搭載されているGDDR6XのMemoryJunctionTemperatureの値を制御する  
温度が設定温度以上に達するとPOWER LIMITの値を下げる。温度に余裕がある場合はPOWER LIMITの値を上げる

##必要条件
Windows10,  [HWiNFO64](https://www.hwinfo.com/),[nvidiaInspector](https://www.nvidiainspector.com/),python3
