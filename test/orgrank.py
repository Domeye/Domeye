import os
from itertools import islice
import json
import pandas as pd
import numpy as np
df =pd.DataFrame(columns=('org_name','asn'))
org_dict = dict()
input_file = open('20210101.as-org2info.txt')
line_num = 14
for line in islice(input_file, 14, None):
    line_num = line_num + 1
    if line.strip() == '# format:aut|changed|aut_name|org_id|opaque_id|source':
        break
    fields = line.strip().split('|')
    org_dict.setdefault(fields[0], fields[2])
input_file.close()
print(org_dict)

input_file = open('20210101.as-org2info.txt')
org_as_dict = dict()

for line in islice(input_file, line_num, None):
    fields = line.strip().split('|')
    org_as_dict.setdefault(org_dict[fields[3]], set()).add(fields[0])
print(org_as_dict)






