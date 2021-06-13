import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('110年2月同性別結婚與終止婚姻.csv')
location = df[(df['性別'] == '計') & (df['相同性別結婚對數'] > 0)]["區域別"]
df = df[(df['區域別'].isin(location)) & (df['性別'] != "計")]

df1 = pd.pivot_table(df, index=["區域別", "性別"]
                     , values=["相同性別結婚對數", "相同性別終止結婚對數"]
                     , fill_value=0)
print(df1)
df2 = df1.filter(like="女", axis=0)
df3 = df1.filter(like="男", axis=0)
x_index1 = df2.index.get_level_values("區域別").array
x_index2 = df3.index.get_level_values("區域別").array
bar_width = 0.8

plt.bar(x_index2, df3["相同性別結婚對數"].array
        , color="lightblue", label="男結婚對數", width=bar_width)
plt.bar(x_index1, df2["相同性別結婚對數"].array, bottom=df3["相同性別結婚對數"].array
        , color="pink", label="女結婚對數", width=bar_width)


plt.xticks(size=8)
plt.legend()
plt.rcParams['font.sans-serif'] = ['Microsoft JhengHei']
plt.title("110年2月高雄各區同性結婚對數堆疊直線圖")
plt.xlabel('高雄各區(對數不為0)')
plt.ylabel('結婚對數')
plt.show()
