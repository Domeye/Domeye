<template>
  <div class="mapDot clearfix">
    <div class="left">
      <div id="map" class="map"></div>
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
</template>

<script>
import {getmapDot, getlongestAsPrefix} from "../../api/apiData";

export default {
  name: 'MapDot',
  props: ["input"],
  data() {
    return {
      basic: '',
      mapData: '',
      descrData: '',
      dot: '',
    }
  },
  watch: {
    input() {
      this.getData();
    }
  },
  mounted() {
    this.getData()
  },
  methods: {
    async getData() {
      await getmapDot(this.input).then( res => {
        this.mapData = res
      })
      await getlongestAsPrefix(this.input).then( res => {
        this.descrData = res['longest_prefix']
      })
      this.getrealData();
    },
    getrealData() {
      let dot_dic ={};
      dot_dic.country = this.mapData.country;
      dot_dic.coord = [this.mapData.longitude, this.mapData.latitude];
      this.dot = [];
      this.dot.push(dot_dic)
      this.basic = {
        '路由前缀': this.descrData['prefix'],
        '归属国家': this.descrData['country'],
        '归属城市': this.mapData.city ? this.mapData.city:'暂无',
        '经 度': this.mapData.longitude,
        '纬 度': this.mapData.latitude,
        '归属AS': this.descrData['ASN'],
        'AS名称': this.descrData['aut_name'],
        '归属机构': this.descrData['org_name'],
      }
      console.log("地图页basic:", this.basic)
      console.log("地图页country:", this.dot[0].country)
      console.log("地图页dot:", this.dot[0].coord)
      this.drawMap();
    },
    drawMap() {
      let map = this.$echarts.init(document.getElementById("map"));
      map.setOption({
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
                data: this.dot,
              }
            }
          ],
      });
      window.onresize = map.resize;
    }
  }
}
</script>

<style lang="scss" scoped>
@import "~@/assets/css/tabpage.css";
.map {
  width: 450px;
  height: 380px;
}
</style>