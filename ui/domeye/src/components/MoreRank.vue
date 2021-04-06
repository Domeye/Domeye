<template>
  <div class="morerank">
    <head-nav />
    <div class="search">
      <el-form :inline="true" ref="form" label-width="80%">
        <el-form-item>
          <el-input v-model="searchContent" placeholder="请输入网站网址或名称">
          </el-input>
        </el-form-item>
        <el-form-item>
          <el-button type="primary" @click="search(searchContent)"
            >搜索</el-button
          >
        </el-form-item>
      </el-form>
    </div>
    <hr />
    <div class="resultwrapper">
      <div class="left-content">
        <div class="barfilter">
          <h3>相关AS</h3>
          <ul>
            <li v-for="i_related_as in related_as" :key="i_related_as.index">
              <div class="first-span">{{ Object.keys(i_related_as)[0] }}</div>
              <div class="second-span">
                {{ Object.values(i_related_as)[0] }}
              </div>
            </li>
          </ul>
        </div>
        <div class="barfilter">
          <h3>相关前缀</h3>
          <ul>
            <li
              v-for="i_related_prefix in this.related_prefix"
              :key="i_related_prefix.index"
            >
              <div class="span-only">{{ i_related_prefix }}</div>
            </li>
          </ul>
        </div>
      </div>
      <div class="list-content">
        <div class="nav-header">
          <i class="el-icon-s-home"></i>
          <span style="color: rgb(68, 68, 68); font-size: 16px">位置：</span>
          <a style="color: rgb(68, 68, 68); font-size: 16px" href="#/website">网站</a>
          <!-- <router-link id="a_under" style="color: rgb(68, 68, 68); font-size: 16px" to="/website">网站</router-link> -->
          <span style="color: rgb(68, 68, 68); font-size: 16px">/ 网站排行榜</span>
          <span style="color: #999999; font-size: 14px"
            >(更新: 2020-04-30)</span
          >
        </div>
        <list-item :website="baidu" />
        <list-item :website="sohu" />
        <list-item :website="tencent" />
        <list-item :website="sina" />
      </div>
    </div>
    <div class="domeye-bottom">
      <span>© Domeye </span>
    </div>
  </div>
</template>

<script>
import HeadNav from "@/components/HeadNav";
import ListItem from "@/components/ListItem";

export default {
  name: "MoreRank",
  components: {
    HeadNav,
    ListItem,
  },
  data() {
    return {
      searchContent: "",
      related_as: [
        {
          14789: "CLOUDFLARENET-AUS",
        },
        {
          14789: "CLOUDFLARENET-AUS",
        },
        {
          14789: "CLOUDFLARENET-AUS",
        },
        {
          14789: "CLOUDFLARENET-AUS",
        },
        {
          14789: "CLOUDFLARENET-AUS",
        },
      ],
      related_prefix: [
        "2001:2e0::/35",
        "2001:2e0::/32",
        "2402:f180:1::/48",
        "2001:2e0:7000::/36",
      ],
      baidu: {
        img:
          "https://topimg.chinaz.net/WebSiteimages/baiducom/969e383d-19b6-4081-b933-a38ca415dd8a_2017_s.png",
        domain: "百度 www.baidu.com",
        rank: "Alexa周排名：3 百度权重为：PR：反链数：345762",
        info:
          "网站简介:百度，全球大的中文搜索引擎、大的中文网站。2000年1月创立于北京中关村。",
        num: 1,
        score: "得分: 4999",
      },
      sohu: {
        img:
          "https://topimg.chinaz.net/WebSiteimages/wwwsohucom/7136b28c-4b8e-469c-b6f0-a98f5147d76c_2017_s.png",
        domain: "搜狐 sohu.com",
        rank: "Alexa周排名：7 百度权重为：PR：反链数：282447",
        info: `网站简介:搜狐网为用户提供24小时不间断的x新闻资讯，及搜索、邮件等网络服务。内容包括
          全球热点事件、突发新闻、时事评论、热播影视剧、体育赛事、行业动态、生活服务信息，以及论坛...`,
        num: 2,
        score: "得分: 4950",
      },
      tencent: {
        img:
          "https://topimg.chinaz.net/WebSiteimages/wwwqqcom/24bfa9c8-4002-4973-a1d8-7c9b981108d0_2017_s.png",
        domain: "腾讯网 qq.com",
        rank: "Alexa周排名：6 百度权重为：PR：反链数：858338",
        info: `网站简介：腾讯网从2003年创立至今，已经成为集新闻信息，区域垂直生活服务、
          社会化媒体资讯和产品为一体的互联网媒体平台。腾讯网下设新闻、科技、财经、娱乐、体育、汽车、时尚等多...`,
        num: 3,
        score: "得分: 4950",
      },
      sina: {
        img:
          "https://topimg.chinaz.net/WebSiteimages/sinacomcn/9c10ca06-b3a4-44f2-bc50-5da4e37e6b6d_2016_s.png",
        domain: "新浪网 sina.com.cn",
        rank: "Alexa周排名：15 百度权重为：PR：反链数：410215",
        info: `网站简介：新浪网为全球用户24小时提供全面及时的中文资讯，内容覆盖国内外突发新闻事件、
          体坛赛事、娱乐时尚、产业资讯、实用信息等，设有新闻、体育、娱乐、财经、科技、房产、汽车...`,
        num: 4,
        score: "得分: 4949",
      },
    };
  },
  mounted() {
  },
  methods: {
  },
};
</script>

<style lang="scss" scoped>
@import "~@/assets/style/reset.css";
.morerank {
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
    // a:link {
    //   text-decoration: underline black;
    // }
  }
  .search {
    margin-top: 45px;
    padding: 12px 0 6px 0;
    margin-left: 228px;
    width: 53%;
    .el-form {
      text-align: center;
      width: 100%;
      .el-form-item {
        margin-bottom: 1px;
      }
      .el-form-item:first-of-type {
        margin-left: 0;
        .el-input /deep/ .el-input__inner {
          width: 500px;
          border: 1px solid rgb(58, 58, 58);
          font-size: 13px;
          border-radius: 4px;
          color: #474747;
          height: 35px;
        }
        .el-input .el-input__inner::-webkit-input-placeholder {
          color: rgb(95, 95, 95);
        }
      }
      .el-form-item:last-of-type {
        margin-left: 40px;
        .el-button {
          line-height: 0.65;
          border-color: rgb(90, 108, 187);
        }
      }
    }
  }
  hr {
    background-color: rgb(202, 202, 202);
    height: 1px;
    border: none;
    width: 100%;
    margin-bottom: 10px;
  }
  .resultwrapper {
    width: 100%;
    display: flex;
    .left-content {
      // float: left;
      // width: 13%;
      flex: 1;
      padding-left: 20px;
      .barfilter {
        padding-bottom: 10px;
        h3 {
          margin: 10px 0 0 0;
          font-weight: normal;
          font-size: 15px;
          color: rgb(68, 68, 68);
        }
        ul {
          padding: 0;
          li {
            position: relative;
            overflow: hidden; // 不懂？？？？
            margin: 5px 0;
            font-size: 12px;
            color: #727272;
            .first-span {
              position: absolute; // absolute相对于 static 定位以外的第一个父元素(ul)进行定位
              left: 0;
              top: 0;
              color: #727272;
            }
            .second-span {
              float: right;
              text-align: right;
              // background: aqua;
              text-indent: -100%; // 不懂？？？？
              font-size: 12px;
            }
            .span-only {
              float: left;
              // position: absolute;
              left: 0;
              top: 0;
              color: #727272;
            }
          }
        }
      }
    }
    .list-content {
      flex: 4;
      margin: auto 5px 20px 20px;
      .nav-header {
        padding: 5px 20px;
        span {
          padding-left: 7px;
        }
      }
    }
  }
}
</style>
