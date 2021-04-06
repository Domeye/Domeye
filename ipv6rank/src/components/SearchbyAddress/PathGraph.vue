<template>
  <div id="pathGraph">
  </div>
</template>

<script>
import {getpathGraph} from "../../api/apiData";

export default {
  name: "PathGraph",
  data() {
    return {
      paths: '',
      myDiagram: null,
    };
  },
  props: ["input", "callback"],
  watch: {
    input() {
      getpathGraph(this.input).then(res => {
        this.paths = res['v6Propagation']
        this.createDiagram();
        this.generateDigraph();
      })
    }
  },
  // updated: function() {
  //   this.$nextTick(function () {
  //     console.log("绘图。。。")
  //     this.createDiagram();
  //     this.generateDigraph();
  //   })
  // },
  mounted() {
    getpathGraph(this.input).then(res => {
      this.paths = res['v6Propagation']
      console.log("this.paths:", this.paths)
      this.createDiagram();
      this.generateDigraph();
    })
  },
  methods: {
    createDiagram: function () {
      let go = window.go;
      let $ = go.GraphObject.make; // 初始化画布
      let self = this;
      let myDiagram = $(go.Diagram, "pathGraph", {
        initialAutoScale: go.Diagram.UniformToFill,
        initialContentAlignment: go.Spot.Center,
        layout: $(go.LayeredDigraphLayout),
        "undoManager.isEnabled": true,
        allowZoom: true, //允许缩放，false为否
        isReadOnly: false, //是否禁用编辑 false否
        mouseOver: (e) => {
          if (self.callback) {
            self.callback();
          }
        },
      });

      myDiagram.nodeTemplate = $(
        go.Node,
        "Spot",
        { locationSpot: go.Spot.Center },
        $(
          go.Shape,
          "Circle",
          {
            fill: "lightgray",
            stroke: null,
            desiredSize: new go.Size(40, 40),
          },
          new go.Binding("fill", "fill")
        ),
        $(go.TextBlock, new go.Binding("text", "text"))
      );

      myDiagram.linkTemplate = $(
        go.Link,
        { selectable: false },
        $(
          go.Shape,
          { strokeWidth: 2, stroke: "#333" },
          new go.Binding("stroke", "stroke")
        )
      );

      this.myDiagram = myDiagram;
    },
    rebuildGraph: function () {
      this.generateDigraph();
    },
    generateDigraph: function () {
      this.myDiagram.startTransaction("generateDigraph");
      this.generateNodes(this.paths);
      this.generateLinks(this.paths);
      this.layout();
      this.myDiagram.commitTransaction("generateDigraph");
    },

    generateNodes: function (paths) {
      let nodes = new Set();
      paths.forEach((path) => {
        let nodeList = path.split(" ");
        nodes = new Set([...nodes, ...nodeList]);
      });

      let nodeArray = [];
      nodes.forEach((node) => {
        nodeArray.push({
          key: parseInt(node, 10),
          text: node,
          fill: "#888",
        });
      });
      this.myDiagram.model.nodeDataArray = nodeArray;
    },
    highLightNode: function (id) {
      let node = this.myDiagram.findNodeForKey(id);
      node.elt(0).fill = "rgba(0,90,156,0.3)";
    },
    highLightNodeList: function (idList) {
      for (let i = 0; i < idList.length; i++) {
        this.highLightNode(id);
      }
    },
    generateLinks: function (paths) {
      let linkArray = [];
      let originNodes = new Set();
      let endNodes = new Set();
      for (let i = 0; i < paths.length; i++) {
        let path = paths[i].split(" ");
        let len = path.length;
        originNodes.add(path[len - 1]);
        endNodes.add(path[0]);
        for (let j = 0; j < len - 1; j++) {
          linkArray.push({ from: path[j], to: path[j + 1] });
        }
      }
      this.myDiagram.model.linkDataArray = linkArray;
      this.originNodes = originNodes;
      this.endNodes = endNodes;
    },
    layout: function () {
      let lay = this.myDiagram.layout;
      this.myDiagram.position;
      lay.columnSpacing = 3;
      lay.layerSpacing = 40;
      lay.cycleRemoveOption = go.LayeredDigraphLayout.CycleDepthFirst;
      lay.layeringOption = go.LayeredDigraphLayout.LayerOptimalLinkLength;
      lay.initializeOption = go.LayeredDigraphLayout.InitDepthFirstOut;
      lay.packOption = 10;
    },
    router: function (func, node) {
      self = this;
      func(node);
      node.findLinksConnected().each(function (link) {
        let nextNodeKey = link.data.to;
        if (nextNodeKey == node.key) {
          return;
        }
        let nextNode = self.myDiagram.findNodeForKey(nextNodeKey);
        self.router(func, nextNode);
      });
    },
  },
};
</script>

<style scoped type="scss">
@import "~@/assets/css/reset.css";
#pathGraph {
  display: flex;
  justify-content: center;
  align-items: center;
  height: 379px;
  width: 876px;
  margin: auto;
  border: 1px solid #c0c0c0;
  background: #ffffff;
  border-radius: 7px;
}
</style>