<template>
  <el-container>
    <!-- <el-header>Header</el-header>
    <el-main>Main</el-main>
    <el-footer>Footer</el-footer> -->
    <path-graph :paths="v6Propagation"></path-graph>
  </el-container>
</template>

<script>
import pathGraph from "@/components/pathGraph";

export default {
  components: {
    pathGraph,
    // StatisticBlock,
  },
  data() {
    return {
      v6Propagation: [
        "206499 34549 37468 13335",
        "34549 1299 6762 13335",
        "206313 9002 59318 13335",
        "50300 6939 60171 328196 13335",
        "49432 48362 8529 13335",
        "205148 6939 23520 27775 13335 13335",
        "49673 48858 12389 3257 13335",
        "34872 6939 3257 59605 13335",
        "209152 6939 6762 13335",
        "34927 6939 8529 38193 13335",
        "49752 6939 9498 58717 13335",
        "61292 6939 60171 328196 13335",
        "49420 6939 262589 14259 13335",
      ],
    };
  },
};
</script>

<style lang="scss">
@import "~@/assets/style/reset.css";
.el-container {
  height: 100%;
  padding: 0px;
  margin: 0px;
  display: flex;
}
</style>
