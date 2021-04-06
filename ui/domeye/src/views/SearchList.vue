<template>
  <div class="searchlist">
    <head-nav />
    <div class="resultwrapper">
      <div class="search-wrapper">
        <span class="search-title">
          关联信息
          <i class="el-icon-caret-bottom"></i>
        </span>
        <el-form :inline="true" ref="form" label-width="80%">
          <el-form-item>
            <el-input
              v-model="form.content"
              placeholder="可搜索探针、IP地址，多个关键字用空格隔开"
            >
            </el-input>
          </el-form-item>
          <el-form-item>
            <el-button type="primary" @click="search(form.content)"
              >搜索</el-button
            >
          </el-form-item>
        </el-form>
      </div>
      <hr />
      <div class="aside">
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
          <ul
            v-if="
              related_prefix.length > showLength &&
              showLength <= related_prefix.length
            "
          >
            <li
              v-for="(i_related_prefix, key) in this.related_prefix"
              :key="i_related_prefix.index"
              v-show="key < showLength"
            >
              <div class="span-only">{{ i_related_prefix }}</div>
            </li>
            <!-- <div class="showMore" @click="showMore" role="button">
              <i class="el-icon-caret-bottom"></i>
              <span>显示更多</span>
            </div> -->
            <el-button
              class="showMore"
              icon="el-icon-caret-bottom"
              @click="showMore"
            >
              显示更多
            </el-button>
          </ul>
          <ul v-if="related_prefix.length <= 20">
            <li
              v-for="i_related_prefix in this.related_prefix"
              :key="i_related_prefix.index"
            >
              <div class="span-only">{{ i_related_prefix }}</div>
            </li>
          </ul>
          <ul
            v-if="
              related_prefix.length > 20 && showLength > related_prefix.length
            "
          >
            <li
              v-for="i_related_prefix in related_prefix"
              :key="i_related_prefix.index"
            >
              <div class="span-only">{{ i_related_prefix }}</div>
            </li>
            <el-button
              class="showLess"
              icon="el-icon-caret-top"
              @click="showLess"
            >
              收起
            </el-button>
          </ul>
        </div>
      </div>
      <div class="rightwrapper">
        <div class="tabs">
          <ul class="list">
            <li
              v-for="(item, index) in this.selectedTab"
              :key="index"
              @click="selectTab(index)"
            >
              <div class="list-item">
                <a
                  href="javaScript:void(0)"
                  :class="{ active: isSelected === index }"
                >
                  {{ item }}
                </a>
              </div>
            </li>
          </ul>
        </div>
        <div class="content">
          <div class="content-container" v-show="isSelected === 0">
            <ul>
              <li v-for="i_AS in this.AS" :key="i_AS.index">
                <h3>{{ i_AS.prefix }}</h3>
                <address>
                  {{ i_AS.source }}
                </address>
                <article>
                  <p v-if="i_AS.ASN">ASN：{{ i_AS.ASN }}</p>
                  <p v-if="i_AS.as_type">as_type：{{ i_AS.as_type }}</p>
                  <p v-if="i_AS.netname">netname：{{ i_AS.netname }}</p>
                  <p v-if="i_AS.country">country：{{ i_AS.country }}</p>
                  <p v-else-if="!i_AS.country">country：null</p>
                  <p v-if="i_AS.description">
                    description：{{ i_AS.description }}
                  </p>
                  <p v-else-if="!i_AS.description">description：null</p>
                  <p v-if="i_AS.organization">
                    organization：{{ i_AS.organization }}
                  </p>
                  <p v-else-if="!i_AS.organization">organization：null</p>
                </article>
              </li>
            </ul>
          </div>
          <div class="content-container" v-show="isSelected === 1">
            <statistic-block :picture="picture" />
            <!-- <statistic-block :picture1_data="picture.picture1_data" :picture1_x="picture.picture1_x" :picture2_data="picture.picture2_data" :picture2_x="picture.picture2_x" :picture3_data="picture.picture3_data" /> -->
          </div>
          <div class="content-container" v-show="isSelected === 2">
            <div class="whois">
              <div class="whois-title">{{ this.whois_title }}</div>
              <div
                class="whois-content"
                style="
                  overflow: hidden;
                  text-overflow: ellipsis;
                  white-space: nowrap;
                "
                v-for="item in this.whois"
                :key="item.index"
              >
                <i class="el-icon-s-tools"></i>
                {{ item }}
              </div>
            </div>
          </div>
          <div class="content-container" v-show="isSelected === 3">
            <relation-graph :relation_graph="relation_graph" />
          </div>
        </div>
      </div>
      <div class="cart-wrapper">
        <div class="wrapper">
          <div class="title">
            <i class="el-icon-caret-right"></i>
            <p>地理位置</p>
          </div>
          <div class="wrapper1" id="wrapper1"></div>
        </div>
        <div class="wrapper">
          <div class="title">
            <i class="el-icon-caret-right"></i>
            <p>网络位置</p>
          </div>
          <div class="wrapper2" id="topov6" ref="topov6"></div>
        </div>
        <div class="wrapper">
          <div class="title">
            <i class="el-icon-caret-right"></i>
            <p>传播路径</p>
          </div>
          <path-graph :paths="v6Propagation"></path-graph>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import HeadNav from "@/components/HeadNav";
import StatisticBlock from "@/components/StatisticBlock";
import RelationGraph from "@/components/RelationGraph";
import pathGraph from "@/components/pathGraph";
import { getAllPrefixApi, getLongestASPrefixApi, getRelatedASApi, getRelationGraphApi } from "@/api/search";
import { getWhoisApi } from "@/api/whois";
import { getPictureApi} from "@/api/picture";
var latjson = require("../assets/data/countrytolat.json");

export default {
  inject: ["reload"], // 在需刷新页面注入App.vue组件提供（provide）的 reload 依赖
  name: "SearchList",
  components: {
    HeadNav,
    pathGraph,
    StatisticBlock,
    RelationGraph,
  },
  data() {
    return {
      form: {
        content: "",
      },
      picture: "",
      ipType: "",
      select: "",
      selectedTab: ["信 息 总 览", "路 由 信 息", "Whois 信 息", "关 联 信 息"],
      isSelected: 0,
      showLength: 20,
      // 点击按钮搜索时 底下这些值会变
      related_as: "",
      related_prefix: "",
      AS: "",
      whois: "",
      whois2: "",
      relation_graph: "",
      whois_title: "",
      country_dot: "",
      countrytolat: "",
      longest_prefix: "",
      asDialogShow: false,
      asDialogData: {},
      v6Propagation: "",
    };
  },
  methods: {
    search(content) {
      this.showLength = 20;
      // 验证是否有效
      // 判断输入ip类型为ipv4还是ipv6
      if (content.indexOf(".") > 0) {
        this.ipType = "ipv4";
      } else {
        this.ipType = "ipv6";
      }
      console.log("ipType:", this.ipType);
      getRelatedASApi(content).then((res) => {
        this.related_as = res["reated_as"];
        //console.log("related_as:", this.related_as);
        //console.log("i_related_as:", Object.keys(this.related_as[0])[0]);
      });
      getAllPrefixApi(content).then((res) => {
        //console.log(res["all_prefix"]);
        this.AS = res["all_prefix"];
      });
      getWhoisApi(content).then((res) => {
        this.whois = Array.from(
          new Set(res["whois"].split("\n").filter((item) => item !== ""))
        );
        // console.log('whois:', this.whois);
        this.whois_title = this.whois[0];
        this.whois2 = this.whois.splice(0, 1);
      });
      getLongestASPrefixApi(content).then((res) => {
        //console.log(res);
        this.longest_prefix = res["longest_prefix"];
        this.country_dot = res["longest_prefix"]["country"];
        this.related_prefix = res["longest_prefix"]["v6Prefixes"];
        this.v6Propagation = res["longest_prefix"]["v6Propagation"]
        this.drawMap();
      });
      getRelationGraphApi(this.form.content).then((res) => {
        // console.log('relation_graph:',res);
        this.relation_graph = res;
      });
      getPictureApi(this.form.content).then((res) => {
        console.log('picture::', res);
        this.picture = res;
      });
      // this.reload();
    },
    showMore(evt) {
      this.showLength = this.showLength + 20;
      let target = evt.target;
      if (target.nodeName == "SPAN") {
        target = evt.target.parentNode;
      }
      target.blur();
    },
    showLess(evt) {
      this.showLength = 20;
      let target = evt.target;
      if (target.nodeName == "SPAN") {
        target = evt.target.parentNode;
      }
      target.blur();
    },
    selectTab(index) {
      this.isSelected = index;
    },
    drawMap() {
      var leti;
      var long;
      var country;
      for (var i = 0; i < latjson.length; i++) {
        if (latjson[i]["code"] == this.country_dot) {
          country = latjson[i]["name"];
          leti = latjson[i]["latitude"];
          long = latjson[i]["longitude"];
          console.log("country:", country);
          console.log("leti:", leti);
          console.log("long:", long);
          break;
        }
      }
      let wrapper1 = this.$echarts.init(document.getElementById("wrapper1"));
      wrapper1.setOption({
        geo: {
          map: "world",
          silent: true, // 禁止图形响应鼠标事件
          roam: false,
          zoom: 1.17,
          itemStyle: {
            color: "rgb(45, 89, 182)", // 背景颜色
            borderColor: "rgb(255, 250, 250)", // 边框颜色
          },
        },
        series: [
          {
            type: "effectScatter", //  指明图表类型：带涟漪效果的散点图
            coordinateSystem: "geo", //  指明绘制在geo坐标系上
            symbolSize: 7,
            data: [
              {
                name: country,
                value: [long, leti],
              },
            ],
          },
        ],
      });
      var choose = this.$refs.topov6;
      var v4;
      var v6;
      if (this.ipType == "ipv4") {
        v4 = choose;
      } else {
        v6 = choose;
      }
      window.RenderTopo(v4, v6, this.country_dot, () => {});
    },
  },
  watch: {
    showLength: function (val) {
      if (this.showLength) {
        // this.$nextTick(() => {})
      }
    },
    relation_graph: function (val) {
      if (this.relation_graph) {

      }
    },
    // picture: function (val) {
    //   if (this.picture) {

    //   }
    // },
    related_as: function (val) {
      if (this.related_as) {
        // this.$nextTick(() => {})
      }
    },
    related_prefix: function (val) {
      if (this.related_prefix) {
        // this.$nextTick(() => {})
      }
    },
    AS: function (val) {
      if (this.AS) {
        // this.$nextTick(() => {})
      }
    },
    whois: function (val) {
      if (this.whois) {
        // this.$nextTick(() => {})
      }
    },
    whois_title: function (val) {
      if (this.whois_title) {
        // this.$nextTick(() => {})
      }
    },
  },
  mounted() {
    this.form.content = this.$route.query.content;
    if (this.form.content.indexOf(".") > 0) {
      this.ipType = "ipv4";
    } else {
      this.ipType = "ipv6";
    }
    getRelatedASApi(this.form.content).then((res) => {
      console.log('related_as', res["reated_as"]);
      this.related_as = res["reated_as"];
    });
    getAllPrefixApi(this.form.content).then((res) => {
      // console.log(res["all_prefix"]);
      this.AS = res["all_prefix"];
    });
    getWhoisApi(this.form.content).then((res) => {
      this.whois = Array.from(
        new Set(res["whois"].split("\n").filter((item) => item !== ""))
      );
      this.whois_title = this.whois[0];
      this.whois2 = this.whois.splice(0, 1);
    });
    getLongestASPrefixApi(this.form.content).then((res) => {
      // console.log(res);
      this.longest_prefix = res["longest_prefix"];
      this.country_dot = res["longest_prefix"]["country"];
      this.related_prefix = res["longest_prefix"]["v6Prefixes"];
      this.v6Propagation = res["longest_prefix"]["v6Propagation"]
      this.drawMap();
    });
    getRelationGraphApi(this.form.content).then((res) => {
      // console.log('relation_graph:',res);
      this.relation_graph = res;
    });
    getPictureApi(this.form.content).then((res) => {
      console.log('picture::', res);
      this.picture = res;
    });
  },
};
</script>

<style lang="scss" scoped>
@import "~@/assets/style/reset.css";
.searchlist {
  height: 100%;
  .navbar {
    z-index: 10;
    background-color: rgb(0, 0, 0);
    height: 45px;
    position: fixed; // 所以head不在正常文档布局流中
    width: 100%;
    top: 0;
    left: 0;
  }
  .resultwrapper {
    background-color: #f9f9f9;
    margin-top: 50px; // 因为head脱离正常文档布局流，所以要设置margin,不然就从最上面开始啦
    margin-bottom: 15px;
    .search-wrapper {
      padding: 10px 0 0 0;
      display: flex;
      align-items: center;
      // align-items: center;
      // height: auto;
      .search-title {
        float: left;
        width: 13%;
        font-size: 18px;
        color: rgb(99, 99, 99);
        margin-left: 20px;
      }
      .el-form {
        display: flex;
        width: 52%;
        padding-left: 20px;
        .el-form-item {
          display: flex;
          align-items: center;
          margin: 0 0 0 0;
          .el-input /deep/ .el-input__inner {
            border: 1px solid rgb(39, 39, 39);
            font-size: 13px;
            border-radius: 4px;
            color: #474747;
            height: 35px;
          }
          .el-input .el-input__inner::-webkit-input-placeholder {
            color: rgb(95, 95, 95);
          }
        }
        .el-form-item:first-of-type {
          width: 90%;
        }
        .el-form-item:last-of-type {
          margin-left: 30px;
          // padding-right: 0px;
          .el-button {
            line-height: 0.65;
            border-color: rgb(90, 108, 187);
          }
        }
        .el-form-item /deep/ .el-form-item__content {
          width: 100%;
          line-height: 35px;
        }
      }
    }
    hr {
      margin: 13px 0 6px 0;
      background-color: rgb(226, 226, 226);
      height: 1px;
      border: none;
    }
    .aside {
      height: auto; // 默认
      float: left;
      width: 13%;
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
            font-size: 11px;
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
              font-size: 10px;
            }
            .span-only {
              float: left;
              // position: absolute;
              left: 0;
              top: 0;
              color: #727272;
            }
          }
          .showMore,
          .showLess {
            display: flex;
            align-items: center;
            justify-content: center;
            width: 50%;
            margin-top: 10px;
            padding: 2px 4px 2px 4px;
            font-size: 13.6px;
            color: #444444;
            margin-left: 1px;
            border: 1px solid rgb(126, 126, 126);
            border-radius: 4px;
            .el-icon-caret-bottom {
              margin-right: 1px;
              line-height: 1.3;
            }
            .el-icon-caret-top {
              margin-right: 1px;
              line-height: 1.3;
            }
          }
        }
      }
    }
    .rightwrapper {
      // height: auto;
      float: left;
      width: 52%;
      margin: auto 5px 20px 20px;
      /* tab选项卡的样式 */
      .tabs {
        display: flex;
        // width: 100%;
        height: 36px;
        // 注：margin：auto可以做到水平居中，但是有个前提条件就是，这个标签比如只是块状元素，并且有个确定的宽度，百分比的宽度也行
        margin: 8px auto 0 auto;
        background-color: #ececec;

        .list {
          display: flex;
          height: 100%;
          margin: 0;
          padding-left: 0;
          width: 100%; // 这个百分比相对于父标签tabs
          border-bottom: 2px solid #ececec;

          li {
            height: 100%;
            display: flex;
            text-align: center;
            margin: 0 39px;
            .list-item {
              a {
                height: 100%;
                display: flex;
                align-items: center;
                align-content: center;
                font-weight: 500;
                padding: 0 9px;
                /* 选中tab时的样式 
                在这里放选中时的tab样式，不生效
                */
              }
            }
          }
          li:first-of-type {
            margin-left: 22px;
          }
          li:last-of-type {
            margin-right: 22px;
          }
          /* 选中tab时的样式 */
          .active {
            border-bottom: 3px solid rgb(43, 119, 219);
            color: #030303;
          }
        }
      }
      .content {
        border: 1px solid #ccc;
        border-top: 1px solid transparent;
        margin: 0 auto 0 auto;
        .content-container {
          width: 100%;
          ul {
            margin: 0;
            // border-right: 1px solid hsl(0, 0%, 82%);
            padding-right: 3%;
            padding-left: 3%;
            li {
              position: relative; // ????
              overflow: hidden;
              padding: 10px 0;
              border-bottom: 1px solid #d8d8d8;
              color: #747474;
              font-size: 12.5px;
              h3 {
                font-size: 13.5px;
                color: #005cd9;
                text-decoration: underline;
                margin-top: 0;
                margin-bottom: 10px;
              }
              address {
                position: absolute;
                right: 0;
                top: 10px;
                font-style: normal;
              }
              article p {
                margin: 6px 0;
                .state {
                  border-radius: 3px;
                  font-size: 11px;
                  padding: 1.5px;
                }
              }
            }
          }
          
          .whois {
            font-size: 14px;
            .whois-title {
              font-size: 17px;
              padding-top: 15px;
              padding-bottom: 15px;
              color: #3e3d7a;
              font-weight: bold;
              text-align: center;
            }
            .whois-content {
              padding-bottom: 6px;
              padding-left: 50px;
              .el-icon-s-tools {
                padding-right: 5px;
              }
            }
          }
        }
      }
    }
    .cart-wrapper {
      height: auto;
      float: left;
      width: 28.2%;
      margin-left: 1.2%;
      // padding: 10px;
      margin-top: 10px;
      // 使用echarts时，记住一定要给容器一个高度
      .wrapper {
        height: 220px;
        width: 100%;
        border: 1px #cfcfcf solid;
        margin-bottom: 15px;
        color: #666666;
        // width: 100%;
        .title {
          margin-left: 2px;
          margin-top: 5px;
          padding-bottom: 2px;
          p {
            margin-left: 3px;
            font-size: 14px;
            display: inline;
          }
        }
        .wrapper1 {
          height: 195px;
          width: 100%;
        }
        .wrapper2 {
          height: 220px;
          width: 100%;
          .sigma-mouse,
          .sigma-scene {
            height: 205px;
          }
        }
        #pathGraph {
          margin-top: 10px;
          height: 350px;
          width: 340px;
        }
      }
      .wrapper:nth-of-type(2) {
        height: 250px;
      }
      .wrapper:nth-of-type(3) {
        height: 398px;
      }
    }
  }
}
</style>
