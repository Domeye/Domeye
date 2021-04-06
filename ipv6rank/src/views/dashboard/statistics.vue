<template>
  <div class="statistics" style="display: flex; flex-direction: column; min-height: 100%;">
    <div class="not-bottom">
      <head-nav />
      <div class="content">
        <statistics-list />
        <div class="main">
          <!--<router-view/>是路由出口，路由匹配到的组件将渲染在这里。-->
          <router-view />
        </div>
      </div>
    </div>
    <div class="bottom">
      <span>@2021 穹眼安全 京ICP备18044233号-2</span>
    </div>
  </div>
</template>

<script>
import StatisticsList from "@/components/StatisticsList";
import HeadNav from "@/components/HeadNav";

export default {
  components: {
    StatisticsList,
    HeadNav,
  },
  data() {
    return {

    }
  }
}
</script>

<style lang='scss' scoped>
  @import "~@/assets/css/reset.css";
  .not-bottom {
    flex: 1;
  }
  .content {
    display: flex;
    .main {
      flex: 1 1 auto;
      margin-top: 15px;
      margin-right: 30px;
      //width: 80%;
    }
  }
</style>