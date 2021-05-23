<template>
	<div class="searchbyNone">
		<div class="tabs">
        <ul class="list">
          <li v-for="(value, key) in tabs_components" :key="key" @click="select(value)">
            <a href="javaScript:void(0)" :class="{active:isSelectedComponent === value}">{{key}}</a>
          </li>
        </ul>
      </div>
      <div class="content">
        <component v-bind:is="currentTabComponent" :search="search"></component>
      </div>
	</div>
</template>

<script>
import Overview from "@/components/Default/Default/Overview";
import AddressAllocate from "@/components/Default/Default/AddressAllocate";
import AddressDeclare from "@/components/Default/Default/AddressDeclare";
import AsResource from "@/components/Default/Default/AsResource";
import WebsiteResource from "@/components/Default/Default/WebsiteResource";
import ActiveAddress from "@/components/Default/Default/ActiveAddress";
import Infrastructure from "@/components/Default/Default/Infrastructure";
import Topo from "@/components/Default/Default/Topo";
import visjs from "@/components/Default/Default/visjs";


export default {
  name: "SearchbyNone",
	props: ['search'],
  data: {
    as: '4134'
  },
	components: {
		Overview,
		AddressAllocate,
		AddressDeclare,
		AsResource,
		WebsiteResource,
		ActiveAddress,
		Infrastructure,
    Topo,
    visjs,
	},
	data() {
		return {
			tabs_components: {'基本概述': 'Overview', '地址分配':'AddressAllocate', '路由宣告':'AddressDeclare', "AS资源":'AsResource', "网站资源":'WebsiteResource', 
         "活跃地址":'ActiveAddress', "基础设施":'Infrastructure', "互联拓扑":'visjs'},
			isSelectedComponent: 'Overview',
		}
	},
	computed: {
		currentTabComponent: function() {
			return this.isSelectedComponent;
		}
	},
  mounted() {},
	methods: {
		select(value) {
			this.isSelectedComponent = value
		}
	}
}
</script>

<style lang="scss" scoped>
.searchbyNone {
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
  }
  /* 选中tab时的样式 */
  .active{
    background: #fff;
    border: 1.3px solid rgb(218, 218, 218);
    border-bottom: 1px solid transparent;
  }
}
</style>