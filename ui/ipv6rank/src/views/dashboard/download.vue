<template>
  <div style="display: flex; flex-direction: column; min-height: 100%">
    <div class="not-bottom">
      <head-nav />
      <!-- <div class="headline">
        <span>CAIDA Services - Overview of CAIDA Data Interfaces and Services</span>
      </div> -->
      <div class="overview" v-show="false">
        <span>CAIDA offers a number of data interfaces and services that provide interesting and insightful views of the data we collect and curate. These services allow a much broader community of users to become familiar with CAIDA data: to view annotated Internet data; to provide feedback on analysis and inference methods; to execute on-demand measurements; or to investigate or correlate to other data.</span>
      </div>
      <div class="title">
        <span>CAIDA Data Interfaces and Services</span>
      </div>
      <div class="table">
        <table border="1" width="100%" style="table-layout:fixed"> 
          <thead>
            <tr class="title">
              <th>序号</th>
              <th>下载地址</th>
              <th>网站大类</th>
              <th>网站子类</th>
              <th>ipv6地址</th>
              <th>地址类型</th>
            </tr>
            <tr class="filter">
              <td></td>
              <td></td>
              <td><input v-model="search.bigtype" placeholder="过滤" type="text"></td>
              <td><input v-model="search.smalltype" placeholder="过滤" type="text"></td>
              <td></td>
              <td></td>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td class="index"><span class="index"></span></td>
              <td><span></span></td>
              <td><span></span></td>
              <td><span></span></td>
              <td><span></span></td>
              <td><span></span></td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>
    <div class="bottom">
      <span>@2021 穹眼安全 京ICP备18044233号-2</span>
    </div>
  </div>
</template>

<script>
import headNav from "@/components/HeadNav";

export default {
  name: "download",
  components: {
    headNav,
  },
  data() {
    return {
      search: {
        bigtype: "",
        smalltype: "",
        as: "",
      },
    }
  }
}
</script>

<style lang="scss" scoped>
@import "~@/assets/css/reset.css";
.not-bottom {
  flex: 1;
}
.headline {
  margin: 10px 0 0 30px;
  font-size: 15px;
  font-weight: bold;
  color: rgb(44, 44, 136);
}
.overview {
  margin: 15px 1.5% 0 1.5%;
  border: 5px solid rgb(226, 226, 226);
  border-radius: 5px;
  padding: 10px;
}
.title {
  margin: 15px 0 0 1.5%;
  font-size: 17px;
  font-weight: bold;
  color: rgb(44, 44, 136)
}
.table table {
  margin-top: 15px;
  margin-left: 1.5%;
  width: 97%;
  height: 350px;
  border-collapse: collapse;
  table, table tr th, table tr td { border:2px solid #b9b9b9; }
  th {
    background: rgb(243, 243, 243);
    height: 34px;
    font-size: 16px;
    color: rgb(56, 56, 56);
    font-weight: normal;
  }
  td {
    height: 32px;
    width: 100%;
    white-space: nowrap;
    overflow: hidden;
    text-overflow: ellipsis;
    input {
      width: 100%;
      height: 100%;
      border: 2px solid rgb(231, 231, 231);
      outline: 2px solid rgb(192, 192, 192);
      color: gray;
      text-indent:7px;
      font-size: 13.5px;
      //border-radius: 5px;
    }
  }
}
</style>
