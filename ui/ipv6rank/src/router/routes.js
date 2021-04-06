const routes = [
  {
    path: '/',
    redirect: {
      name: 'home'
    }
  },
  {
    path: '/home',
    name: 'home',
    component: () => import('@/views/dashboard/home')
  },
  {
    path: '/website',
    name: 'website',
    component: () => import('@/views/dashboard/website')
  },
  {
    path: '/address',
    name: 'address',
    component: () => import('@/views/dashboard/address')
  },
  {
    path: '/statistics',
    name: 'statistics',
    component: () => import('@/views/dashboard/statistics'),
    children: [
      {
        path: '',
        component: () => import('@/views/dashboard/statistics1'),
        redirect: '/statistics/one/1',
        children: [
          { 
            path: '/statistics/one/1',
            component: () => import('@/views/dashboard/statistics1-1'),
          },
          { 
            path: '/statistics/one/2',
            component: () => import('@/views/dashboard/statistics1-2'),
          },
        ]
      },
      { 
        path: '/statistics/two',
        component: () => import('@/views/dashboard/statistics2'),
        redirect: '/statistics/two/1',
        children: [
          { 
            path: '/statistics/two/1',
            component: () => import('@/views/dashboard/statistics2-1'),
          },
          { 
            path: '/statistics/two/2',
            component: () => import('@/views/dashboard/statistics2-2'),
          },
          { 
            path: '/statistics/two/3',
            component: () => import('@/views/dashboard/statistics2-3'),
          },
        ]
      },
      { 
        path: 'three',
        component: () => import('@/views/dashboard/statistics3'),
      },
    ]
  },
  {
    path: '/blog',
    name: 'blog',
    component: () => import('@/views/dashboard/blog'),
  },
  {
    path: '/download',
    name: 'download',
    component: () => import('@/views/dashboard/download'),
  },
  {
    path:'/test',
    name:'test',
    component:() => import('@/testSass/test')
  },
  {
    path:'/lifecycle',
    name:'lifecycle',
    component:() => import('@/testSass/lifecycle')
  },
  {
    path:'/el-table',
    name:'el-table',
    component:() => import('@/testSass/el-table')
  },
  {
    path:'/scale',
    name:'scale',
    component:() => import('@/testSass/scale')
  }

]

export default routes
