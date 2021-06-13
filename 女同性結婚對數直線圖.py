import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('110年2月同性別結婚與終止婚姻.csv')
df = df[(df['相同性別結婚對數'] > 0)]
df1 = df[(df['性別'] == '女')].groupby("區域別").sum()
df2 = df1['相同性別結婚對數']

key_array = df2.keys().array
value_array = df2.array

print(df2)
plt.rcParams['font.sans-serif'] = ['Microsoft JhengHei']
plt.bar(key_array, value_array, color="pink")
plt.title("110年2月高雄各區女同性結婚對數直線圖")
plt.xlabel('高雄各區(對數不為0)')
plt.ylabel('結婚對數')
plt.show()
