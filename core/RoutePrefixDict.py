# -*- coding: utf-8 -*-
# author:Pei Zhang
# contact: zhangpei@bupt.edu.cn
# datetime:2020/4/26 15:36
# software: PyCharm

"""
Extract AS attributes from different data source,including bgp ribs, caida data ,whois ,irr database.
"""
import os
import json

class RoutePrefixDict:

    def __init__(self, rib_dir):
        self.prefix_num = 0
        self.rib_dir = rib_dir
        self.prefix_dict = dict()

    def get_ribfilelist(self, start,end):
        ribfilelist = open('ribfilelist.txt', 'a')
        F = []
        for root, dirs, files in os.walk(self.rib_dir):
            for file in files:
                # print file.decode('gbk')    #文件名中有中文字符时转码
                if ('bview' in file) and ('.data' in file):
                    t = root+'/'+file

                    F.append(t)  # 将所有的文件名添加到L列表中
                    ribfilelist.writelines(t)
                    ribfilelist.write('\n')
        ribfilelist.close()
        return F  # 返回

    def get_updatesfilelist(self, start,end):
        updatesfilelist = open('updatesfilelist.txt', 'a')
        F = []
        for root, dirs, files in os.walk(self.rib_dir):
            for file in files:
                # print file.decode('gbk')    #文件名中有中文字符时转码
                if ('updates' in file) and ('.data' in file):
                    t = root+'/'+file

                    F.append(t)  # 将所有的文件名添加到L列表中
                    updatesfilelist.writelines(t)
                    updatesfilelist.write('\n')
        updatesfilelist.close()
        return F  # 返回

    def get_prefixas_mapping(self,filelist):
        #filelist = ['/home/Phoenix/data/rrc00/2019.10/bview.20191001.0000.data']
        for file in filelist:
            with open(file) as f:
                for line in f:
                    route = line.split('|')
                    if len(route) < 7:
                        continue
                    path = route[6].split(' ')
                    prefix = route[5]
                    timestamp = route[1]
                    vp, asn = path[0], path[-1]
                    self.prefix_dict.setdefault(prefix, dict())
                    self.prefix_dict[prefix].setdefault('ASMapping', dict())
                    self.prefix_dict[prefix]['ASMapping'].setdefault(asn, dict())
                    self.prefix_dict[prefix]['ASMapping'][asn].setdefault(timestamp,int())
                    self.prefix_dict[prefix]['ASMapping'][asn][timestamp]=self.prefix_dict[prefix]['ASMapping'][asn][timestamp]+1
            print(file+' finished')

    def get_updates_ts(self, filelist):

        for file in filelist:
            with open(file) as f:
                for line in f:
                    fields = line.strip().split('|')
                    timestamp, flag, vp, prefix = fields[1], fields[2], fields[4], fields[5]
                    self.prefix_dict.setdefault(prefix, dict())
                    self.prefix_dict[prefix].setdefault('updates', dict())
                    self.prefix_dict[prefix]['updates'].setdefault(flag, dict())
                    self.prefix_dict[prefix]['updates'][flag].setdefault(timestamp, int())
                    self.prefix_dict[prefix]['updates'][flag][timestamp] = self.prefix_dict[prefix]['updates'][flag][timestamp]+1
            print(file + ' finished')

    def write_to_file(self, filename):
        js = json.dumps(self.prefix_dict)
        file = open(filename, 'w')
        file.write(js)
        file.close()

    def read_filelist(self,filename):
        F = []
        with open(filename) as f:
            for line in f:
                F.append(line.rstrip('\n'))
        return F

if __name__=="__main__":
    prefix_dict = RoutePrefixDict('/home/Phoenix/data/rrc00')
    #fl=prefix_dict.get_ribfilelist('2019.01','2021.01')
    #fl=prefix_dict.get_updatesfilelist('2019.01','2021.01')
    fl=prefix_dict.read_filelist('updatesfilelist.txt')

    prefix_dict.get_updates_ts(fl)
    fl = prefix_dict.read_filelist('ribfilelist.txt')

    prefix_dict.get_prefixas_mapping(fl)
    prefix_dict.write_to_file('RoutePrefix.txt')
