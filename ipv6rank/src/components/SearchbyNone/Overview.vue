<template>
  <div class="overview">
    <div class="block">
      <div class="number">
        <!--引入千分位计算-->
        <div class="world">全球：54,521,760,719</div>
        <div class="china">中国：XXXX</div>
      </div>
      <div class="text">已分配v6地址总数</div>
    </div>
    <div class="block">
      <div class="number">
        <div class="world">全球：XXXXXXXXX</div>
        <div class="china">中国：XXXX</div>
      </div>
      <div class="text">已宣告v6地址总数</div>
    </div>
    <div class="block">
      <div class="number">
        <div class="world">全球：8,643,924,113</div>
        <div class="china">中国：XXXX</div>
      </div>
      <div class="text">可路由v6地址总数</div>
    </div>
    <div class="block">
      <div class="number">
        <div class="world">全球：86,439,241</div>
        <div class="china">中国：XXXX</div>
      </div>
      <div class="text">可路由自治域总数</div>
    </div>
    <div class="block">
      <div class="number">
        <div class="world">全球：XXXXXXXXX</div>
        <div class="china">中国：XXXX</div>
      </div>
      <div class="text">活跃地址总数</div>
    </div>
    <div class="block">
      <div class="number">
        <div class="world">全球：XXXXXXXXXX</div>
        <div class="china">中国：XXXX</div>
      </div>
      <div class="text">网站资源总数</div>
    </div>
    <div class="time">数据更新于2021年 4月5日</div>
  </div>
</template>

<script>
export default {
  name: 'Overview'
}
</script>

<style lang="scss" scoped>
.overview {
  width: 790px;
  height: 360px;
  padding: 25px 45px 0 45px;
  position: relative;
  //display: flex;
}
.block {
  display: inline-block;
  margin: 8px 30px;
  //flex: 0 1 auto;
  width: 202px;
  height: 145px;
  .number {
    width: 202px;
    height: 105px;
    //border: 1px solid rgb(22, 22, 75);
    background: rgba(233, 233, 233, 0.1);
    box-shadow: 0px 0px 5px 0px rgb(204, 204, 204);
    border-radius: 7px;
    text-align: center;
    .world {
      padding-top: 23px;
      font-size: 16px;
      font-weight: bold;
      color: rgb(99, 35, 35);
    }
    .china {
      margin-top: 13px;
      font-size: 15px;
      font-weight: bold;
    }
  }
  .text {
    font-size: 14.5px;
    margin-top: 14px;
    text-align: center;
    //margin-top: 5px;
  }
}
.time {
  height: 22px;
  width: 780px;
  text-align: center;
  font-size: 14px;
  position: absolute;
  margin: auto;  // 使用auto居中一定要设置宽度，且为块级元素(即有剩余空间的元素)
  bottom: 5px;
}
</style>