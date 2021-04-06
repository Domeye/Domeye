sigma.canvas.nodes.border = function(node, context, settings) {
  var prefix = settings('prefix') || '';

  context.fillStyle = node.color || settings('defaultNodeColor');
  context.beginPath();
  context.arc(
    node[prefix + 'x'],
    node[prefix + 'y'],
    node[prefix + 'size'],
    0,
    Math.PI * 2,
    true
  );

  context.closePath();
  context.fill();

  // Adding a border
  context.lineWidth = node.borderWidth || 1.2;
  context.strokeStyle = node.borderColor || 'rgba(0,0,0,0.5)';
  context.stroke();
};

sigma.classes.graph.addMethod('outneighbors', function(nodeId) {
    var k,
    neighbors = {},
    index = this.outNeighborsIndex[nodeId] || {};

    for (k in index)
        neighbors[k] = this.nodesIndex[k];

    return neighbors;
});

sigma.classes.graph.addMethod('allneighbors', function(nodeId) {
    var k,
        neighbors = {},
        index = this.allNeighborsIndex[nodeId] || {};

    for (k in index)
        neighbors[k] = this.nodesIndex[k];

    return neighbors;
});

sigma.classes.graph.addMethod('peers', function(nodeId) {
    var peers;
    var outArr=[], inArr=[];
    outIndex = this.outNeighborsIndex[nodeId];
    inIndex = this.inNeighborsIndex[nodeId];
    for (k in outIndex){
        e = outIndex[k];
        e0 = e[Object.keys(e)[0]];
        outArr.push({n:this.nodesIndex[k], e:e0});
    }
    outArr.sort(function(a,b) {
        var keyA = a.e.transmit;
        var keyB = b.e.transmit;
        if (keyA > keyB) return -1;
        if (keyA < keyB) return 1;
        return 0;
    });
    for (k in inIndex){
        e = inIndex[k];
        e0 = e[Object.keys(e)[0]];
        inArr.push({n:this.nodesIndex[k], e:e0})
    }
    inArr.sort(function(a,b) {
        var keyA = a.e.transmit;
        var keyB = b.e.transmit;
        if (keyA > keyB) return -1;
        if (keyA < keyB) return 1;
        return 0;
    });
    peers = {'out':outArr,'in':inArr};
    return peers;
});

var graph_v4;
var graph_v6;
var sig_v4;
var sig_v6;
const path = './static/topo/country_topo/';
/*
    RenderTopo方法
    说明：渲染各个国家的拓扑连接图
    v4elem(可选): ipv4拓扑图挂载dom节点
    v6elem(可选): ipv6拓扑图挂载dom节点
    countrycode(可选): 需要渲染的国家，数据格式为iso标准国家代码
    callback: 节点点击事件的回调函数
   
*/
function RenderTopo(v4elem, v6elem, countrycode = 'CN', callback) {
    var _ = {
        $: function (id) {
            return document.getElementById(id);
        }
    };

    var blink_color = ['#0088cc', '#ff5500'];
    var settings = {
      minEdgeSize: 0.2,
      maxEdgeSize: 1,
      minNodeSize: 3,
      maxNodeSize: 5,
      labelThreshold: 3.5,
      defaultLabelColor: '#fff',
      defaultLabelSize: 10,
      borderSize: 1.2,
      defaultNodeBorderColor: '#fff',
      zoomingRatio: 1.1,
      sideMargin: 0.3,
      mouseZoomDuration: 0,
      skipErrors: true,
      defaultNodeType: 'border',
      doubleClickEnabled: false
    };

    var blink_nodes = [];
    var origin_color = {};
    var blink_nodes_6 = [];
    var origin_color_6 = {};
    var blink_dict = {};

    if (v4elem) {
        sigma.parsers.json( path + countrycode + 'v4.json',
            {
                renderer: {
                    container: v4elem,
                    type: 'canvas'
                },
                settings: settings
            },
            function (s) {
                if (s.graph.nodes('extra_data')) {
                    blink_nodes = s.graph.nodes('extra_data').blink;
                    s.graph.dropNode('extra_data');
                }
    
                graph_v4 = s.graph;
                sig_v4 = s;
    
                bindEvents(s, blink_nodes, 'ipv4');
                s.refresh();
            }
        );
    }

    if (v6elem) {
        console.log("country11:", countrycode.toString())
        sigma.parsers.json(path + countrycode + 'v6.json', //'/bgp/static/topo/topo-v6.json',
        {
            renderer: {
                container: v6elem,
                type: 'canvas'
            },
            settings: settings
        },
        function (s) {
            if (s.graph.nodes('extra_data')) {
                blink_nodes_6 = s.graph.nodes('extra_data').blink;
                s.graph.dropNode('extra_data');
            }
            graph_v6 = s.graph;
            sig_v6 = s;

            bindEvents(s, blink_nodes, 'ipv6');
            s.refresh();
        }
        );
    }
    
    function bindEvents(s, blink_nodes, t) {
        var stat = 'default';

        s.graph.nodes().forEach(function (n) {
            n.originalColor = n.color;
        });
        s.graph.edges().forEach(function (e) {
            e.originalColor = e.color;
            e.originalSize = e.size;
        });

        s.bind('rightClickStage', function (e) {
            s.cameras[0].goTo({x: 0, y: 0, ratio: 1, angle: 0});
            s.refresh();
        });

        s.bind('overNode', function (e) {
            if (stat == 'clickNode')
                return;
            var nodeId = e.data.node.id;
            toKeep = s.graph.allneighbors(nodeId);
            toKeep[nodeId] = e.data.node;

            s.graph.nodes().forEach(function (n) {
                if (toKeep[n.id]) {
                    if (n.color.startsWith('#ff'))
                        n.color = '#ff5500';
                    else
                        n.color = '#0099ff';
                }
                else
                    n.color = n.originalColor
            });
            s.graph.edges().forEach(function (e) {
                if (nodeId == e.source || nodeId == e.target) {
                    e.size = 0.6;
                }
                else
                    e.color = e.originalColor;
            });
            s.refresh({skipIndexation: true});
        });

        s.bind('clickNode', function (e) {
            callback('clickNode', e)
            stat = 'clickNode';
            var nodeId = e.data.node.id;
            toKeep = s.graph.allneighbors(nodeId);
            toKeep[nodeId] = e.data.node;

            s.graph.nodes().forEach(function (n) {
                if (toKeep[n.id])
                    if (n.color.startsWith('#ff'))
                        n.color = '#ff5500';
                    else
                        n.color = '#0099ff';
                else {
                    n.hidden = true;
                }
            });

            s.graph.edges().forEach(function (e) {
                if (nodeId == e.source || nodeId == e.target) {
                    e.size = 0.6;

                }
                else
                    e.hidden = true;

            });
            s.refresh({skipIndexation: true});
        });

        s.bind('outNode', function (e) {
            if (stat == 'clickNode')
                return;
            s.graph.nodes().forEach(function (n) {
                n.color = n.originalColor;
            });

            s.graph.edges().forEach(function (e) {
                e.color = e.originalColor;
                e.size = e.originalSize;
            });

            // Same as in the previous event:
            s.refresh({skipIndexation: true});
        });

        s.bind('clickStage', function (e) {
            stat = 'default';
            s.graph.nodes().forEach(function (n) {
                n.color = n.originalColor;
                n.hidden = false;
            });

            s.graph.edges().forEach(function (e) {
                e.color = e.originalColor;
                e.hidden = false;
            });

            s.refresh({skipIndexation: true});
        });
    }
}
