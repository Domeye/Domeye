import os
import json
import numpy as np
import pandas as pd
as_dict=dict()
with open(os.path.abspath(r"../output/dict/as_dict_rel.txt"), 'r') as f:
     as_dict = json.load(f)

#ali_aslist=['24429','37963','38369','45096','45102','45103','45104','59051','59052','59053','59054','59054','59028']
as_rel_dict=dict()
for key in as_dict.keys():
    as_rel=dict()
    as_rel.setdefault('asname',as_dict[key]['descr'])
    as_rel.setdefault('country', as_dict[key]['country'])

    if 'as_type' in as_dict[key].keys():
        as_rel.setdefault('as_type',as_dict[key]['as_type'])
    else:
        as_rel.setdefault('as_type', list())

    if 'customer' in as_dict[key].keys():
        as_rel.setdefault('customer',as_dict[key]['customer'])
    else:
        as_rel.setdefault('customer', list())

    if 'peer' in as_dict[key].keys():
        as_rel.setdefault('peer',as_dict[key]['peer'])
    else:
        as_rel.setdefault('peer', list())

    if 'provider' in as_dict[key].keys():
        as_rel.setdefault('provider',as_dict[key]['provider'])
    else:
        as_rel.setdefault('provider', list())

    if 'sibling-as' in as_dict[key].keys():
        as_rel.setdefault('sibling-as',as_dict[key]['sibling-as'])
    else:
        as_rel.setdefault('sibling-as', list())

    if 'v4Prefixes' in as_dict[key].keys():
        as_rel.setdefault('v4Prefixes',as_dict[key]['v4Prefixes'])
    else:
        as_rel.setdefault('v4Prefixes', list())

    if 'v6Prefixes' in as_dict[key].keys():
        as_rel.setdefault('v6Prefixes',as_dict[key]['v6Prefixes'])
    else:
        as_rel.setdefault('v6Prefixes', list())

    if 'v4Peer' in as_dict[key].keys():
        as_rel.setdefault('v4Peer',as_dict[key]['v4Peer'])
    else:
        as_rel.setdefault('v4Peer', list())

    if 'v6Peer' in as_dict[key].keys():
        as_rel.setdefault('v6Peer',as_dict[key]['v6Peer'])
    else:
        as_rel.setdefault('v6Peer', list())

    as_rel_dict.setdefault(key,as_rel)

df1=pd.DataFrame.from_dict(as_rel_dict,orient='index')
df1.to_excel('asrel.xlsx')

