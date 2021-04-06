<template>
  <div class="websiteRank">
    <div
      class="tag"
      style="width: 120px; height: 32px; background-color: #f12f3d"
    >
      <span style="line-height: 32px; font-size: 14px; color: #fff"
        >热门网站支持度</span
      >
    </div>
    <div class="row">
      <div class="column">
        <div class="title">
          <span class="category">政府</span>
        </div>
        <el-table
          :data="websiteData"
          :header-cell-style="{ 'text-align': 'center' }"
          :cell-style="{ 'text-align': 'center' }"
        >
          <el-table-column type="index" label="排名" align="center" />
          <el-table-column prop="website" label="网站" />
          <el-table-column prop="linked" label="链接数" />
          <el-table-column prop="support" label="支持度" />
        </el-table>
        <div class="bottom" @click="moreRank">
          <el-button class="more">更多排行</el-button>
        </div>
      </div>
      <!-- <router-view /> -->

      <div class="column">
        <div class="title">
          <span class="category">央企</span>
        </div>
        <el-table
          :data="websiteData"
          :header-cell-style="{ 'text-align': 'center' }"
          :cell-style="{ 'text-align': 'center' }"
        >
          <el-table-column type="index" label="排名" align="center" />
          <el-table-column prop="website" label="网站" />
          <el-table-column prop="linked" label="链接数" />
          <el-table-column prop="support" label="支持度" />
        </el-table>
        <div class="bottom" @click="moreRank">
          <el-button class="more">更多排行</el-button>
        </div>
      </div>

      <div class="column">
        <div class="title">
          <span class="category">教育</span>
        </div>
        <el-table
          :data="websiteData"
          :header-cell-style="{ 'text-align': 'center' }"
          :cell-style="{ 'text-align': 'center' }"
        >
          <el-table-column type="index" label="排名" align="center" />
          <el-table-column prop="website" label="网站" />
          <el-table-column prop="linked" label="链接数" />
          <el-table-column prop="support" label="支持度" />
        </el-table>
        <div class="bottom" @click="moreRank">
          <el-button class="more">更多排行</el-button>
        </div>
      </div>
    </div>
    <div class="row">
      <div class="column">
        <div class="title">
          <span class="category">金融</span>
        </div>
        <!--table顶部效果,底部border和左边的border-->
        <el-table
          :data="websiteData"
          :header-cell-style="{ 'text-align': 'center' }"
          :cell-style="{ 'text-align': 'center' }"
        >
          <el-table-column type="index" label="排名" align="center" />
          <el-table-column prop="website" label="网站" />
          <el-table-column prop="linked" label="链接数" />
          <el-table-column prop="support" label="支持度" />
        </el-table>
        <div class="bottom" @click="moreRank">
          <el-button class="more">更多排行</el-button>
        </div>
      </div>

      <div class="column">
        <div class="title">
          <span class="category">门户</span>
        </div>
        <el-table
          :data="websiteData"
          :header-cell-style="{ 'text-align': 'center' }"
          :cell-style="{ 'text-align': 'center' }"
        >
          <el-table-column type="index" label="排名" align="center" />
          <el-table-column prop="website" label="网站" />
          <el-table-column prop="linked" label="链接数" />
          <el-table-column prop="support" label="支持度" />
        </el-table>
        <div class="bottom" @click="moreRank">
          <el-button class="more">更多排行</el-button>
        </div>
      </div>

      <div class="column">
        <div class="title">
          <span class="category">煤体</span>
        </div>
        <el-table
          :data="websiteData"
          :header-cell-style="{ 'text-align': 'center' }"
          :cell-style="{ 'text-align': 'center' }"
        >
          <el-table-column type="index" label="排名" align="center" />
          <el-table-column prop="website" label="网站" />
          <el-table-column prop="linked" label="链接数" />
          <el-table-column prop="support" label="支持度" />
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
  name: "WebsiteRank",
  data() {
    return {
      websiteData: [
        {
          website: "新浪",
          linked: 4,
          support: "99%,",
        },
        {
          website: "搜狐",
          linked: 4,
          support: "98%",
        },
        {
          website: "百度",
          linked: 4,
          support: "97%",
        },
        {
          website: "网易",
          linked: 4,
          support: "96%",
        },
        {
          website: "中国政府网",
          linked: 4,
          support: "95%",
        },
        {
          website: "腾讯",
          linked: 4,
          support: "94%",
        },
        {
          website: "京东",
          linked: 4,
          support: "93%",
        },
        {
          website: "阿里",
          linked: 4,
          support: "92%",
        },
        {
          website: "苏宁",
          linked: 4,
          support: "91%",
        },
        {
          website: "国美",
          linked: 4,
          support: "90%",
        },
      ],
    };
  },
  methods: {
    moreRank() {
      this.$router.push("/moreRank");
    },
  },
};
</script>

<style lang="scss" scoped>
@import "~@/assets/style/reset.css";
.websiteRank {
  // width: 98%;
  .tag {
    margin: 0 auto;
    text-align: center;
    margin-left: 0;
    margin-bottom: 8px;
    border-radius: 4px;
    border-bottom: 2px solid #e6e5eb;
  }
  .row {
    width: 100%;
    margin-bottom: 12px;
    .column {
      display: inline-block;
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