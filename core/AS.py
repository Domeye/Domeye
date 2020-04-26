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

def extract_as_type(file,asinfo_dict):

    input_file = open(file)
    for line in islice(input_file, 6, None):
        fields = line.strip().split('|')
        if fields[0] in asinfo_dict.keys():
            asinfo_dict[fields[0]].setdefault('as_type', fields[2])
    input_file.close()



def extract_sibling(file,asinfo_dict):
    org_dict=dict()
    input_file = open(file)
    line_num=14
    for line in islice(input_file, 14, None):
        line_num=line_num+1;

        if line.strip()=='# format:aut|changed|aut_name|org_id|opaque_id|source':
            break
        fields=line.strip().split('|')
        org_dict.setdefault(fields[0],fields[2]+'_'+fields[3])
    input_file.close()

    input_file = open(file)
    org_as_dict=dict()
    for line in islice(input_file, line_num, None):
        fields = line.strip().split('|')
        org_as_dict.setdefault(fields[3],set()).add(fields[0])

    input_file.close()
    input_file = open(file)
    for line in islice(input_file, line_num, None):
        fields = line.strip().split('|')
        if fields[0] in asinfo_dict.keys():
            asinfo_dict[fields[0]].setdefault('sibling',org_as_dict[fields[3]])
            asinfo_dict[fields[0]].setdefault('org_name', org_dict[fields[3]])
            asinfo_dict[fields[0]].setdefault('aut_name', fields[2])
    input_file.close()



def extract_peers(rib_dir,asinfo_dict):

    file_name = os.listdir(rib_dir)
    for file in file_name:
        filename = rib_dir+ file
        with open(filename) as f:
            for line in f:
                route = line.split('|')
                if len(route) < 7:
                    continue
                path = route[6].split(' ')
                prefix = route[5]
                prefix_version=IP(prefix).version()
                if len(path) > 1:
                    path_pairs = zip(path, path[1:])  # 前一个asn与后一个asn组成pair
                    for pair in path_pairs:
                        if pair[0]==pair[1]:
                            continue
                        if prefix_version==4:
                             if pair[1] in asinfo_dict.keys():
                                asinfo_dict[pair[1]].setdefault("v4Upstream",set()).add(pair[0])
                                asinfo_dict[pair[1]].setdefault("v4Peer", set()).add(pair[0])
                             if pair[0] in asinfo_dict.keys():
                                asinfo_dict[pair[0]].setdefault("v4Downstream", set()).add(pair[1])
                                asinfo_dict[pair[0]].setdefault("v4Peer", set()).add(pair[1])
                        if prefix_version == 6:
                            if pair[1] in asinfo_dict.keys():
                                asinfo_dict[pair[1]].setdefault("v6Upstream", set()).add(pair[0])
                                asinfo_dict[pair[1]].setdefault("v6Peer", set()).add(pair[0])
                            if pair[0] in asinfo_dict.keys():
                                asinfo_dict[pair[0]].setdefault("v6Downstream", set()).add(pair[1])
                                asinfo_dict[pair[0]].setdefault("v6Peer", set()).add(pair[1])

                    if prefix_version == 4:
                        if path[-1] in asinfo_dict.keys():
                            asinfo_dict[pair[-1]].setdefault("v4Propagation", set()).add(route[6])
                            asinfo_dict[pair[-1]].setdefault("v4Prefixes", set()).add(prefix)
                    if prefix_version == 6:
                        if path[-1] in asinfo_dict.keys():
                            asinfo_dict[pair[-1]].setdefault("v6Propagation", set()).add(route[6])
                            asinfo_dict[pair[-1]].setdefault("v6Prefixes", set()).add(prefix)

def write_asinfo_file(filename,asinfo_dict):

    for key in asinfo_dict.keys():
        if 'v4Upstream' in asinfo_dict[key].keys():
           asinfo_dict[key]["v4Upstream"]= list(asinfo_dict[key]["v4Upstream"])
        if 'v4Downstream' in asinfo_dict[key].keys():
           asinfo_dict[key]["v4Downstream"] = list(asinfo_dict[key]["v4Downstream"])
        if 'sibling' in asinfo_dict[key].keys():
           asinfo_dict[key]["sibling"] = list(asinfo_dict[key]["sibling"])
        if 'v6Upstream' in asinfo_dict[key].keys():
           asinfo_dict[key]["v6Upstream"]= list(asinfo_dict[key]["v6Upstream"])
        if 'v6Downstream' in asinfo_dict[key].keys():
           asinfo_dict[key]["v6Downstream"] = list(asinfo_dict[key]["v6Downstream"])
        if 'v4Peer' in asinfo_dict[key].keys():
           asinfo_dict[key]["v4Peer"] = list(asinfo_dict[key]["v4Peer"])
        if 'v6Peer' in asinfo_dict[key].keys():
           asinfo_dict[key]["v6Peer"]= list(asinfo_dict[key]["v6Peer"])
        if 'v4Prefixes' in asinfo_dict[key].keys():
           asinfo_dict[key]["v4Prefixes"] = list(asinfo_dict[key]["v4Prefixes"])
        if 'v6Prefixes' in asinfo_dict[key].keys():
           asinfo_dict[key]["v6Prefixes"] = list(asinfo_dict[key]["v6Prefixes"])
        if 'v4Propagation' in asinfo_dict[key].keys():
           asinfo_dict[key]["v4Propagation"] = list(asinfo_dict[key]["v4Propagation"])
        if 'v6Propagation' in asinfo_dict[key].keys():
           asinfo_dict[key]["v6Propagation"] = list(asinfo_dict[key]["v6Propagation"])

    js = json.dumps(asinfo_dict)
    file = open(filename, 'w')
    file.write(js)
    file.close()

def process_yd(filename,asinfo_dict):

    prefix_dict=dict()
    as_dict=dict()
    with open(filename) as f:
        for line in f:
            route = line.split('|')
            if len(route) < 7:
                continue
            vp =route[4]
            prefix = route[5]
            path = route[6].split(' ')
            asn=path[-1]
            if asn=='9808':
                prefix_dict.setdefault(asn,set()).add(prefix)
            if vp=='9808':
                as_dict.setdefault(prefix,route[6])

    file = open('9808', 'w')
    for prefix in prefix_dict['9808']:
        file.writelines(prefix)
        file.write('\n')
    file.close()

    file = open('9808toall.txt', 'w')
    for prefix in as_dict.keys():
        paths = as_dict[prefix].split(' ')
        strpath=''
        for asn in paths:
            if asn in asinfo_dict.keys():
              asinfo=asn+'('+asinfo_dict[asn]['descr']+','+asinfo_dict[asn]['country']+')'+' '
              strpath=strpath+asinfo
        file.writelines(prefix+" "+strpath)
        file.write('\n')
    file.close()



def init_as(file):
    as_dict = dict()
    with open(file,encoding='UTF-8') as f:
        for line in f:
            fields = line.strip().split(' ', 1)
            asn=fields[0][2:]
            org_country=fields[1].rsplit(',',1)
            asinfo_dict=dict()
            asinfo_dict.setdefault('descr', org_country[0].strip())
            asinfo_dict.setdefault('country', org_country[1].strip())
            as_dict.setdefault(asn, asinfo_dict)
    return as_dict

def main():
    root_path = os.path.abspath(os.path.dirname(__file__)).split('shippingSchedule')[0]
    basedir = root_path + "\\as.txt"
    as_dict=init_as(basedir)
    rib_dir=root_path+"\\ribs\\"
    extract_peers(rib_dir,as_dict)
    file=root_path+"\\caida\\20200401.as-org2info.txt"
    extract_sibling(file,as_dict)
    file = root_path + "\\caida\\20200401.as2types.txt"
    extract_as_type(file,as_dict)
    write_asinfo_file('asinfo.txt',as_dict)
    print(as_dict)
    #file=root_path + "\\rib.20200422-0000.data"
    #process_yd(file,as_dict)




if __name__ == '__main__':
    main()
