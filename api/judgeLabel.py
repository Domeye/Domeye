from flask import Flask, request
from flask_cors import cross_origin
from create_trees import *
import collections
import json
import socket
import csv
import os


app = Flask(__name__)


def after_request(response):
    """
    Solve cross-domain issues
    :param response:
    :return:
    """
    response.headers['Access-Control-Allow-Origin'] = request.headers.get('Origin') or 'http://127.0.0.1:9528'
    response.headers['Access-Control-Allow-Methods'] = 'PUT,GET,POST,DELETE'
    response.headers['Access-Control-Allow-Headers'] = 'Content-Type,Authorization,Accept,Origin,Referer,User-Agent'
    response.headers['Access-Control-Allow-Credentials'] = 'true'
    return response


def is_ipv6(content):
    try:
        socket.inet_pton(socket.AF_INET6, content)
    except socket.error:  # not a valid ip
        return False
    return True


@app.route('/judge', methods=["POST"])
@cross_origin()
def judge():
    search_content = json.loads(request.get_data(as_text=True))['input_search']
    result = {}
    if is_ipv6(search_content):
        result['tabs'] = ['地理位置', '网络位置', '传播路径', '路由波动', '路由宣告', '关联关系', 'Whois', '网站域名']
        result['input_type'] = 'ipv6'
        return result
    elif search_content.isdigit():
        print('输入的为AS号')
    else:
        result['key'] = ''
        result['input_type'] = 'valid'
        print("请输入ipv6地址、AS号、国家之一")


@app.route('/geo_position', methods=["POST"])
@cross_origin()
def geo_position():
    search_content = json.loads(request.get_data(as_text=True))['input_search']
    longest_prefix_group = as_prefix_trie.find_all(search_content)[-1]  # 取最长匹配
    AS_raw = json.loads(longest_prefix_group[1])
    ans = dict()
    ans['country'] = AS_raw.get('country')
    ans['introduction'] = '暂无介绍'
    ans['city'] = ''
    ans['postal_code'] = ''
    ans['accuracy_radius'] = ''
    ans['latitude'] = float(0)
    ans['longitude'] = float(0)
    print(ans['country'])
    if ans['country'] != '':
        try:
            ans['latitude'] = countrytolat_dic.get(AS_raw.get('country')).get('latitude')
            ans['longitude'] = countrytolat_dic.get(AS_raw.get('country')).get('longitude')
        except:
            print("no match")
    try:
        if geo_prefix_trie.find_all(search_content):
            each_pre = geo_prefix_trie.find_all(search_content)[-1][0]
            ans['country'] = geo_dic.get(each_pre).get('country')
            ans['city'] = '暂无' if geo_dic.get(each_pre).get('city') == '' else geo_dic.get(each_pre).get('city')
            ans['postal_code'] = geo_dic.get(each_pre).get('postal_code')
            ans['latitude'] = float(geo_dic.get(each_pre).get('latitude'))
            ans['longitude'] = float(geo_dic.get(each_pre).get('longitude'))
            ans['accuracy_radius'] = geo_dic.get(each_pre).get('accuracy_radius')
    except:
        print("null")
    return ans


@app.route('/longest_as_prefix', methods=["POST"])
@cross_origin()
def longest_as_prefix():
    search_content = json.loads(request.get_data(as_text=True))['input_search']
    longest_prefix_group = as_prefix_trie.find_all(search_content)[-1]
    prefix = longest_prefix_group[0]  # 获取Prefix
    AS_raw = json.loads(longest_prefix_group[1])  # 获取insert
    AS_raw['prefix'] = prefix

    keys = list(AS_raw.keys())
    prefix_dict = {}
    prefix_dict['keys'] = keys
    prefix_dict['longest_prefix'] = AS_raw
    return prefix_dict


@app.route('/longest_inet6_prefix', methods=["POST"])
@cross_origin()
def longest_inet6_prefix():
    search_content = json.loads(request.get_data(as_text=True))['input_search']
    longest_prefix_group = inet6num_prefix_trie.find_all(search_content)[-1]
    prefix = longest_prefix_group[0]
    prefix_dict = json.loads(longest_prefix_group[1])

    prefix_dict['prefix'] = prefix
    return prefix_dict


def get_longest_AS_prefix(address):
    longest_prefix_group = as_prefix_trie.find_all(address)[-1]
    prefix = longest_prefix_group[0]  # 获取Prefix
    AS_raw = json.loads(longest_prefix_group[1])  # 获取insert
    AS_raw['prefix'] = prefix

    keys = list(AS_raw.keys())
    prefix_dict = {}
    prefix_dict['keys'] = keys
    prefix_dict['longest_prefix'] = AS_raw
    return prefix_dict


@app.route('/path_graph', methods=["POST"])
@cross_origin()
def path_graph():
    search_content = json.loads(request.get_data(as_text=True))['input_search']
    v6Propagation = get_longest_AS_prefix(search_content)['longest_prefix']['v6Propagation']
    return {'v6Propagation': v6Propagation}


@app.route('/three_picture', methods=["POST"])
@cross_origin()
def three_picture():
    search_content = json.loads(request.get_data(as_text=True))['input_search']
    prefix_raw = IPv6_prefix_trie.find_all(search_content)
    dic_name = "/home/ASDict/RoutePrefix.txt"
    prefix_dic = {}
    with open(dic_name, 'r') as dic_file:
        dic_raw = json.load(dic_file)
    prefix_all = []
    try:
        for each in reversed(prefix_raw):
            each_prefix = each[0]
            prefix_all.append(each_prefix)
        print(prefix_all)

        for each in prefix_all:
            prefix_dic = dic_raw.get(each)
            if dic_raw.get(each):
                print(prefix_dic)
                break
    except:
        print("null")
    ans = {}
    picture12_x = dic_raw.get('updatetimelist')
    picture3_x = dic_raw.get('ribtimelist')
    picture1_data = []
    picture2_data = []
    picture1_raw_y = prefix_dic.get('updates').get('A').keys()
    picture2_raw_y = prefix_dic.get('updates').get('W').keys()
    picture3_data = []
    for each_time in picture12_x:
        if each_time in picture1_raw_y:
            picture1_data.append(prefix_dic.get('updates').get('A').get(each_time))
        else:
            picture1_data.append(0)
        if each_time in picture2_raw_y:
            picture2_data.append(prefix_dic.get('updates').get('A').get(each_time))
        else:
            picture2_data.append(0)
    ans['picture12_x'] = picture12_x
    ans['picture1_data'] = picture1_data
    ans['picture2_data'] = picture2_data

    picture3_raw = prefix_dic.get("ASMapping").keys()
    for each_as in picture3_raw:
        for each_time in picture3_x:
            each_data = []
            each_data.append(each_time)
            each_data.append(each_as)
            if each_time in prefix_dic.get("ASMapping").get(each_as).keys():
                each_data.append(prefix_dic.get("ASMapping").get(each_as).get(each_time) * 1000000 + 968973)
                each_data.append(prefix_dic.get("ASMapping").get(each_as).get(each_time))
            else:
                each_data.append(0)
                each_data.append(0)
            picture3_data.append(each_data)
    ans['picture3_data'] = picture3_data
    return ans


@app.route('/relation_graph', methods=["POST"])
@cross_origin()
def relation_graph():
    search_content = json.loads(request.get_data(as_text=True))['input_search']
    longest_prefix_group1 = as_prefix_trie.find_all(search_content)[-1]
    prefix1 = longest_prefix_group1[0]
    AS_raw = json.loads(longest_prefix_group1[1])
    ASN1 = AS_raw.get('ASN')
    desc1 = AS_raw.get('descr')
    country1 = AS_raw.get('country')
    print(ASN1)

    longest_prefix_group2 = inet6num_prefix_trie.find_all(search_content)[-1]
    prefix2 = longest_prefix_group2[0]
    print(prefix2)
    prefix_dict2 = json.loads(longest_prefix_group2[1])
    desc2 = prefix_dict2.get('descr')
    country2 = prefix_dict2.get('country')

    longest_prefix_group3 = route6_prefix_trie.find_all(search_content)[-1]
    prefix3 = longest_prefix_group3[0]
    print(prefix3)
    prefix_dict3 = json.loads(longest_prefix_group3[1])
    desc3 = prefix_dict3.get('descr')
    country3 = prefix_dict3.get('country')

    graph = {}
    graph["nodes"] = []
    graph["links"] = []
    node1 = {
        "id": "1",
        "name": prefix1,
        "symbolSize": 33,
        "x": 200,
        "y": -120,
        "value": "Real-time Routing",
        "category": 1
    }
    graph["nodes"].append(node1)
    node2 = {
        "id": "2",
        "name": ASN1,
        "symbolSize": 33,
        "x": -87.93029,
        "y": -6.8120565,
        "value": "ASN",
        "category": 2
    }
    graph["nodes"].append(node2)
    if prefix2.split('/')[1] != '0':
        node3 = {
            "id": "3",
            "name": prefix2,
            "symbolSize": 33,
            "x": 82.80825,
            "y": -203.1144,
            "value": "inet6num",
            "category": 3
        }
        graph["nodes"].append(node3)
    if prefix2.split('/')[1] != '0':
        node4 = {
            "id": "4",
            "name": prefix3,
            "symbolSize": 35.58095333333333,
            "x": 290,
            "y": -10,
            "value": "route6",
            "category": 7
        }
        graph["nodes"].append(node4)
    node5 = {
        "id": "5",
        "name": country1,
        "symbolSize": 33,
        "x": 40,
        "y": 140,
        "value": "country",
        "category": 5
    }
    graph["nodes"].append(node5)
    if country2:
        node6 = {
            "id": "6",
            "name": country2,
            "symbolSize": 33,
            "x": 250,
            "y": 170,
            "value": "country",
            "category": 5
        }
        graph["nodes"].append(node6)
    if country3:
        node7 = {
            "id": "7",
            "name": country3,
            "symbolSize": 33,
            "x": 160,
            "y": 230,
            "value": "country",
            "category": 5
        }
        graph["nodes"].append(node7)
    node8 = {
        "id": "8",
        "name": desc1,
        "symbolSize": 33,
        "x": -250,
        "y": -100,
        "value": "description",
        "category": 6
    }
    graph["nodes"].append(node8)
    if desc2:
        node9 = {
            "id": "9",
            "name": desc2,
            "symbolSize": 33,
            "x": -250,
            "y": 100,
            "value": "description",
            "category": 6
        }
        graph["nodes"].append(node9)
    if desc3:
        node10 = {
            "id": "10",
            "name": desc3,
            "symbolSize": 33,
            "x": -250,
            "y": -300,
            "value": "description",
            "category": 6
        }
        graph["nodes"].append(node10)

    graph["links"] = [
        {
            "source": "2",
            "target": "1"
        },
        {
            "source": "5",
            "target": "1"
        },
        {
            "source": "5",
            "target": "2"
        },
        {
            "source": "6",
            "target": "3"
        },
        {
            "source": "7",
            "target": "4"
        },
        {
            "source": "8",
            "target": "1"
        },
        {
            "source": "8",
            "target": "2"
        },
        {
            "source": "8",
            "target": "5"
        },
        {
            "source": "9",
            "target": "3"
        },
        {
            "source": "10",
            "target": "4"
        }]

    graph["categories"] = [{"name": ""}, {"name": "Real-time Routing"}, {"name": "ASN"}, {"name": "inet6num"},
                           {"name": ""}, {"name": "country"}, {"name": "descpription"}, {"name": "route6"},
                           {"name": ""}]
    return graph


@app.route('/whois', methods=["POST"])
@cross_origin()
def whois():
    search_content = json.loads(request.get_data(as_text=True))['input_search']
    order = "whois " + search_content
    result = os.popen(order).read()  # os.popen() 方法用于从一个命令打开一个管道.参数是命令
    try:
        whois = str(result)
        whois_dict = {}
        whois_dict['whois'] = whois
        return whois_dict
    except:
        whois = "There is something wrong with your insert address. Please check it!"
        whois_dict = {}
        whois_dict['whois'] = whois
        return whois_dict


def create_dict():
    csv_file = open("/home/domain_api/res.csv", encoding='gbk')
    csv_reader_lines = csv.reader(csv_file)
    dict = {}
    for one_line in csv_reader_lines:
        ipv6_addresses = one_line[2].replace('"', '').replace(' ', '')
        domain_name = one_line[0]
        domain_type = one_line[3]
        IPv6_AS = one_line[8]
        IPv6_AS_name = one_line[9]
        IPv6_AS_descr = one_line[10]
        IPv6_AS_country = one_line[11]
        IID_type = one_line[12]
        content = one_line[13]
        structure = one_line[14]
        screenshot = one_line[15]
        network = one_line[16]
        subpage = one_line[17]
        v6support = one_line[18]

        if len(ipv6_addresses) != 0:
            ipv6_address_list = ipv6_addresses.split(',')

            for each_address in ipv6_address_list:
                address_dic = {}
                address_dic['domain_name'] = domain_name
                address_dic['domain_type'] = domain_type
                address_dic['IPv6_AS'] = IPv6_AS
                address_dic['IPv6_AS_name'] = IPv6_AS_name
                address_dic['IPv6_AS_description'] = IPv6_AS_descr
                address_dic['IPv6_AS_country'] = IPv6_AS_country
                address_dic['IID_type'] = IID_type
                if content == '#N/A':
                    address_dic['content'] = 0
                    address_dic['structure'] = 0
                    address_dic['screenshot'] = 0
                    address_dic['network'] = 0
                    address_dic['subpage'] = 0
                    address_dic['v6support'] = 0
                else:
                    address_dic['content'] = float(content)
                    address_dic['structure'] = float(structure)
                    address_dic['screenshot'] = float(screenshot)
                    address_dic['network'] = float(network)
                    address_dic['subpage'] = float(subpage)
                    address_dic['v6support'] = float(v6support)
                if each_address in dict.keys():
                    dict[each_address].append(address_dic)
                else:
                    dict[each_address] = []
                    dict[each_address].append(address_dic)
    return dict


@app.route('/website_domain', methods=["POST"])
@cross_origin()
def website_domain():
    search_content = json.loads(request.get_data(as_text=True))['input_search']
    dict = create_dict()
    ans = {}
    ans['picture_indicator'] = [
        {'name': 'content', 'max': 1},
        {'name': 'structure', 'max': 1},
        {'name': 'screenshot', 'max': 1},
        {'name': 'network', 'max': 1},
        {'name': 'subpage', 'max': 1},
    ]
    try:
        address_list = dict.get(search_content)
        address_dict = {}
        for each in address_list:
            if each.get('v6support') == 0:
                continue
            else:
                address_dict = each
                break
        ans["data"] = address_dict
        ans["data"]["IPv6_address"] = search_content
        picture_data = []
        picture_data.append(address_dict.get('content'))
        picture_data.append(address_dict.get('structure'))
        picture_data.append(address_dict.get('screenshot'))
        picture_data.append(address_dict.get('network'))
        picture_data.append(address_dict.get('subpage'))
        ans["picture_data"] = [
            {
                'value': picture_data,
            }
        ]
    except:
        ans["data"] = "There is no matching domain name for this address"
        ans["picture_data"] = [0, 0, 0, 0, 0]
    return ans


if __name__ == "__main__":
    IPv6_prefix_file = "/home/ipv6_space_api/routeviews-rv6-20201021-1200.pfx2as"
    IPv6_prefix_trie = create_IPv6_tree(IPv6_prefix_file)
    as_prefix_trie = create_asinfo_tree()
    inet6num_prefix_trie = create_inet6num_tree()
    route6_prefix_trie = create_route6_tree()
    geo_prefix_trie = create_geo_tree()
    dic_file = open("asinfo.txt", 'r')
    dic = {}
    for line in dic_file:
        dic = json.loads(line)
    dic_file.close()
    geo_raw = "/home/ASDict/geoipv6.csv"
    geo_dic = {}
    csv_file = open(geo_raw)
    csv_reader_lines = csv.reader(csv_file)
    for one_line in csv_reader_lines:
        each_geo = {}
        each_geo['country'] = one_line[2]
        each_geo['city'] = one_line[3]
        each_geo['postal_code'] = one_line[4]
        each_geo['latitude'] = one_line[5]
        each_geo['longitude'] = one_line[6]
        each_geo['accuracy_radius'] = one_line[7]
        geo_dic[one_line[1]] = each_geo  # v6网段为键
    countrytolat_dic = {'AD': {'latitude': 42.546245, 'longitude': 1.601554}, 'AE': {'latitude': 23.424076, 'longitude': 53.847818}, 'AF': {'latitude': 33.93911, 'longitude': 67.709953}, 'AG': {'latitude': 17.060816, 'longitude': -61.796428}, 'AI': {'latitude': 18.220554, 'longitude': -63.068615}, 'AL': {'latitude': 41.153332, 'longitude': 20.168331}, 'AM': {'latitude': 40.069099, 'longitude': 45.038189}, 'AN': {'latitude': 12.226079, 'longitude': -69.060087}, 'AO': {'latitude': -11.202692, 'longitude': 17.873887}, 'AQ': {'latitude': -75.250973, 'longitude': -0.071389}, 'AR': {'latitude': -38.416097, 'longitude': -63.616672}, 'AS': {'latitude': -14.270972, 'longitude': -170.132217}, 'AT': {'latitude': 47.516231, 'longitude': 14.550072}, 'AU': {'latitude': -25.274398, 'longitude': 133.775136}, 'AW': {'latitude': 12.52111, 'longitude': -69.968338}, 'AZ': {'latitude': 40.143105, 'longitude': 47.576927}, 'BA': {'latitude': 43.915886, 'longitude': 17.679076}, 'BB': {'latitude': 13.193887, 'longitude': -59.543198}, 'BD': {'latitude': 23.684994, 'longitude': 90.356331}, 'BE': {'latitude': 50.503887, 'longitude': 4.469936}, 'BF': {'latitude': 12.238333, 'longitude': -1.561593}, 'BG': {'latitude': 42.733883, 'longitude': 25.48583}, 'BH': {'latitude': 25.930414, 'longitude': 50.637772}, 'BI': {'latitude': -3.373056, 'longitude': 29.918886}, 'BJ': {'latitude': 9.30769, 'longitude': 2.315834}, 'BM': {'latitude': 32.321384, 'longitude': -64.75737}, 'BN': {'latitude': 4.535277, 'longitude': 114.727669}, 'BO': {'latitude': -16.290154, 'longitude': -63.588653}, 'BR': {'latitude': -14.235004, 'longitude': -51.92528}, 'BS': {'latitude': 25.03428, 'longitude': -77.39628}, 'BT': {'latitude': 27.514162, 'longitude': 90.433601}, 'BV': {'latitude': -54.423199, 'longitude': 3.413194}, 'BW': {'latitude': -22.328474, 'longitude': 24.684866}, 'BY': {'latitude': 53.709807, 'longitude': 27.953389}, 'BZ': {'latitude': 17.189877, 'longitude': -88.49765}, 'CA': {'latitude': 56.130366, 'longitude': -106.346771}, 'CC': {'latitude': -12.164165, 'longitude': 96.870956}, 'CD': {'latitude': -4.038333, 'longitude': 21.758664}, 'CF': {'latitude': 6.611111, 'longitude': 20.939444}, 'CG': {'latitude': -0.228021, 'longitude': 15.827659}, 'CH': {'latitude': 46.818188, 'longitude': 8.227512}, 'CI': {'latitude': 7.539989, 'longitude': -5.54708}, 'CK': {'latitude': -21.236736, 'longitude': -159.777671}, 'CL': {'latitude': -35.675147, 'longitude': -71.542969}, 'CM': {'latitude': 7.369722, 'longitude': 12.354722}, 'CN': {'latitude': 35.86166, 'longitude': 104.195397}, 'CO': {'latitude': 4.570868, 'longitude': -74.297333}, 'CR': {'latitude': 9.748917, 'longitude': -83.753428}, 'CU': {'latitude': 21.521757, 'longitude': -77.781167}, 'CV': {'latitude': 16.002082, 'longitude': -24.013197}, 'CX': {'latitude': -10.447525, 'longitude': 105.690449}, 'CY': {'latitude': 35.126413, 'longitude': 33.429859}, 'CZ': {'latitude': 49.817492, 'longitude': 15.472962}, 'DE': {'latitude': 51.165691, 'longitude': 10.451526}, 'DJ': {'latitude': 11.825138, 'longitude': 42.590275}, 'DK': {'latitude': 56.26392, 'longitude': 9.501785}, 'DM': {'latitude': 15.414999, 'longitude': -61.370976}, 'DO': {'latitude': 18.735693, 'longitude': -70.162651}, 'DZ': {'latitude': 28.033886, 'longitude': 1.659626}, 'EC': {'latitude': -1.831239, 'longitude': -78.183406}, 'EE': {'latitude': 58.595272, 'longitude': 25.013607}, 'EG': {'latitude': 26.820553, 'longitude': 30.802498}, 'EH': {'latitude': 24.215527, 'longitude': -12.885834}, 'ER': {'latitude': 15.179384, 'longitude': 39.782334}, 'ES': {'latitude': 40.463667, 'longitude': -3.74922}, 'ET': {'latitude': 9.145, 'longitude': 40.489673}, 'FI': {'latitude': 61.92411, 'longitude': 25.748151}, 'FJ': {'latitude': -16.578193, 'longitude': 179.414413}, 'FK': {'latitude': -51.796253, 'longitude': -59.523613}, 'FM': {'latitude': 7.425554, 'longitude': 150.550812}, 'FO': {'latitude': 61.892635, 'longitude': -6.911806}, 'FR': {'latitude': 46.227638, 'longitude': 2.213749}, 'GA': {'latitude': -0.803689, 'longitude': 11.609444}, 'GB': {'latitude': 55.378051, 'longitude': -3.435973}, 'GD': {'latitude': 12.262776, 'longitude': -61.604171}, 'GE': {'latitude': 42.315407, 'longitude': 43.356892}, 'GF': {'latitude': 3.933889, 'longitude': -53.125782}, 'GG': {'latitude': 49.465691, 'longitude': -2.585278}, 'GH': {'latitude': 7.946527, 'longitude': -1.023194}, 'GI': {'latitude': 36.137741, 'longitude': -5.345374}, 'GL': {'latitude': 71.706936, 'longitude': -42.604303}, 'GM': {'latitude': 13.443182, 'longitude': -15.310139}, 'GN': {'latitude': 9.945587, 'longitude': -9.696645}, 'GP': {'latitude': 16.995971, 'longitude': -62.067641}, 'GQ': {'latitude': 1.650801, 'longitude': 10.267895}, 'GR': {'latitude': 39.074208, 'longitude': 21.824312}, 'GS': {'latitude': -54.429579, 'longitude': -36.587909}, 'GT': {'latitude': 15.783471, 'longitude': -90.230759}, 'GU': {'latitude': 13.444304, 'longitude': 144.793731}, 'GW': {'latitude': 11.803749, 'longitude': -15.180413}, 'GY': {'latitude': 4.860416, 'longitude': -58.93018}, 'GZ': {'latitude': 31.354676, 'longitude': 34.308825}, 'HK': {'latitude': 22.396428, 'longitude': 114.109497}, 'HM': {'latitude': -53.08181, 'longitude': 73.504158}, 'HN': {'latitude': 15.199999, 'longitude': -86.241905}, 'HR': {'latitude': 45.1, 'longitude': 15.2}, 'HT': {'latitude': 18.971187, 'longitude': -72.285215}, 'HU': {'latitude': 47.162494, 'longitude': 19.503304}, 'ID': {'latitude': -0.789275, 'longitude': 113.921327}, 'IE': {'latitude': 53.41291, 'longitude': -8.24389}, 'IL': {'latitude': 31.046051, 'longitude': 34.851612}, 'IM': {'latitude': 54.236107, 'longitude': -4.548056}, 'IN': {'latitude': 20.593684, 'longitude': 78.96288}, 'IO': {'latitude': -6.343194, 'longitude': 71.876519}, 'IQ': {'latitude': 33.223191, 'longitude': 43.679291}, 'IR': {'latitude': 32.427908, 'longitude': 53.688046}, 'IS': {'latitude': 64.963051, 'longitude': -19.020835}, 'IT': {'latitude': 41.87194, 'longitude': 12.56738}, 'JE': {'latitude': 49.214439, 'longitude': -2.13125}, 'JM': {'latitude': 18.109581, 'longitude': -77.297508}, 'JO': {'latitude': 30.585164, 'longitude': 36.238414}, 'JP': {'latitude': 36.204824, 'longitude': 138.252924}, 'KE': {'latitude': -0.023559, 'longitude': 37.906193}, 'KG': {'latitude': 41.20438, 'longitude': 74.766098}, 'KH': {'latitude': 12.565679, 'longitude': 104.990963}, 'KI': {'latitude': -3.370417, 'longitude': -168.734039}, 'KM': {'latitude': -11.875001, 'longitude': 43.872219}, 'KN': {'latitude': 17.357822, 'longitude': -62.782998}, 'KP': {'latitude': 40.339852, 'longitude': 127.510093}, 'KR': {'latitude': 35.907757, 'longitude': 127.766922}, 'KW': {'latitude': 29.31166, 'longitude': 47.481766}, 'KY': {'latitude': 19.513469, 'longitude': -80.566956}, 'KZ': {'latitude': 48.019573, 'longitude': 66.923684}, 'LA': {'latitude': 19.85627, 'longitude': 102.495496}, 'LB': {'latitude': 33.854721, 'longitude': 35.862285}, 'LC': {'latitude': 13.909444, 'longitude': -60.978893}, 'LI': {'latitude': 47.166, 'longitude': 9.555373}, 'LK': {'latitude': 7.873054, 'longitude': 80.771797}, 'LR': {'latitude': 6.428055, 'longitude': -9.429499}, 'LS': {'latitude': -29.609988, 'longitude': 28.233608}, 'LT': {'latitude': 55.169438, 'longitude': 23.881275}, 'LU': {'latitude': 49.815273, 'longitude': 6.129583}, 'LV': {'latitude': 56.879635, 'longitude': 24.603189}, 'LY': {'latitude': 26.3351, 'longitude': 17.228331}, 'MA': {'latitude': 31.791702, 'longitude': -7.09262}, 'MC': {'latitude': 43.750298, 'longitude': 7.412841}, 'MD': {'latitude': 47.411631, 'longitude': 28.369885}, 'ME': {'latitude': 42.708678, 'longitude': 19.37439}, 'MG': {'latitude': -18.766947, 'longitude': 46.869107}, 'MH': {'latitude': 7.131474, 'longitude': 171.184478}, 'MK': {'latitude': 41.608635, 'longitude': 21.745275}, 'ML': {'latitude': 17.570692, 'longitude': -3.996166}, 'MM': {'latitude': 21.913965, 'longitude': 95.956223}, 'MN': {'latitude': 46.862496, 'longitude': 103.846656}, 'MO': {'latitude': 22.198745, 'longitude': 113.543873}, 'MP': {'latitude': 17.33083, 'longitude': 145.38469}, 'MQ': {'latitude': 14.641528, 'longitude': -61.024174}, 'MR': {'latitude': 21.00789, 'longitude': -10.940835}, 'MS': {'latitude': 16.742498, 'longitude': -62.187366}, 'MT': {'latitude': 35.937496, 'longitude': 14.375416}, 'MU': {'latitude': -20.348404, 'longitude': 57.552152}, 'MV': {'latitude': 3.202778, 'longitude': 73.22068}, 'MW': {'latitude': -13.254308, 'longitude': 34.301525}, 'MX': {'latitude': 23.634501, 'longitude': -102.552784}, 'MY': {'latitude': 4.210484, 'longitude': 101.975766}, 'MZ': {'latitude': -18.665695, 'longitude': 35.529562}, 'NA': {'latitude': -22.95764, 'longitude': 18.49041}, 'NC': {'latitude': -20.904305, 'longitude': 165.618042}, 'NE': {'latitude': 17.607789, 'longitude': 8.081666}, 'NF': {'latitude': -29.040835, 'longitude': 167.954712}, 'NG': {'latitude': 9.081999, 'longitude': 8.675277}, 'NI': {'latitude': 12.865416, 'longitude': -85.207229}, 'NL': {'latitude': 52.132633, 'longitude': 5.291266}, 'NO': {'latitude': 60.472024, 'longitude': 8.468946}, 'NP': {'latitude': 28.394857, 'longitude': 84.124008}, 'NR': {'latitude': -0.522778, 'longitude': 166.931503}, 'NU': {'latitude': -19.054445, 'longitude': -169.867233}, 'NZ': {'latitude': -40.900557, 'longitude': 174.885971}, 'OM': {'latitude': 21.512583, 'longitude': 55.923255}, 'PA': {'latitude': 8.537981, 'longitude': -80.782127}, 'PE': {'latitude': -9.189967, 'longitude': -75.015152}, 'PF': {'latitude': -17.679742, 'longitude': -149.406843}, 'PG': {'latitude': -6.314993, 'longitude': 143.95555}, 'PH': {'latitude': 12.879721, 'longitude': 121.774017}, 'PK': {'latitude': 30.375321, 'longitude': 69.345116}, 'PL': {'latitude': 51.919438, 'longitude': 19.145136}, 'PM': {'latitude': 46.941936, 'longitude': -56.27111}, 'PN': {'latitude': -24.703615, 'longitude': -127.439308}, 'PR': {'latitude': 18.220833, 'longitude': -66.590149}, 'PS': {'latitude': 31.952162, 'longitude': 35.233154}, 'PT': {'latitude': 39.399872, 'longitude': -8.224454}, 'PW': {'latitude': 7.51498, 'longitude': 134.58252}, 'PY': {'latitude': -23.442503, 'longitude': -58.443832}, 'QA': {'latitude': 25.354826, 'longitude': 51.183884}, 'RE': {'latitude': -21.115141, 'longitude': 55.536384}, 'RO': {'latitude': 45.943161, 'longitude': 24.96676}, 'RS': {'latitude': 44.016521, 'longitude': 21.005859}, 'RU': {'latitude': 61.52401, 'longitude': 105.318756}, 'RW': {'latitude': -1.940278, 'longitude': 29.873888}, 'SA': {'latitude': 23.885942, 'longitude': 45.079162}, 'SB': {'latitude': -9.64571, 'longitude': 160.156194}, 'SC': {'latitude': -4.679574, 'longitude': 55.491977}, 'SD': {'latitude': 12.862807, 'longitude': 30.217636}, 'SE': {'latitude': 60.128161, 'longitude': 18.643501}, 'SG': {'latitude': 1.352083, 'longitude': 103.819836}, 'SH': {'latitude': -24.143474, 'longitude': -10.030696}, 'SI': {'latitude': 46.151241, 'longitude': 14.995463}, 'SJ': {'latitude': 77.553604, 'longitude': 23.670272}, 'SK': {'latitude': 48.669026, 'longitude': 19.699024}, 'SL': {'latitude': 8.460555, 'longitude': -11.779889}, 'SM': {'latitude': 43.94236, 'longitude': 12.457777}, 'SN': {'latitude': 14.497401, 'longitude': -14.452362}, 'SO': {'latitude': 5.152149, 'longitude': 46.199616}, 'SR': {'latitude': 3.919305, 'longitude': -56.027783}, 'ST': {'latitude': 0.18636, 'longitude': 6.613081}, 'SV': {'latitude': 13.794185, 'longitude': -88.89653}, 'SY': {'latitude': 34.802075, 'longitude': 38.996815}, 'SZ': {'latitude': -26.522503, 'longitude': 31.465866}, 'TC': {'latitude': 21.694025, 'longitude': -71.797928}, 'TD': {'latitude': 15.454166, 'longitude': 18.732207}, 'TF': {'latitude': -49.280366, 'longitude': 69.348557}, 'TG': {'latitude': 8.619543, 'longitude': 0.824782}, 'TH': {'latitude': 15.870032, 'longitude': 100.992541}, 'TJ': {'latitude': 38.861034, 'longitude': 71.276093}, 'TK': {'latitude': -8.967363, 'longitude': -171.855881}, 'TL': {'latitude': -8.874217, 'longitude': 125.727539}, 'TM': {'latitude': 38.969719, 'longitude': 59.556278}, 'TN': {'latitude': 33.886917, 'longitude': 9.537499}, 'TO': {'latitude': -21.178986, 'longitude': -175.198242}, 'TR': {'latitude': 38.963745, 'longitude': 35.243322}, 'TT': {'latitude': 10.691803, 'longitude': -61.222503}, 'TV': {'latitude': -7.109535, 'longitude': 177.64933}, 'TW': {'latitude': 23.69781, 'longitude': 120.960515}, 'TZ': {'latitude': -6.369028, 'longitude': 34.888822}, 'UA': {'latitude': 48.379433, 'longitude': 31.16558}, 'UG': {'latitude': 1.373333, 'longitude': 32.290275}, 'UM': {'latitude': 0, 'longitude': 0}, 'US': {'latitude': 37.09024, 'longitude': -95.712891}, 'UY': {'latitude': -32.522779, 'longitude': -55.765835}, 'UZ': {'latitude': 41.377491, 'longitude': 64.585262}, 'VA': {'latitude': 41.902916, 'longitude': 12.453389}, 'VC': {'latitude': 12.984305, 'longitude': -61.287228}, 'VE': {'latitude': 6.42375, 'longitude': -66.58973}, 'VG': {'latitude': 18.420695, 'longitude': -64.639968}, 'VI': {'latitude': 18.335765, 'longitude': -64.896335}, 'VN': {'latitude': 14.058324, 'longitude': 108.277199}, 'VU': {'latitude': -15.376706, 'longitude': 166.959158}, 'WF': {'latitude': -13.768752, 'longitude': -177.156097}, 'WS': {'latitude': -13.759029, 'longitude': -172.104629}, 'XK': {'latitude': 42.602636, 'longitude': 20.902977}, 'YE': {'latitude': 15.552727, 'longitude': 48.516388}, 'YT': {'latitude': -12.8275, 'longitude': 45.166244}, 'ZA': {'latitude': -30.559482, 'longitude': 22.937506}, 'ZM': {'latitude': -13.133897, 'longitude': 27.849332}, 'ZW': {'latitude': -19.015438, 'longitude': 29.154857}}
    app.after_request(after_request)
    app.run(host="::", port=7077)
