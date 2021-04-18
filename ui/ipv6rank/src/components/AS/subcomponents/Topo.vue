<template>
  <div class="topov6 clearfix">
    <div class="left">
      <div class="topo" ref="topo"></div>
    </div>
    <div class="right">
      <div style="position: relative;">
        <h4 class="right-title">AS网络位置信息</h4>
        <ul>
          <li v-for="(val, key, i) in basic" :key="i">
            <div class="front">{{key}} :</div>
            <div class="following">{{val}}</div>
          </li>
        </ul>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'Topo',
  props: {
    res: {
      type: Object,
      default: null
    }
  },
  data() {
    return {
      basic: {},
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
  mounted(){
    if(this.res && !this.flag){
      this.handleChange(this.res)
    }
  },
  methods: {
    handleChange(newVal){
      this.basic = {
        'AS编号': newVal['ASN'],
        'AS类型': newVal['as_type'],
        'AS名称': newVal['aut_name'],
        '归属国家': newVal['country'],
        '描述信息': newVal['descr'],
        '机构编号': newVal['org_id'],
        '机构名称': newVal['org_name'],
        '经度': newVal['position'][0],
        '纬度': newVal['position'][1]
      }
      this.$nextTick(() => {
        RenderTopo(null, this.$refs.topo, this.basic["归属国家"], () => {})
      })
      this.flag = true
    }
  }
}
</script>
<style scoped src="@/assets/css/tabpage.css"></style>
<style scoped lang='scss'>
.topo {
  padding-top: 10px;
  padding-bottom: 10px;
  height:350px;
  .sigma-mouse,
  .sigma-scene {
  height: 350px;
  }
}
</style>
