<template>
  <div class="probe">
    <div class="graph_probe" id="graph_probe"></div>
  </div>
</template>

<script>
import {get3Picture} from "@/api/apiData";

export default {
  name: 'ProbenumGraph',
  props: ['input'],
  data() {
    return {
      picData: '',
      timeData: '',
      probeData1: '',
      probeData2: '',
    }
  },
  watch: {
    input() {
      get3Picture(this.input).then(res => {
        this.picData = res;
        console.log("探针数目:", this.picData)
        this.timeData = this.picData['picture12_x'];
        this.probeData1 = this.picData['picture1_data'];
        this.probeData2 = this.picData['picture2_data'];
        this.drawGraph_probe();
      })
    }
  },
  mounted() {
    get3Picture(this.input).then(res => {
      this.picData = res;
      this.timeData = this.picData['picture12_x'];
      this.probeData1 = this.picData['picture1_data'];
      this.probeData2 = this.picData['picture2_data'];
      this.drawGraph_probe();
    })
  },
  methods: {
    drawGraph_probe() {
      let graph_probe = this.$echarts.init(document.getElementById('graph_probe'))
      var total_data1 = [];
      for (var i = 0; i<this.timeData.length; i++) {
        total_data1.push([this.timeData[i], this.probeData1[i]])
      }
      var total_data2 = [];
      for (var i = 0; i<this.timeData.length; i++) {
        total_data2.push([this.timeData[i], this.probeData2[i]])
      }
      graph_probe.setOption({
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
      window.onresize = graph_probe.resize;
    }
  }
}
</script>

<style lang="scss" scoped>
.graph_probe{
  width: 878px;
  height:380px;
}
</style>>