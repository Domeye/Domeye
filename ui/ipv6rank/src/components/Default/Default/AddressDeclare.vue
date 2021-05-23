<template>
  <div class="declare">
    <div class="top">
      <div class="title">全球v6地址资源宣告情况</div>
    </div>
    <div class="chart" id="v6Chart2"></div>
    <div class="footer">
      <div class="intro">截止至2021年4月5日 全球已宣告v6资源总数为86万亿 中国占23万亿</div>
      <a class="link" href="" >详细</a>
      <i class="el-icon-d-arrow-right"></i>
    </div>
  </div>
</template>

<script>
import v6_advertised from "@/utils/v6_advertised.json";
import countrytolat from "@/utils/countrytolat.json";

export default {
  name: "AddressDeclare",
  data() {
    return {
      title: '',
      v6_advertised_map: null,  // 全部排序
      v6_advertised_sort: null,  // 前20名
    }
  },
  mounted() {
    this.title = "全球v6地址资源宣告情况"
    this.v6_advertised_map = this.jsonSort(v6_advertised).slice(0, 20)
    console.log("v6地址已宣告：", this.v6_advertised_map)
    this.v6_advertised_sort = this.jsonSort(v6_advertised)
    this.drawV6Map()
  },
  methods: {
    /**
     * @description: 将国家按照v6资宣告数进行排序
     * @param {数组} v6_advertised
     * @return {数组} 降序排序过后的数组
     */
    jsonSort(v6_advertised) {
      v6_advertised.sort(function(x, y) { return parseInt(x['value']) - parseInt(y['value'])});
      return v6_advertised.reverse()  // 输出为降序
    },
    drawV6Map() {
      let map = this.$echarts.init(document.getElementById("v6Chart2"))
      var datax = []
      var datay= []
      for (var item of this.v6_advertised_map) {
        datax.push(item["name"])
        datay.push(item["value"])
      }
      map.setOption({
        tooltip: {
          trigger: "item",
          formatter: function (params) {
            for (var item of countrytolat) {
              if (item['code'] == params.name) {
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
            name: 'advertised',
            type: 'bar',
            barWidth: '65%',
            label: {
              show: true,
              position: 'top',
              color: 'gray',
              fontSize: '13',
              formatter: function(params) {
                //console.log("series params:", params)
                return String((params.value/1000000000000).toFixed(12)).slice(0, -11) 
              },
            },
            data: datay,
          }
        ]
      });
      window.onresize = map.resize;
    }
  }
}
</script>

<style lang="scss" scoped>
.declare {
  width: 880px;
  height: 380px;
  .top {
    display: flex;
    justify-content: center;
    .title {
      margin: 20px auto auto auto;
      font-size: 17px;
    }
  }
  .chart {
    margin-top: 10px;
    width: 880px;
    height: 302px;
  }
  .footer {
    margin-left: 50px;
    display: flex;
    justify-content: center;
    .intro {
      font-size: 14px;
      margin-right: 30px;
    }
    a {
      font-size: 14px;
      letter-spacing: 1px;
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