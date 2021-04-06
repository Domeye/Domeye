<template>
  <div class="graph">
    <div class="relationG" id="relationG"></div>
  </div>
</template>

<script>
import { getrelationGraph } from "../../api/apiData";

export default {
  name: "RelationGraph",
  props: ["input"],
  data() {
    return {
      relation_graph: "",
    };
  },
  watch: {
    input() {
      getrelationGraph(this.input).then((res) => {
        this.relation_graph = res;
        this.drawChart();
      });
    },
  },
  mounted() {
    getrelationGraph(this.input).then((res) => {
      this.relation_graph = res;
      this.drawChart();
    });
  },
  methods: {
    drawChart() {
      console.log("关联关系:", this.relation_graph);
      const chartDom = document.getElementById("relationG");
      const chart = this.$echarts.init(chartDom);
      let nowClientWidth = document.documentElement.clientWidth;
      function nowSize(val, initWidth = 1280) {
        return val * (nowClientWidth / initWidth);
      }
      var graph = {
        nodes: this.relation_graph.nodes,
        links: this.relation_graph.links,
        categories: this.relation_graph.categories,
      };
      graph.nodes.forEach(function (node) {
        node.label = {
          show: true,
          fontSize: 12,
        };
        node.symbolSize = 33;
      });
      chart.setOption({
        tooltip: {
          formatter: "{c}",
          textStyle: {
            fontSize: 13,
          },
        },
        grid: {
          left: 60,
        },
        legend: [
          {
            data: graph.categories.map(function (val) {
              return val.name;
            }),
            itemGap: 13,
            itemHeight: 13,
            itemWidth: 22,
            textStyle: {
              fontSize: 13,
            },
          },
        ],
        animationDuration: 1500,
        animationEasingUpdate: "quinticInOut",
        series: [
          {
            type: "graph",
            layout: "none",
            top: 70,
            bottom: 1,
            // height: 450,
            data: graph.nodes,
            links: graph.links,
            categories: graph.categories,
            zoom: 0.8,
            label: {
              position: "top",
              formatter: "{b}",
            },
            lineStyle: {
              color: "source",
              curveness: 0.3,
            },
            emphasis: {
              focus: "adjacency",
              lineStyle: {
                width: 6,
              },
            },
          },
        ],
      });
      window.onresize = chart.resize;
    },
  },
};
</script>

<style lang="scss" scoped>
.graph {
  height: 370px;
  width: 878px;
  .relationG {
    height: 383px;
    width: 878px;
  }
}
</style>
