<template>
  <div id="app">
    <router-view v-if="isRouterAlive"/>
  </div>
</template>

<script>
export default {
  name: "app",
  provide() {
    return{
      reload: this.reload
    }
  },
  data() {
    return {
      isRouterAlive: true
    }
  },
  methods: {
    reload() {
      this.isRouterAlive = false;
      this.$nextTick(function(){
        this.isRouterAlive = true
      })
    }
  }
}
</script>

<style lang="scss">
html, body, #app {
  height: 100%;
  width: 100%;
  margin: 0;
  padding: 0;
  // font-size: 14px;
}
</style>
