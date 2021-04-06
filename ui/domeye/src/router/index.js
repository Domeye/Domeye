import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '../views/Home.vue'

const originalPush = VueRouter.prototype.push
VueRouter.prototype.push = function push (location) {
 return originalPush.call(this, location).catch(err => err)
}

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home
  },
  {
    path: '/login',
    name: 'Login',
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () => import(/* webpackChunkName: "about" */ '../views/Login.vue')
  },
  {
    path: '/register',
    name: 'Register',
    component: () => import(/* webpackChunkName: "about" */ '../views/Register.vue')
  },
  {
    path: '/admin',
    name: 'Admin',
    component: () => import(/* webpackChunkName: "about" */ '../views/Admin.vue')
  },
  {
    path: '/logout',
    name: 'Logout',
    component: () => import(/* webpackChunkName: "about" */ '../views/Logout.vue')
  },
  {
    path: '/searchlist',
    name: 'SearchList',
    component: () => import(/* webpackChunkName: "about" */ '../views/SearchList.vue')
  },
  {
    path: '/website',
    name: 'Website',
    component: () => import(/* webpackChunkName: "about" */ '../views/Website.vue'),
    // children: [
    //   {
    //     path: 'moreRank',
    //     // name: 'MoreRank',
    //     component: () => import(/* webpackChunkName: "about" */ '../components/MoreRank.vue')
    //   },
    // ]
  },
  {
    path: '/address',
    name: 'Address',
    component: () => import(/* webpackChunkName: "about" */ '../views/Address.vue')
  },
  {
    path: '/data',
    name: 'Data',
    component: () => import(/* webpackChunkName: "about" */ '../views/Data.vue')
  },
  {
    path: '/report',
    name: 'Report',
    component: () => import(/* webpackChunkName: "about" */ '../views/Report.vue')
  },
  {
    path: '/test',
    name: 'Test',
    component: () => import(/* webpackChunkName: "about" */ '../views/Test.vue')
  },
  {
    path: '/moreRank',
    name: 'MoreRank',
    component: () => import(/* webpackChunkName: "about" */ '../components/MoreRank.vue')
  },
  {
    path: '/moreDetail',
    name: 'MoreDetail',
    component: () => import(/* webpackChunkName: "about" */ '../components/MoreDetail.vue')
  },
]

// 创建 router 实例，然后传 `routes` 配置
const router = new VueRouter({
  mode: 'hash',
  base: process.env.BASE_URL,
  routes
})

export default router
