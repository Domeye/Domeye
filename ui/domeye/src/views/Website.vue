<template>
  <div class="website">
    <head-nav />
    <div class="search">
      <el-form :inline="true" ref="form" label-width="80%">
        <el-form-item>
          <el-input v-model="searchContent" placeholder="请输入网站网址或名称">
          </el-input>
        </el-form-item>
        <el-form-item>
          <el-button type="primary" @click="search(searchContent)"
            >搜索</el-button
          >
        </el-form-item>
      </el-form>
    </div>
    <hr />
    <website-rank />
    <area-rank />
    <routing-rank />
    <div class="domeye-bottom">
      <span>© Domeye </span>
    </div>
  </div>
</template>

<script>
import HeadNav from "@/components/HeadNav";
import WebsiteRank from "@/components/WebsiteRank";
import AreaRank from "@/components/AreaRank";
import RoutingRank from "@/components/RoutingRank";
export default {
  name: "Website",
  components: {
    HeadNav,
    WebsiteRank,
    AreaRank,
    RoutingRank,
  },
  data() {
    return {
      searchContent: "",
    };
  },
};
</script>

<style lang="scss" scoped>
@import "~@/assets/style/reset.css";  // 为啥不引入也能生效？？？？
.website {
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
  .search {
    margin-top: 45px;
    padding: 12px 30px 6px 30px;
    .el-form {
      text-align: center;
      .el-form-item {
          margin-bottom: 1px;
      }
      .el-form-item:first-of-type {
        .el-input /deep/ .el-input__inner {
            width: 400px;
            border: 1px solid rgb(58, 58, 58);
            font-size: 13px;
            border-radius: 4px;
            color: #474747;
            height: 35px;
          }
          .el-input .el-input__inner::-webkit-input-placeholder {
            color: rgb(95, 95, 95);
          }
      }
      .el-form-item:last-of-type {
        margin-left: 20px;
        .el-button {
          line-height: 0.65;
          border-color: rgb(90, 108, 187);
        }
      }
    }
  }
  hr {
    background-color: rgb(202, 202, 202);
    height: 1px;
    border: none;
    width: 100%;
    margin-bottom: 15px;
  }
  .websiteRank, .areaRank, .routingRank {
    margin: 10px 25px 40px 25px;
  }
}
</style>
