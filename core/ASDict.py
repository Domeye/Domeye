# -*- coding: utf-8 -*-
# author:Pei Zhang
# contact: zhangpei@bupt.edu.cn
# datetime:2020/4/26 15:36
# software: PyCharm

"""
Extract AS attributes from different data source,including bgp ribs, caida data ,whois ,irr database.
"""
import os
from itertools import islice
import json
from IPy import IP
import numpy as np
import pandas as pd

class ASDict:

    def __init__(self, aslist_filename,as2types_filename,as2org_filename,rib_dir):
        self.as_dict = dict()
        self.as_count = 0
        self.aslist_filename = aslist_filename
        self.as2types_filename = as2types_filename
        self.as2org_filename = as2org_filename
        self.rib_dir = rib_dir

    def init_asinfo(self):
        with open(self.aslist_filename, encoding='UTF-8') as f:
            for line in f:
                fields = line.strip().split(' ', 1)
                asn = fields[0]
                org_country = fields[1].rsplit(',', 1)
                asinfo_dict = dict()
                if len(org_country)>1:
                   asinfo_dict.setdefault('descr', org_country[0].strip())
                   asinfo_dict.setdefault('country', org_country[1].strip())
                else:
                   asinfo_dict.setdefault('descr', org_country[0].strip())
                   asinfo_dict.setdefault('country', org_country[0].strip())
                self.as_dict.setdefault(asn, asinfo_dict)
                self.as_count = self.as_count+1



    def extract_as_type(self):
        input_file = open(self.as2types_filename)
        for line in islice(input_file, 6, None):
            fields = line.strip().split('|')
            if fields[0] in self.as_dict.keys():
                self.as_dict[fields[0]].setdefault('as_type', fields[2])
        input_file.close()

    def extract_sibling(self):
        org_dict = dict()
        input_file = open(self.as2org_filename)
        line_num = 14
        for line in islice(input_file, 14, None):
            line_num = line_num + 1;

            if line.strip() == '# format:aut|changed|aut_name|org_id|opaque_id|source':
                break
            fields = line.strip().split('|')
            org_dict.setdefault(fields[0], fields[2] + '_' + fields[3])
        input_file.close()

        input_file = open(self.as2org_filename)
        org_as_dict = dict()
        for line in islice(input_file, line_num, None):
            fields = line.strip().split('|')
            org_as_dict.setdefault(fields[3], set()).add(fields[0])

        input_file.close()
        input_file = open(self.as2org_filename)
        for line in islice(input_file, line_num, None):
            fields = line.strip().split('|')
            if fields[0] in self.as_dict.keys():
                self.as_dict[fields[0]].setdefault('sibling', org_as_dict[fields[3]])
                self.as_dict[fields[0]].setdefault('org_name', org_dict[fields[3]])
                self.as_dict[fields[0]].setdefault('aut_name', fields[2])
        input_file.close()


    def extract_peers(self):
        file_name = os.listdir(self.rib_dir)
        for file in file_name:
            filename = self.rib_dir + file
            with open(filename) as f:
                for line in f:
                    route = line.split('|')
                    if len(route) < 7:
                        continue
                    path = route[6].split(' ')
                    prefix = route[5]
                    prefix_version = IP(prefix).version()
                    if len(path) > 1:
                        path_pairs = zip(path, path[1:])  # 前一个asn与后一个asn组成pair
                        for pair in path_pairs:
                            if pair[0] == pair[1]:
                                continue
                            if prefix_version == 4:
                                if pair[1] in self.as_dict.keys():
                                    self.as_dict[pair[1]].setdefault("v4Upstream", set()).add(pair[0])
                                    self.as_dict[pair[1]].setdefault("v4Peer", set()).add(pair[0])
                                if pair[0] in self.as_dict.keys():
                                    self.as_dict[pair[0]].setdefault("v4Downstream", set()).add(pair[1])
                                    self.as_dict[pair[0]].setdefault("v4Peer", set()).add(pair[1])
                            if prefix_version == 6:
                                if pair[1] in self.as_dict.keys():
                                    self.as_dict[pair[1]].setdefault("v6Upstream", set()).add(pair[0])
                                    self.as_dict[pair[1]].setdefault("v6Peer", set()).add(pair[0])
                                if pair[0] in self.as_dict.keys():
                                    self.as_dict[pair[0]].setdefault("v6Downstream", set()).add(pair[1])
                                    self.as_dict[pair[0]].setdefault("v6Peer", set()).add(pair[1])

                        if prefix_version == 4:
                            if path[-1] in self.as_dict.keys():
                                self.as_dict[pair[-1]].setdefault("v4Propagation", set()).add(route[6])
                                self.as_dict[pair[-1]].setdefault("v4Prefixes", set()).add(prefix)
                        if prefix_version == 6:
                            if path[-1] in self.as_dict.keys():
                                self.as_dict[pair[-1]].setdefault("v6Propagation", set()).add(route[6])
                                self.as_dict[pair[-1]].setdefault("v6Prefixes", set()).add(prefix)


    def write_to_file(self, filename):
        js = json.dumps(self.as_dict)
        file = open(filename, 'w')
        file.write(js)
        file.close()



    def create_as_dict(self):
        self.init_asinfo()
        self.extract_peers()
        self.extract_sibling()
        self.extract_as_type()
        for key in self.as_dict.keys():
            if 'v4Upstream' in self.as_dict[key].keys():
                self.as_dict[key]["v4Upstream"] = list(self.as_dict[key]["v4Upstream"])
            if 'v4Downstream' in self.as_dict[key].keys():
                self.as_dict[key]["v4Downstream"] = list(self.as_dict[key]["v4Downstream"])
            if 'sibling' in self.as_dict[key].keys():
                self.as_dict[key]["sibling"] = list(self.as_dict[key]["sibling"])
            if 'v6Upstream' in self.as_dict[key].keys():
                self.as_dict[key]["v6Upstream"] = list(self.as_dict[key]["v6Upstream"])
            if 'v6Downstream' in self.as_dict[key].keys():
                self.as_dict[key]["v6Downstream"] = list(self.as_dict[key]["v6Downstream"])
            if 'v4Peer' in self.as_dict[key].keys():
                self.as_dict[key]["v4Peer"] = list(self.as_dict[key]["v4Peer"])
            if 'v6Peer' in self.as_dict[key].keys():
                self.as_dict[key]["v6Peer"] = list(self.as_dict[key]["v6Peer"])
            if 'v4Prefixes' in self.as_dict[key].keys():
                self.as_dict[key]["v4Prefixes"] = list(self.as_dict[key]["v4Prefixes"])
            if 'v6Prefixes' in self.as_dict[key].keys():
                self.as_dict[key]["v6Prefixes"] = list(self.as_dict[key]["v6Prefixes"])
            if 'v4Propagation' in self.as_dict[key].keys():
                self.as_dict[key]["v4Propagation"] = list(self.as_dict[key]["v4Propagation"])
            if 'v6Propagation' in self.as_dict[key].keys():
                self.as_dict[key]["v6Propagation"] = list(self.as_dict[key]["v6Propagation"])

        return self.as_dict

    def load_dict(self,filename):
        with open(filename, 'r') as f:
            self.as_dict = json.load(f)
        return self.as_dict



if __name__=="__main__":
    aslist_filename = '/home/Domeye/data/rir/2021-04-25/asn.txt'
    astype_filename= '/home/Domeye/data/caida/20201101.as2types.txt'
    asorg_filename = '/home/Domeye/data/caida/20210401.as-org2info.txt'
    rib_dir = '/home/Domeye/data/routing/ribs/'
    as_dict = ASDict(aslist_filename,astype_filename,asorg_filename,rib_dir)
    as_dict.create_as_dict()
    as_dict.write_to_file('/home/Domeye/output/dict/as_dict.txt')



