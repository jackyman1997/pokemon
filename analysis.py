# %%
import pandas as pd

df = pd.read_excel('data.xlsx')
df2 = df[ df['Win rates'] != 1 ]

df2[  ]
# %%
df2[ max(df2['Win rates']) ]
# %%
