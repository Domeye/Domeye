<template>
  <div class="allocate">
    <div class="top">
      <div class="title">已分配地址排名前20国家：</div>
    </div>
    <div class="chart" id="v6Chart1"></div>
    <div class="footer">
      <div class="intro">xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxsssssssssssxxxxxxxxxxxxx</div>
      <a class="link" href="" >详细</a>
      <i class="el-icon-d-arrow-right"></i>
    </div>
  </div>
</template>

<script>
var v6_allocated = require("@/utils/v6_allocated.json");
var countrytolat = require("@/utils/countrytolat.json");

export default {
  name: "AsResource",
  data() {
    return {
      title: '',
      v6_allocated_map: null,  // 全部排序
      v6_allocated_sort: null,  // 前20名
    }
  },
  mounted() {
    this.title = "已分配v6地址排名前20国家："
    this.v6_allocated_map = this.jsonSort(v6_allocated).slice(0, 20)
    console.log("v6地址已分配：", this.AS_allocated_map)   // 输出的键值为0,1,2,3....
    this.v6_allocated_sort = this.jsonSort(v6_allocated)
    this.drawASMap1()
  },
  methods: {
    jsonSort(array) {
      array.sort(function(x, y) { return parseInt(x['value']) - parseInt(y['value'])});
      return array.reverse()  // 输出为降序
    },
    drawASMap1() {
      let map = this.$echarts.init(document.getElementById("v6Chart1"))
      var datax = []
      var datay= []
      for (var item of this.v6_allocated_map) {
        datax.push(item["name"])
        datay.push(item["value"])
      }
      map.setOption({
        tooltip: {
          trigger: "item",
          formatter: function (params) {
            //console.log("params:", params)
            for (var item of countrytolat) {
              if (item['code'] = params.name) {
                var countryname = item['name']
              }
            }
            var value = params.value + "";
            return (
              "% Allocated AS space" + "<br/>" + countryname + " : " + value
            );
          },
        },
        grid: {
          top: 15,
          left: '6%',
          right: '6%',
          bottom: 10,
          containLabel: true
        },
        xAxis: [
          {
            type: 'category',
            data: datax,
            axisTick: {
                alignWithLabel: true
            }
          }
        ],
        yAxis: [
          {
            type: 'value',
            name: '亿',
            axisLabel: {
              formatter: function (value) {
                //return value.toString().slice(0, -11) + ' 亿'
                return value/1000000000000 + ' 万亿'
              }
            }
          }
        ],
        series: [
          {
            name: 'allocated',
            type: 'bar',
            barWidth: '65%',
            // label: {
            //   show: true,
            //   formatter: function(params) {
            //     console.log("series params:", params)
            //   }
            // },
            data: datay
          }
        ]
      });
      window.onresize = map.resize;
    },
  }
}
</script>

<style lang="scss" scoped>
.allocate {
  width: 880px;
  height: 380px;
  .top {
    display: flex;
    .title {
      margin: 20px 320px auto 100px;
      font-size: 17px;
    }
  }
  .chart {
    margin-top: 10px;
    width: 880px;
    height: 300px;
  }
  .footer {
    display: flex;
    .intro {
      width: 815px;
      text-align: center;
    }
    a {
      font-size: 14.5px;
      letter-spacing: 2px;
      color: rgb(48, 49, 117);
    }
    a:hover {
      border-bottom: 1.5px solid #7e7e7e;
    }
    i {
      display: flex;
      align-items: center;
    }
  }
}
</style>