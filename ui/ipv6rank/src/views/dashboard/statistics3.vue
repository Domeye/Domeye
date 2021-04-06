<template>
  <div class="statistics3">
    <!-- <statistics-list /> -->
    <div class="main">
        <router-view />
        我是3！！！！！！！
    </div>
  </div>
</template>

<script>
import StatisticsList from "@/components/StatisticsList";

export default {
  components: {
    StatisticsList,
  },
  data() {
    return {

    }
  }
}
</script>

<style lang='scss' scoped>

</style>