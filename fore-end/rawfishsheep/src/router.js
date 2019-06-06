import Vue from 'vue'
import Router from 'vue-router'
import index from '@/components/index.vue'
import login from '@/components/user/user-login.vue'
Vue.use(Router)

export default new Router({
  mode: 'history',
  base: 'rfs',
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
      component: () => import('@/components/user/user-logout.vue'),
      meta: {
        requireLogin: false,
        requreAdmin: false,
      }
    },
    {
      path: '/register',
      name: 'register',
      component: () => import('@/components/user/user-register.vue'),
      meta: {
        requireLogin: false,
        requreAdmin: false,
      }
    },
    {
      path: '/settlement',
      name: 'settlement',
      component: () => import('@/components/settlement/app-settlement.vue'),
      meta: {
        requireLogin: true,
        requreAdmin: false,
      }
    },
    {
      path: '/order',
      component: () => import('@/components/order/app-order.vue'),
      meta: {
        requireLogin: true,
        requreAdmin: false,
      },
    },
    {
      path: '/order/:orderid',
      component: () => import('@/components/order/order-detail.vue'),
      props: true,
      meta: {
        requireLogin: true,
        requreAdmin: true,
      }
    },
    {
      path: '/backstage',
      component: () => import('@/components/backstage/bs-index.vue'),
      children: [
        {
          path: 'dashboard',
          component: () => import('@/components/backstage/bs-dashboard.vue'),
          meta: {
            requireLogin: true,
            requreAdmin: true,
          }
        },
        {
          path: 'goods',
          component: () => import('@/components/backstage/bs-goods.vue'),
          meta: {
            requireLogin: true,
            requreAdmin: true,
          }
        },
        {
          path: 'user',
          component: () => import('@/components/backstage/bs-user.vue'),
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

    { 
      path: '*', 
      component: () => import('@/components/404NotFound.vue'),
      meta: {
        requireLogin: false,
        requreAdmin: false,
      }
    }

    // {
    //   path: '/about',
    //   name: 'about',
    //   // route level code-splitting
    //   // this generates a separate chunk (about.[hash].js) for this route
    //   // which is lazy-loaded when the route is visited.
    //   component: () => import(/* webpackChunkName: "about" */ './views/About.vue')
    // }

    ,
    {
      path: '/search',
      name: 'search',
      component: () => import('@/components/search/search.vue'),
      meta: {
        requireLogin: false,
        requreAdmin: false,
      }
    }
  ]
})
