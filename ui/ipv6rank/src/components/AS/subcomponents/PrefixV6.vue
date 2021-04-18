<template>
  <el-table
    :data="tableData"
    border
    :default-sort = "{prop: 'date', order: 'descending'}"
    height="100%"
    style="width: 100%">
    <el-table-column
      prop="prefix"
      label="v6前缀"
      sortable
      width="250">
    </el-table-column>
    <el-table-column
      prop="description"
      label="描述"
      sortable
      width="400">
    </el-table-column>
    <el-table-column
      prop="country"
      sortable
      label="国家">
    </el-table-column>
  </el-table>
</template>

<script>
export default {
  name: 'PrefixV6',
  props: {
    res: {
      type: Object,
      default: null
    }
  },
  data() {
    return {
      tableData: [],
      flag: false // 标志是否已经渲染，即是否执行过handleChange
    }
  },
  watch: {
    res(newVal){
      if(newVal && !this.flag){
        this.handleChange(newVal)
      }
    }
  },
  mounted(){
    if(this.res && !this.flag){
      this.handleChange(this.res)
    }
  },
  methods: {
    formatData(data){
      this.tableData = []
      let len = data.length
      for(let i = 0; i < len; i++){
        let item = {}
        item['prefix'] = data[i]
        item['description'] = '描述信息_'+i
        item['country'] = '国家信息_'+i
        this.tableData.push(item)
      }
    },
    handleChange(newVal){
      this.formatData(newVal['v6Prefixes'])
      this.flag = true
    }
  }
}
</script>
<style scoped lang='scss'>
</style>
