<template>
  <div class="searchlist">
    <div class="head">
      <head-nav />
    </div>
    <div class="resultwrapper">
      <div class="search-wrapper">
        <span class="search-title">探针搜索</span>
        <el-form :inline="true" ref="form" label-width="80%">
          <el-form-item>
            <el-input
              v-model="form.content"
              placeholder="可搜索探针、IP地址，多个关键字用空格隔开"
            >
              <el-select v-model="select" slot="append" placeholder="探针">
                <el-option
                  v-for="item in options"
                  :key="item.select"
                  :label="item.label"
                  :value="item.select"
                >
                </el-option>
              </el-select>
            </el-input>
          </el-form-item>
          <el-form-item>
            <el-button type="primary" @click="search">搜索</el-button>
          </el-form-item>
        </el-form>
      </div>
      <hr />
      <div class="aside">
        <div class="barfilter">
          <h3>机构</h3>
          <ul>
            <li v-for="organization in organizations" :key="organization.name">
              <a
                href="javascript:void(0)"
                @click="setResultsFilter(organization.name)"
                >{{ organization.name }}</a
              >
              <span :style="{ width: (organization.num * 100) / 119 + '%' }">{{
                organization.num
              }}</span>
            </li>
          </ul>
        </div>
        <div class="barfilter">
          <h3>省份</h3>
          <ul>
            <li v-for="location in locations" :key="location.name">
              <a
                href="javascript:void(0)"
                @click="setResultsFilter(location.name)"
                >{{ location.name }}</a
              >
              <span :style="{ width: (location.num * 100) / 119 + '%' }">{{
                location.num
              }}</span>
            </li>
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
                  >{{ item }}</a
                >
              </div>
            </li>
          </ul>
        </div>
        <div class="content">
          <div class="content-container" v-show="isSelected === 0">
            <ul>
              <li v-for="probe in this.probes" :key="probe.name">
                <h3>{{ probe.name }} ({{ probe.ip }})</h3>
                <address>
                  {{ probe.location.organization }},{{
                    probe.location.province
                  }}
                </address>
                <div class="check-wrapper">
                  <!--注： v-if为条件渲染 只有在指令内的表达式为true时 才会显示, disabled表示禁用状态 灰色显示-->
                  <input
                    type="checkbox"
                    v-if="probe.state != 'active'"
                    disabled
                  />
                  <input
                    type="checkbox"
                    v-if="probe.state == 'active'"
                    v-model="probe.inCart"
                    @change="handleProbeSelect(probe, $event)"
                  />
                  <label>选为探针源</label>
                </div>
                <article>
                  <p>类型：{{ probe.type }}</p>
                  <p>测试类型：ping, traceout, curl</p>
                  <p>
                    状态：<span
                      class="state"
                      :style="{
                        color: '#fff',
                        'background-color':
                          probe.state == 'active' ? 'green' : 'gray',
                      }"
                      >{{ probe.state }}(--)</span
                    >
                  </p>
                </article>
              </li>
            </ul>
          </div>
          <div class="content-container" v-show="isSelected === 1">
            <!--<statistic-block /> -->
            <div class="block">
              <div class="title">
                <p>全球分布</p>
              </div>
              <div class="echart1" id="echart1" ref="echart1"></div>
            </div>
            <div class="block">
              <div class="title">
                <p>数据统计</p>
              </div>
              <div class="echart2" id="echart2" ref="echart2"></div>
            </div>
            <div class="block">
              <div class="title">
                <p>数据分布</p>
              </div>
              <div class="echart3" id="echart3" ref="echart3"></div>
            </div>
          </div>
          <div class="content-container" v-show="isSelected === 2"></div>
          <div class="content-container" v-show="isSelected === 3"></div>
        </div>
      </div>
      <div class="cart-wrapper">
        <h3>已选探针</h3>
        <div class="empty" v-show="!this.cartProbe.length">未选中任何探针</div>
        <div class="items" v-show="this.cartProbe.length">
          <!--因为要频繁切换 所以用v-show 不用v-if-->
          <ul>
            <li v-for="probe in this.cartProbe" :key="probe.name">
              {{ probe.name }} ({{ probe.ip }})
              <a @click="deleteProbeandFresh(probe)" href="javascript:void(0)">
                <i class="el-icon-remove" style="color: red"></i>
              </a>
            </li>
          </ul>
          <button class="cart-submit" @click="sendTasks()">任务下发</button>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import HeadNav from "@/components/HeadNav";
// import StatisticBlock from "@/components/StatisticBlock";

export default {
  name: "SearchList",
  components: {
    HeadNav,
    // StatisticBlock,
  },
  data() {
    return {
      form: {
        content: "",
      },
      options: [
        {
          select: "选项1",
          label: "探针",
        },
        {
          select: "选项2",
          label: "IP",
        },
      ],
      select: "",
      locations: "",
      organizations: "",
      probes: "",
      cartProbe: [], // 新建一个数组array
      selectedTab: ["搜 索 结 果", "统 计 结 果", "全 球 视 角", "相 关 漏 洞"],
      isSelected: 0,
    };
  },
  methods: {
    search() {},
    setResultsFilter() {},
    selectTab(index) {
      this.isSelected = index;
    },
    handleProbeSelect(probe, event) {
      console.log("选中true 取消false: ", event.target.checked);
      if (event.target.checked) {
        this.cartProbe.push(probe); // 往Array中填加元素 pop为删除最后一个元素。问题：点击之后之前的probe的属性也会被改变
      } else {
        var i = this.cartProbe.indexOf(probe); // 没找到返回-1
        console.log("复选框取消探针的索引i:", i);
        this.cartProbe.splice(i, 1); // 使用splice删除数组指定元素
      }
    },
    sendTasks() {},
    deleteProbeandFresh(probe) {
      var i = this.cartProbe.indexOf(probe);
      this.cartProbe.splice(i, 1); // 使用splice删除数组指定元素
      let rep_probes = this.probes;
      var probes_i = rep_probes.indexOf(probe);
      // 同时左边的复选框也要更新删除
      rep_probes[probes_i]["inChart"] = false; // 设置属性是不会产生视图更新的
      this.probes = rep_probes;
      // this.$forceUpdate();
      console.log("被删除probe的ip：", probe["ip"]);
      console.log("被删除probe的复选框状态：", probe["inChart"]);
    },
    getWorld() {
      this.drawChart();
    },
    drawChart() {
      // 基于准备好的dom，初始化echarts实例
      let map1 = this.$echarts.init(document.getElementById("echart1"));
      // 绘制图表
      map1.setOption({
        series: {
          type: "pie",
          data: [
            { name: "A", value: 1212 },
            { name: "B", value: 2323 },
            { name: "C", value: 1919 },
          ],
        },
      });
      let map2 = this.$echarts.init(document.getElementById("echart2"));
      // 绘制图表
      map2.setOption({
        series: {
          type: "pie",
          data: [
            { name: "A", value: 1212 },
            { name: "B", value: 2323 },
            { name: "C", value: 1919 },
          ],
        },
      });
      let map3 = this.$echarts.init(document.getElementById("echart3"));
      // 绘制图表
      map3.setOption({
        series: {
          type: "pie",
          data: [
            { name: "A", value: 1212 },
            { name: "B", value: 2323 },
            { name: "C", value: 1919 },
          ],
        },
      });
    },
  },
  mounted() {
    this.$axios
      .get(
        "http://39.104.95.182:11923/admin/probeQueryByKeyword?search=%E5%8C%97%E4%BA%AC"
      )
      .then((res) => {
        this.organizations = res.data.organizations;
        this.locations = res.data.locations;
        this.probes = res.data.probes; // 注：data和probe在es6中的数据类型都是object
        for (let probe of this.probes) {
          probe["inCart"] = false;
        }
        console.log(this.probes);
      });
    this.getWorld();
  },
};
</script>

<style lang="scss">
// 问题：把scoped去掉之后 并没有影响到其他部件的css样式？？？？？？？
@import "~@/assets/style/reset.css";
.searchlist {
  height: 100%;
  .head {
    z-index: 10;
    height: 53px;
    background-color: rgb(0, 0, 0);
    position: fixed; // 所以head不在正常文档布局流中
    width: 100%;
    top: 0;
    left: 0;
    .navbar {
      margin: 0 20px 0 20px;
    }
  }
  .resultwrapper {
    height: 100%;
    background-color: #f9f9f9;
    margin-top: 53px; // 因为head脱离正常文档布局流，所以要设置margin,不然就从最上面开始啦
    .search-wrapper {
      padding: 10px 0 0 0;
      // display: flex;
      // align-items: center;
      // height: auto;
      .search-title {
        float: left;
        width: 15%;
        font-size: 22px;
        color: #777;
        margin-left: 40px;
      }
      .el-form {
        display: flex;
        width: 53%;
        // margin-left: 30px; 设置无效？？？？ 会跑到前一个元素那里
        padding-left: 30px;
        .el-form-item {
          display: flex;
          align-items: center;
          margin: 0 0 0 0;
          .el-input .el-input-group__append {
            width: 15%;
            color: #4e4e4e;
            vertical-align: baseline;
            // height: 35px;
          }
          .el-input /deep/ .el-input__inner {
            // background-color: #7d6f6f00;
            border: 1px solid rgb(39, 39, 39);
            font-size: 13px;
            border-radius: 4px;
            color: #474747;
            height: 35px;
          }
          .el-input .el-input__inner::-webkit-input-placeholder {
            color: rgb(95, 95, 95);
          }
          .el-select .el-select__caret {
            color: #4e4e4e;
          }
        }
        .el-form-item:first-of-type {
          width: 83%;
        }
        .el-form-item:last-of-type {
          margin-left: 55px;
          // padding-right: 0px;
          .el-button {
            line-height: 0.65;
          }
        }
        .el-form-item .el-form-item__content {
          width: 100%;
          line-height: 35px;
        }
        .el-form-item
          /deep/
          .el-form-item__content
          > .el-input
          > .el-input__inner {
          border-right: transparent;
          border-top-right-radius: 0;
          border-bottom-right-radius: 0;
        }
        .el-form-item
          /deep/
          .el-input-group__append
          > .el-select
          > .el-input
          > .el-input__inner {
          border-left: transparent;
          border-top-left-radius: 0;
          border-bottom-left-radius: 0;
        }
        .el-form-item /deep/ .el-input-group {
          // vertical-align: middle;
        }
      }
    }
    hr {
      margin: 10px 0 10px 0;
      background-color: #eee;
      height: 1px;
      border: none;
    }
    .aside {
      height: auto; // 默认
      float: left;
      width: 15%;
      padding-left: 40px;
      .barfilter {
        h3 {
          margin: 10px 0 0 0;
          font-weight: normal;
          font-size: 17px;
        }
        ul {
          padding: 0;
          li {
            position: relative;
            overflow: hidden; // 不懂？？？？
            margin: 5px 0;
            font-size: 12px;
            color: #727272;
            // display: inline;
            a {
              position: absolute; // absolute相对于 static 定位以外的第一个父元素(ul)进行定位
              left: 0;
              top: 0;
              color: #727272;
            }
            span {
              float: right;
              text-align: right;
              background: aqua;
              text-indent: -100%; // 不懂？？？？
            }
          }
        }
      }
    }
    .rightwrapper {
      height: auto;
      float: left;
      width: 53%;
      margin: auto 10px auto 30px;
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
          // justify-content: space-around;
          margin: 0;
          padding: 0;
          width: 100%; // 这个百分比相对于父标签tabs
          border-bottom: 3px solid #ececec;

          li {
            height: 100%;
            display: flex;
            text-align: center;
            // padding: 0 20px;
            // margin: 0 22px;
            .list-item {
              a {
                height: 100%;
                display: flex;
                align-items: center;
                align-content: center;
                font-weight: 500;
                padding: 0 15px;
                margin: 0 26px;
                /* 选中tab时的样式 
                在这里放选中时的tab样式，不生效
                */
              }
            }
          }
          /* 选中tab时的样式 */
          .active {
            // background: rgb(255, 255, 255);
            // border: 1.5px solid rgb(230, 174, 252);
            border-bottom: 3px solid rgb(43, 119, 219);
            color: #030303;
            // width: 120%;
            // border-bottom-width: 15px;
          }
        }
      }
      .content {
        // width: 100%;
        height: auto;
        border: 1px solid #ccc;
        border-top: 1px solid transparent;
        margin: 0 auto 0 auto;
        padding-top: 14px;
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
              .check-wrapper {
                position: absolute; // 其父元素为
                right: 0;
                bottom: 15px;
                input {
                  vertical-align: middle; // 把此元素放在父元素的中部
                }
                label {
                  vertical-align: middle;
                }
              }
            }
          }
          .block {
            height: 100%;
            // width: 100%;
            margin: 15px;
            padding: 0 10px;
            border: 1px solid rgb(224, 224, 224);
            .echart1 {
              height: 100%;
              width: 100%;
              // position: absolute;
              margin-left: 170px;
            }
            .echart2 {
              height: 100%;
              width: 100%;
              margin-left: 170px;
            }
            .echart3 {
              height: 100%;
              width: 100%;
              margin-left: 170px;
            }
          }
        }
      }
    }
    .cart-wrapper {
      height: auto;
      float: left;
      width: 20%;
      margin-left: 1.5%;
      border: 1px rgb(97, 97, 97) solid;
      border-radius: 3px;
      padding: 10px;
      margin-top: 10px;
      h3 {
        margin: 0;
        font-weight: normal;
        font-size: 16.5px;
        color: #202020;
      }
      .empty {
        color: #666;
        font-size: 14.5px;
        margin: 15px auto 15px auto;
      }
      .items {
        margin: 15px 0 0 0;
        ul {
          margin-bottom: 22px;
          padding: 0;
          color: #666;
          font-size: 14.5px;
          li {
            margin: 0 auto 5px 0;
            position: relative;
            a {
              position: absolute;
              right: 3%; // absolute不是相对于父元素定位吗？？设置0后 贴到浏览器了
            }
          }
        }
        button {
          background: #1eadc4;
          border-radius: 4px;
          border: 0;
          height: 30px;
          width: 88px;
          color: white;
          font-size: 14.5px;
        }
      }
    }
  }
}
</style>
