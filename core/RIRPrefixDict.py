# -*- coding: utf-8 -*-
# author:Pei Zhang
# contact: zhangpei@bupt.edu.cn
# datetime:2021/4/25 15:36
# software: PyCharm

"""
Extract rir prefix attributes from different data source,including bgp ribs, caida data ,whois ,irr database.
country attributes including:
basic info:
"""

import os
from itertools import islice
import json
from IPy import IP
import numpy as np
import pandas as pd
import math
import random

class RIRPrefixDict:

    def __init__(self, v4_file,v6_file):
        self.v4_file = v4_file
        self.v6_file = v6_file
        self.v4_dict=dict()
        self.v6_dict=dict()

    def get_ipv4_info(self):
        df=pd.read_csv(self.v4_file)
        df.drop_duplicates('prefix','first',inplace=True)
        df_new = df.set_index('prefix', drop=True, append=False, inplace=False, verify_integrity=False)
        self.v4_dict = df_new.to_dict(orient='index')
        print(self.v4_dict)


    def get_ipv6_info(self):
        df = pd.read_csv(self.v6_file)
        df.drop_duplicates('prefix', 'first', inplace=True)
        df_new = df.set_index('prefix', drop=True, append=False, inplace=False, verify_integrity=False)
        self.v6_dict = df_new.to_dict(orient='index')
        print(self.v6_dict)



if __name__ == "__main__":
    rir_dict=RIRPrefixDict(os.path.abspath(r"../output/csv/rir_ipv4.csv"),os.path.abspath(r"../output/csv/rir_ipv6.csv"))
    rir_dict.get_ipv4_info()
    rir_dict.get_ipv6_info()