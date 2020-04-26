# -*- coding: utf-8 -*-
# author:Pei Zhang
# contact: zhangpei@bupt.edu.cn
# datetime:2020/4/26 17:53
# software: PyCharm

"""
文件说明：
"""
import requests        #导入requests包
from bs4 import    BeautifulSoup
import os
import subprocess
import time

def get_as_whois(url):

    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36'}
    AS_info_dict=dict()
    base_dir='https://bgp.potaroo.net'
    strhtml = requests.get(url,headers)
    soup = BeautifulSoup(strhtml.text, 'lxml')
    data = soup.select('body > pre > a')
    count=0
    for item in data:

        count=count+1
        if int(item.get_text()[2:].strip())<52257:
            continue

        command='whois '+item.get_text().strip()
        file= open('/public/whois/'+item.get_text()[2:].strip()+'.txt', 'w')
        subprocess.call(command, shell=True, stdout=file, stderr=subprocess.STDOUT)
        file.close()
        if count%50==0:
            time.sleep(5)



def main():

    url='https://bgp.potaroo.net/cidr/autnums.html'
    get_as_whois(url)


if __name__=='__main__':
    main()
