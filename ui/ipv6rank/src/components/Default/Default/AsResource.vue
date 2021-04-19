<template>
  <div class="as">
    <div class="top">
      <div class="title">{{title}}</div>
    </div>
    <div class="middle">
      <div class="switch">
        <div class="allocated">
          <button @click="to_allocated" ></button>
          <span>已分配</span>
        </div>
        <div class="advertised">
          <button @click="to_advertised"></button>
          <span>可路由</span>
        </div>
      </div>
      <div class="chart" id="asChart"></div>
    </div>
    <div class="footer">
      <div class="intro">{{footer}}</div>
      <a class="link" href="" >详细</a>
      <i class="el-icon-d-arrow-right"></i>
    </div>
  </div>
</template>

<script>
import AS_allocated from "@/utils/AS_allocated.json";
import AS_advertised from "@/utils/AS_advertised.json";
import countrytolat from "@/utils/countrytolat.json";

export default {
  name: "AsResource",
  data() {
    return {
      title: "全球AS资源分配情况",
      AS_allocated_map: null,  // 全部排序
      AS_allocated_sort: null,  // 前20名
      AS_advertised_map: null,
      AS_advertised_sort: null,
      AS_map: null,
      footer: "截止至2021年4月5日 全球已分配AS数目为总数为100333 中国占1982",
      bar_color: "rgb(184, 53, 53)"
    }
  },
  mounted() {
    this.AS_allocated_map = this.jsonSort(AS_allocated).slice(0, 20)
    this.AS_map =  this.AS_allocated_map
    this.AS_allocated_sort = this.jsonSort(AS_allocated)
    this.AS_advertised_map = this.jsonSort(AS_advertised).slice(0, 20)
    this.AS_advertised_sort = this.jsonSort(AS_advertised)
    this.drawASMap()
  },
  methods: {
    /**
     * @description: 将国家按照AS资源分配/路由数进行排序
     * @param {数组} as_array
     * @return {数组} 降序排序过后的数组
     */
    jsonSort(as_array) {
      as_array.sort(function(x, y) { return parseInt(x['value']) - parseInt(y['value'])});
      return as_array.reverse()  // 输出为降序
    },
    to_allocated() {
      this.title = "全球AS资源分配情况"
      this.AS_map =  this.AS_allocated_map
      this.footer = "截止至2021年4月5日 全球已分配AS数目为总数为100333 中国占1982"
      this.bar_color = "rgb(184, 53, 53)"
      this.drawASMap()
    },
    to_advertised() {
      this.title = "全球AS资源路由情况"
      this.AS_map = this.AS_advertised_map
      this.footer = "截止至2021年4月5日 全球可路由AS数目为总数为72177 中国占637"
      this.bar_color = "rgb(58, 60, 153)"
      this.drawASMap()
    },
    drawASMap() {
      let map = this.$echarts.init(document.getElementById("asChart"))
      var datax = []
      var datay= []
      for (var item of this.AS_map) {
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
          top: 17,
          left: '2%',
          right: '2%',
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
            axisLabel: {
              formatter: function (value) {
                //return value.toString().slice(0, -4) + ' 千'
                return value/1000 + '千'
              }
            }
          }
        ],
        series: [
          {
            name: 'allocated',
            type: 'bar',
            itemStyle: {
              color: this.bar_color,  // 怎么控制颜色变化
            },
            barWidth: '65%',
            label: {
              show: true,
              position: 'top',
              color: 'gray',
              fontSize: '13',
              formatter: function(params) {
                return String((params.value/1000).toFixed(3)).slice(0, -4)
              },
            },
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
    justify-content: center;
    .title {
      margin: 20px auto auto auto;
      font-size: 17px;
    }
  }
  .middle {
    display: flex;
    flex-direction: row;
    .switch {
      padding-left: 20px;
      padding-top: 100px;
      margin-right: 2px;
      display: flex;
      flex-direction: column;
      button {
        margin: 0;
        width: 28px;
        height: 18px;
      }
      .allocated {
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
        margin-top: 40px;
        button {
          background: rgb(58, 60, 153);
          border: rgba(58, 60, 151, 0.5);
          margin-right: 5px;
        }
      }
      span {
        font-size: 13px;
      }
    }
    .chart {
      margin-top: 10px;
      width: 770px;
      height: 302px;
    }
  }
  .footer {
    margin-left: 80px;
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