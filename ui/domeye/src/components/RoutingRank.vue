<template>
  <div class="routingRank">
    <div
      class="tag"
      style="width: 120px; height: 32px; background-color: #f12f3d"
    >
      <span style="line-height: 32px; font-size: 14px; color: #fff"
        >路由宣告排名</span
      >
    </div>
    <div class="row">
      <div class="column">
        <div class="title">
          <span class="category">中国电信</span>
        </div>
        <el-table
          :data="routingData"
          :header-cell-style="{ 'text-align': 'center' }"
          :cell-style="{ 'text-align': 'center' }"
        >
          <el-table-column prop="ASNumber" label="AS号" />
          <el-table-column prop="organization" label="机构名称" />
          <el-table-column prop="routerNumber" label="路由条数" />
        </el-table>
        <div class="bottom" @click="moreRank">
          <el-button class="more">更多排行</el-button>
        </div>
      </div>

      <div class="column">
        <div class="title">
          <span class="category">中国移动</span>
        </div>
        <!--table顶部效果,底部border和左边的border-->
        <el-table
          :data="routingData"
          :header-cell-style="{ 'text-align': 'center' }"
          :cell-style="{ 'text-align': 'center' }"
        >
          <el-table-column prop="ASNumber" label="AS号" />
          <el-table-column prop="organization" label="机构名称" />
          <el-table-column prop="routerNumber" label="路由条数" />
        </el-table>
        <div class="bottom" @click="moreRank">
          <el-button class="more">更多排行</el-button>
        </div>
      </div>

      <div class="column">
        <div class="title">
          <span class="category">中国联通</span>
        </div>
        <el-table
          :data="routingData"
          :header-cell-style="{ 'text-align': 'center' }"
          :cell-style="{ 'text-align': 'center' }"
        >
          <el-table-column prop="ASNumber" label="AS号" />
          <el-table-column prop="organization" label="机构名称" />
          <el-table-column prop="routerNumber" label="路由条数" />
        </el-table>
        <div class="bottom" @click="moreRank">
          <el-button class="more">更多排行</el-button>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "RoutingRank",
  data() {
    return {
      routingData: [
        {
          ASNumber: "AS4834 ",
          organization: "中国电信",
          routerNumber: 34,
        },
        {
          ASNumber: "AS9800   ",
          organization: "中国移动",
          routerNumber: 35,
        },
        {
          ASNumber: "AS9600   ",
          organization: "中国联通",
          routerNumber: 22,
        },
        {
          ASNumber: "AS8864   ",
          organization: "中网联盟",
          routerNumber: 12,
        },
        {
          ASNumber: "AS12963  ",
          organization: "阿里云",
          routerNumber: 30,
        },
        {
          ASNumber: "AS4808   ",
          organization: "百度云",
          routerNumber: 25,
        },
        {
          ASNumber: "AS12333 ",
          organization: "京东云",
          routerNumber: 18,
        },
        {
          ASNumber: "AS9233 ",
          organization: "中国教育网",
          routerNumber: 9,
        },
        {
          ASNumber: "AS4728   ",
          organization: "中国联通",
          routerNumber: 12,
        },
        {
          ASNumber: "AS9877   ",
          organization: "中国广电",
          routerNumber: 27,
        },
      ],
    };
  },
  methods: {
      moreRank() {
        this.$router.push("/moreRank");
    },
  }
};
</script>

<style lang="scss" scoped>
@import "~@/assets/style/reset.css";
.routingRank {
  // width: 100%;
  .tag {
    margin: 0 auto;
    margin-left: 0;
    margin-bottom: 8px;
    text-align: center;
    border-radius: 4px;
    border-bottom: 2px solid #e6e5eb;
  }
  .row {
    width: 100%;
    display: flex;
    margin-bottom: 20px;
    .column {
      margin: auto 1.5%;
      width: 31%;
      .title {
        width: 100%;
        border-bottom: 2px solid #e6e5eb;
        text-align: left;
        .category {
          line-height: 230%;
          border-left: 3px solid rgb(77, 101, 209);
          padding-left: 2%; // padding针对距内部元素
          font-size: 17px;
        }
      }
      .el-table {
        font-size: 14px;
        width: 100%;
      }
      .bottom {
        text-align: center;
        margin: 0;
        padding: 0;
        .el-button {
          border-top-left-radius: 0;
          border-top-right-radius: 0;
          border-top: transparent;
        }
      }
    }
    .column:first-of-type {
      margin-left: 0;
    }
    .column:last-of-type {
      margin-right: 0;
    }
  }
}
</style>
