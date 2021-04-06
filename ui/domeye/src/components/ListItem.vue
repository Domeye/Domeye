<template>
  <div class="list">
    <div class="list-wrap">
      <a href="#" @click="goDetail"><img :src="website.img"  alt=""></a>
      <p class="list-item">
        <span >网站：</span>
        <span style="padding-top: 5px">域名：</span>
        <span style="padding-top: 5px">IPv6地址：</span>
        <span style="padding-top: 5px">AS名称：</span>
        <span style="padding-top: 5px">AS类型：</span>
      </p>
      <div class="rank">
        <span class="support">{{website.num}}</span>
        <div class="firstLine">
          <span>指标1</span>
          <span>指标2</span>
        </div>
        <div class="secondLine">
          <span>指标3</span>
          <span>指标4</span>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
  export default {
    name: "ListItem",
    props: {
      website: {
        type: Object,
        default(){
          return {}
        }
      }
    },
    methods:{
      goDetail(){
        this.$router.push('/moreDetail')
      }
    }
  }
</script>

<style lang="scss" scoped>
  .list{
    height: 160px;
    padding: 5px 10px;
    // border: 2px solid #f5f5f5;
    .list-wrap{
      display: flex;
      img{
        float: left;
        width: 160px;
        height: 130px;
        padding: 15px 15px;
      }
      .list-item{
        width: 310px;
        display: flex;
        flex-direction: column;
        padding: 10px 0;
        align-items: flex-start;
        font: 12px/1.5 tahoma,arial,\5b8b\4f53;
        text-align: justify;
      }
      .rank{
        border: 2px solid #DDD;
        width: 90px;
        height: 74px;
        position: relative;
        top: 40px;
        left:20px;
        font-size: 12px;
        text-align: center;
        .support{
          color: #f60404;
          display: block;
          padding-bottom:6px;
          padding-top: 6px;
          font-size: 16px;
          font-weight: bold;
        }
        .firstLine {
          margin-bottom: 3px;
          span:first-of-type {
            padding-right: 3px;
          }
          span:last-of-type {
            padding-left: 3px;
          }
        }
        .secondLine {
          margin-bottom: 3px;
          span:first-of-type {
            padding-right: 3px;
          }
          span:last-of-type {
            padding-left: 3px;
          }
        }
      }
    }
  }
  .list:hover{
    background-color: #f1f1f1;
  }
</style>
