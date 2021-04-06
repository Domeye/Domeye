<template>
  <div class="report">
    <div class="block">
      <div class="echart1" id="echart1"></div>
    </div>
    <div class="block">
      <div class="echart2" id="echart2"></div>
    </div>
    <div class="block">
      <!-- <div class="title">
        <p>数据分布</p>
      </div> -->
      <div class="echart3" id="echart3"></div>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      picture2: "",
    };
  },
  props: ["picture"],
  watch: {
    picture: function (newVal, oldVal) {
      this.picture2 = newVal;
      this.drawChart();
    },
  },
  methods: {
    drawChart() {
      let map1 = this.$echarts.init(document.getElementById("echart1"));
      var timeData = this.picture2["picture12_x"];
      // timeData = timeData.map(function (str) {
      //   return str.replace("2021/", "");
      // });
      var data1 = this.picture2["picture1_data"];
      var total_data1 = [];
      for (var i = 0; i<timeData.length; i++) {
        total_data1.push([timeData[i], data1[i]])
      }
      console.log("total_data1:", total_data1);
      map1.setOption({
        title: {
          text: "u报文数目随时间变化",
          left: "center",
          textStyle: {
            fontSize: 15,
            fontWeight: "normal",
          },
        },
        tooltip: {
          trigger: "axis",
          axisPointer: {
            animation: false,
          },
        },
        axisPointer: {
          link: {xAxisIndex: 'all'}
        },
        // splitNumber: 13,  // 允许显示多少横刻度
        xAxis: {
          type: "time",
          boundaryGap: true,
          axisLine: { onZero: false },
          interval: 1000 * 3600 * 24, // x轴时间间隔显示为24小时
          data: timeData,
          axisLabel : {//坐标轴刻度标签的相关设置。
            // interval: 140,
            formatter: function (value, idx) {
              var date = new Date(value)
              const hour = date.getHours();
              const minute = date.getMinutes();
              const second = date.getSeconds();
              return [date.getMonth() + 1, date.getDate()].join('-');
              // return idx === 0 ? value : [date.getMonth() + 1, date.getDate()].join('-');  // 判断 ？对值：错值
            }
          },
        },
        yAxis: {
          name: "u报文数目",
          type: "value",
          max: function(value){
            return value.max+2;
          },
          minInterval: 1,
        },
        series: {
          name: "报文数",
          type: "line",
          symbolSize: 0,
          hoverAnimation: false,
          data: total_data1,
        },
      }),
      window.onresize = map1.resize;
      let map2 = this.$echarts.init(document.getElementById("echart2"));
      var data2 = this.picture2["picture2_data"];
      var total_data2 = [];
      for (var i = 0; i<timeData.length; i++) {
        total_data2.push([timeData[i], data2[i]])
      }
      map2.setOption({
        title: {
          text: "w报文数目随时间变化",
          left: "center",
          textStyle: {
            fontSize: 15,
            fontWeight: "normal",
          },
        },
        tooltip: {
          trigger: "axis",
          axisPointer: {
            animation: false,
          },
        },
        // dataZoom: [
        //   {
        //       show: true,
        //       realtime: true,
        //       start: 0,
        //       end: 1,
        //   },
        //   {
        //       type: 'inside',
        //       realtime: true,
        //       start: 0,
        //       end: 1,
        //   },
        // ],
        grid: {
          // bottom: 130,
        },
        xAxis: {
          type: "time",
          boundaryGap: true,
          data: timeData,  // 有无都可
          interval: 1000 * 3600 * 24, 
          axisLabel : {//坐标轴刻度标签的相关设置。
            // interval: 140,
            formatter: function (value, idx) {
              var date = new Date(value)
              return [date.getMonth() + 1, date.getDate()].join('-');
              // return idx === 0 ? value : [date.getMonth() + 1, date.getDate()].join('-');  // 判断 ？对值：错值
            }
          },
        },
        yAxis: {
          name: "w报文数目",
          type: "value",
          max: function(value){
            return value.max+2;
          },
          minInterval: 1,
        },
        series: {
          name: "报文数",
          type: "line",
          symbolSize: 0,
          hoverAnimation: false,
          data: total_data2,  // 是一组有2个字段的二维数组
        },
      });
      window.onresize = map2.resize;
      let map3 = this.$echarts.init(document.getElementById("echart3"));
      var data3 = this.picture2["picture3_data"];
      data3.sort((a, b) => a[0].localeCompare(b[0]));
      if (data3) {
        var data3_x = data3.map(function(value, index) { return value[0]; });
        var data3_y_rep = data3.map(function(value, index) { return value[1];});
        var data3_y = Array.from(new Set(data3_y_rep))
        var new_data3 = new Array()
        for (var i = 0; i<data3.length; i++) {
          new_data3.push([i, i, data3[i][3]])
        }
        console.log("new_data3::", new_data3)
      }
      map3.setOption({
        title: {
          text: "AS号数目随时间变化",
          left: "center",
          textStyle: {
            fontSize: 16,
            fontWeight: "normal",
          },
        },
        grid: {
          top: "15%",
          bittom: 100,
        },
        xAxis: {
          type: 'category',
          data: data3_x,
          boundaryGap: false,
          axisLabel : {//坐标轴刻度标签的相关设置。
            interval: 0,
            rotate: "-45",
          },
          splitLine: {
            lineStyle: {
              type: "dashed",
            },
          },
        },
        yAxis: {
          name: "AS号",
          type: 'category',
          data: data3_y,
          splitLine: {
            lineStyle: {
              type: "dashed",
            },
          },
          scale: true,
        },
        series: [
          {
            data: new_data3,
            type: "scatter",
            symbolSize: function (data) {
              return data[2] / 3;
            },
            emphasis: {
              focus: "series",
              label: {
                show: true,
                formatter: function (param) {
                  return param.data[2];
                },
                position: "top",
              },
            },
            itemStyle: {
              shadowBlur: 10,
              shadowColor: "rgba(120, 36, 50, 0.5)",
              shadowOffsetY: 5,
            },
          },
        ],
      });
      window.onresize = map3.resize;
    },
  },
};
</script>

<style lang="scss">
@import "~@/assets/style/reset.css";
.report {
  height: 100%;
  width: 100%;
  .block {
    display: flex;
    justify-content: center;
    // width: 100%;
    margin: 20px 10px;
    border: 1px solid rgb(224, 224, 224);
    .echart1 {
      padding-left: 0;
      height: 370px;
      width: 634px;
      margin-top: 20px;
    }
    .echart2 {
      padding-left: 0;
      height: 320px;
      width: 634px;
      margin-top: 15px;
    }
    .echart3 {
      margin-top: 20px;
      height: 335px;
      width: 634px;
      // margin-left: 15px;
    }
  }
}
</style>
