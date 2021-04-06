import json
import numpy as np
import pandas as pd


def get_ICP_prefix(s,as_dict):

      if s['asn'] in as_dict.keys():
          if 'v6Prefixes' in as_dict[s['asn']].keys():
              df = pd.DataFrame(as_dict[s['asn']]['v6Prefixes'])
              df['asn']=s['asn']
              df['as-name']=s['as-name']
              df['cnname']=s['cnname']
              df.to_excel('AS'+s['asn']+s['cnname']+'.xls')

      return s

if __name__=="__main__":

    with open('asinfo.txt', 'r') as f:
        as_dict = json.load(f)

    df = pd.read_excel('ICP.xls')
    df['asn']=df['asn'].astype(str)
    new_df=df.apply(get_ICP_prefix,args=(as_dict,),axis=1)

