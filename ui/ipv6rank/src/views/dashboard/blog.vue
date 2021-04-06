<template>
  <div class="blog" style="display: flex; flex-direction: column; min-height: 100%;">
    <div class="not-bottom">
      <head-nav />
    </div>
    <div class="bottom">
      <span>@2021 穹眼安全 京ICP备18044233号-2</span>
    </div>
  </div>
</template>

<script>
import HeadNav from "@/components/HeadNav";

export default {
  components: {
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
</style>