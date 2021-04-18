<template>
  <div class="mapDot clearfix">
    <div class="left">
      <div id="map" class="map"></div>
    </div>
    <div class="right">
      <div style="position: relative;">
        <h4 class="right-title">AS基本信息</h4>
        <ul>
          <li v-for="(val, key, i) in basic" :key="i">
            <div class="front">{{key}} :</div>
            <div class="following">{{val}}</div>
          </li>
        </ul>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'BasicInfo',
  props: {
    res: {
      type: Object,
      default: null
    }
  },
  data() {
    return {
      basic: {},
      dot: [],
      flag: false // 标志是否已经渲染，即是否执行过handleChange
    }
  },
  watch: {
    res(newVal){
      if(newVal && !this.flag){
        this.handleChange(newVal)
      }
    }
  },
  mounted(){
    if(this.res && !this.flag){
      this.handleChange(this.res)
    }
  },
  methods: {
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
      // window.onresize = map.resize;
    },
    handleChange(newVal){
      this.basic = {
        'AS编号': newVal['ASN'],
        'AS类型': newVal['as_type'],
        'AS名称': newVal['aut_name'],
        '归属国家': newVal['country'],
        '描述信息': newVal['descr'],
        '机构编号': newVal['org_id'],
        '机构名称': newVal['org_name'],
        '经度': newVal['position'][0],
        '纬度': newVal['position'][1]
      }
      let dot_dic = {}
      dot_dic.country = newVal['country']
      dot_dic.coord = [newVal['position'][0], newVal['position'][1]]
      this.dot = []
      this.dot.push(dot_dic)
      this.$nextTick(() => {
        this.drawMap()
      })
      this.flag = true
    }
  }
}
</script>
<style scoped src="@/assets/css/tabpage.css"></style>
<style scoped lang='scss'>
.map {
  width: 450px;
  height: 380px;
}
</style>
