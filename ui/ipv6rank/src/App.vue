<template>
  <div id="app">
    <router-view/>
  </div>
</template>

<script>
  export default{
    name: 'App',
    provide() {   // 传递给子组件的参数
      return {
        reload: this.reload
      }
    },
    data() {
      return {
        isRouterAlive: true,
      }
    },

    methods: {
      reload() {
        this.isRouterAlive = false
        this.$nextTick(() => {
          console.log(this)
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
}

// 定义整个滚动条
::-webkit-scrollbar{
  width: 5px;  // 定义竖滚动条的宽度
  height: 5px;  // 定义横向滚动条的高度
}

// 定义滚动条上的滚动滑块
::-webkit-scrollbar-thumb{ 
  border-radius: 10px;
  // height: 5px;
  background: rgb(165, 165, 165);
}

// 定义滚动条轨道
::-webkit-scrollbar-track{ 
  box-shadow: inset 0 0 5px rgb(241, 241, 241);
  border-radius: 5px;
  background: rgba(248, 248, 248, 0.897);
}

</style>
