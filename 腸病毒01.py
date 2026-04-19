"""
1.每年腸病毒就診人次畫成長條圖
2.每週腸病毒就診人次畫成折線圖
3.腸病毒就診類別畫成圓餅圖
4.年齡別腸病毒就診人次畫成長條圖
5.各縣市腸病毒就診人次畫成長條圖 , 2格
6.六都與非六都腸病毒就診人次佔比畫成圓餅圖
7.各六都腸病毒就診人次比率畫成圓餅圖
"""

import ssl

import matplotlib.pyplot as plt
import pandas as pd

# 建立一個不檢查憑證的上下文
ssl._create_default_https_context = ssl._create_unverified_context

url = "https://od.cdc.gov.tw/eic/NHI_EnteroviralInfection.csv"

df = pd.read_csv(url)
plt.figure(figsize=(16, 10), dpi=120)
plt.rcParams["font.sans-serif"] = "Microsoft JhengHei"
print(df.columns)
# 1.每年腸病毒就診人次畫成長條圖
plt.subplot(241)
s1 = df.groupby("年")["腸病毒健保就診人次"].sum()
plt.bar(s1.index, s1.values / 10000)
plt.xlabel("年份", fontsize=16)
plt.ylabel("腸病毒就診人次 (萬)", fontsize=16)
plt.title("每年腸病毒就診人次", fontsize=24)
plt.grid(axis="y", linestyle="--", alpha=0.5)
for i in s1.index:
    plt.text(i, s1[i] / 10000, f"{s1[i]:,}人", ha="center", va="bottom", fontsize=10)
# 2.每週腸病毒就診人次畫成折線圖
plt.subplot(242)
s2 = df.groupby("週")["腸病毒健保就診人次"].sum()
plt.plot(s2.index, s2.values / 10000)
plt.xlabel("週數", fontsize=16)
plt.ylabel("腸病毒就診人次 (萬)", fontsize=16)
plt.title("每週腸病毒就診人次", fontsize=24)
for i in s2.index[::5]:  # 每隔5週顯示一次數字
    plt.text(
        i,
        s2[i] / 10000,
        f"{s2[i]:,}人",
        ha="center",
        va="bottom",
        fontsize=10,
    )
    plt.plot(i, s2[i] / 10000, marker="o")
plt.text(
    s2.idxmax(),
    s2.max() / 10000,
    f"第{s2.idxmax()}週: \n{s2.max():,}人",
    ha="center",
    va="bottom",
    fontsize=10,
    color="red",
)

# 3.腸病毒就診類別畫成圓餅圖
plt.subplot(243)
s3 = df.groupby("就診類別")["腸病毒健保就診人次"].sum()
plt.pie(
    s3.values,
    labels=s3.index,
    autopct="%10.2f%%",
    startangle=45,
    colors=["#ff9999", "#66b3ff", "#99ff99", "#ffcc99"],
)

# 4.年齡別腸病毒就診人次畫成長條圖
plt.subplot(244)
s4 = df.groupby("年齡別")["腸病毒健保就診人次"].sum()
print(s4.index)
years = ["0~2", "3~6", "7~12", "13~15", "16~18", "19~24", "25~64", "65+"]
s4 = s4[years]
plt.bar(s4.index, s4.values / 10000)
plt.xlabel("年齡別", fontsize=16)
plt.ylabel("腸病毒就診人次 (萬)", fontsize=16)
plt.title("年齡別腸病毒就診人次", fontsize=24)
plt.xticks(rotation=45)
for i in range(len(s4.index)):
    plt.text(
        s4.index[i],
        s4.iloc[i] / 10000,
        f"{s4.values[i]:,}人",
        ha="center",
        va="bottom",
        fontsize=10,
    )

# 5.各縣市腸病毒就診人次畫成長條圖 , 2格
plt.subplot(223)
county_list = [
    "基隆市",
    "台北市",
    "新北市",
    "桃園市",
    "新竹市",
    "新竹縣",
    "苗栗縣",  # 北部
    "台中市",
    "彰化縣",
    "南投縣",
    "雲林縣",
    "嘉義市",
    "嘉義縣",  # 中部
    "台南市",
    "高雄市",
    "屏東縣",  # 南部
    "宜蘭縣",
    "花蓮縣",
    "台東縣",  # 東部
    "澎湖縣",
    "金門縣",
    "連江縣",  # 離島
]
s5 = df.groupby("縣市")["腸病毒健保就診人次"].sum()
s5 = s5[county_list]
plt.bar(s5.index, s5.values)
plt.xlabel("縣市", fontsize=16)
plt.ylabel("腸病毒就診人次", fontsize=16)
plt.title("各縣市腸病毒就診人次", fontsize=24)
plt.xticks(rotation=45)
for i in range(len(s5.index)):
    plt.text(
        s5.index[i],
        s5.values[i],
        f"{s5.values[i]:,}人",
        ha="center",
        va="bottom",
        fontsize=10,
    )


# 6.六都與非六都腸病毒就診人次佔比畫成圓餅圖
plt.subplot(247)
df["六都"] = df["縣市"].apply(
    lambda x: (
        "六都"
        if x in ["台北市", "新北市", "桃園市", "台中市", "台南市", "高雄市"]
        else "非六都"
    )
)
s6 = df.groupby("六都")["腸病毒健保就診人次"].sum()
plt.pie(s6.values, labels=s6.index, autopct="%.2f%%")


# 7.各六都腸病毒就診人次比率畫成圓餅圖
plt.subplot(248)
s7 = df[df["六都"] == "六都"].groupby("縣市")["腸病毒健保就診人次"].sum()
plt.pie(s7.values, labels=s7.index, autopct="%.2f%%")

plt.tight_layout()
plt.show()
