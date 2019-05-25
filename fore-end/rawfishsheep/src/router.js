import Vue from 'vue'
import Router from 'vue-router'

// import index from '@/components/app-index.vue'
// import register from '@/components/user-register.vue'
// import login from '@/components/user-login.vue'
// import logout from '@/components/user-logout.vue'
// import settlement from '@/components/app-settlement.vue'
// import order from '@/components/app-order.vue'
// import backstage from '@/components/bs-index.vue'
// import backstage_dashboard from '@/components/backstage/bs-dashboard.vue'
// import backstage_goods from '@/components/backstage/bs-goods.vue'
// import backstage_user from '@/components/backstage/bs-user.vue'
Vue.use(Router)

export default new Router({
  mode: 'history',
  base: 'rfs',
  routes: [
    {
      path: '/',
      name: 'index',
      component: () => import('@/components/app-index'),
      meta: {
        requireLogin: false,
        requreAdmin: false,
      }
    },
    {
      path: '/login',
      name: 'login',
      component: () => import('@/components/user-login.vue'),
      meta: {
        requireLogin: false,
        requreAdmin: false,
      }
    },
    {
      path: '/logout',
      name: 'logout',
      component: () => import('@/components/user-logout.vue'),
      meta: {
        requireLogin: false,
        requreAdmin: false,
      }
    },
    {
      path: '/register',
      name: 'register',
      component: () => import('@/components/user-register.vue'),
      meta: {
        requireLogin: false,
        requreAdmin: false,
      }
    },
    {
      path: '/settlement',
      name: 'settlement',
      component: () => import('@/components/app-settlement.vue'),
      meta: {
        requireLogin: true,
        requreAdmin: false,
      }
    },
    {
      path: '/order',
      component: () => import('@/components/app-order.vue'),
      meta: {
        requireLogin: true,
        requreAdmin: false,
      },
    },
    {
      path: '/order/:orderid',
      component: () => import('@/components/order/od-detail.vue'),
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
  ]
})
