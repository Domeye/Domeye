<template>
  <div id="PeerV4"></div>
</template>

<script>
import G6 from '@antv/g6'
export default {
  name: 'PeerV4',
  props: {
    res: {
      type: Object,
      default: null
    }
  },
  data() {
    return {
      flag: false // 标志是否已经渲染，即是否执行过handleChange
    }
  },
  watch: {
    res(newVal){
      if(newVal && !this.flag){
        this.handleChange(newVal)
      }
    }
  },
  mounted() {
    if(this.res && !this.flag){
      this.handleChange(this.res)
    }
  },
  methods: {
    drawGraph(data){  
      const graph = new G6.TreeGraph({
        container: 'PeerV4',
        width: 878,
        height: 380,
        // fitView: true, // 图自适应窗口大小
        modes: {
          default: [
            {
              type: 'collapse-expand',
              onChange: function onChange(item, collapsed) {
                const data = item.get('model');
                data.collapsed = collapsed;
                return true;
              },
            },
            'drag-canvas',
            'zoom-canvas',
          ],
        },
        defaultNode: {
          size: 26,
          anchorPoints: [
            [0, 0.5],
            [1, 0.5],
          ],
        },
        defaultEdge: {
          type: 'cubic-horizontal',
        },
        layout: {
          type: 'mindmap',
          direction: 'H',
          getHeight: () => {
            return 16;
          },
          getWidth: () => {
            return 16;
          },
          getVGap: () => {
            return 10;
          },
          getHGap: () => {
            return 80;
          },
          getSide: (d) => {
            if (d.id === 'v4Upstream') {
              return 'left';
            }
            return 'right';
          },
        },
      });

      let centerX = 0;
      graph.node(function (node) {
        if (node.id === 'center') {
          centerX = node.x;
        }

        return {
          // label: node.id,
          labelCfg: {
            position:
              node.children && node.children.length > 0
                ? 'left'
                : node.x > centerX
                ? 'right'
                : 'left',
            offset: 5,
          },
        };
      });

      graph.data(data);
      graph.render();
      graph.fitView();  // 图自适应窗口大小
    },
    handleChange(newVal){
      let data = {
        id: 'center',
        label: newVal['ASN'],
        children: [
          {
            id: 'v4Upstream',
            label: 'v4Upstream',
            children: []
          },
          {
            id: 'v4Downstream',
            label: 'v4Downstream',
            children: []
          }
        ]
      }

      let len = newVal['v4Upstream'].length
      for(let i = 0; i < len; i++){
        data.children[0].children.push(
          {
            id: 'v4Upstream_' + i,
            label: newVal['v4Upstream'][i]
          }
        )
      }
      
      len = newVal['v4Downstream'].length
      for(let i = 0; i < len; i++){
        data.children[1].children.push(
          {
            id: 'v4Downstream_' + i,
            label: newVal['v4Downstream'][i]
          }
        )
      }
      
      this.drawGraph(data)

      this.flag = true
    }
  },
}
</script>
<style scoped lang='scss'>
</style>
