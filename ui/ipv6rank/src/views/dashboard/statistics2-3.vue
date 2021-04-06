<template>
  <div class="statistics2-3">
    <ul class="tabs">
      <li v-for="(item, index) in selected" :key="index" @click="select(index)" :class="{active:isSelected === index}">
        {{item}}
      </li>
    </ul>
    <div class="clear"></div>
    <div class="content-container"  v-show="isSelected === 0"></div>
    <div class="content-container"  v-show="isSelected === 1"></div>
    <div class="content-container"  v-show="isSelected === 2"></div>
    <div class="content-container"  v-show="isSelected === 3"></div>
    <div class="content-container"  v-show="isSelected === 4"></div>
  </div>
</template>

<script>

export default {
  components: {
  },
  data() {
    return {
      selected: ['标签一', '标签二', '标签三', '标签四', '标签五'],
      isSelected: 0,
    }
  },
  methods: {
    select(index) {
      this.isSelected = index;
    }
  }
}
</script>

<style lang='scss' scoped>
@import "~@/assets/css/reset.css";
.statistics2-3 {
  .tabs {
    margin-left: 20px;
    li {
      float: left;
      margin-bottom: -1px;
      margin-right: 25px;
      padding-left: 8px;
      padding-right: 8px;
      padding-top: 4px;
      padding-bottom: 2px;
      border: 1px solid  rgb(22, 22, 110);
      background-color: #dfdfdf;
      cursor: pointer;
    }
    .active {
      border-bottom: 1px solid white;
      background-color: #ffffff;
      cursor: auto;
    }
  }
  .content-container {
    height: 800px;
    padding: 10px;
    border: 1px solid  rgb(22, 22, 110);
  }
  .clear {
    clear: both;
  }
}
</style>