import Vue from 'vue'
import Router from 'vue-router'

import index from '@/components/index.vue'
import settlement from '@/components/app-settlement.vue'
import order from '@/components/app-order.vue'
import backstage from '@/components/bs-index.vue'
import backstage_dashboard from '@/components/backstage/bs-dashboard.vue'
import backstage_goods from '@/components/backstage/bs-goods.vue'
import backstage_user from '@/components/backstage/bs-user.vue'
Vue.use(Router)

export default new Router({
  mode: 'history',
  routes: [
    {
      path: '/',
      name: 'index',
      component: index,
      meta:{
        requreLogin: false,
        requreAdmin: false,
      }
    },
    {
      path: '/settlement',
      name: 'settlement',
      component: settlement,
      meta: {
        requreLogin: true,
        requreAdmin: false,
      }
    },
    {
      path: '/order',
      component: order,
      meta: {
        requreLogin: true,
        requreAdmin: false,
      }
    },
    {
      path: '/backstage',
      component: backstage,
      children: [
        { path: 'dashboard', component: backstage_dashboard },
        { path: 'goods', component: backstage_goods },
        { path: 'user', component: backstage_user },
      ],
      meta: {
        requreLogin: true,
        requreAdmin: true,
      }
    },
    // {
    //   path: '/about',
    //   name: 'about',
    //   // route level code-splitting
    //   // this generates a separate chunk (about.[hash].js) for this route
    //   // which is lazy-loaded when the route is visited.
    //   component: () => import(/* webpackChunkName: "about" */ './views/About.vue')
    // }
  ]
})
