<template>
  <div style="display: flex; flex-direction: column; min-height: 100%">
    <div class="not-bottom">
      <head-nav />
      <div class="content" v-show="false">
        <div class="realcontent"></div>
        <div id="img" class="img">
        </div>
      </div>
      <div class="overview">
        <span>CAIDA offers a number of data interfaces and services that provide interesting and insightful views of the data we collect and curate. </span>
      </div>
      <div class="tabs">
        <ul class="list">
          <li v-for="(item, index) in selected" :key="index" @click="select(index)">
            <a href="javaScript:void(0)" :class="{active:isSelected === index}">{{item}}</a>
          </li>
        </ul>
        <input placeholder="搜索：" v-model="search">
      </div>
      <div class="tab-content">
        <div class="content-container" v-show="isSelected === 0">
          <website-table :originalData="govern" />
          <!--在该页面获得数据，进行相应类别数据传参，以及搜索框内容传参-->
        </div>
        <div class="content-container" v-show="isSelected === 1">
          <website-table :originalData="edu" />
        </div>
        <div class="content-container" v-show="isSelected === 2">
          <website-table :originalData="finance" />
        </div>
        <div class="content-container" v-show="isSelected === 3">
          <website-table :originalData="media" />
        </div>
        <div class="content-container" v-show="isSelected === 4">
          <website-table :originalData="site" />
        </div>
      </div>
    </div>
    <div class="bottom">
      <span>@2021 穹眼安全 京ICP备18044233号-2</span>
    </div>
  </div>
</template>

<script>
import headNav from "@/components/HeadNav";
import websiteTable from "@/components/WebsiteTable";

export default {
  name: "website",
  components: {
    headNav,
    websiteTable,
  },
  data() {
    return {
      selected: ['政 府','教 育','金 融','媒 体', '门 户'],
      isSelected: 0,
      search: '',
      govern: [],
      edu: [],
      finance: [],
      media: [],
      site: [],
    };
  },
  mounted() {
    this.drawImg();
    this.$axios({
      method: 'post',
      //url: 'http://10.6.101.12:7076/website_zf',
      url: 'http://api.ipv6rank.com:7076/website_zf',
    }).then(res => {
      for (let index of res['data']['ans'].keys()) {
        if (res['data']['ans'][index]['ipv6_addresses']) {
          if (res['data']['ans'][index]['ipv6_addresses'].includes(',')) {
            var a = res['data']['ans'][index]['ipv6_addresses'].indexOf(",")
            res['data']['ans'][index]['ipv6_addresses'] = res['data']['ans'][index]['ipv6_addresses'].substring(0, a)
          }
          this.govern.push(res['data']['ans'][index])
        }
      }
      console.log('governData', this.govern)
    })
    this.$axios({
      method: 'post',
      //url: 'http://10.6.101.12:7076/website_jy',
      url: 'http://api.ipv6rank.com:7076/website_jy',
    }).then(res => {
      for (let index of res['data']['ans'].keys()) {
        if (res['data']['ans'][index]['ipv6_addresses']) {
          if (res['data']['ans'][index]['ipv6_addresses'].includes(',')) {
            var a = res['data']['ans'][index]['ipv6_addresses'].indexOf(",")
            res['data']['ans'][index]['ipv6_addresses'] = res['data']['ans'][index]['ipv6_addresses'].substring(0, a)
          }
          this.edu.push(res['data']['ans'][index])
        }
      }
      console.log('eduData', this.edu)
    })
    this.$axios({
      method: 'post',
      //url: 'http://10.6.101.12:7076/website_jr',
      url: 'http://api.ipv6rank.com:7076/website_jr',
    }).then(res => {
      for (let index of res['data']['ans'].keys()) {
        if (res['data']['ans'][index]['ipv6_addresses']) {
          if (res['data']['ans'][index]['ipv6_addresses'].includes(',')) {
            var a = res['data']['ans'][index]['ipv6_addresses'].indexOf(",")
            res['data']['ans'][index]['ipv6_addresses'] = res['data']['ans'][index]['ipv6_addresses'].substring(0, a)
          }
          this.finance.push(res['data']['ans'][index])
        }
      }
      console.log('financeData', this.finance)
    })
    this.$axios({
      method: 'post',
      //url: 'http://10.6.101.12:7076/website_mt',
      url: 'http://api.ipv6rank.com:7076/website_mt',
    }).then(res => {
      for (let index of res['data']['ans'].keys()) {
        if (res['data']['ans'][index]['ipv6_addresses']) {
          if (res['data']['ans'][index]['ipv6_addresses'].includes(',')) {
            var a = res['data']['ans'][index]['ipv6_addresses'].indexOf(",")
            res['data']['ans'][index]['ipv6_addresses'] = res['data']['ans'][index]['ipv6_addresses'].substring(0, a)
          }
          this.media.push(res['data']['ans'][index])
        }
      }
      console.log('mediaData', this.media)
    })
    this.$axios({
      method: 'post',
      //url: 'http://10.6.101.12:7076/website_mh',
      url: 'http://api.ipv6rank.com:7076/website_mh',
    }).then(res => {
      for (let index of res['data']['ans'].keys()) {
        if (res['data']['ans'][index]['ipv6_addresses']) {
          if (res['data']['ans'][index]['ipv6_addresses'].includes(',')) {
            var a = res['data']['ans'][index]['ipv6_addresses'].indexOf(",")
            res['data']['ans'][index]['ipv6_addresses'] = res['data']['ans'][index]['ipv6_addresses'].substring(0, a)
          }
          this.site.push(res['data']['ans'][index])
        }
      }
      console.log('siteData', this.site)
    })
  },
  methods: {
    select(index) {
      this.isSelected = index
    },
    drawImg() {
      let mychart = this.$echarts.init(document.getElementById("img"));
      let nowClientWidth = document.documentElement.clientWidth;
      function nowSize(val, initWidth=1280){
        return val * (nowClientWidth/initWidth);
      }
      mychart.setOption({
        xAxis: {
          type: 'category',
          data: ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun'],
          axisLabel: {
            textStyle: {
              fontSize: 12,
            }
          }
        },
        yAxis: {
          type: 'value',
          axisLabel: {
            textStyle: {
              fontSize: 12,
            }
          }
        },
        grid: {
          top: "15%",
          left: "13%",
          right: "13%",
          bottom: "15%"
        },
        series: [{
          data: [120, 200, 150, 80, 70, 110, 130],
          type: 'bar'
        }]
      });
      window.onresize = mychart.resize;
    },
    // 没用
    handleCurrentChange(currentPage) {
      this.currentPage = currentPage;
      // this.currentChangePage(this.originalData, currentPage);
    },
    currentChangePage(list, currentPage) {
      let from = (currentPage - 1) * this.pageSize;
      let to = currentPage * this.pageSize;
      this.filterData = [];
      for (; from < to; from++) {
        if (list[from]) {
          this.pageList.push(list[from]);
        }
      }
    },
  },
};
</script>

<style lang="scss" scoped>
@import "~@/assets/css/reset.css";
.not-bottom {
  flex: 1;
}
.content {
  margin-top: 15px;
  margin-bottom: 6px;
  display: flex;
  .realcontent {
    width: 75%;
    height: 270px;
    margin-left: 1.5%;
    border: 1px solid rgb(180, 180, 180);
    background: rgb(214, 214, 214);
    display: inline-block;
    vertical-align: top;
    margin-right: 1%;
    // margin-left: 30px;
  }
  .img {
    width: 21%;
    height: 268px;
    border: 1.5px solid rgb(180, 180, 180);
    border-radius: 4px;
    margin-right: 1.5%;
  }
}
.overview {
  margin: 15px 1.5% 0 1.5%;
  border: 3px solid rgb(226, 226, 226);
  border-radius: 5px;
  padding: 10px;
}
.tabs{
  display: flex;
  width: 97%;
  height: 34px;
  margin: 15px auto 0 auto;
  /*border-bottom: 1px solid #000;*/
  background-color: #f5f5f5;
  .list{
    margin-left: 0;
    display: flex;
    width: 100%;
    position: relative;
    li {
      margin-right: 30px;
      //width: 4%;
    }
    li:first-child{
      margin-left: 35px;
    }
    li{
      height: 34px;
      a{
        margin-top: 6px;
        padding: 2px 7px 5px 7px;
        height: 19px;
        color: #009a61;
        font-size: 18px;
        width: 41.5px;
      }
    }
    .active{
      background: #fff;
      border: 1.2px solid rgb(207, 207, 207);
      border-bottom: 1px solid transparent;
    }
  }
  input {
    flex-shrink: 0;
    width:210px;
    height:23px;
    margin-top: 5px;
    margin-right: 35px;
    border-radius: 2px;
    border: 1px solid rgb(187, 187, 187);
    outline: 1px solid rgb(221, 221, 221);
    text-indent:3px;
    color: rgb(56, 56, 56);
  }
}
.tab-content {
  width: 97%;
  //border: 1px solid rgb(194, 194, 194);
  margin: 0 auto;
  background-color: #fff;
}
</style>
