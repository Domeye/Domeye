<template>
  <div class="as">
    <div class="top">
      <div class="title">{{title}}</div>
      <div class="switch">
        <div class="allocated">
          <button class="allocated" @click="to_allocated" ></button>
          <span>已分配</span>
        </div>
        <div class="advertised">
          <button class="advertised" @click="to_advertised"></button>
          <span>可路由</span>
        </div>
      </div>
    </div>
    <div class="chart" id="asChart"></div>
    <div class="footer">
      <div class="intro">xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxsssssssssssxxxxxxxxxxxxx</div>
      <a class="link" href="" >详细</a>
      <i class="el-icon-d-arrow-right"></i>
    </div>
  </div>
</template>

<script>
var AS_allocated = require("@/utils/AS_allocated.json");
var AS_advertised = require("@/utils/AS_advertised.json");
var countrytolat = require("@/utils/countrytolat.json");

export default {
  name: "AsResource",
  data() {
    return {
      title: '',
      AS_allocated_map: null,  // 全部排序
      AS_allocated_sort: null,  // 前20名
      AS_advertised_map: null,
      AS_advertised_sort: null,
    }
  },
  mounted() {
    this.title = "已分配ASN 排名前20国家："
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
    to_allocated() {
      this.title = "已分配ASN 排名前20国家："
      this.drawASMap1()
    },
    to_advertised() {
      this.title = "可路由ASN 排名前20国家："
      this.drawASMap2()
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
            type: 'value'
          }
        ],
        series: [
          {
            name: 'allocated',
            type: 'bar',
            itemStyle: {
              color: "rgb(184, 53, 53)",
            },
            barWidth: '65%',
            data: datay
          }
        ]
      });
      window.onresize = map.resize;
    },
    drawASMap2() {
      let map = this.$echarts.init(document.getElementById("asChart"))
      var datax = []
      var datay= []
      for (var item of this.AS_advertised_map) {
        datax.push(item["name"])
        datay.push(item["value"])
      }
      map.setOption({
        tooltip: {
          trigger: "item",
          formatter: function (params) {
            for (var item of countrytolat) {
              if (item['code'] = params.name) {
                var countryname = item['name']
              }
            }
            var value = params.value + "";
            return (
              "% Advertised AS space" + "<br/>" + countryname + " : " + value
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
            name: 'advertised',
            type: 'bar',
            itemStyle: {
              color: "rgb(58, 60, 153)",
            },
            barWidth: '65%',
            data: datay
          }
        ]
      });
      window.onresize = map.resize;
    }
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
      margin: 20px 320px auto 100px;
      font-size: 17px;
    }
    .switch {
      display: flex;
      height: 25px;
      margin-top: 22px;
      button {
        width: 31px;
        height: 20px;
      }
      .allocated {
        margin-right: 15px;
        display: flex;
        align-items: center;
        button {
          background: rgb(184, 53, 53);
          border: rgba(172, 50, 50, 0.5);
          margin-right: 5px;
        }
      }
      .advertised {
        display: flex;
        align-items: center;
        button {
          background: rgb(58, 60, 153);
          border: rgba(58, 60, 151, 0.5);
          margin-right: 5px;
        }
      }
      span {
        font-size: 14.5px;
      }
    }
  }
  .chart {
    margin-top: 5px;
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