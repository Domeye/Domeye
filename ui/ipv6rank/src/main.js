import Vue from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'
// import './utils/rem.js'

import axios from 'axios';
Vue.prototype.$axios = axios;

import ElementUI from 'element-ui'
import 'element-ui/lib/theme-chalk/index.css'
Vue.use(ElementUI)

import echarts from 'echarts';
import 'echarts/map/js/world'
Vue.prototype.$echarts = echarts;

import BaiduMap from 'vue-baidu-map'
Vue.use(BaiduMap,{
  ak: '9YnzLvjb8L6tb0pa24Xyexbbcb49Huc5'
})

Vue.config.productionTip = false

new Vue({
  router,
  store,
  render: h => h(App)
}).$mount('#app')
