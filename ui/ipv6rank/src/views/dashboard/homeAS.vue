<template>
  <!-- <div style="position: relative; padding-bottom: 40px; min-height: 100%;"> -->
  <div style="display: flex; flex-direction: column; min-height: 100vh;">
    <div class="not-bottom">
      <HeadNav />
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
      <AS :search="search"/>
    </div>
    <div class="bottom">
      <span>@2021 穹眼安全 京ICP备18044233号-2</span>
    </div>
  </div>
</template>

<script>
  import HeadNav from "@/components/HeadNav"
  import AS from "@/components/AS"
  export default {
    name: "homeAS",
    data() {
      return {
        search: '4134'
      }
    },
    inject:['reload'],
    components:{
      HeadNav,
      AS
    },
    methods: {
      searchButton() {
        console.log('search='+this.search)
      }
    }
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
  .bottom {
    background: rgb(245, 245, 245);
  }
</style>