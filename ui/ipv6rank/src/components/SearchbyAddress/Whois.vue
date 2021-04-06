<template>
  <div class="whois">
    <el-scrollbar>
      <div class="whois-title">注册局WHOIS主机: {{ this.whois_title }}</div>
      <div
        class="whois-content"
        style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap"
        v-for="item in this.whois"
        :key="item.index"
      >
        <div v-if="item.includes('%')" class="space">
          {{ item }}
        </div>
        <div v-else>{{ item }}</div>
      </div>
    </el-scrollbar>
  </div>
</template>

<script>
import {getWhois} from "../../api/apiData";

export default {
  name: "whois",
  props: ["input"],
  data() {
    return {
      dataw: '',
      whois: "",
      whois_title: "",
    };
  },
  watch: {
    input() {
      getWhois(this.input).then(res => {
        this.dataw = res['whois']
        this.whois = Array.from(new Set(this.dataw.split('\n').filter(item => item!=='')))
        this.whois_title = this.whois[0];
        this.whois.splice(0, 1);
      })
    }
  },
  mounted() {
    getWhois(this.input).then(res => {
      this.dataw = res['whois']
      console.log("whois原始信息：", this.dataw)
      // split() 方法用于把一个字符串分割成字符串数组，filter返回一个新数组
      // this.whois = Array.from(new Set(this.dataw.split('\n').filter(item => item!=='')))
      this.whois = this.dataw.split('\n').filter(item => item!=='')
      this.whois_title = this.whois[0].substr(2);
      this.whois.splice(0, 1); // splice() 返回被删除的项目，该方法会改变原始数组
      console.log("whois:", this.whois)
    })
  },
};
</script>

<style lang="scss" scoped>
.whois {
  width: 840px;
  height: 380px;
  display: flex;
  flex-direction: column;
  flex-wrap: wrap;
  //font-size: 18.5px;
  padding-left: 40px;
  padding-bottom: 10px;
  .el-scrollbar {
    height: 380px; /*此处一定要设置高度，不然内层的计算属性不生效*/
  }
  .el-scrollbar /deep/ .el-scrollbar__wrap {
    // width: 300px; /*将垂直滚动条挤到可视区域之外*/
    //height: 0; /*将水平滚动条挤到可视区域之外*/
    overflow-x: hidden;
  }
  .whois-title {
    padding-top: 7px;
    padding-bottom: 10px;
    color: #3e3d7a;
    font-weight: bold;
    text-align: center;
  }
  .space {
    margin: 7px auto 7px auto;
  }
  // p:nth-of-type(2), 选择每个p元素是其父级的第二个p元素
  .whois-content:nth-of-type(4){
    margin: auto auto 7px auto;
  }
  .whois-content:last-of-type{
    margin: 10px auto 10px auto;
  }
}
</style>