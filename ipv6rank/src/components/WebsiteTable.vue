<template>
    <div class="website-table">
        <table border="1" width="100%" style="table-layout:fixed"> 
          <thead>
            <tr class="title">
              <th width="3%">序号</th>
              <th width="14%">域名</th>
              <th width="12%">网站名称</th>
              <th width="10%">网站分类</th>
              <th width="19%">ipv6地址</th>
              <th width="10%">地址类型</th>
              <th width="4%">国家</th>
              <th width="5.5%">AS号</th>
              <th>AS名称</th>
              <th width="5%">支持度</th>
            </tr>
            <!-- <tr class="filter">
              <td></td>
              <td></td>
              <td><input v-model="search.bigtype" placeholder="过滤" type="text"></td>
              <td><input v-model="search.smalltype" placeholder="过滤" type="text"></td>
              <td></td>
              <td></td>
              <td></td>
              <td><input v-model="search.as" placeholder="过滤" type="text"></td>
              <td></td>
              <td></td>
            </tr> -->
          </thead>
          <tbody>
            <tr v-for="(item, index) in originalData.slice((currentPage-1)*pagesize, currentPage*pagesize)" :key="index">
              <td class="index"><span class="index">{{index + (currentPage-1) * pagesize + 1}}</span></td>
              <td :title=item.domain><span>{{item.domain}}</span></td>
              <td :title=item.domain_name><span>{{item.domain_name}}</span></td>
              <td :title=item.domain_subtype><span>{{item.domain_subtype}}</span></td>
              <td :title=item.ipv6_addresses><span>{{item.ipv6_addresses}}</span></td>
              <td :title=item.IID_type><span>{{item.IID_type}}</span></td>
              <td class="country" :title=item.IPv6_AS_country><span class="country">{{item.IPv6_AS_country}}</span></td>
              <td :title=item.IPv6_AS><span>{{item.IPv6_AS}}</span></td>
              <td :title=item.IPv6_AS_name><span>{{item.IPv6_AS_name}}</span></td>
              <td :title=item.v6support><span>{{item.v6support}}</span></td>
            </tr>
          </tbody>
        </table>
        <el-pagination 
          @current-change="handleCurrentChange"
          :current-page="currentPage"
          :page-size="pagesize"
          :pager-count="11"
          layout="total, prev, pager, next"
          :total="originalData.length"
        ></el-pagination>
      </div>
</template>

<script>
export default {
  name: "websiteTable",
  data() {
    return {
      currentPage:1,
      pagesize:30,
      // search: {
      //   bigtype: "",
      //   smalltype: "",
      //   as: "",
      // },
    }
  },
  props: ['originalData'],
  computed: {
    // filterData() {
    //   const search = this.search;
    //   // 代码冗余
    //   if (search.bigtype && !search.smalltype && !search.as) {
    //     return this.originalData.filter((data) => {
    //       // some() 方法用于检测数组中的元素是否满足指定条件（其返回的是true/false）
    //       return Object.keys(data).some((key) => {
    //         // 一个数据，只要其中有一个key对应的值和输入有匹配，即下面return的为true，则上面return的为true，则该数据(data)可以被返回，则被加到filter创建的数组
    //         return String(data["domain_type"]).toLowerCase().indexOf(search.bigtype) > -1;
    //       });
    //     });
    //   } else if (!search.bigtype && !search.smalltype && search.as) {
    //     return this.originalData.filter((data) => {
    //       // some() 方法用于检测数组中的元素是否满足指定条件（其返回的是true/false）
    //       return Object.keys(data).some((key) => {
    //         // 一个数据，只要其中有一个key对应的值和输入有匹配，即下面return的为true，则上面return的为true，则该数据(data)可以被返回，则被加到filter创建的数组
    //         return String(data["IPv6_AS"]).toLowerCase().indexOf(search.as) > -1;
    //       });
    //     });
    //   } else if (!search.bigtype && search.smalltype && !search.as) {
    //     return this.originalData.filter((data) => {
    //       // some() 方法用于检测数组中的元素是否满足指定条件（其返回的是true/false）
    //       return Object.keys(data).some((key) => {
    //         // 一个数据，只要其中有一个key对应的值和输入有匹配，即下面return的为true，则上面return的为true，则该数据(data)可以被返回，则被加到filter创建的数组
    //         return String(data["domain_subtype"]).toLowerCase().indexOf(search.smalltype) > -1;
    //       });
    //     });
    //   } else if (search.bigtype && !search.smalltype && search.as) {
    //     return this.originalData.filter((data) => {
    //       // some() 方法用于检测数组中的元素是否满足指定条件（其返回的是true/false）
    //       return Object.keys(data).some((key) => {
    //         // 一个数据，只要其中有一个key对应的值和输入有匹配，即下面return的为true，则上面return的为true，则该数据(data)可以被返回，则被加到filter创建的数组
    //         return (
    //           String(data["IPv6_AS"]).toLowerCase().indexOf(search.as) > -1 &&
    //           String(data["domain_type"]).toLowerCase().indexOf(search.bigtype) > -1
    //         );
    //       });
    //     });
    //   }
    //   else if (!search.bigtype && search.smalltype && search.as) {
    //     return this.originalData.filter((data) => {
    //       // some() 方法用于检测数组中的元素是否满足指定条件（其返回的是true/false）
    //       return Object.keys(data).some((key) => {
    //         // 一个数据，只要其中有一个key对应的值和输入有匹配，即下面return的为true，则上面return的为true，则该数据(data)可以被返回，则被加到filter创建的数组
    //         return (
    //           String(data["IPv6_AS"]).toLowerCase().indexOf(search.as) > -1 &&
    //           String(data["domain_subtype"]).toLowerCase().indexOf(search.smalltype) > -1
    //         );
    //       });
    //     });
    //   }
    //   else if (search.bigtype && search.smalltype && !search.as) {
    //     return this.originalData.filter((data) => {
    //       // some() 方法用于检测数组中的元素是否满足指定条件（其返回的是true/false）
    //       return Object.keys(data).some((key) => {
    //         // 一个数据，只要其中有一个key对应的值和输入有匹配，即下面return的为true，则上面return的为true，则该数据(data)可以被返回，则被加到filter创建的数组
    //         return (
    //           String(data["domain_type"]).toLowerCase().indexOf(search.bigtype) > -1 &&
    //           String(data["domain_subtype"]).toLowerCase().indexOf(search.smalltype) > -1
    //         );
    //       });
    //     });
    //   } else if (search.bigtype && search.smalltype && search.as) {
    //     return this.originalData.filter((data) => {
    //       // some() 方法用于检测数组中的元素是否满足指定条件（其返回的是true/false）
    //       return Object.keys(data).some(() => {
    //         // 一个数据，只要其中有一个key对应的值和输入有匹配，即下面return的为true，则上面return的为true，则该数据(data)可以被返回，则被加到filter创建的数组
    //         return (
    //           String(data["domain_type"]).toLowerCase().indexOf(search.bigtype) > -1 &&
    //           String(data["domain_subtype"]).toLowerCase().indexOf(search.smalltype) > -1 &&
    //           String(data["IPv6_AS"]).toLowerCase().indexOf(search.as) > -1
    //         );
    //       });
    //     });
    //   } else {
    //     return this.originalData
    //   }
    // },
  },
  mounted() {},
  methods: {
    handleCurrentChange(currentPage) {
      this.currentPage = currentPage;
    },
  }
}
</script>

<style lang="scss" scoped>
.website-table {
  margin-top: 9px;
  width:100%;
  table, table tr th, table tr td { border:1px solid #b9b9b9; }
  table {
    width: 100%;
    border-collapse: collapse;
    th {
      background: rgb(243, 243, 243);
      height: 34px;
      font-size: 16px;
      font-weight: normal;
    }
    tbody td {
      height: 32px;
      width: 100%;
      white-space: nowrap;
			overflow: hidden;
			text-overflow: ellipsis;
    }
    td[class*=index], td[class*=country] {
        text-align: center;
      }
    td span:not([class*=index]):not([class*=country]){
      margin-left: 10px;
      margin-right: 10px;
    }
    // thead {
    //   width: 100%;
    //   tr {
    //     width: 100%;
    //     td {
    //       height: 30px;
    //       width: 100%;
    //       input {
    //         width: 98%;
    //         height: 100%;
    //         border: 2.2px solid rgb(231, 231, 231);
    //         outline: 2px solid rgb(192, 192, 192);
    //         color: gray;
    //         text-indent:7px;
    //         //border-radius: 5px;
    //       }
    //     }
    //   }
    // }
  }
  .el-pagination {
    margin-top: 5px;
  }
  .el-pagination /deep/ .el-pagination__total {
      font-size: 14px;
      color: rgb(87, 87, 87);
  }
  .el-pagination /deep/ .el-icon {
      font-size: 14px;
  }
  .el-pagination /deep/ .el-pager li{
    font-size: 14px;
    li:not([class*=active]) {
      color: rgb(87, 87, 87);
    }
  }
}
</style>
