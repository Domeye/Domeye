<template>
  <div class="allocate">
    <div class="top">
      <div class="title">排名前20国家数据：</div>
    </div>
    <div class="asChart" id="asChart"></div>
    <div class="intro"></div>
    <div class="button"></div>
  </div>
</template>

<script>
var AS_allocated = require("@/utils/AS_allocated.json");
var AS_advertised = require("@/utils/AS_advertised.json");

export default {
  name: "AsResource",
  data() {
    return {
      AS_allocated_map: null,  // 全部排序
      AS_allocated_sort: null,  // 前20名
      AS_advertised_map: null,
      AS_advertised_sort: null,
    }
  },
  mounted() {
    this.AS_allocated_map = this.jsonSort(AS_allocated).slice(0, 20)
    console.log("已分配：", this.AS_allocated_map)   // 输出的键值为0,1,2,3....
    this.AS_allocated_sort = this.jsonSort(AS_allocated)
    this.AS_advertised_map = this.jsonSort(AS_advertised).slice(0, 20)
    console.log("已路由：", this.AS_advertised_map)
    this.AS_advertised_sort = this.jsonSort(AS_advertised)
    this.drawASMap1()
  },
  methods: {
    jsonSort(array) {
      array.sort(function(x, y) { return parseInt(x['value']) - parseInt(y['value'])});
      return array.reverse()  // 输出为降序
    },
    drawASMap1() {
      let map = this.$echarts.init(document.getElementById("asChart"))
      var datax = []
      var datay= []
      for (var item of this.AS_allocated_map) {
        datax.push(item["name"])
        datay.push(item["value"])
      }
      map.setOption({
        tooltip: {
          trigger: "item",
          formatter: function (params) {
            var value = params.value + "";
            return (
              "% Allocated AS space" + "<br/>" + params.name + " : " + value
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
            type: 'value'
          }
        ],
        series: [
          {
            name: 'allocated',
            type: 'bar',
            barWidth: '60%',
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
.as {
  width: 880px;
  height: 380px;
  .top {
    display: flex;
    .title {
      margin: 15px 450px auto 55px;
      font-size: 18px;
    }
    button {
      width: 35px;
      height: 23px;
      margin-top: 19px;
    }
    button:first-of-type {
      background: rgb(184, 53, 53);
      border: rgba(172, 50, 50, 0.5);
      margin-right: 20px;
    }
    button:last-of-type {
      background: rgb(58, 60, 153);
      border: rgba(58, 60, 151, 0.5);
      margin-right: 20px;
    }
  }
  .asChart {
    margin-top: 10px;
    width: 880px;
    height: 300px;
  }
}
</style>