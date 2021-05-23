<template>
	<div class="searchbyAddress">
		<div class="tabs">
        <ul class="list">
          <li v-for="(value, key) in tabs_components" :key="key" @click="select(value)">
            <a href="javaScript:void(0)" :class="{active:isSelectedComponent === value[Object.keys(value)[0]]}">{{Object.keys(value)[0]}}</a>
          </li>
        </ul>
      </div>
      <div class="content">
        <keep-alive>
          <component v-bind:is="currentTabComponent" :input="search"></component>
        </keep-alive>
      </div>
	</div>
</template>

<script>
import MapDot from "@/components/Address/Address/MapDot";
import TopoV6 from "@/components/Address/Address/TopoV6";
import PathGraph from "@/components/Address/Address/PathGraph";
import ProbenumGraph from "@/components/Address/Address/ProbenumGraph";
import AsnumGraph from "@/components/Address/Address/AsnumGraph";
import RelationGraph from "@/components/Address/Address/RelationGraph";
import Whois from "@/components/Address/Address/Whois";
import WebsiteDomain from "@/components/Address/Address/WebsiteDomain";

export default {
  name: "SearchbyAddress",
	props: ['search'],
	components: {
	  MapDot,
    TopoV6,
    PathGraph,
    ProbenumGraph,
    AsnumGraph,
    RelationGraph,
    Whois,
    WebsiteDomain,
	},
	data() {
		return {
			tabs_components: '',
			isSelectedComponent: 'MapDot',
		}
	},
  mounted() {
    this.$axios({
      method: "post",
      url: "http://10.99.8.12:7079/judge",
      data: {
        input_search: this.search,
      }
    }).then( res => {
      this.tabs_components = res['data']['tabs']
    })
  },
	computed: {
		currentTabComponent: function() {
			return this.isSelectedComponent;
		}
	},
	methods: {
		select(value) {
			this.isSelectedComponent = value[Object.keys(value)[0]]
		}
	}
}
</script>

<style lang="scss" scoped>
.searchbyAddress {
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