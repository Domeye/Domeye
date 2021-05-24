# -*- coding: utf-8 -*-
# author:Pei Zhang
# contact: zhangpei@bupt.edu.cn
# datetime:2021/4/25 15:36
# software: PyCharm

"""
Extract country attributes from different data source,including bgp ribs, caida data ,whois ,irr database.
country attributes including:
basic info: country_fullname,country_shortname,country_chinesefullname,country_two,country_three
country-num,country-phonenum,counrty_shicha,country_lon,country_lat
country as counts and list
country IPv4 AS counts and list
country IPv6 AS counts and list
country IPv4 AS topo
country IPv6 AS topo
country IPv4 AS boundary
country IPv6 AS boundary
country org
country RIR IPv4
congtry RIR IPv6
country RIR AS
"""
import os
from itertools import islice
import json
from IPy import IP
import numpy as np
import pandas as pd
import math
import random
from collections import defaultdict, Counter

class CountryDict:

    def __init__(self, country_file,as_dict_file,rib_file):
        self.country_dict = dict()
        self.country_count = 0
        self.asn_map = {}  # key:asn, value:tuple(country_code,country_cn_name,as_name)
        self.asn_map_with_cn = {}  # key: asn with cn_name
        self.country_file=country_file
        self.rib_file=rib_file
        self.as_dict_file=as_dict_file
        with open(as_dict_file, 'r') as f:
            self.as_dict = json.load(f)


    def init_countryinfo(self):
        df = pd.read_excel(self.country_file,sheet_name='全球国家')
        df.columns=['country_fullname','country_shortname','country_chinesefullname','country_shortname','country_two','country_three','country-num','country-phonenum','counrty_shicha','country_lon','country_lat']
        df_new = df.set_index('country_two', drop=True, append=False, inplace=False, verify_integrity=False)
        self.country_dict=df_new.to_dict(orient='index')

    def get_country_routing(self):
        for key in self.as_dict.keys():
            con=self.as_dict[key]['country']
            if con not in self.country_dict.keys():
                continue
            self.country_dict[con].setdefault("routing_as_list", list()).append(key)
            if 'v6Prefixes' in self.as_dict[key].keys():
                self.country_dict[con].setdefault("routing_v6as_list", list()).append(key)
                self.country_dict[con].setdefault("routing_v6prefixes", list()).extend(self.as_dict[key]['v6Prefixes'])
                v6prefixes_32num = self.compute_subprefix(self.country_dict[con]['routing_v6prefixes'], 32)
                v6prefixes_48num = self.compute_subprefix(self.country_dict[con]['routing_v6prefixes'], 48)
                v6prefixes_num = len(self.country_dict[con]['routing_v6prefixes'])
                self.country_dict[con].setdefault('v6prefixes_32num', v6prefixes_32num)
                self.country_dict[con].setdefault('v6prefixes_48num', v6prefixes_48num)
                self.country_dict[con].setdefault('v6prefixes_num', v6prefixes_num)


            if 'v4Prefixes' in self.as_dict[key].keys():
                self.country_dict[con].setdefault("routing_v4as_list", list()).append(key)
                self.country_dict[con].setdefault("routing_v4prefixes", list()).extend(self.as_dict[key]['v4Prefixes'])
                v4prefixes_num = len(self.country_dict[con]['routing_v4prefixes'])
                self.country_dict[con].setdefault('v4prefixes_num', v4prefixes_num)

    def get_country_rir(self):


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

    def calc_topo(self,cc_topo):
        colors = ['#0055ff', '#0088ff', '#00aaff', '#33bbff', '#66ccff', '#99ddff']
        topo = defaultdict(lambda: {'nodes': [], 'edges': []})
        for ccode, topo_info in cc_topo.items():
            node_count = len(topo_info['nodes_counter'])
            edge_count = len(topo_info['edges_counter'])
            order = 0  # 出现次序
            enode_num = 0  # 边缘点个数
            for node, out_count in topo_info['nodes_counter'].most_common():  # node:asn,out_count:出现次数; 按出现次数从大到小排序
                if out_count == 0 and enode_num == 0:  # 首次遇到出现次数为0的，就依此来计算边缘点个数
                    enode_num = node_count - order
                    break
                order += 1
            order = 0
            # print '(',enode_num,',', node_count,')'
            tmp = (node_count - enode_num) * 1.5 if enode_num != node_count else node_count
            for node, out_count in topo_info['nodes_counter'].most_common():
                r = math.log(order + 1) / math.log(tmp + 1) if out_count > 0 else 1  # 计算半径，若是边缘点则为1，否则按出现次序越前则半径越小
                if r >= 0.9 and r != 1.0:
                    print
                    node, 'r=', r
                color = colors[int(r * 5)]
                w = random.random() * math.pi * 2 if out_count > 0 \
                    else (order % enode_num) * (math.pi / enode_num) * 2  # 计算角度，若是边缘点则均匀分布边缘一周，否则随机
                as_info = self.asn_map_with_cn[node]
                topo[ccode]['nodes'].append({
                    "color": color,
                    "name": as_info[2],
                    "country_code": as_info[0],
                    "country": as_info[1],
                    "y": 5 * r * math.sin(w),
                    "x": 5 * r * math.cos(w),
                    "label": node,
                    "id": node,
                    "_id": node.split()[0],
                    # "size": 0.0
                    "size": 1 - r
                })
                if node.find("(") != -1:
                    print
                    'find ' + topo[ccode]['nodes'][-1]['id']
                order += 1
            edge_id = 0
            for edge, trans_count in topo_info['edges_counter'].most_common():  # edge:pair,trans_count:出现次数
                r = float(edge_id + 1) / (edge_count + 1)
                color = colors[int(r * 5)]
                topo[ccode]['edges'].append({
                    "target": edge[1],
                    "color": color,
                    "source": edge[0],
                    "transmit": trans_count,
                    "id": str(edge_id),
                    "size": 0
                })
                edge_id += 1
        return topo

    def analysis(self,filename,cn_name, cc_topo_v4, cc_topo_v6):
        row = 0
        with open(filename) as f:
            for line in f:
                row += 1
                if row % 1000000 == 0:
                    print
                    '  analyzed ' + str(row) + ' rows...'
                route = line.split('|')
                if len(route) < 7:
                    continue
                prefix = route[5]
                path = route[6].split(' ')
                if len(path) > 1:
                    path_pairs = zip(path, path[1:])  # 前一个asn与后一个asn组成pair
                    for pair in path_pairs:
                        # print (pair)
                        as_infol = self.asn_map.get(pair[0], None)
                        as_infor = self.asn_map.get(pair[1], None)
                        tmp0 = pair[0] + cn_name[pair[0]] if cn_name.get(pair[0]) else pair[0]
                        tmp1 = pair[1] + cn_name[pair[1]] if cn_name.get(pair[1]) else pair[1]
                        pair = (tmp0, tmp1)
                        if as_infol and as_infor and as_infol[0] == as_infor[
                            0]:  # 若为相同国家         (as_infol[0]=='CN' or as_infor[0]=='CN')；and (as_infol[0]=='CN' or as_infor[0]=='CN')and not (as_infol[0]=='CN' and as_infor[0]=='CN'): #
                            if ':' in prefix:
                                cc_topo_v6[as_infol[0]]['nodes_counter'][pair[0]] += 1
                                cc_topo_v6[as_infol[0]]['nodes_counter'][pair[1]] += 0
                                cc_topo_v6[as_infol[0]]['edges_counter'][tuple(pair)] += 1
                            else:
                                cc_topo_v4[as_infol[0]]['nodes_counter'][pair[0]] += 1
                                cc_topo_v4[as_infol[0]]['nodes_counter'][pair[1]] += 0
                                cc_topo_v4[as_infol[0]]['edges_counter'][tuple(pair)] += 1


    def get_country_topo(self):
        with open(os.path.abspath(r"../data/country/cctoname.json")) as f:
            cc_map = json.load(f)
        cn_name = dict()
        with open(os.path.abspath(r"../data/country/asncnname.txt")) as f:
            for line in f.readlines():
                asn, name = line.strip().split(' ', 1)
                cn_name[asn] = ' (' + name + ')'
        with open('/home/Domeye/data/rir/2021-04-25/asn.txt') as f:
            for i in f.readlines():
                fields = i.strip().split(' ', 1)
                asn = fields[0].strip()
                org_country = fields[1].rsplit(',', 1)
                if len(org_country) > 1:
                   cc = org_country[1].strip()
                   asname = org_country[0]
                else:
                   cc = org_country[0].strip()
                   asname = org_country[0]
                if cn_name.get(asn):
                    asn_with_cn = asn + cn_name[asn]
                    self.asn_map_with_cn[asn_with_cn] = (cc, cc_map.get(cc, ''), asname)
                else:
                    self.asn_map_with_cn[asn] = (cc, cc_map.get(cc, ''), asname)
                self.asn_map[asn] = (cc, cc_map.get(cc, ''), asname)

        cc_topo_v4 = defaultdict(lambda: {'nodes_counter': Counter(), 'edges_counter': Counter()})
        cc_topo_v6 = defaultdict(lambda: {'nodes_counter': Counter(),
                                          'edges_counter': Counter()})  # key:country_code, value:dict{两个counter,其一为与某asn相连的asn的出现次数，其二为各pair的出现次数}
        self.analysis(self.rib_file, cn_name, cc_topo_v4, cc_topo_v6)
        topo_v4 = self.calc_topo(cc_topo_v4)
        topo_v6 = self.calc_topo(cc_topo_v6)
        for key, value in topo_v4.items():
            if key in self.country_dict.keys():
               self.country_dict[key].setdefault('v4_topo',value)
        for key, value in topo_v6.items():
            if key in self.country_dict.keys():
               self.country_dict[key].setdefault('v6_topo',value)

    def write_to_file(self, filename):
        js = json.dumps(self.country_dict)
        file = open(filename, 'w')
        file.write(js)
        file.close()



if __name__=="__main__":
    country_dict = CountryDict(os.path.abspath(r"../data/country/country.xlsx"),os.path.abspath(r"../output/dict/as_dict.txt"),os.path.abspath(r"../data/routing/ribs/bview.20210425.0800.data"))
    country_dict.init_countryinfo()
    country_dict.get_country_topo()
    country_dict.write_to_file(os.path.abspath(r"../output/dict/country_dict.txt"))