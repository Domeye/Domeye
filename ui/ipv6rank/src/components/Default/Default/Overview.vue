<template>
  <div class="overview">
    <div class="above">
      <div class="chart" id="v61"></div>
      <div class="chart" id="v62"></div>
      <div class="chart" id="as"></div>
    </div>
    <div class="below">
      <div class="block">
        <div class="text">
          <i class="el-icon-caret-right"></i>已分配v6地址总数：
        </div>
        <!--引入千分位计算-->
        <div class="world">全球：54,521,760,719</div>
        <div class="china">中国：XXXX</div>
      </div>
      <div class="block">
        <div class="text">
          <i class="el-icon-caret-right"></i>已宣告v6地址总数：
        </div>
        <div class="world">全球：XXXXXXXXX</div>
        <div class="china">中国：XXXX</div>
      </div>
      <div class="block">
        <div class="text">
          <i class="el-icon-caret-right"></i>可路由自治域总数：
        </div>
        <div class="world">全球：86,439,241</div>
        <div class="china">中国：XXXX</div>
      </div>
    </div>
    <div class="time">数据更新于2021年 4月5日</div>
  </div>
</template>

<script>
export default {
  name: 'Overview',
  data() {
    return {}
  },
  mounted() {
    this.drawChart1()
    this.drawChart2()
    this.drawChart3()
  },
  methods: {
    drawChart1() {
      let chart = this.$echarts.init(document.getElementById("v61"))
      chart.setOption({
        title: {
          text: '近十年v6地址分配数目变化',
          textStyle: {
            fontSize: 15,
            fontWeight: 'lighter',
            color: 'black',
          },
          //x:'center',
          left: '21%'
          //textAlign: 'center',
        },
        grid: {
          containLabel: true,
          top: '18%',
          left: 0,
          right: 0,
          bottom: 0,
        },
        xAxis: {
          type: 'category',
          data: ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
        },
        yAxis: {
          type: 'value'
        },
        series: [{
          data: [820, 932, 901, 934, 1290, 1330, 1320],
          type: 'line',
          smooth: true
        }]
      })
      window.onresize = chart.resize;
    },
    drawChart2() {
      let chart = this.$echarts.init(document.getElementById("v62"))
      chart.setOption({
        title: {
          text: '近十年v6地址可路由数目变化',
          textStyle: {
            fontSize: 15,
            fontWeight: 'lighter',
            color: 'black',
          },
          // x:'center',
          left: '20%',
        },
        grid: {
          containLabel: true,
          top: '18%',
          left: 0,
          right: 0,
          bottom: 0,
        },
        xAxis: {
          type: 'category',
          data: ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
        },
        yAxis: {
          type: 'value'
        },
        series: [{
          data: [820, 932, 901, 934, 1290, 1330, 1320],
          type: 'line',
          smooth: true
        }]
      })
      window.onresize = chart.resize;
    },
    drawChart3() {
      let chart = this.$echarts.init(document.getElementById("as"))
      chart.setOption({
        title: {
          text: '近十年AS数目变化',
          textStyle: {
            fontSize: 15,
            fontWeight: 'lighter',
            color: 'black',
          },
          //x:'center',
          left: '30%',
        },
        grid: {
          containLabel: true,
          top: '18%',
          left: 0,
          right: 0,
          bottom: 0,
        },
        xAxis: {
          type: 'category',
          data: ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
        },
        yAxis: {
          type: 'value'
        },
        series: [{
          data: [820, 932, 901, 934, 1290, 1330, 1320],
          type: 'line',
          smooth: true
        }]
      })
      window.onresize = chart.resize;
    },
  }
}
</script>

<style lang="scss" scoped>
.overview {
  width: 868px;
  height: 360px;
  padding: 15px 5px 0 5px;
  position: relative;
  //display: flex;
}
.above {
  display: flex;
  justify-content: space-around;
  .chart {
    width: 270px;
    height: 200px;
  }
}
.below {
  margin-top: 20px;
  display: flex;
  justify-content: space-around;
  .block {
    width: 195px;
    height: 100px;
    // background: rgba(233, 233, 233, 0.1);
    // box-shadow: 0px 0px 5px 0px rgb(204, 204, 204);
    // border-radius: 7px;
    //text-align: center;
    .text {
      font-size: 14.5px;
      padding-top: 10px;
    }
    .world {
      margin-top: 14px;
      font-size: 14.5px;
      //color: rgb(99, 35, 35);
      padding-left: 14px;
    }
    .china {
      margin-top: 5px;
      font-size: 14.5px;
      padding-left: 14px;
    }
  }
}
.time {
  display: flex;
  justify-content: center;
  font-size: 14px;
  margin-top: 19px;
}
</style>