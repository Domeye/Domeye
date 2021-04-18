<template>
  <div>
    <div class="tabs">
      <ul class="list">
        <li v-for="(item, index) in selected" :key="index" @click="select(index)">
          <a href="javaScript:void(0)" :class="{active:isSelected === index}">{{item}}</a>
        </li>
      </ul>
    </div>
    <div class="content">
      <!-- 失活的组件将会被缓存！-->
      <keep-alive>
        <component :is="componentList[isSelected]" :res="res"></component>
      </keep-alive>
    </div>
  </div>
</template>

<script>
import {getASInfo} from "@/api/apiData";
import BasicInfo from './subcomponents/BasicInfo'
import AnnouncePath from './subcomponents/AnnouncePath'
import PeerV4 from './subcomponents/PeerV4'
import PeerV6 from './subcomponents/PeerV6'
import PrefixV4 from './subcomponents/PrefixV4'
import PrefixV6 from './subcomponents/PrefixV6'
import Topo from './subcomponents/Topo'
import Whois from './subcomponents/Whois'
export default {
  name: 'AS',
  data() {
    return {
      isSelected: 0,
      selected: ['基本信息','网络位置','传播路径','v4前缀','v6前缀','v4peer','v6peer','whois'],
      componentList: ['BasicInfo','Topo','AnnouncePath','PrefixV4','PrefixV6','PeerV4','PeerV6','Whois'],
      res: null
    }
  },
  methods: {
    select(index){
      this.isSelected = index
    }
  },
  components: {
    BasicInfo,
    AnnouncePath,
    PeerV4,
    PeerV6,
    PrefixV4,
    PrefixV6,
    Topo,
    Whois
  },
  props: {
    search: {
      type: String,
      default: ''
    }
  },
  created() {
    getASInfo(this.search).then(res => {
      // console.log(res)
      this.res = res
    })
  }
}
</script>
<style scoped lang='scss'>
  /* tab选项卡的样式 */
  .tabs{
    display: flex;
    justify-content: center;
    width: 880px;
    height: 36px;
    margin: 35px auto 0 auto;
    /*border-bottom: 1px solid #000;*/
    background-color: #f5f5f5;
    .list{
      display: flex;
      justify-content: space-around;
      width: 100%;
      position: relative;
      li:first-child{
        margin-left: 50px;
      }
      li:last-child{
        margin-right: 50px;
      }
      li{
        height: 30px;
        a{
          margin-top: 5px;
          padding: 3px 6px 8px 6px;
          height: 20px;
          color: #009a61;
          font-size: 18px;
        }
      }
    }
  }
  /* 内容样式 */
  .content{
    width: 878px;
    height: 380px;
    border: 1px solid rgb(194, 194, 194);
    margin: 0 auto;
    background-color: #fff;
    overflow-y:hidden; 
  }
  /* 选中tab时的样式 */
  .active{
    background: #fff;
    border: 1.3px solid rgb(218, 218, 218);
    border-bottom: 1px solid transparent;
  }
</style>
