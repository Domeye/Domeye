<template>
  <div
    class="wall-box"
    :style="{ background: 'red', transform: transformScale, width: width, height: '700px' }"
  ></div>
</template>

<script>
export default {
  data() {
    return {
      transformScale: "",
      width: "",
    };
  },
  mounted() {
    this.autoSetScale(); // 进页面先执行一次页面高度和宽度计算然后赋值
    window.addEventListener('resize', () => {
      this.autoSetScale()
    }, false)
  },
  methods: {
    autoSetScale() {
      let zoom = (window.innerHeight / 800).toFixed(3);
      this.transformScale = `scale(${zoom})`;
      this.width = `${(window.innerWidth / zoom).toFixed(2)}px`;
    },
  },
};
</script>