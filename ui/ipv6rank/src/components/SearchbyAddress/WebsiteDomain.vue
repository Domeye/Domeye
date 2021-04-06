<template>
  <div class="webdomain clearfix">
    <div class="left">
      <div id="radar" class="radar"></div>
    </div>
    <div class="right">
      <div style="position: relative;">
        <h4 class="right-title">网站域名相关信息</h4>
        <ul>
          <li v-for="(item, index) in Object.keys(basic)" :key="index">
            <div class="front">{{item}} :</div>
            <div class="following">{{basic[item]}}</div>
          </li>
        </ul>
      </div>
    </div>
  </div>
</template>

<script>
import {getwebDomain, getlongestAsPrefix} from "../../api/apiData";

export default {
  name: 'WebsiteDomain',
  props: ["input"],
  data() {
    return {
      data_webDomain: '',
      data_as: '',
      radarData: '',
      indicator: '',
      basic: '',
    }
  },
  watch: {
    input() {
      this.getData();
    }
  },
  mounted() {
    this.getData();
  },
  methods: {
    async getData() {
      await getwebDomain(this.input).then(res => {
        this.data_webDomain = res
      })
      await getlongestAsPrefix(this.input).then(res => {
        this.data_as = res['longest_prefix']
      })
      this.getrealData();
    },
    getrealData() {
      this.radarData = this.data_webDomain['picture_data'];
      this.indicator = this.data_webDomain['picture_indicator'];
      this.basic = {
        '网站名称':this.data_webDomain['data']['domain_name'] ? this.data_webDomain['data']['domain_name']:'暂未查询到相关信息',
        '网站类型': this.data_webDomain['data']['domain_type']? this.data_webDomain['data']['domain_type']:'暂未查询到相关信息',
        'IPv6地址': this.data_webDomain['data']['IPv6_AS_country']? this.data_webDomain['data']['IPv6_AS_country']:'暂未查询到相关信息',
        '所属AS': this.data_webDomain['data']['IPv6_AS']? this.data_webDomain['data']['IPv6_AS']:'暂未查询到相关信息',
        'AS名称': this.data_webDomain['data']['IPv6_AS_name']? this.data_webDomain['data']['IPv6_AS_name']:'暂未查询到相关信息',
        'AS描述' : this.data_webDomain['data']['IPv6_AS_description']? this.data_webDomain['data']['IPv6_AS_description']:'暂未查询到相关信息',
        '地址类型': this.data_webDomain['data']['IID_type']? this.data_webDomain['data']['IID_type']:'暂未查询到相关信息',
        'IPv6支持度': this.data_webDomain['data']['v6support']? this.data_webDomain['data']['v6support']:'暂未查询到相关信息',
        '路由前缀': this.data_as['prefix']? this.data_as['prefix']:'暂未查询到相关信息',
      }
      console.log("网站basic:", this.basic)
      this.drawRadar();
    },
    drawRadar() {
      let radar = this.$echarts.init(document.getElementById('radar'))
      radar.setOption({
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
          type: 'radar',
          data: this.radarData
        }]
      })
      window.onresize = radar.resize;
    }
  }
}
</script>

<style lang="scss" scoped>
@import "~@/assets/css/tabpage.css";
.radar {
  width: 450px;
  height: 380px;
  margin-left: 10px;
}
</style>