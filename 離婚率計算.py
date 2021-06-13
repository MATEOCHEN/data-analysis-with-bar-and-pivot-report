import pandas as pd

df = pd.read_csv('110年2月同性別結婚與終止婚姻.csv')
df1 = df[(df['性別'] == '女')]
df2 = df1['相同性別結婚對數'].sum()
df3 = df1['相同性別終止結婚對數'].sum()
divorce_rate = df3/df2 * 100

print(f"高雄二月女同性戀總結婚對數共計{df2}對")
print(f"高雄二月女同性戀總離婚對數共計{df3}對")
print(f"高雄二月女同性戀離婚比例為{round(divorce_rate,2)}%")
