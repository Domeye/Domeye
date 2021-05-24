# -*- coding: utf-8 -*-
# author:Pei Zhang
# contact: zhangpei@bupt.edu.cn
# datetime:2020/4/26 15:36
# software: PyCharm

"""
Extract org attributes from different data source,including bgp ribs, caida data ,whois ,irr database.
org attributes including:
org name
org chinese name
org as counts and list
org IPv4 AS counts and list
org IPv6 AS counts and list
org IPv4 Prefixes counts and list
org IPv6 Prefixes counts and list
org IPv4 RIR prefixes counts and list
org IPv6 RIR prefixes counts and list
"""
import os
from itertools import islice
import json
import IPy
from IPy import IP
import numpy as np
import pandas as pd

class OrgDict:

    def __init__(self, as2org_file,as_dict_file):
        self.as2org_file=as2org_file
        with open(as_dict_file, 'r') as f:
            self.as_dict = json.load(f)
        self.org_count=0
        self.org_dic=dict()

    def init_org(self):
        org_temp=dict()
        input_file = open(self.as2org_file)
        line_num = 14
        for line in islice(input_file, 14, None):
            line_num = line_num + 1
            if line.strip() == '# format:aut|changed|aut_name|org_id|opaque_id|source':
                break
            fields = line.strip().split('|')
            orginfo_dict=dict()
            orginfo_dict.setdefault('name',fields[2])
            orginfo_dict.setdefault('country',fields[3])
            orginfo_dict.setdefault('source',fields[4])
            orginfo_dict.setdefault('as_count', 0)
            orginfo_dict.setdefault('as_list', list())
            orginfo_dict.setdefault('opaque_id_count', 0)
            orginfo_dict.setdefault('opaque_id_list', list())
            orginfo_dict.setdefault('v6as_count', 0)
            orginfo_dict.setdefault('v6as_list', list())
            orginfo_dict.setdefault('v4as_count', 0)
            orginfo_dict.setdefault('v4as_list', list())
            orginfo_dict.setdefault('v4prefixes_count', 0)
            orginfo_dict.setdefault('v4prefixes', list())
            orginfo_dict.setdefault('v6prefixes_count', 0)
            orginfo_dict.setdefault('v6prefixes', list())
            orginfo_dict.setdefault('v6prefixes_32num', 0)
            orginfo_dict.setdefault('v6prefixes_48num', 0)
            org_temp.setdefault(fields[0],orginfo_dict)
        input_file.close()

        input_file = open(self.as2org_file)

        for line in islice(input_file, line_num, None):
            fields = line.strip().split('|')
            org=org_temp[fields[3]]
            if fields[0] in self.as_dict.keys():
               asinfo=self.as_dict[fields[0]]
               asinfo.setdefault('org_id', fields[3])
               asinfo.setdefault('opaque_id', fields[4])
            else:
               astemp=dict()
               astemp.setdefault('aut_name',fields[2])
               astemp.setdefault('org_id', fields[3])
               astemp.setdefault('opaque_id', fields[4])
               self.as_dict.setdefault(fields[0],astemp)

            asinfo = self.as_dict[fields[0]]

            org['as_list'].append(fields[0])
            org['as_count']=org['as_count']+1
            org['opaque_id_list'].append(fields[4])
            org['opaque_id_count'] = org['opaque_id_count'] + 1
            if 'v6Prefixes' in asinfo.keys():
                org['v6as_count']=org['v6as_count']+1
                org['v6as_list'].append(fields[0])
                org['v6prefixes'].extend(asinfo['v6Prefixes'])
                org['v6prefixes_count']=len(org['v6prefixes'])
                org['v6prefixes_32num']=self.compute_subprefix(org['v6prefixes'],32)
                org['v6prefixes_48num']=self.compute_subprefix(org['v6prefixes'],48)

            if 'v4Prefixes' in asinfo.keys():
                org['v4as_count'] = org['v4as_count'] + 1
                org['v4as_list'].append(fields[0])
                org['v4prefixes'].extend(asinfo['v4Prefixes'])
                org['v4prefixes_count'] = len(org['v4prefixes'])

        for key in org_temp.keys():
            o=org_temp[key]
            o['opaque_id_list']=list(set(o['opaque_id_list']))
            o['opaque_id_count'] = len(o['opaque_id_list'])
            self.org_dic.setdefault(o['name'],o)

    def compute_subprefix(self,prefixlist,block_num):
        num=0
        for prefix in prefixlist:

            fields = prefix.split('/')
            if len(fields) == 2:
                if fields[1].isdigit():
                    lenf = int(fields[1])
                    if lenf <= block_num:
                        temp = 2 ** (block_num - lenf)
                        num = num + temp
        return num



    def write_to_file(self, filename):
        js = json.dumps(self.org_dic)
        file = open(filename, 'w')
        file.write(js)
        file.close()

    def load_from_file(self,filename):
        print(filename)
        with open(filename, 'r') as f:
            self.org_dic = json.load(f)


    def get_rank(self):
        df1=pd.DataFrame.from_dict(self.org_dic,orient='index')
        df1.to_excel('org.xlsx')

    def get_RIR_info(self,filename):
        opaque_id_dict = dict()
        with open(os.path.abspath(r"../data/rir/ipv6.csv"), encoding='UTF-8') as f:
            for line in f:
                fields = line.strip().split(',')
                if len(fields[4]) != 0:
                    key = fields[4] + '_' + fields[2].upper()
                    key = key.replace('-', '')
                    opaque_id_dict.setdefault(key, list()).append(fields[0])

        for key in self.org_dic.keys():
            o= self.org_dic[key]
            o['v6_rir_prefixes_count']=0
            o['v6_rir_prefixes_list'] = list()
            o['v6_rir_prefixes_32num'] = 0
            o['v6_rir_prefixes_48num'] = 0
            for opaque in o['opaque_id_list']:
                if len(opaque)!=0:
                    if opaque in opaque_id_dict.keys():
                        o['v6_rir_prefixes_list'].extend(opaque_id_dict[opaque])
                        o['v6_rir_prefixes_count']=len(o['v6_rir_prefixes_list'])
                        o['v6_rir_prefixes_32num'] = self.compute_subprefix(o['v6_rir_prefixes_list'],32)
                        o['v6_rir_prefixes_48num'] = self.compute_subprefix(o['v6_rir_prefixes_list'],48)


if __name__=="__main__":
    org_dict=OrgDict(os.path.abspath(r"../data/caida/20210401.as-org2info.txt"),os.path.abspath(r"../output/dict/as_dict.txt"))
    org_dict.init_org()
    org_dict.get_RIR_info(os.path.abspath(r"../data/rir/ipv6.csv"))
    org_dict.write_to_file(os.path.abspath(r"../output/dict/org_dict.txt"))
    #org_dict.load_from_file(os.path.abspath(r"../output/dict/org_dict.txt"))

    org_dict.get_rank()
