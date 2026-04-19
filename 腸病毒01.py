'''
1.每年腸病毒就診人次畫成長條圖
2.每週腸病毒就診人次畫成折線圖
3.腸病毒就診類別畫成圓餅圖
4.年齡別腸病毒就診人次畫成長條圖
5.各縣市腸病毒就診人次畫成長條圖 , 2格
6.六都與非六都腸病毒就診人次佔比畫成圓餅圖
7.各六都腸病毒就診人次比率畫成圓餅圖
'''
import matplotlib.pyplot as plt
imort pandas as pd

url = 'https://od.cdc.gov.tw/eic/NHI_EnteroviralInfection.csv'

