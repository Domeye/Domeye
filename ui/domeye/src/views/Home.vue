<template>
  <div class="home">
    <el-container style="height: 100%" direction="vertical">
      <el-header style="height: 45px">
        <head-nav />
      </el-header>
      <el-main style="height: 900px">
        <div class="search">
          <el-form ref="form" label-width="40%">
            <el-form-item>
              <el-input
                v-model="form.content"
                placeholder="请输入机构名称、自治域、城市、IP前缀等关键词搜索"
              >
              </el-input>
            </el-form-item>
            <el-form-item>
              <div class="button">
                <el-button type="primary" @click="search">搜索</el-button>
              </div>
            </el-form-item>
          </el-form>
        </div>
        <world-map></world-map>
      </el-main>
      <el-footer style="height: 23px">
        <div class="domeye-bottom">
          <span>© Domeye </span>
        </div>
      </el-footer>
    </el-container>
  </div>
</template>

<script>
// @ is an alias to /src
import WorldMap from "@/components/WorldMap";
import HeadNav from "@/components/HeadNav";

export default {
  name: "Home",
  components: {
    HeadNav,
    WorldMap,
  },
  data() {
    return {
      form: {
        content: "",
      },
      select: "",
    };
  },
  methods: {
    search() {
      this.$router.push({
        path: "/searchlist",
        query: {
          content: this.form.content,
        },
      });
    },
  }
};
</script>

<style lang="scss" scoped>
@import "~@/assets/style/reset.css";
.home {
  height: 100%;
  .el-container {
    padding: 0px;
    margin: 0px;
    .el-header {
      background-color: rgb(0, 0, 0);
      position: fixed;
      z-index: 10; // 所以head不在正常文档布局流中
      width: 100%;
      top: 0;
      left: 0;
      padding: 0;
    }
    .el-main {
      margin: 0 0 0 0;
      padding: 0 0 0 0;
      background-color: rgb(19, 19, 19);
      // overflow-y: hidden;
      display: flex;
      align-items: center;
      justify-content: center;
      .search {
        text-align: center;
        width: 45%;
        z-index: 3;
        .el-form {
          display: flex;
          width: 100%;
          .el-form-item /deep/ .el-form-item__content {
            margin-left: 0 !important; // 解决嵌在element.style中的样式代码
          }
          .el-form-item {
            margin-bottom: 60px;
            .el-input /deep/ .el-input__inner {
              background-color: #7d6f6f00;
              border: 1px solid #555;
              font-size: 13px;
              border-radius: 4px;
              color: #c4c4c4;
            }
            .el-input /deep/ .el-input__inner::-webkit-input-placeholder {
              color: rgb(146, 146, 146);
            }
          }
          .el-form-item:first-of-type {
            width: 75%;
          }
          .el-form-item:last-of-type {
            .button {
              width: 120px;
              .el-button {
                width: 60%;
                height: 39px;
                background: rgb(90, 108, 187);
                border-color: rgb(90, 108, 187);
              }
            }
            width: 20%;
          }
        }
      }
      .echarts-map {
        position: fixed; // fixed生成固定定位的元素，相对于浏览器窗口进行定位。
        z-index: 1;
        top: 5%;
      }
    }
    .el-footer {
      width: 100%;
      background-color: rgb(0, 0, 0);
      position: fixed;
      z-index: 10; // 所以head不在正常文档布局流中
      bottom: 0;
      color: rgb(255, 255, 255);
      display: flex;
      align-items: center;
      justify-content: center;
    }
  }
}
</style>
