<template>
  <div class="home">
    <div class="dashboard">
      <ul class="list">
        <li class="link"><a href="#">链接1</a></li>
        <li class="link"><a href="#">链接2</a></li>
        <li class="link"><a href="#">链接3</a></li>
        <li class="link"><a href="#">链接4</a></li>
      </ul>
    </div>
    <div class="middle">
      <el-input placeholder="请输入IPv6地址" v-model="search" >
<!--        <i class="el-icon-search" slot="prepend"></i>-->
        <el-button type="primary" slot="append" style="width: 80px;">Search</el-button>
      </el-input>
    </div>
    <div class="card">
      <el-tabs tab-position="top" type="border-card" v-model="activeName" class="card-item">
        <el-tab-pane label="测试数据1" name="first" class="tab-container"><test></test></el-tab-pane>
        <el-tab-pane label="测试数据2" name="second">
          <ul>
            <li>key: value</li>
            <li>key: value</li>
            <li>key: value</li>
            <li>key: value</li>
            <li>key: value</li>
            <li>key: value</li>
          </ul>
        </el-tab-pane>
        <el-tab-pane label="测试数据3" name="third">测试数据3</el-tab-pane>
        <el-tab-pane label="测试数据4" name="fourth">测试数据4</el-tab-pane>
        <el-tab-pane label="测试数据5" name="fifth">测试数据5</el-tab-pane>
        <el-tab-pane label="测试数据6" name="sixth">测试数据6</el-tab-pane>
      </el-tabs>
    </div>
  </div>
</template>

<script>
  import Test from './test'
  export default {
    name: "index",
    components:{
      Test
    },
    data() {
      return {
        search: '', // input输入框
        activeName:'first',
      }
    }
  }
</script>

<style>
  * {
    margin: 0;
    padding: 0;
  }
  a {
  display: inline-block;
  text-decoration: none;
  color: #999;
  }

  ul {
  list-style: none;
  }
  li{

    margin-left: 8px;
  }
  .list {
    display: flex;
    justify-content: space-between;
    width: 320px;
    margin: 16px 0 12px 16px;
    font-size: 14px;
  }
  .list a {
    padding: 5px;
  }
  .middle{
    width: 800px;
    margin: 70px auto 20px auto;
  }
  .card{
    width: 1000px;
    margin: 100px auto 0 230px;
  }
  .card-item{
    position: relative;
    left: 50px;
  }
  /* 重置el-input样式, style标签上不能加 scoped */
  .el-input__inner {
    line-height: 50px;
    height: 50px;
    border-radius: 8px;
    border: 2px solid #DCDFE6;
    border-right: 2px solid transparent;
  }
  .el-input__inner:focus {
    border-color: #4e6ef2;
  }
  .el-input-group__append{
    position: relative;
    left: -2px;
    border: 2px solid #4e6ef2;
    border-bottom-right-radius: 8px;
    border-top-right-radius: 8px;
    color: #fff;
    background-color: #4e6ef2;
  }
  .el-tabs__item {
    width: 150px;
    height: 50px;
    line-height: 50px;
    text-align: center;
  }
  .el-tabs--card>.el-tabs__header .el-tabs__nav{
    border: 1px solid #DCDFE6;
  }

  /* 底部border透明 */
  .el-tabs--card>.el-tabs__header{
    border-bottom: 1px solid transparent;
  }
  .el-tabs__nav{
    position: relative;
    left: 50px;
  }
</style>
