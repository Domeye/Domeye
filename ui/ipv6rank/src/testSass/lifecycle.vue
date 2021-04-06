<template>
  <div>
    <sonlife :son="son" />
    <button @click="click()"></button>
    <p>{{ firstNum }}</p>
    <p>{{ secondNum }}</p>
    <p>{{ thirdNum }}</p>
  </div>
</template>
 
<script>
import sonlife from "@/testSass/sonlife";

export default {
  components: {
    sonlife,
  },
  computed: {
    secondNum() {
      // firstNum 从一开始就与之绑定关联
      console.log("secondNum is computing: " + this.firstNum * 100);
      return this.firstNum * 100;
    },
  },
  data() {
    return {
      firstNum: 0,
      thirdNum: 0,
      son: 1,
    };
  },
  watch: {
    firstNum(val) {
      // firstNum 只有在发生改变时，才会进入该逻辑
      console.log("firstNum is watched: " + val);
      this.thirdNum = val * 100;
    },
  },
  created() {
    // 该步骤在 data() 数据实例化之前。
    // 此时改变 data() 中的数据是不会触发 change 事件的，无法进入 watch 代码部分。
    this.firstNum = 1;
  },
  mounted() {
    // 该步骤在 data 数据实例化之后。
    // 此时改变 data 中的数据是会触发 change 事件的，也就能被 watch 到。
    console.log("firstNum now: ", this.firstNum);
    this.firstNum = 2;
  },
  methods: {
    click() {
      this.son = this.son + 1;
    }
  }
};
</script>