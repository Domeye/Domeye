<template>
  <div class="statistics1-1">
    <div class="info">
      本页面提供全球各国as自治系统总数排名、总个数排名情况。本排名最后更新时间是 2021-02-02日 。
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
</template>

<script>

export default {
  components: {
  },
  data() {
    return {
     
    }
  },
  methods: {
    
  }
}
</script>

<style lang='scss' scoped>
@import "~@/assets/css/reset.css";
.statistics1-1 {
  .info {
    margin-top: 5px;
    padding-left: 10px;
    font-size: 16px;
    // border: 2px solid rgb(214, 214, 214);
    // border-radius: 8px;
    // padding: 5px 5px 5px 15px;
    // width: 700px;
    // height: 20px;
  }
  .table table {
    margin-top: 20px;
    height: 400px;
    border-collapse: collapse;
    //border: 1px solid rgb(22, 22, 110);
    tr th, tr td { border:1px solid rgb(226, 226, 226); }
    th {
      background: rgb(243, 243, 243);
      height: 34px;
      font-size: 16px;
      color: rgb(0, 0, 0);
      font-weight: normal;
    }
    td {
      height: 32px;
      width: 100%;
      white-space: nowrap;
      overflow: hidden;
      text-overflow: ellipsis;
    }
  }
}
</style>