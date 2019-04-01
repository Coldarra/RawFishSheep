import Vue from "vue"
import VueRouter from "vue-router"

// 引入组件

import index from './page/index.vue'
import login from './page/login.vue'
import home from './page/home.vue'
import notFound from './page/404.vue'
// 要告诉 vue 使用 vueRouter
Vue.use(VueRouter);

let routes = [{
    path: '/',
    component: index,
    // name: '',
    // hidden: true
},
{
    path: '/index',
    component: index,
    // name: '',
    // hidden: true
},
{
    path: '/login',
    component: login,
    // name: '',
    // hidden: true
},
{
    path: '/404',
    component: notFound,
    // name: '',
    // hidden: true
},
{
    path: '/home',
    component: home,
    // name: '',
    // hidden: true
},

];
var router = new VueRouter({
    mode: 'history',
    routes
})
export default router;