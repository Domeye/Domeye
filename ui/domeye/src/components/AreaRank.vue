<template>
  <div class="areaRank">
    <div
      class="tag"
      style="width: 120px; height: 32px; background-color: #f12f3d"
    >
      <span style="line-height: 32px; font-size: 14px; color: #fff"
        >地区分布排行</span
      >
    </div>
    <div class="row">
      <div class="column">
        <div class="title">
          <span class="category">中国电信</span>
        </div>
        <!--table顶部效果,底部border和左边的border-->
        <el-table
          :data="areaData"
          :header-cell-style="{ 'text-align': 'center' }"
          :cell-style="{ 'text-align': 'center' }"
        >
          <el-table-column type="index" label="排名" align="center" />
          <el-table-column prop="number32" label="地址块数(/32)" />
          <el-table-column prop="number" label="地址块数" />
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
          :data="areaData"
          :header-cell-style="{ 'text-align': 'center' }"
          :cell-style="{ 'text-align': 'center' }"
        >
          <el-table-column type="index" label="排名" align="center" />
          <el-table-column prop="number32" label="地址块数(/32)" />
          <el-table-column prop="number" label="地址块数" />
        </el-table>
        <div class="bottom" @click="moreRank">
          <el-button class="more">更多排行</el-button>
        </div>
      </div>

      <div class="column">
        <div class="title">
          <span class="category">中国联通</span>
        </div>
        <!--table顶部效果,底部border和左边的border-->
        <el-table
          :data="areaData"
          :header-cell-style="{ 'text-align': 'center' }"
          :cell-style="{ 'text-align': 'center' }"
        >
          <el-table-column type="index" label="排名" align="center" />
          <el-table-column prop="number32" label="地址块数(/32)" />
          <el-table-column prop="number" label="地址块数" />
        </el-table>
        <div class="bottom" @click="moreRank">
          <el-button class="more">更多排行</el-button>
        </div>
      </div>
    </div>
    <div class="row">
      <div class="column">
        <div class="title">
          <span class="category">教育网</span>
        </div>
        <!--table顶部效果,底部border和左边的border-->
        <el-table
          :data="areaData"
          :header-cell-style="{ 'text-align': 'center' }"
          :cell-style="{ 'text-align': 'center' }"
        >
          <el-table-column type="index" label="排名" align="center" />
          <el-table-column prop="number32" label="地址块数(/32)" />
          <el-table-column prop="number" label="地址块数" />
        </el-table>
        <div class="bottom" @click="moreRank">
          <el-button class="more">更多排行</el-button>
        </div>
      </div>

      <div class="column">
        <div class="title">
          <span class="category">中国联盟</span>
        </div>
        <!--table顶部效果,底部border和左边的border-->
        <el-table
          :data="areaData"
          :header-cell-style="{ 'text-align': 'center' }"
          :cell-style="{ 'text-align': 'center' }"
        >
          <el-table-column type="index" label="排名" align="center" />
          <el-table-column prop="number32" label="地址块数(/32)" />
          <el-table-column prop="number" label="地址块数" />
        </el-table>
        <div class="bottom" @click="moreRank">
          <el-button class="more">更多排行</el-button>
        </div>
      </div>

      <div class="column">
        <div class="title">
          <span class="category">阿里云</span>
        </div>
        <el-table
          :data="areaData"
          :header-cell-style="{ 'text-align': 'center' }"
          :cell-style="{ 'text-align': 'center' }"
        >
          <el-table-column type="index" label="排名" align="center" />
          <el-table-column prop="number32" label="地址块数(/32)" />
          <el-table-column prop="number" label="地址块数" />
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
  name: "AreaRank",
  data() {
    return {
      areaData: [
        {
          website: "新浪",
          number32: 14,
          number: 20,
        },
        {
          website: "新浪",
          number32: 14,
          number: 20,
        },
        {
          website: "新浪",
          number32: 14,
          number: 20,
        },
        {
          website: "新浪",
          number32: 14,
          number: 20,
        },
        {
          website: "新浪",
          number32: 14,
          number: 20,
        },
        {
          website: "新浪",
          number32: 14,
          number: 20,
        },
        {
          website: "新浪",
          number32: 14,
          number: 20,
        },
        {
          website: "新浪",
          number32: 14,
          number: 20,
        },
        {
          website: "新浪",
          number32: 14,
          number: 20,
        },
        {
          website: "新浪",
          number32: 14,
          number: 20,
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
.areaRank {
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
