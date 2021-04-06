<template>
  <div class="moredetail">
    <head-nav />
    <div class="describe">
      <div class="describe-top">
        <div>
          <span style="font-size: 24px; font-weight: 500">{{
            website.name
          }}</span>
          {{ website.domain }}
        </div>
        <div>数据更新 2020-05-06</div>
      </div>
      <div class="describe-bottom">
        <div class="describe-bottom-left">
          <div>
            <span class="detail-rank">{{ website.rank[0].score }}</span>
            <span>{{ website.rank[0].rankName }}</span>
          </div>

          <div>
            <span class="detail-rank">{{ website.rank[1].score }}</span>
            <span>{{ website.rank[1].rankName }}</span>
          </div>

          <div>
            <span class="detail-rank">{{ website.rank[2].score }}</span>
            <span>{{ website.rank[2].rankName }}</span>
          </div>
        </div>
        <div class="describe-bottom-right">
          <div style="padding-top: 5px; float: left; padding-left: 20px">
            <a
              href="https://jd.com"
              style="
                display: block;
                width: 76px;
                height: 28px;
                border: 2px solid #ddd;
                border-radius: 15px;
                line-height: 28px;
              "
              >网站信息</a
            >
          </div>
          <div style="padding-top: 5px; float: left; padding-left: 20px">
            所属类型: 综合其他，搜素引擎
          </div>
          <div style="padding-top: 5px; float: left; padding-left: 20px">
            所属地区: 北京，海淀
          </div>
        </div>
      </div>

      <div class="website-intro">
        <div class="website-intro-top">
          <div class="title">网站简介</div>
        </div>
        <div class="website-info">
          <div style="background-color: #f8f8f8">
            <el-menu
              mode="horizontal"
              style="background-color: #f8f8f8; width: 600px; margin: 0 auto"
            >
              <el-menu-item>站点介绍</el-menu-item>
              <el-menu-item>站点介绍</el-menu-item>
              <el-menu-item>站点介绍</el-menu-item>
              <el-menu-item>站点介绍</el-menu-item>
              <el-menu-item>站点介绍</el-menu-item>
            </el-menu>
          </div>
          <div style="display: flex">
            <img :src="website.img" />
            <p class="website-desc">
              {{ website.desc }}
            </p>
          </div>
        </div>
      </div>

      <div class="service-info">
        <div class="info">
          <p style="font-weight: bold; font-size: 14px">备案信息</p>
          <p>单位名称：{{ website.list[0].company }}</p>
          <p>单位性质：{{ website.list[0].type }}</p>
          <p>网站备案：{{ website.list[0].websiteRecord }}</p>
          <p>网站名称：{{ website.list[0].name }}</p>
          <p>网站首页：{{ website.list[0].index }}</p>
        </div>

        <div class="info">
          <p style="font-weight: bold; font-size: 14px">服务器</p>
          <p>Ip地址：{{ website.list[1].ip }}</p>
          <p>服务器地址：{{ website.list[1].serviceAdd }}</p>
          <p>服务器类型：{{ website.list[1].type }}</p>
          <p>页面类型：{{ website.list[1].pageType }}</p>
          <p>响应时间：{{ website.list[1].time }}</p>
        </div>

        <div class="info">
          <p style="font-weight: bold; font-size: 14px">域名</p>
          <p>域名: {{ website.list[2].domainName }}</p>
          <p>域名注册商: {{ website.list[2].registerCompany }}</p>
          <p>域名服务器：</p>
          <p>创建时间: {{ website.list[2].start }}</p>
          <p>到期时间: {{ website.list[2].end }}</p>
        </div>
      </div>

      <div class="chart">
        <div class="website-intro-top">
          <div class="title">数据分析</div>
        </div>
        <div class="show-chart">
          <div>
            <div class="chart-title">{{ website.chart.chartTitle }}</div>
            <div
              id="myChart"
              class="mycharts"
              :style="{ width: '520px', height: '400px' }"
            ></div>
          </div>

          <div class="right-chart">
            <div class="chart-title" style="padding-bottom: 15px">
              {{ website.chart.tableTitle }}
            </div>
            <el-table :data="table1" :show-header="false" style="width: 400px">
              <el-table-column type="index" />
              <el-table-column prop="name" />
              <el-table-column prop="data" />
              <el-table-column prop="change" />
            </el-table>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import HeadNav from "@/components/HeadNav";

export default {
  name: "MoreDetail",
  components: {
    HeadNav,
  },
  //   props:{
  //       website:{
  //         type:Object,
  //         default(){
  //           return{}
  //         }
  //       }
  //     },
  data() {
    return {
      table1: [
        { name: "百度", data: 1234, change: "-0" },
        { name: "百度", data: 1234, change: "-0" },
        { name: "百度", data: 1234, change: "-0" },
        { name: "百度", data: 1234, change: "-0" },
        { name: "百度", data: 1234, change: "-0" },
        { name: "百度", data: 1234, change: "-0" },
        { name: "百度", data: 1234, change: "-0" },
        { name: "百度", data: 1234, change: -0 },
      ],
      website: {
        name: "百度",
        domain: "www.baidu.com",
        rank: [
          { score: 1, rankName: "总排名" },
          { score: 1, rankName: "北京" },
          { score: 1, rankName: "搜素引擎" },
        ],
        info: { type: "综合其他,搜素引擎", region: "北京,海淀" },
        img:
          "https://topimg.chinaz.net/WebSiteimages/unionbaiducom/06b9fa80-f112-4e12-98da-b1d403d2a21d_2016_s.png",
        desc:
          "百度，全球大的中文搜索引擎、大的中文网站。2000年1月创立于北京中关村。",
        list: [
          {
            company: "北京百度网讯科技有限公司",
            type: "企业",
            websiteRecord: "京ICP证030173号-1",
            name: "百度",
            index: "baidu.com",
          },
          {
            ip: "220.181.57.216",
            serviceAdd: "广东省 中国移动互联网",
            type: "Apache",
            pageType: "text/html",
            time: "42毫秒",
          },
          {
            domainName: "baidu.com",
            registerCompany: "MarkMonitor Inc",
            domainService: "",
            start: "1999年10月11日",
            end: "2026年10月11日",
          },
        ],
        chart: { chartTitle: "搜索引擎趋势图", tableTitle: "搜素引擎排名" },
      },
    };
  },
  mounted() {
    this.drawLine();
  },
  methods: {
    drawLine() {
      let myChart = this.$echarts.init(document.getElementById("myChart"));
      myChart.setOption({
        color: ["#3398DB"],
        tooltip: {
          trigger: "axis",
          axisPointer: {
            // 坐标轴指示器，坐标轴触发有效
            type: "shadow", // 默认为直线，可选为：'line' | 'shadow'
          },
        },
        grid: {
          left: "3%",
          right: "4%",
          bottom: "3%",
          containLabel: true,
        },
        xAxis: [
          {
            type: "category",
            data: ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"],
            axisTick: {
              alignWithLabel: true,
            },
          },
        ],
        yAxis: [
          {
            type: "value",
          },
        ],
        series: [
          {
            name: "直接访问",
            type: "bar",
            barWidth: "60%",
            data: [10, 52, 200, 334, 390, 330, 220],
          },
        ],
      });
    },
  },
};
</script>

<style lang="scss" scoped>
.moredetail {
  height: 100%;
  .navbar {
    z-index: 10;
    height: 45px;
    background-color: rgb(0, 0, 0);
    position: fixed; // 所以head不在正常文档布局流中
    width: 100%;
    top: 0;
    left: 0;
    // margin: 0 20px 0 20px;
  }
  .describe {
    width: 80%;
    margin-top: 45px;
    margin-left: 120px;
    // margin: 0 auto;
    background-color: #fff;
    border: 1px solid #f8f8f8;
    padding: 15px 0;
  }
  .describe-top {
    display: flex;
    justify-content: space-between;
    padding: 15px 30px;
  }

  .describe-bottom {
    display: flex;
    a {
        text-align: center;
    }
  }
  .describe-bottom-left {
    display: flex;
    justify-content: space-evenly;
    padding: 30px 0;
    width: 650px;
  }
  .detail-rank {
    display: block;
    color: #4d7bb9;
    font-size: 36px;
  }

  .describe-bottom-right {
    width: 330px;
    height: 120px;
    border: 2px solid #ddd;
    margin-right: 20px;
    background-color: #fcfcfc;

    display: flex;
    flex-direction: column;
    align-items: flex-start;
    justify-content: space-around;
  }
  .describe-bottom-right a:hover {
    color: #f60404;
  }

  .website-intro {
    width: 960px;
    margin: 0 auto;
  }
  .website-intro-top {
    height: 32px;
    padding: 15px 0;
    text-align: center;
  }
  .title {
    float: left;
    line-height: 32px;
    width: 86px;
    border: 1px solid #fcfcfc;
    background-color: #4f9cee;
    color: #fff;
    font-size: 14px;
    font-weight: bold;
  }
  .website-info {
    border: 1px solid #ddd;
  }
  .website-desc {
    height: 152px;
    margin: 0;
    padding: 20px 10px;
  }

  .service-info {
    display: flex;
    width: 960px;
    margin: 0 auto;
  }
  .service-info .info {
    background-color: #f8f8f8;
    border: 1px solid #e7e7eb;
    width: 320px;
    padding: 15px;
  }

  .show-chart {
    border: 1px solid #ddd;
    display: flex;
    justify-content: space-around;
  }
  img {
    float: left;
    width: 140px;
    height: 112px;
    padding: 20px;
  }
  p {
    text-align: justify;
    margin: 0;
    height: 30px;
  }

  .chart {
    width: 960px;
    margin: 0 auto;
  }
  .chart-title {
    padding-top: 15px;
    font-size: 14px;
    font-weight: bold;
  }
}
</style>
