<template>
  <el-container class="layout" style="border: 1px solid #eee">
    <el-aside width="200px" style="background-color: rgb(238, 241, 246)">ASIDE</el-aside>
    <el-container>
      <el-header style="text-align: right; font-size: 12px">HRADER</el-header>
      <el-main>
        <el-table id="tableData" :data="tableData" :height="height">
          <el-table-column prop="date" label="日期" width="140"></el-table-column>
          <el-table-column prop="name" label="姓名" width="120"></el-table-column>
          <el-table-column prop="address" label="地址"></el-table-column>
        </el-table>
      </el-main>
    </el-container>
  </el-container>
</template>
<script>
export default {
  name: "AutoHeightTable",
  data() {
    const item = {
      date: "2016-05-02",
      name: "王小虎",
      address: "上海市普陀区金沙江路 1518 弄"
    };
    return {
      tableData: Array(100).fill(item),
      height: "200px"
    };
  },
  mounted() {
    this.getAutoHeight();
    const self = this;
    window.onresize = function() {
      self.getAutoHeight();
    };
  },
  methods: {
    getAutoHeight() {
      let el = document.querySelector("#tableData"),
        elParent = el.parentNode,
        pt = this.getStyle(elParent, "paddingTop"),
        pb = this.getStyle(elParent, "paddingBottom");
      this.$nextTick(() => {
        this.height = elParent.clientHeight - (pt + pb) + "px";
      });
    },
    getStyle(obj, attr) {
      // 兼容IE浏览器
      let result = obj.currentStyle
        ? obj.currentStyle[attr].replace("px", "")
        : document.defaultView
            .getComputedStyle(obj, null)[attr].replace("px", "");
      return Number(result);
    }
  }
};
</script>
<style>
.layout {
  height: 100%;
  width: 100%;
  overflow: hidden;
}
.el-header {
  background-color: #b3c0d1;
  color: #333;
  line-height: 60px;
}

.el-aside {
  color: #333;
}
.el-main {
  overflow: hidden !important;
}
</style>
