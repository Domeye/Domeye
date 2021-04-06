<template>
  <div class="topov6 clearfix">
    <div class="left">
      <div class="topo" ref="topo"></div>
    </div>
    <div class="right">
      <div style="position: relative;">
        <h4 class="right-title">IPv6网络位置信息</h4>
        <ul>
          <li v-for="(item, index) in Object.keys(basic)" :key="index">
            <div class="front">{{item}} :</div>
            <div class="following">{{basic[item]}}</div>
          </li>
        </ul>
      </div>
    </div>
  </div>
</template>

<script>
import {getlongestAsPrefix, getlongestInet6Prefix} from "../../api/apiData";

export default {
  name: 'TopoV6',
  props: ["input"],
  data() {
    return {
      basic: '',
      descrData_as: '',
      descrData_inet6: '',
    }
  },
  watch: {
    input() {
      this.getData();
    }
  },
  mounted() {
    this.getData()
  },
  methods: {
    async getData() {
      await getlongestAsPrefix(this.input).then(res => {
        this.descrData_as = res['longest_prefix']
      })
      await getlongestInet6Prefix(this.input).then(res => {
        this.descrData_inet6 = res
      })
      this.getrealData();
      console.log('拓扑图basic:', this.basic)
    },
    getrealData() {
      this.basic = {
        '路由前缀': this.descrData_as['prefix'],
        'AS名称': this.descrData_as['aut_name'],
        '归属国家': this.descrData_as['country'],
        'AS类型': this.descrData_as['as_type'],
        'AS描述': this.descrData_as['descr'],
        '归属机构': this.descrData_as['org_name'],
        '维护人': this.descrData_inet6['admin-c'],
      }
      RenderTopo(null, this.$refs.topo, this.basic["归属国家"], () => {});
    }
  }
}
</script>

<style lang="scss" scoped>
@import "~@/assets/css/tabpage.css";
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