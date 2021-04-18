<template>
  <div>
    {{whois}}
  </div>
</template>

<script>
import {getWhois} from "@/api/apiData";
export default {
  name: 'Whois',
  props: {
    res: {
      type: Object,
      default: null
    }
  },
  data() {
    return {
      whois: '',
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
    handleChange(newVal){
      getWhois(newVal['ASN']).then(res => {
        this.whois = res.whois
      })
      // getWhois('2001:2e0::1').then(res => {
      //   this.whois = res.whois
      // })
    }
  },
}
</script>
<style scoped lang='scss'>
</style>
