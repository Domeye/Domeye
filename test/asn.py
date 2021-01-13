import numpy as np
import pandas as pd
import re
#显示所有列
pd.set_option('display.max_columns', None)
#显示所有行
pd.set_option('display.max_rows', None)
#设置value的显示长度为100，默认为50
pd.set_option('max_colwidth',100)
df =pd.DataFrame(columns=('as','descr','country'))
with open('asn.txt', encoding='UTF-8') as f:
    aslist=[]
    descrlist=[]
    country =[]
    for line in f:
        fields = line.strip().split(' ', 1)
        asn = fields[0]
        org_country = fields[1].rsplit(',', 1)
        asinfo_dict = dict()
        if len(org_country) > 1:
           aslist.append(asn)
           descrlist.append(org_country[0].strip())
           country.append(org_country[1].strip())
        else:
           aslist.append(asn)
           descrlist.append(org_country[0].strip())
           country.append(org_country[0].strip())
    df['as']=aslist
    df['descr']=descrlist
    df['country']=country

    df1=df.groupby('country')['as'].nunique().sort_values()
    asn_num=pd.DataFrame({"country":df1.index,"num":df1.values})
    asn_num.to_csv('country_asn.csv')

    print(asn_num)






