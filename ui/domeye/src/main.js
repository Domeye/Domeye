import Vue from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'
import ElementUI from 'element-ui';
// import 'element-ui/lib/theme-chalk/index.css';
import './assets/style/element-variables.scss';
import echarts from 'echarts';
import 'echarts/map/js/world.js';
import 'echarts/map/js/china.js';
import axios from 'axios';
import VueResource from 'vue-resource';
//import 'lib-flexible/flexible.js'

Vue.config.productionTip = false
// Vue.forceUpdate();
Vue.use(ElementUI);
Vue.use(VueResource);
Vue.prototype.$echarts = echarts;
Vue.prototype.$axios= axios;  // 则在组件methods中使用 $axios命令

new Vue({
  router,
  store,
  render: h => h(App)
}).$mount('#app')
