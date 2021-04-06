<template>
  <!-- <div style="position: relative; padding-bottom: 40px; min-height: 100%;"> -->
  <div style="display: flex; flex-direction: column; min-height: 100vh;">
    <div class="not-bottom">
      <head-nav />
      <div class="img">
        <img src="~@/assets/images/AS.png" alt="">
      </div>
      <div class="middle">
        <el-form :inline="true" ref="form">
            <el-form-item>
              <el-input v-model="search" placeholder="请输入要查询的IP地址" @keyup.enter.native="searchButton()"></el-input>
            </el-form-item>
            <el-form-item>
              <el-button type="primary" @click="searchButton()">Search</el-button>
            </el-form-item>
          </el-form>
      </div>
      <div class="tabs">
        <ul class="list">
          <li v-for="(item, index) in selected" :key="index" @click="select(index)">
            <a href="javaScript:void(0)" :class="{active:isSelected === index}">{{item}}</a>
          </li>
        </ul>
      </div>
      <div class="content">
        <div class="content-container clearfix"  v-show="isSelected === 0">
          <div class="left">
            <div id="container" class="chart-container1"></div>
          </div>
          <div class="right">
            <div style="position: relative;">
              <h4 class="right-title">IPv6地理位置信息</h4>
              <ul>
                <li v-for="(item, index) in Object.keys(basic)" :key="index">
                    <div class="front">{{item}} :</div>
                    <div class="following">{{basic[item]}}</div>
                </li>
              </ul>
            </div>
          </div>
        </div>
        <div class="content-container clearfix" v-show="isSelected === 1">
          <div class="left">
            <div class="topov6" id="topov6" ref="topov6"></div>
          </div>
          <div class="right">
            <div style="position: relative;">
              <h4 class="right-title">IPv6网络位置信息</h4>
              <ul>
                <li v-for="(item, index) in Object.keys(route)" :key="index">
                  <div class="front">{{item}} :</div>
                  <div class="following">{{route[item]}}</div>
                </li>
              </ul>
            </div>
          </div>
        </div>
        <div class="content-container" v-show="isSelected === 2">
          <path-graph :paths="v6Propagation" :isclick="isclick"></path-graph>
        </div>
        <div class="content-container" v-show="isSelected === 3">
          <div id="pos3" class="pos3"></div>
        </div>
        <div class="content-container" v-show="isSelected === 4">
          <statistic-block :picture="picture" />
        </div>
        <div class="content-container" v-show="isSelected === 5">
          <relation-graph :relation_graph="relation_graph" />
        </div>
        <div class="content-container" v-show="isSelected === 6">
          <div class="whois">
            <el-scrollbar>
              <div class="whois-title">{{ this.whois_title }}</div>
              <div
                      class="whois-content"
                      style="
                      overflow: hidden;
                      text-overflow: ellipsis;
                      white-space: nowrap;
                    "
                      v-for="item in this.whois"
                      :key="item.index"
              >
                <i class="el-icon-s-tools"></i>
                {{ item }}
              </div>
            </el-scrollbar>
          </div>
        </div>
        <div class="content-container clearfix" v-show="isSelected === 7">
          <div class="organization_as">
            <el-scrollbar>
              <div class="whois-title">4134兄弟AS相关信息</div>
              <div class="whois-table">
                <table border="1" width="100%" style="table-layout:fixed"> 
                  <thead>
                    <tr class="title">
                      <th width="7%">asn</th>
                      <th width="15%">as-name</th>
                      <th>mnt-by</th>
                      <th width="30%">descr</th>
                    </tr>
                  </thead>
                  <tbody>
                    <tr v-for="(item, index) in list4134" :key="index">
                      <td :title=item.asn class="asn"><span class="asn">{{item.asn}}</span></td>
                      <td :title=item.as_name><span>{{item.as_name}}</span></td>
                      <td :title=item.mnt_by><span>{{item.mnt_by}}</span></td>
                      <td :title=item.descr><span>{{item.descr}}</span></td>
                    </tr>
                  </tbody>
                </table>
              </div>
            </el-scrollbar>
          </div>
        </div>
      </div>
    </div>
    <div class="bottom">
      <span>@2021 穹眼安全 京ICP备18044233号-2</span>
    </div>
  </div>
</template>

<script>
  import headNav from "@/components/HeadNav";
  import pathGraph from "@/components/pathGraph";
  import RelationGraph from "@/components/RelationGraph";
  import StatisticBlock from "@/components/StatisticBlock";
  import StatisticBlockt from "@/components/StatisticBlockt";
  import {requestBasic, requestWebSite,requestPos3Data, requestInet6, requestMapData} from "../../network/requestHome";
  let json = require('@/utils/countrytolat.json');
  let json4134 = require('@/utils/4134.json');
  export default {
    name: "index",
    inject:['reload'],
    components:{
      headNav,
      pathGraph,
      RelationGraph,
      StatisticBlock,
      StatisticBlockt,
    },
    data() {
      return {
        search: '', // input输入框
        selected: ['地理位置','网络位置','传播路径','路由波动', '路由宣告','关联关系','Whois','机构AS'],
        details: ['前缀', '国家', '洲', '城市', '经纬度', '自治域', '机构', '运营商', '网路类型', '技术联系人', '邮箱', '电话'],
        isSelected:0, // 默认选中第一个
        //首页地图定位需要的数据
        city:'',
        country:'',
        longitude:'',
        latitude:'',
        basic: {},
        route: [],
        inet: [],
        whois: [],
        isclick: false,
        whois_title: "",
        tableData: [],
        data: [],  // 世界地图经纬度信息
        relation_graph: "",
        picture: "",
        v6Propagation:[],
        indicator: [], //雷达图的各个维度
        chartData: [], //雷达图series 中的data
        // 路由波动图的数据
        pos3Data1:[],
        pos3Data2:[],
        timeData:[],
        list4134: null,
      }
    },
    mounted() {
        this.getIP();
        this.paint()
        this.getExcel();
    },
    methods:{
      select(index) {
        this.isSelected = index
        if (index == 1){
          window.RenderTopo(null, this.$refs.topov6, this.basic["归属国家"], () => {});
        }
        if(index === 2) {
          this.isclick = true
        }else{
          this.isclick = false
        }
      },
      paint() {
        let myChart = this.$echarts.init(document.getElementById('container'))
        let nowClientWidth = document.documentElement.clientWidth;
        function nowSize(val, initWidth=1280){
          return val * (nowClientWidth/initWidth);
        }
        myChart.setOption({
          tooltip: {
            trigger: 'item',
            triggerOn: 'mousemove'
          },
          series: [
            {
              type: "map",
              name: "test",
              coordinateSystem:'geo',
              label: {
                show: false,
                position: "top",
                margin: 5
              },
              mapType: "world",
              roam: false,
              zoom: 1.15,
              // center: [115.97, 29.71],
              // 去除各个国家上的小红点
              showLegendSymbol: false,
              markPoint: {//动态标记
                large: true,//这个选项，悬浮自动失效
                symbolSize: 9,
                symbol: 'circle',
                itemStyle: {
                  normal: {
                    shadowBlur: 2,
                    shadowColor: 'rgba(37, 140, 249, 0.8)',
                    color: '#f00'
                  }
                },
                data: this.data
              }
            }
          ],
        })
        window.onresize = myChart.resize;
      },
      // 雷达图
      paint1() {
        let myChartlei = this.$echarts.init(document.getElementById('leidatu'))
        let nowClientWidth = document.documentElement.clientWidth;
        function nowSize(val, initWidth=1280){
          return val * (nowClientWidth/initWidth);
        }
        myChartlei.setOption({
          title: {
            // text: '基础雷达图'
          },
          tooltip: {},
          legend: {
            // data: ['预算分配（Allocated Budget）', '实际开销（Actual Spending）']
          },
          radar: {
            // shape: 'circle',
            name: {
              textStyle: {
                color: '#fff',
                backgroundColor: '#999',
                borderRadius: 2,
                padding: [2, 4],
                fontSize: 11,
              }
            },
            indicator: this.indicator
          },
          series: [{
            // name: '预算 vs 开销（Budget vs spending）',
            type: 'radar',
            // areaStyle: {normal: {}},
            data: this.chartData
          }]
        })
        window.onresize = myChartlei.resize;
      },
      // 路由波动图
      paintPos3() {
        let myChartpos = this.$echarts.init(document.getElementById('pos3'))
        var total_data1 = [];
        for (var i = 0; i<this.timeData.length; i++) {
          total_data1.push([this.timeData[i], this.pos3Data1[i]])
        }
        var total_data2 = [];
        for (var i = 0; i<this.timeData.length; i++) {
          total_data2.push([this.timeData[i], this.pos3Data2[i]])
        }
        var timeData = this.timeData;
        console.log('total_data1:', total_data1);
        console.log('total_data2:', total_data2)
        myChartpos.setOption({
          axisPointer: {
            link: {xAxisIndex: 'all'}
          },
          dataZoom: [
            {
              show: true,
              realtime: true,
              start: 0,
              end: 60,
              xAxisIndex: [0, 1],
              height: 22,
              bottom: 5,
            },
            {
              type: 'inside',
              realtime: true,
              start: 0,
              end: 60,
              xAxisIndex: [0, 1]
            }
          ],
          grid: [{
            top: 23,
            left: 50,
            right: 50,
            height: 125
          }, {
            left: 50,
            right: 50,
            top: 200,
            height: 110
          }],
          xAxis: [
            {
              type: 'time',
              boundaryGap: false,
              axisLine: {onZero: true},
              splitLine:{  
                show:false  
              },
              interval: 1000 * 3600 * 8,
              axisLabel: {
                textStyle: {
                  fontSize: 14,
                },
                formatter: function (value, idx) {
                  var date = new Date(value)
                  const hour = date.getHours();
                  const minute = date.getMinutes() < 10 ? '0' + date.getMinutes() : date.getMinutes();
                  const second = date.getSeconds();
                  return [date.getMonth() + 1, date.getDate()].join('-') + ' ' + [date.getHours(), minute].join(':');
                  // return idx === 0 ? value : [date.getMonth() + 1, date.getDate()].join('-');  // 判断 ？对值：错值
                }
              }
            },
            {
              gridIndex: 1,
              type: 'time',
              boundaryGap: false,
              axisLine: {onZero: true},
              splitLine:{  
                show:false  
              },
              interval: 1000 * 3600 * 8,
              position: 'top',
              axisLabel: {
                textStyle: {
                  fontSize: 14,
                },
                formatter: function (value, idx) {
                  var date = new Date(value)
                  const hour = date.getHours();
                  const minute = date.getMinutes() < 10 ? '0' + date.getMinutes() : date.getMinutes();
                  const second = date.getSeconds();
                  return [date.getMonth() + 1, date.getDate()].join('-') + ' ' + [date.getHours(), minute].join(':');
                  // return idx === 0 ? value : [date.getMonth() + 1, date.getDate()].join('-');  // 判断 ？对值：错值
                }
              }
            }
          ],
          yAxis: [
            {
              name: '',
              type: 'value',
              max: function(value){
                return value.max+2;
              },
              minInterval: 1,
              axisLabel: {
                textStyle: {
                  fontSize: 13,
                }
              }
            },
            {
              gridIndex: 1,
              name: '',
              type: 'value',
              max: function(value){
                return value.max+2;
              },
              minInterval: 1,
              inverse: true,
              axisLabel: {
                textStyle: {
                  fontSize: 13,
                }
              }
            }
          ],
          series: [
            {
              name: '',
              top: 0,
              type: 'line',
              lineStyle: {
                width: 2,
              },
              symbolSize: 0,
              hoverAnimation: false,
              data: total_data1,
            },
            {
              name: '',
              type: 'line',
              lineStyle: {
                width: 2,
              },
              xAxisIndex: 1,
              yAxisIndex: 1,
              symbolSize: 0,
              hoverAnimation: false,
              data: total_data2,
            }
          ]
        })
        window.onresize = myChartpos.resize;
      },
      // 网络请求相关的方法  
      getIP() {
        this.$axios({
          method: 'get',
          url: 'http://api.ipv6rank.com:7075/get_ip',
          //url: 'http://10.6.101.12:7075/get_ip',
        }).then(res => {
          console.log("res::", res);
          this.search = res['data']['ip'];
          // this.getData();
          this.getBasicData()
          this.getAddData()
          this.getRouteData()
          this.getPosData()
          this.getRelationGraph()
          this.getWhoIsData()
          this.getPicture()
        }).catch(error => {
          console.log(error);
        })
      },
      // 地理位置数据请求
      getBasicData() {
        console.info("ip获取到::", this.search);
        // 验证IPv6地址是否合法
        let pattern = new RegExp(/^s*((([0-9A-Fa-f]{1,4}:){7}([0-9A-Fa-f]{1,4}|:))|(([0-9A-Fa-f]{1,4}:){6}(:[0-9A-Fa-f]{1,4}|((25[0-5]|2[0-4]d|1dd|[1-9]?d)(.(25[0-5]|2[0-4]d|1dd|[1-9]?d)){3})|:))|(([0-9A-Fa-f]{1,4}:){5}(((:[0-9A-Fa-f]{1,4}){1,2})|:((25[0-5]|2[0-4]d|1dd|[1-9]?d)(.(25[0-5]|2[0-4]d|1dd|[1-9]?d)){3})|:))|(([0-9A-Fa-f]{1,4}:){4}(((:[0-9A-Fa-f]{1,4}){1,3})|((:[0-9A-Fa-f]{1,4})?:((25[0-5]|2[0-4]d|1dd|[1-9]?d)(.(25[0-5]|2[0-4]d|1dd|[1-9]?d)){3}))|:))|(([0-9A-Fa-f]{1,4}:){3}(((:[0-9A-Fa-f]{1,4}){1,4})|((:[0-9A-Fa-f]{1,4}){0,2}:((25[0-5]|2[0-4]d|1dd|[1-9]?d)(.(25[0-5]|2[0-4]d|1dd|[1-9]?d)){3}))|:))|(([0-9A-Fa-f]{1,4}:){2}(((:[0-9A-Fa-f]{1,4}){1,5})|((:[0-9A-Fa-f]{1,4}){0,3}:((25[0-5]|2[0-4]d|1dd|[1-9]?d)(.(25[0-5]|2[0-4]d|1dd|[1-9]?d)){3}))|:))|(([0-9A-Fa-f]{1,4}:){1}(((:[0-9A-Fa-f]{1,4}){1,6})|((:[0-9A-Fa-f]{1,4}){0,4}:((25[0-5]|2[0-4]d|1dd|[1-9]?d)(.(25[0-5]|2[0-4]d|1dd|[1-9]?d)){3}))|:))|(:(((:[0-9A-Fa-f]{1,4}){1,7})|((:[0-9A-Fa-f]{1,4}){0,5}:((25[0-5]|2[0-4]d|1dd|[1-9]?d)(.(25[0-5]|2[0-4]d|1dd|[1-9]?d)){3}))|:)))(%.+)?s*$/)
        if(pattern.test(this.search)) {
          requestMapData(this.search).then(res => {
            console.log("requestMapData::", res)
            this.city  = res.city ? res.city:'暂无'
            this.country = res.country
            this.longitude = res.longitude
            this.latitude = res.latitude
            let obj = {}
            obj.name = res.country
            obj.coord = [res.longitude,res.latitude]
            this.data = []
            this.data.push(obj)
            this.paint()
            this.reload()
          })
          requestBasic(this.search).then(res => {
            console.log("requestBasic::", res)
            this.v6Propagation = res['longest_prefix']['v6Propagation']
            Object.keys(res.longest_prefix).forEach(key => {
              if (!res[key]) delete res[key]
            })
            let {ASN, as_type, aut_name, country, descr, org_id, org_name, prefix, sibling} = res.longest_prefix
            this.basic = {
              '路由前缀': prefix,
              '归属国家': this.country,
              '归属城市': this.city,
              '经 度': this.longitude,
              '纬 度': this.latitude,
              '归属AS': ASN,
              'AS名称': aut_name,
              '归属机构': org_name
            }
          }).catch(error => {
            console.log(error);
          })
        }else{
          alert('IPv6地址格式有误')
        }
      },
      // 网络位置请求方法
      getAddData() {
        requestBasic(this.search).then(res => {
          requestInet6(this.search).then(res => {
            this.route['维护人'] = res['admin-c']
          })
          Object.keys(res.longest_prefix).forEach(key => {
            if (!res[key]) delete res[key]
          })
          let {ASN, as_type, aut_name, country, descr, org_id, org_name, prefix, sibling} = res.longest_prefix
          this.route = {
            '路由前缀': prefix,
            'AS名称': aut_name,
            '归属国家': country,
            'AS类型': as_type,
            'AS描述': descr,
            '归属机构': org_name,
            // '邮箱' : 'mail',
            // '电话': 'phone'
          }
          // console.log(this.center);
        }).catch(error => {
          console.log(error);
        })
      },
      // 路由波动数据请求
      getPosData() {
        requestPos3Data(this.search).then(res => {
          console.log('pos::',res);
          this.timeData = res.picture12_x
          this.pos3Data1 = res.picture1_data
          this.pos3Data2 = res.picture2_data
          // this.timeData = this.timeData.map(item => {
          //   return item.replace('2021/','')
          // })
          this.paintPos3()
        })
      },
      // 网站数据请求
      getRouteData() {
        requestWebSite(this.search).then(res => {
           this.chartData = res.picture_data
           this.indicator = res.picture_indicator
          // console.log('111',res.picture_data,res.picture_indicator);
          this.paint1()
          requestBasic(this.search).then(res => {
            this.inet['路由前缀'] = res.longest_prefix.prefix ?res.longest_prefix.prefix:'暂未查询到相关信息'
          })
          // Object.keys(res.longest_prefix).forEach(key => {
          //   if (!res[key]) delete res[key]
          // })
          let {domain_name, domian_type,IPv6_address,v6support,IPv6_AS_name, IPv6_AS_description, IID_type, IPv6_AS} = res.data
          this.inet = {
            '网站名称': domain_name ? domain_name:'暂未查询到相关信息',
            '网站类型': domian_type? domian_type:'暂未查询到相关信息',
            // '网站子类': 'city',
            'IPv6地址': IPv6_address? IPv6_address:'暂未查询到相关信息',
            '所属AS': IPv6_AS? IPv6_AS:'暂未查询到相关信息',
            'AS名称': IPv6_AS_name? IPv6_AS_name:'暂未查询到相关信息',
            'AS描述' : IPv6_AS_description? IPv6_AS_description:'暂未查询到相关信息',
            '地址类型': IID_type? IID_type:'暂未查询到相关信息',
            'IPv6支持度': v6support? v6support:'暂未查询到相关信息'
          }
          // console.log(this.center);
        }).catch(error => {
          console.log(error);
        })
      },
      getWhoIsData() {
        this.$axios({
          method: 'post',
          url: 'http://api.ipv6rank.com:7072/whois',
          //url: 'http://10.6.101.12:7072/whois',
          data:{
            ip_address: this.search
          }
        }).then(res => {
          // console.log(res.data.whois.split('\n').filter(item => item!==''));
          this.whois = Array.from(new Set(res.data.whois.split('\n').filter(item => item!=='')))
          this.whois_title = this.whois[0];
          this.whois.splice(0, 1);
        }).catch(error => {
          console.log(error);
        })
      },
      getRelationGraph() {
        this.$axios({
          method: 'post',
          url: 'http://api.ipv6rank.com:7071/relation_graph',
          //url: 'http://10.6.101.12:7071/relation_graph',
          data:{
            ip_address: this.search
          }
        }).then(res => {
          this.relation_graph = res['data'];
        }).catch(error => {
          console.log(error);
        })
      },
      getPicture() {
        this.$axios({
          method: 'post',
          url: 'http://api.ipv6rank.com:7073/picture',
          //url: 'http://10.6.101.12:7073/picture',
          data:{
            ip_address: this.search
          }
        }).then(res => {
          this.picture = res['data'];
          console.log("res::", this.picture)
        }).catch(error => {
          console.log(error);
        })
      },
      getExcel() {
        this.list4134 = json4134;
        console.log('json4134:', json4134[0].as_name);
      },

      // 点击搜索后请求所有的数据
      searchButton() {
        this.$router.push({name: 'homeAfterSearch', params: {searchContent: this.search}});
      }
    },
  }
</script>

<style lang="scss" scoped>
  @import "~@/assets/css/reset.css";
  .not-bottom {
    flex: 1;
  }
  .img{
    img {
      position: relative;
      width: 18%;
    }
    margin-top: 3.8%;
    text-align: center;
  }
  .middle{
    width: 600px;
    margin: 20px auto;
    .el-form-item {
      margin: 0;
    }
    .el-form-item:first-of-type {
      width: 87%;
    }
    .el-form-item:last-of-type {
      width: 13%;
    }
    .el-form-item /deep/ .el-form-item__content {
      line-height: 100%;
      display: inline;
    }
    .el-input /deep/ .el-input__inner {
      height: 37px;
      border-radius: 6px 0 0 6px;
      border: 2px solid #d4d4d4;
      border-right: 1px solid transparent;
    }
    .el-input /deep/ .el-input__inner:focus {
      border-color: #b6b6b6;
    }
    .el-form-item /deep/ .el-button--primary {
      font-size: 15px;
      background-color: #b6b6b6;
      border-color: #cecece;
    }
    .el-button {
      height: 37px;
      width: 80px;
      border-radius: 0 6px 6px 0;
      display: flex;
      justify-content: center;
      align-items: center;
    }
  }
  /* tab选项卡的样式 */
  .tabs{
    display: flex;
    justify-content: center;
    width: 880px;
    height: 36px;
    margin: 35px auto 0 auto;
    /*border-bottom: 1px solid #000;*/
    background-color: #f5f5f5;
    .list{
      display: flex;
      justify-content: space-around;
      width: 100%;
      position: relative;
      li:first-child{
        margin-left: 50px;
      }
      li:last-child{
        margin-right: 50px;
      }
      li{
        height: 30px;
        a{
          margin-top: 5px;
          padding: 3px 6px 8px 6px;
          height: 20px;
          color: #009a61;
          font-size: 18px;
        }
      }
    }
  }
  /* 内容样式 */
  .content{
    width: 878px;
    height: 380px;
    border: 1px solid rgb(194, 194, 194);
    margin: 0 auto;
    background-color: #fff;
    .content-container{
      .left{
        width: 450px;
        height: 380px;
        float: left;
        .topov6 {
          padding-top: 10px;
          padding-bottom: 10px;
          height:350px;
          //width: 450px;
          .sigma-mouse,
          .sigma-scene {
            height: 350px;
          }
        }
        .chart-container1 {
          width: 450px;
          height: 380px;
        }
        .chart-container2 {
          width: 450px;
          height: 380px;
          margin-left: 10px;
        }
      }
      .right{
        width: 370px;
        float: right;
        //font-size: 13px;
        .right-title{
          margin-left: 50px;
          padding: 3px 0;
          width: 220px;
          text-align: center;
          margin-top: 20px;
          margin-bottom: 15px;
          border: 1px solid #666;
        }
        ul li{
          display: flex;
          margin-bottom: 12px;
          .front {
            flex: 1;
            text-align: right;
          }
          .following {
            flex: 2;
            margin-left: 10px;
            text-overflow: ellipsis;
            overflow: hidden;
            white-space: nowrap
          }
        }
      }
      #pathGraph {
        display: flex;
        justify-content: center;
        align-items: center;
        height: 379px;
        width: 876px;
        margin-left: 0;
      }
      .pos3{
        width: 878px;
        height:380px;
      }
      .whois {
        width: 855px;
        height: 380px; /*这里我用了计算属性*/
        display: flex;
        flex-direction: column;
        flex-wrap: wrap;
        //font-size: 18.5px;
        padding-left: 25px;
        padding-bottom: 10px;
        .el-scrollbar{
          height: 380px; /*此处一定要设置高度，不然内层的计算属性不生效*/
        }
        .el-scrollbar /deep/ .el-scrollbar__wrap {
          // width: 300px; /*将垂直滚动条挤到可视区域之外*/
          //height: 0; /*将水平滚动条挤到可视区域之外*/
          overflow-x: hidden;
        }
        .whois-title {
          padding-top: 7px;
          padding-bottom: 7px;
          color: #3e3d7a;
          font-weight: bold;
          text-align: center;
        }
      }
      .organization_as {
        width: 878px;
        height: 380px; /*这里我用了计算属性*/
        display: flex;
        .whois-table {
          width: 95%;
          margin-left: 2.5%;
          table, table tr th, table tr td { border:1px solid #b9b9b9; }
          table {
            width: 100%;
            border-collapse: collapse;
            font-size: 15px;
            th {
              background: rgb(243, 243, 243);
              height: 34px;
              font-size: 16px;
              font-weight: normal;
            }
            tbody td {
              height: 32px;
              width: 100%;
              white-space: nowrap;
              overflow: hidden;
              text-overflow: ellipsis;
            }
            td[class*=asn] {
              text-align: center;
            }
            td span:not([class*=asn]){
              margin-left: 5px;
              margin-right: 5px;
            }
          }
        }
        .el-scrollbar{
          height: 380px; /*此处一定要设置高度，不然内层的计算属性不生效*/
        }
        .el-scrollbar /deep/ .el-scrollbar__wrap {
          // width: 300px; /*将垂直滚动条挤到可视区域之外*/
          //height: 0; /*将水平滚动条挤到可视区域之外*/
          overflow-x: hidden;
        }
        .whois-title {
          padding-top: 8px;
          padding-bottom: 10px;
          color: #3e3d7a;
          font-weight: bold;
          text-align: center;
        }
      }
    }
    /* 清浮动 */
    .clearfix:after{
      content: "" ;
      display: block;
      height: 0;
      clear: both;
      visibility: hidden;
    }
  }
  /* 选中tab时的样式 */
  .active{
    background: #fff;
    border: 1.3px solid rgb(218, 218, 218);
    border-bottom: 1px solid transparent;
  }
 
  .map {
    height: 380px;
  }
  .bottom {
    background: rgb(245, 245, 245);
  }
</style>
