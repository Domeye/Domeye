<template>
  <div class="websiteResource">
    <div class="website_map" id="website_map"></div>
  </div>
</template>

<script>
import mapdata from "@/utils/mapData.json";
import geoCoord from "@/utils/geoCoord.json";

export default {
  name: "WebsiteResource",
  data() {
    return{}
  },
  mounted() {
    this.drawMap()
    // console.log('map_data:', data)
    // console.log('geoCoord:', geoCoord)
  },
  methods: {
    drawMap() {
      let map = this.$echarts.init(document.getElementById("website_map"));
      var convertData = function (data) {
        var res = [];
        for (var i = 0; i < data.length; i++) {
          var geoCoord_ = geoCoord[data[i].name];
          if (geoCoord_) {
            res.push({
              name: data[i].name,
              value: geoCoord_.concat(data[i].value)
            });
          }
        }
        //console.log("res:", res)
        return res;
      };
      map.setOption({
        tooltip : {
          //trigger: 'item',
          formatter: function (params) {
            console.log(params)
            return params.seriesName + '<br>' + params.data.name + ": " + params.value[2]
          }
        },
        // geo: 地理坐标系组件用于地图的绘制，支持在地理坐标系上绘制散点图，线集。
        geo: {
          show: true,
          map: 'world',
          roam: false,
        },
        series: [
          {
            name: '网站资源',
            type: 'scatter',  // 可以应用在直角坐标系，极坐标系，地理坐标系上。
            coordinateSystem: 'geo',
            data: convertData(mapdata),
            /**
             * @param 第一个为数据值value，第二个为数据项参数
             */
            symbolSize: function(val, params) {
              if (val[2] > 5000) {
                return val[2] / 1000;  // 为了进行隐藏看不见
              } else {
                return val[2] / 180;
              }
            },
            itemStyle: {
              color: 'MidnightBlue'
            },
          },
          {
            name: 'Top 3',
            type: 'effectScatter',
            coordinateSystem: 'geo',
            data: convertData(mapdata.sort(function(a, b) {
              return b.value - a.value;
            }).slice(0, 4)),
            symbolSize: function(val) {
              return val[2] / 450;
            },
            showEffectOn: 'render',
            rippleEffect: {
              brushType: 'stroke'
            },
            hoverAnimation: true,
            itemStyle: {
              color: 'MidnightBlue',
              shadowBlur: 15,
              shadowColor: 'MidnightBlue'
            },
            zlevel: 3
          }
        ]
      })
    }
  }
}
</script>

<style lang="scss" scoped>
.websiteResource {
  width: 878px;
  height: 380px;
}
.website_map {
  width: 878px;
  height: 380px;
}
</style>