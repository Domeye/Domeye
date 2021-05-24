import IPy
from IPy import IP
import ipaddress
#print(len(list(ipaddress.ip_network('2001:fd0::/36').subnets(new_prefix=36))))
#print(2**12)
import os
from itertools import islice
import json

as_dict=dict()
with open(os.path.abspath(r"../output/dict/as_dict.txt"), 'r') as f:
     as_dict = json.load(f)

with open(os.path.abspath(r"../data/caida/20210401.asrel-caida.txt")) as f:
    for line in f:
        if '#' in line:
            continue
        fields=line.strip().split('|')
        if fields[2] =='-1':
            if fields[0] in as_dict.keys():
                as_dict[fields[0]].setdefault('customer',set()).add(fields[1])
            if fields[1] in as_dict.keys():
                as_dict[fields[1]].setdefault('provider', set()).add(fields[0])

        if fields[2] =='0':
            if fields[0] in as_dict.keys():
                as_dict[fields[0]].setdefault('peer',set()).add(fields[1])
            if fields[1] in as_dict.keys():
                as_dict[fields[1]].setdefault('peer',set()).add(fields[0])

with open(os.path.abspath(r"../data/caida/20210401.asrel-probink.txt")) as f:
    for line in f:
        if '#' in line:
            continue
        fields=line.strip().split('|')
        if fields[2] =='-1':
            if fields[0] in as_dict.keys():
                as_dict[fields[0]].setdefault('customer',set()).add(fields[1])
            if fields[1] in as_dict.keys():
                as_dict[fields[1]].setdefault('provider', set()).add(fields[0])

        if fields[2] =='0':
            if fields[0] in as_dict.keys():
                as_dict[fields[0]].setdefault('peer',set()).add(fields[1])
            if fields[1] in as_dict.keys():
                as_dict[fields[1]].setdefault('peer',set()).add(fields[0])

        if fields[2] =='1':
            if fields[0] in as_dict.keys():
                as_dict[fields[0]].setdefault('sibling-as',set()).add(fields[1])
            if fields[1] in as_dict.keys():
                as_dict[fields[1]].setdefault('sibling-as',set()).add(fields[0])

for key in as_dict.keys():
    if 'customer' in as_dict[key].keys():
         as_dict[key]["customer"] = list(as_dict[key]["customer"])
    if 'provider' in as_dict[key].keys():
         as_dict[key]["provider"] = list(as_dict[key]["provider"])
    if 'peer' in as_dict[key].keys():
         as_dict[key]["peer"] = list(as_dict[key]["peer"])
    if 'sibling-as' in as_dict[key].keys():
         as_dict[key]["sibling-as"] = list(as_dict[key]["sibling-as"])

js = json.dumps(as_dict)
file = open(os.path.abspath(r"../output/dict/as_dict_rel.txt"), 'w')
file.write(js)
file.close()





