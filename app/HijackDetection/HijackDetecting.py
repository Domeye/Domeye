# -*- coding: utf-8 -*-
# author:Pei Zhang
# contact: zhangpei@bupt.edu.cn
# datetime:2020/4/27 9:48
# software: PyCharm

"""
文件说明：
"""
# -*- coding: utf-8 -*-
# author:Pei Zhang
# contact: zhangpei@bupt.edu.cn
# datetime:2020/4/26 17:34
# software: PyCharm

"""
BGP Hijacking detection including Prefix Hijacking, Route leak .
"""

import time
from datetime import datetime
import json
import os

Hijack_events_dict = dict()


def init_asinfo(file):
    with open(file, 'r') as f:
        AS_dict = json.load(f)
    print('加载AS字典成功！')
    AS_dict['7049']['v4Peer'].append('7908')

    return AS_dict


def write_event_file(dict, as_dict):
    Hijack_events_file = open('hijack_events.txt', 'a')

    Hijack_events_file.writelines(dict['prefix'])
    Hijack_events_file.write('\n')
    Hijack_events_file.writelines("ori_as:" + dict['ori_as'])
    Hijack_events_file.write('\n')
    Hijack_events_file.writelines("moas_set:" + str(list(dict['moas_set'])))
    Hijack_events_file.write('\n')
    Hijack_events_file.writelines("duration:" + str(dict['duration']))
    Hijack_events_file.write('\n')
    for asn in dict['moas_set']:
        if asn in as_dict.keys():
            line_str = asn + ':' + as_dict[asn]["descr"] + ' country:' + as_dict[asn]["country"]
            Hijack_events_file.writelines(line_str)
            Hijack_events_file.write('\n')

    Hijack_events_file.writelines("starttime:" + dict['starttime'])
    Hijack_events_file.write('\n')
    Hijack_events_file.writelines("endtime:" + dict['endtime'])
    Hijack_events_file.write('\n')
    Hijack_events_file.writelines("------------------------------------------")
    Hijack_events_file.write('\n')
    Hijack_events_file.close()


def write_begin_file(dict, as_dict):
    Hijack_events_file = open('hijack_begin_events.txt', 'a')

    Hijack_events_file.writelines(dict['prefix'])
    Hijack_events_file.write('\n')
    Hijack_events_file.writelines("ori_as:" + dict['ori_as'])
    Hijack_events_file.write('\n')
    Hijack_events_file.writelines("moas_set:" + str(list(dict['moas_set'])))
    Hijack_events_file.write('\n')

    for asn in dict['moas_set']:
        if asn in as_dict.keys():
            line_str = asn + ':' + as_dict[asn]["descr"] + ' country:' + as_dict[asn]["country"]
            Hijack_events_file.writelines(line_str)
            Hijack_events_file.write('\n')

    Hijack_events_file.writelines("starttime:" + dict['starttime'])
    Hijack_events_file.write('\n')

    Hijack_events_file.writelines("------------------------------------------")
    Hijack_events_file.write('\n')
    Hijack_events_file.close()


def init_rtb(rib_file):
    prefix_dict = dict()
    with open(rib_file) as f:
        for line in f:
            fields = line.strip().split('|')
            timestamp = fields[1]
            prefix = fields[5]
            path = fields[6]
            try:
                as_path_fields = fields[6].split(' ')
                vp, asn = as_path_fields[0], as_path_fields[-1]
            except Exception as e:
                print(e, line_count, sep=':')

            prefix_dict.setdefault(prefix, dict())
            prefix_dict[prefix].setdefault('moasset', set()).add(asn)
            prefix_dict[prefix].setdefault('firsttime', timestamp)
            prefix_dict[prefix].setdefault(vp, path)

    totlemoas = 0
    for prefix in prefix_dict.keys():
        moasset = prefix_dict[prefix]['moasset'].copy()
        moasnum = len(moasset)
        del prefix_dict[prefix]['moasset']
        if moasnum > 1:
            prefix_dict[prefix].setdefault('ismoasnow', True)
            prefix_dict[prefix].setdefault('moaseventid', 1)
            prefix_dict[prefix].setdefault('starttime', prefix_dict[prefix]['firsttime'])
            prefix_dict[prefix].setdefault('endtime', '0')

            totlemoas = totlemoas + 1
        else:
            prefix_dict[prefix].setdefault('ismoasnow', False)
            prefix_dict[prefix].setdefault('moaseventid', 0)
            prefix_dict[prefix].setdefault('starttime', '0')
            prefix_dict[prefix].setdefault('endtime', '0')
    print('初始化路由表成功！')
    return prefix_dict


def is_event(ori_as, moas_set, as_dict):
    peers = set()
    siblings = set()

    for asn in moas_set:
        if '{' in asn:
            return False

        asn_num = int(asn)
        if asn_num in range(64511, 65536):
            return False

        if asn in as_dict.keys():

            if 'v4Peer' in as_dict[asn].keys():
                temp_peer = set(as_dict[asn]['v4Peer'])
                temp_peer.discard(asn)
                if temp_peer is not None:
                    peers = peers | temp_peer

            if 'v6Peer' in as_dict[asn].keys():

                temp_peer = set(as_dict[asn]['v6Peer'])
                temp_peer.discard(asn)
                if temp_peer is not None:
                    peers = peers | temp_peer
            if 'sibling' in as_dict[asn].keys():
                temp_siblings = set(as_dict[asn]['sibling'])
                temp_siblings.discard(asn)
                if temp_siblings is not None:
                    siblings = siblings | temp_siblings

    for asn in moas_set:
        if peers is not None:
            if asn in peers:
                return False
        if siblings is not None:
            if asn in siblings:
                return False
    return True


def update_checking(file, prefix_dict, as_dict):
    changed_flag = 0
    moas_change_count = 0
    new_moas_count = 0

    with open(file) as f:
        for line in f:
            fields = line.strip().split('|')
            timestamp, flag, vp, prefix = fields[1], fields[2], fields[4], fields[5]
            ori_as = ''
            if flag == 'W':
                if prefix in prefix_dict.keys():
                    if vp in prefix_dict[prefix].keys():
                        del prefix_dict[prefix][vp]
                        changed_flag = 1
            else:
                as_path = fields[6]
                if prefix in prefix_dict.keys():
                    if vp in prefix_dict[prefix].keys():
                        opath = prefix_dict[prefix][vp]
                        ori_as = opath.split(' ')[-1]
                        if opath != as_path:
                            prefix_dict[prefix][vp] = as_path
                            changed_flag = 1
                    else:
                        prefix_dict[prefix].setdefault(vp, as_path)
                        changed_flag = 1
                else:
                    prefix_dict.setdefault(prefix, dict())
                    prefix_dict[prefix].setdefault(vp, as_path)
                    prefix_dict[prefix].setdefault('ismoasnow', False)
                    prefix_dict[prefix].setdefault('moaseventid', 0)
                    prefix_dict[prefix].setdefault('firsttime', timestamp)
                    prefix_dict[prefix].setdefault('starttime', '0')
                    prefix_dict[prefix].setdefault('endtime', '0')
                    changed_flag = 1

            if changed_flag == 1:

                moasset = set()
                for ovp in prefix_dict[prefix].keys():
                    if ovp not in ['ismoasnow', 'moaseventid', 'firsttime', 'starttime', 'endtime']:
                        vppath = prefix_dict[prefix][ovp]
                        vppath_fields = vppath.split(' ')
                        oasn = vppath_fields[-1]
                        moasset.add(oasn)
                moasnum = len(moasset)

                if moasnum > 1:
                    if prefix_dict[prefix]['ismoasnow']:
                        eventid = prefix_dict[prefix]['moaseventid']
                        if prefix in Hijack_events_dict.keys():
                            if eventid in Hijack_events_dict[prefix].keys():
                                if Hijack_events_dict[prefix][eventid]['moas_set'].isdisjoint(moasset):
                                    Hijack_events_dict[prefix][eventid]['moas_set'] = \
                                    Hijack_events_dict[prefix][eventid]['moas_set'] | moasset

                    else:
                        prefix_dict[prefix]['moaseventid'] = prefix_dict[prefix]['moaseventid'] + 1
                        prefix_dict[prefix]['ismoasnow'] = True
                        prefix_dict[prefix]['starttime'] = timestamp

                        if '{' not in ori_as:
                            if is_event(ori_as, moasset, as_dict):
                                Hijack_events_dict.setdefault(prefix, dict())

                                event_dict = dict()
                                event_dict['prefix'] = prefix
                                event_dict['starttime'] = datetime.utcfromtimestamp(int(timestamp)).strftime(
                                    "%Y-%m-%d %H:%M:%S")
                                event_dict['ori_as'] = ori_as

                                event_dict['moas_set'] = moasset
                                Hijack_events_dict[prefix].setdefault(prefix_dict[prefix]['moaseventid'], event_dict)
                                write_begin_file(event_dict, as_dict)

                else:
                    if prefix_dict[prefix]['ismoasnow']:
                        prefix_dict[prefix]['endtime'] = timestamp
                        duration = int(prefix_dict[prefix]['endtime']) - int(prefix_dict[prefix]['starttime'])
                        eventid = prefix_dict[prefix]['moaseventid']
                        if prefix in Hijack_events_dict.keys():
                            if eventid in Hijack_events_dict[prefix].keys():
                                Hijack_events_dict[prefix][eventid]['endtime'] = datetime.utcfromtimestamp(
                                    int(timestamp)).strftime("%Y-%m-%d %H:%M:%S")
                                Hijack_events_dict[prefix][eventid]['duration'] = duration
                                end_as = list(moasset)[0]
                                Hijack_events_dict[prefix][eventid]['end_as'] = moasset

                                write_event_file(Hijack_events_dict[prefix][eventid], as_dict)

                    prefix_dict[prefix]['ismoasnow'] = False
                    prefix_dict[prefix]['starttime'] = '0'
                    prefix_dict[prefix]['endtime'] = '0'
                changed_flag = 0


def main():
    rib_dir = '/home/hijackchecking/ribs/rrc00_bview.20200401.0000.data'
    update_dir = '/home/hijackchecking/updates/'
    as_dict = init_asinfo('/home/hijackchecking/asinfo.txt')

    prefix_dict = init_rtb(rib_dir)

    file_name = os.listdir(update_dir)
    for file in file_name:
        update_checking(update_dir + file, prefix_dict, as_dict)


if __name__ == '__main__':
    main()
