import Vue from 'vue'
import Router from 'vue-router'

import index from '@/components/index.vue'
import register from '@/components/register.vue'
import login from '@/components/login.vue'
import logout from '@/components/logout.vue'
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
      meta: {
        requireLogin: false,
        requreAdmin: false,
      }
    },
    {
      path: '/login',
      name: 'login',
      component: login,
      meta: {
        requireLogin: false,
        requreAdmin: false,
      }
    },
    {
      path: '/logout',
      name: 'logout',
      component: logout,
      meta: {
        requireLogin: false,
        requreAdmin: false,
      }
    },
    {
      path: '/register',
      name: 'register',
      component: register,
      meta: {
        requireLogin: false,
        requreAdmin: false,
      }
    },
    {
      path: '/settlement',
      name: 'settlement',
      component: settlement,
      meta: {
        requireLogin: true,
        requreAdmin: false,
      }
    },
    {
      path: '/order',
      component: order,
      meta: {
        requireLogin: true,
        requreAdmin: false,
      }
    },
    {
      path: '/backstage',
      component: backstage,
      children: [
        {
          path: 'dashboard',
          component: backstage_dashboard,
          meta: {
            requireLogin: true,
            requreAdmin: true,
          }
        },
        {
          path: 'goods',
          component: backstage_goods,
          meta: {
            requireLogin: true,
            requreAdmin: true,
          }
        },
        {
          path: 'user', component: backstage_user,
          meta: {
            requireLogin: true,
            requreAdmin: true,
          }
        },
      ],
      meta: {
        requireLogin: true,
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
