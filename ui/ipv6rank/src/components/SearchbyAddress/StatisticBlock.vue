<template>
  <div class="report">
    <div class="echart3" id="echart3"></div>
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
      if (this.picture2){
        this.drawChart();
      }
    },
  },
  methods: {
    drawChart() {
      let map3 = this.$echarts.init(document.getElementById("echart3"));
      let nowClientWidth = document.documentElement.clientWidth;
      function nowSize(val, initWidth=1280){
        return val * (nowClientWidth/initWidth);
      }
      var data3 = this.picture2["picture3_data"];
      if (data3) {
        data3.sort((a, b) => a[0].localeCompare(b[0]));
        console.log("data3::", data3)
        var data3_x = data3.map(function(value, index) { return value[0].substr(0, 7); });
        var data3_y_rep = data3.map(function(value, index) { return value[1];});
        var data3_y = Array.from(new Set(data3_y_rep))
        var new_data3 = new Array();
        for (var i = 0; i<data3.length; i++) {
          new_data3.push([i, i, data3[i][3]])
        }
        console.log("new_data3::", new_data3)
        // console.log("new_data3[2]::", new_data3[0])
      }
      map3.setOption({
        title: {
          text: "AS号数目随时间变化",
          left: "center",
          textStyle: {
            fontSize: 16,
            fontWeight: "bold",
          },
        },
        grid: {
          top: "13%",
          bottom: 50,
        },
        // dataZoom: [
        //   {
        //       show: true,
        //       realtime: true,
        //       start: 0,
        //       end: 80,
        //   },
        //   {
        //       type: 'inside',
        //       realtime: true,
        //       start: 0,
        //       end: 80,
        //   },
        // ],
        xAxis: {
          type: 'category',
          data: data3_x,
          boundaryGap: false,
          axisLabel : {//坐标轴刻度标签的相关设置。
            interval: 0,
            rotate: "-45",
            textStyle: {
              fontSize: 13,
            }
          },
          splitLine: {
            lineStyle: {
              type: "dashed",
            },
          },
        },
        yAxis: {
          name: "AS号",
          nameTextStyle: {
            fontSize: 14,
          },
          fontSize: 14,
          type: 'category',
          data: data3_y,
          axisLabel: {
            textStyle: {
              fontSize: 14,
            }
          },
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
                fontSize: 13,
                fontWeight: "bold",
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
.report {
  height: 360px;
  width: 878px;
  .echart3 {
    margin: 16px 5px 0 5px;
    height: 345px;
    width: 878px;
  }
}
</style>
