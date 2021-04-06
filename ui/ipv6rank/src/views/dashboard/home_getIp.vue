<template>
  <!-- <div style="position: relative; padding-bottom: 40px; min-height: 100%;"> -->
  <div style="display: flex; flex-direction: column; min-height: 100vh;">
    <div class="not-bottom">
      <head-nav />
      <div class="img">
        <img src="~@/assets/images/logo.png" alt="">
      </div>
      <div class="middle">
        <el-form :inline="true" ref="form">
            <el-form-item>
              <el-input v-model="search" placeholder="请输入要查询的IP地址/AS号/国家名称" @keyup.enter.native="searchButton()"></el-input>
            </el-form-item>
            <el-form-item>
              <el-button type="primary" @click="searchButton()">Search</el-button>
            </el-form-item>
          </el-form>
      </div>
      <div class="tabs">
        <ul class="list">
          <li v-for="(item, index) in selected" :key="index" @click="select(index)">
            <a href="javaScript:void(0)" :class="{active:isSelected === index}">{{item}}</a>
          </li>
        </ul>
      </div>
      <div class="content">
        <div v-if="this.input_type === ''">
          <map-dot :input="search" v-show="isSelected === 0" />
          <topo-v6 :input="search" v-if="isSelected === 1" />
          <!-- <path-graph :input="search" :isclick="isclick" :needRefresh="true" v-show="isSelected === 2" /> -->
          <path-graph :input="search" v-if="isSelected === 2" />
          <probenum-graph :input="search" v-show="isSelected === 3" />
          <asnum-graph :input="search" v-show="isSelected === 4" />
          <relation-graph :input="search" v-show="isSelected === 5" />
          <whois :input="search" v-show="isSelected === 6" />
          <website-domain :input="search" v-show="isSelected === 7"/>
        </div>
        <div v-if="this.input_type === 'ipv6'">
          <map-dot :input="search" v-show="isSelected === 0" />
          <topo-v6 :input="search" v-if="isSelected === 1" />
          <!-- <path-graph :input="search" :isclick="isclick" :needRefresh="true" v-show="isSelected === 2" /> -->
          <path-graph :input="search" v-if="isSelected === 2" />
          <probenum-graph :input="search" v-show="isSelected === 3" />
          <asnum-graph :input="search" v-show="isSelected === 4" />
          <relation-graph :input="search" v-show="isSelected === 5" />
          <whois :input="search" v-show="isSelected === 6" />
          <website-domain :input="search" v-show="isSelected === 7"/>
        </div>
        <div v-else-if="this.input_type === 'AS'">
        </div>
        <div v-else-if="this.input_type === 'country'">
        </div>
      </div>
    </div>
    <div class="bottom">
      <span>@2021 穹眼安全 京ICP备18044233号-2</span>
    </div>
  </div>
</template>

<script>
  import HeadNav from "@/components/HeadNav";
  import MapDot from "@/components/SearchbyAddress/MapDot";
  import TopoV6 from "@/components/SearchbyAddress/TopoV6";
  import PathGraph from "@/components/SearchbyAddress/PathGraph";
  import ProbenumGraph from "@/components/SearchbyAddress/ProbenumGraph";
  import AsnumGraph from "@/components/SearchbyAddress/AsnumGraph";
  import RelationGraph from "@/components/SearchbyAddress/RelationGraph";
  import Whois from "@/components/SearchbyAddress/Whois";
  import WebsiteDomain from "@/components/SearchbyAddress/WebsiteDomain";
  import {getjudgeResult} from "../../api/apiData";
  export default {
    name: "index",
    inject:['reload'],
    components:{
      HeadNav,
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
        search: '', // input输入框
        selected: '',
        isSelected:0, // 默认选中第一个
        input_type: '',
        isclick: false,
      }
    },
    mounted() {
      this.getIP();
    },
    methods:{
      select(index) {
        this.isSelected = index
      },
      getIP() {
        this.$axios({
          method: 'get',
          url: 'http://api.ipv6rank.com:7075/get_ip',
        }).then(res => {
          this.search = res['data']['ip'];
          getjudgeResult(this.search).then( res => {
            if(['ipv6', 'AS', 'country'].includes(res['input_type'])) {
              this.selected = res['tabs']
              this.input_type = res['input_type']
            } else {
              alert('请输入正确的v6地址/AS号/国家名称');
            }
          })
        }).catch(error => {
          console.log(error);
        })
      },
      // 点击搜索按钮后，进入另一个页面
      searchButton() {
        this.$router.push({name: 'homeAfterSearch', params: {searchContent: this.search}});
      }
    },
  }
</script>

<style lang="scss" scoped>
  @import "~@/assets/css/reset.css";
  .not-bottom {
    flex: 1;
  }
  .img{
    img {
      position: relative;
      width: 18%;
    }
    margin-top: 3.8%;
    text-align: center;
  }
  .middle{
    width: 600px;
    margin: 20px auto;
    .el-form-item {
      margin: 0;
    }
    .el-form-item:first-of-type {
      width: 87%;
    }
    .el-form-item:last-of-type {
      width: 13%;
    }
    .el-form-item /deep/ .el-form-item__content {
      line-height: 100%;
      display: inline;
    }
    .el-input /deep/ .el-input__inner {
      height: 37px;
      border-radius: 6px 0 0 6px;
      border: 2px solid #d4d4d4;
      border-right: 1px solid transparent;
    }
    .el-input /deep/ .el-input__inner:focus {
      border-color: #b6b6b6;
    }
    .el-form-item /deep/ .el-button--primary {
      font-size: 15px;
      background-color: #b6b6b6;
      border-color: #cecece;
    }
    .el-button {
      height: 37px;
      width: 80px;
      border-radius: 0 6px 6px 0;
      display: flex;
      justify-content: center;
      align-items: center;
    }
  }
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
  .bottom {
    background: rgb(245, 245, 245);
  }
</style>