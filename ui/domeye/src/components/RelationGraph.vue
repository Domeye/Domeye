<template>
  <div class="graph">
      <div class="relationG" id="relationG"></div>
  </div>
</template>

<script>
export default {
  name: "RelationGraph",
  props:["relation_graph"],
  data() {
      return {
          relation_graph2: "",
      }
  },
  watch: {
      relation_graph: function(newVal, oldVal) {
          this.relation_graph2 = newVal;
          this.drawChart();
      }
  },
  methods: {
    drawChart() {
      console.log("relation_graph::::", this.relation_graph2);
      const chartDom = document.getElementById("relationG");
      const chart = this.$echarts.init(chartDom);
      var graph = {
        nodes: this.relation_graph2.nodes,
        links: this.relation_graph2.links,
        categories: this.relation_graph2.categories,
      };
      graph.nodes.forEach(function (node) {
        node.label = {
          show: node.symbolSize > 30,
        };
      });
      chart.setOption({
        tooltip: {
            formatter: "{c}",
        },
        legend: [
          {
            data: graph.categories.map(function (val) {
              return val.name;
            }),
            // itemGap: 20,
          },
        ],
        animationDuration: 1500,
        animationEasingUpdate: "quinticInOut",
        series: [
          {
            // name: "Les Miserables",
            type: "graph",
            layout: "none",
            top: 100,
            height: 450,
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
                width: 8,
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

<style lang="scss" scopesd>
@import "~@/assets/style/reset.css";
.graph {
  height: 100%;
  width: 100%;
  display: flex;
  justify-content: center;
  .relationG {
      margin-top: 10px;
      height: 610px;
      width: 630px;
  }
}
</style>
