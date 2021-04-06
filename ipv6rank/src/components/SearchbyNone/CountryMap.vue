<template>
  <div class="countrymap clearfix">
    <div class="left">
      <el-carousel :interval="6000" arrow="always" indicator-position="outside">
        <el-carousel-item>
          <div id="map1" class="map"></div>
        </el-carousel-item>
        <el-carousel-item>
          <div id="map2" class="map"></div>
        </el-carousel-item>
        <el-carousel-item>
          <div id="map3" class="map"></div>
        </el-carousel-item>
        <el-carousel-item>
          <div id="map4" class="map"></div>
        </el-carousel-item>
        <el-carousel-item>
          <div id="map5" class="map"></div>
        </el-carousel-item>
      </el-carousel>
    </div>
    <div class="right">
      <div style="position: relative">
        <div class="desc">
          <h4 class="intro">v6地址和AS号在各个国家的资源分配情况</h4>
          <div class="intro_item"><i class="el-icon-caret-right"></i>allocated space:<br> 各个国家已分配v6资源在全球的占比情况，其中占比最高的是美国（9.02%），其次是中国（8.59%）。</div>
          <div class="intro_item"><i class="el-icon-caret-right"></i>cc allocated space:<br> 各个国家可路由v6地址占已分配v6资源的比例。</div>
          <div class="intro_item"><i class="el-icon-caret-right"></i>advertised space:<br> 各个国家可路由v6地址在全球的占比情况，其中占比最高的是美国（23.56%）。</div>
          <div class="intro_item"><i class="el-icon-caret-right"></i>allocated space:<br> 各个国家已分配AS号数量在全球的占比情况，其中占比最高的是美国（28.60%）。</div>
          <div class="intro_item"><i class="el-icon-caret-right"></i>cc allocated space:<br> 各个国家可路由AS号占已分配AS号的比例。</div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
var realDatav61 = require("@/utils/realDatav61.json");
var realDatav62 = require("@/utils/realDatav62.json");
var realDatav63 = require("@/utils/realDatav63.json");
var realDataAS1 = require("@/utils/realDataAS1.json");
var realDataAS2 = require("@/utils/realDataAS2.json");

export default {
  name: "countryMap",
  data() {
    return {};
  },
  mounted() {
    this.drawSwitchMapIPv61();
    this.drawSwitchMapIPv62();
    this.drawSwitchMapIPv63();
    this.drawSwitchMapAS1();
    this.drawSwitchMapAS2();
  },
  methods: {
    drawSwitchMapIPv61() {
      let map1 = this.$echarts.init(document.getElementById("map1"));
      this.$nextTick(() => {
        map1.resize();
      })
      map1.setOption({
        title: {
          top: 15,
          text: 'IPv6 allocated space',
          left: 'center',
          textStyle: {
            fontSize: 15.5,
          }
        },
        tooltip: {
          trigger: "item",
          formatter: function (params) {
            var value = params.value + "";
            return (
              "% Allocated IPv6 space" + "<br/>" + params.name + " : " + value*100 + "%"
            );
          },
        },
        visualMap: {
          min: 0.0,
          max: 0.1,
          text: ["High", "Low"],
          precision: 3, //设置小数精度，默认0没有小数
          realtime: false,
          calculable: true,
          color: ["SteelBlue", "LightSteelBlue"],
          itemWidth: 13,
          itemHeight: 80,
          left: 10,
          top: 200,
        },
        series: [
          {
            type: "map",
            mapType: "world",
            top: 75,
            //left: 60,
            zoom: 1.2,
            roam: false,
            itemStyle: {
              emphasis: {
                label: {
                  show: true,
                },
              },
            },
            data: realDatav61,
          },
        ],
      });
      window.onresize = map1.resize;
    },
    drawSwitchMapIPv62() {
      let map2 = this.$echarts.init(document.getElementById("map2"));
      this.$nextTick(() => {
        map2.resize();
      })
      map2.setOption({
        title: {
          top: 15,
          text: 'IPv6 cc allocated space',
          left: 'center',
          textStyle: {
            fontSize: 15.5,
          }
        },
        tooltip: {
          trigger: "item",
          formatter: function (params) {
            var value = params.value + "";
            return (
              "% cc Allocated IPv6 space" + "<br/>" + params.name + " : " + value*100 + "%"
            );
          },
        },
        visualMap: {
          min: 0.0,
          max: 1.0,
          text: ["High", "Low"],
          precision: 3, //设置小数精度，默认0没有小数
          realtime: false,
          calculable: true,
          color: ["SteelBlue", "LightSteelBlue"],
          itemWidth: 13,
          itemHeight: 80,
          left: 10,
          top: 200,
        },
        series: [
          {
            type: "map",
            mapType: "world",
            top: 75,
            //left: 50,
            zoom: 1.2,
            roam: false,
            itemStyle: {
              emphasis: {
                label: {
                  show: true,
                },
              },
            },
            data: realDatav62,
          },
        ],
      });
      window.onresize = map2.resize;
    },
    drawSwitchMapIPv63() {
      let map3 = this.$echarts.init(document.getElementById("map3"));
      this.$nextTick(() => {
        map3.resize();
      })
      map3.setOption({
        title: {
          top: 15,
          text: 'IPv6 advertised space',
          left: 'center',
          textStyle: {
            fontSize: 15.5,
          }
        },
        tooltip: {
          trigger: "item",
          formatter: function (params) {
            var value = params.value + "";
            return (
              "% Advertised IPv6 space" + "<br/>" + params.name + " : " + value*100 + "%"
            );
          },
        },
        visualMap: {
          min: 0.0,
          max: 0.25,
          text: ["High", "Low"],
          precision: 3, //设置小数精度，默认0没有小数
          realtime: false,
          calculable: true,
          color: ["SteelBlue", "LightSteelBlue"],
          itemWidth: 13,
          itemHeight: 80,
          left: 10,
          top: 200,
        },
        series: [
          {
            type: "map",
            mapType: "world",
            top: 75,
            //left: 50,
            zoom: 1.2,
            roam: false,
            itemStyle: {
              emphasis: {
                label: {
                  show: true,
                },
              },
            },
            data: realDatav63,
          },
        ],
      });
      window.onresize = map3.resize;
    },
    drawSwitchMapAS1() {
      let map4 = this.$echarts.init(document.getElementById("map4"));
      this.$nextTick(() => {
        map4.resize();
      })
      map4.setOption({
        title: {
          top: 15,
          text: 'AS allocated space',
          left: 'center',
          textStyle: {
            fontSize: 15.5,
          }
        },
        tooltip: {
          trigger: "item",
          formatter: function (params) {
            var value = params.value + "";
            return (
              "% Allocated AS space" + "<br/>" + params.name + " : " + (value*100).toFixed(2) + "%"
            );
          },
        },
        visualMap: {
          min: 0.0,
          max: 0.3,
          text: ["High", "Low"],
          precision: 3, //设置小数精度，默认0没有小数
          realtime: false,
          calculable: true,
          color: ["SteelBlue", "LightSteelBlue"],
          itemWidth: 13,
          itemHeight: 80,
          left: 10,
          top: 200,
        },
        series: [
          {
            type: "map",
            mapType: "world",
            top: 75,
            //left: 50,
            zoom: 1.2,
            roam: false,
            itemStyle: {
              emphasis: {
                label: {
                  show: true,
                },
              },
            },
            data: realDataAS1,
          },
        ],
      });
      window.onresize = map4.resize;
    },
    drawSwitchMapAS2() {
      let map5 = this.$echarts.init(document.getElementById("map5"));
      this.$nextTick(() => {
        map5.resize();
      })
      map5.setOption({
        title: {
          top: 15,
          text: 'AS cc allocated space',
          left: 'center',
          textStyle: {
            fontSize: 15.5,
          }
        },
        tooltip: {
          trigger: "item",
          formatter: function (params) {
            var value = params.value + "";
            return (
              "% cc Allocated AS space" + "<br/>" + params.name + " : " + (value*100).toFixed(2) + "%"
            );
          },
        },
        visualMap: {
          min: 0.0,
          max: 1.0,
          text: ["High", "Low"],
          precision: 3, //设置小数精度，默认0没有小数
          realtime: false,
          calculable: true,
          color: ["SteelBlue", "White"],
          itemWidth: 13,
          itemHeight: 80,
          left: 10,
          top: 200,
        },
        series: [
          {
            type: "map",
            mapType: "world",
            top: 75,
            //left: 50,
            zoom: 1.2,
            roam: false,
            itemStyle: {
              emphasis: {
                label: {
                  show: true,
                },
              },
            },
            data: realDataAS2,
          },
        ],
      });
      window.onresize = map5.resize;
    },
  },
};
</script>

<style lang="scss" scoped>
@import "~@/assets/css/tabpage.css";
.left {
  width: 480px;
}
.el-carousel /deep/.el-carousel__container {
  //width: 100%;
  height: 340px;
  button {
    height: 30px;
    width: 30px;
  }
}
.map {
  margin-left: 13px;
  width: 450px;
  height: 340px;
}
.right {
  width: 380px;
}
.intro {
  margin: 13px auto 13px 20px;
}
.intro_item {
  margin: 5px 10px 10px auto;
}
</style>