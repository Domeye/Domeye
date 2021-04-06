<template>
  <div class="address">
    <head-nav />
    <div class="filter">
      <el-form :inline="true" :model="formInline" class="demo-form-inline">
        <el-form-item label="国家:">
          <el-select v-model="formInline.region" placeholder="请输入国家名称">
            <el-option label="中国" value="中国"></el-option>
            <el-option label="美国" value="美国"></el-option>
          </el-select>
        </el-form-item>
        <el-form-item label="类型:">
          <el-select v-model="formInline.region" placeholder="请输入AS类型">
            <el-option label="区域一" value="shanghai"></el-option>
            <el-option label="区域二" value="beijing"></el-option>
          </el-select>
        </el-form-item>
        <el-form-item>
          <el-button type="primary" @click="onSubmit">过滤</el-button>
        </el-form-item>
      </el-form>
    </div>
    <div class="content">
      <div class="realcontent"></div>
      <div class="img"></div>
    </div>
    <div class="table">
      <el-table :data="tableData" border style="width: 100%">
        <el-table-column prop="date" label="日期" width="180">
        </el-table-column>
        <el-table-column prop="name" label="姓名" width="180">
        </el-table-column>
        <el-table-column prop="address" label="地址"> </el-table-column>
      </el-table>
    </div>
    <div class="domeye-bottom">
      <span>© Domeye </span>
    </div>
  </div>
</template>

<script>
import HeadNav from "@/components/HeadNav";
export default {
  name: "Address",
  components: {
    HeadNav,
  },
  data() {
    return {
      tableData: [
        {
          date: "2016-05-02",
          name: "王小虎",
          address: "上海市普陀区金沙江路 1518 弄",
        },
        {
          date: "2016-05-04",
          name: "王小虎",
          address: "上海市普陀区金沙江路 1517 弄",
        },
        {
          date: "2016-05-01",
          name: "王小虎",
          address: "上海市普陀区金沙江路 1519 弄",
        },
        {
          date: "2016-05-03",
          name: "王小虎",
          address: "上海市普陀区金沙江路 1516 弄",
        },
      ],
      formInline: {
        user: "",
        region: "",
      },
    };
  },
  methods: {
    onSubmit() {
      console.log("submit!");
    },
  },
};
</script>

<style lang="scss" scoped>
// @import "~@/assets/style/reset.css";
.address {
  height: 100%;
  .navbar {
    z-index: 10;
    height: 45px;
    background-color: rgb(0, 0, 0);
    position: fixed; // 所以head不在正常文档布局流中
    width: 100%;
    top: 0;
    left: 0;
    // margin: 0 20px 0 20px;
  }
  .filter {
    margin-top: 62px;
    text-align: center;
    .el-form {
      .el-form-item {
        margin-bottom: 0;
        margin-right: 20px;
        .el-button {
          height: 37px;
          border-color: rgb(90, 108, 187);
        }
      }
      .el-form-item /deep/ .el-input__inner {
        height: 38px;
      }
      .el-form-item /deep/ .el-form-item__content {
        line-height: 38px;
      }
      .el-form-item /deep/ .el-form-item__label {
        line-height: 38px;
      }
    }
  }
  .content {
    margin-top: 30px;
    display: flex;
    .realcontent {
      width: 830px;
      height: 300px;
      margin-left: 40px;
      border: 1px solid rgb(180, 180, 180);
      background: rgb(214, 214, 214);
      display: inline-block;
      vertical-align: top;
      margin-right: 30px;
      // margin-left: 30px;
    }
    .img {
      width: 320px;
      height: 300px;
      border: 2px solid rgb(180, 180, 180);
      border-radius: 4px;
      margin-right: 20px;
    }
  }
  .table {
    margin: 45px 40px 40px 40px;
  }
  // .bottom {
  //   background: black;
  //   color: white;
  //   height: 23px;
  //   font-size: 12px;
  //   display: flex;
  //   align-items: center;
  //   justify-content: center;
  // }
}
</style>
