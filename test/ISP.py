import numpy as np
import pandas as pd

SEARCH_STRING = 'APAN'

df = pd.read_csv('as.csv')
#df_ICP= df[df['descr'].str.contains('baidu|Huawei|ALIBABA|Taobao|TENCENT|Baidu|JDCOM|Sankuai',case=False)|df['as-name'].str.contains('baidu|Huawei|ALIBABA|Taobao|TENCENT|Baidu|JDCOM|Sankuai',case=False)]
df_ICP = df[df['descr'].str.contains(SEARCH_STRING,case=False)|df['as-name'].str.contains(SEARCH_STRING,case=False)|df['organisation'].str.contains(SEARCH_STRING,case=False)]
df_ICP.to_csv(SEARCH_STRING + '.csv')
# print(df_ICP.head)
print(df_ICP)