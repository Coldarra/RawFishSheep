import Vue from "vue"
import VueRouter from "vue-router"

// 引入组件

import index from './page/index.vue'
import index3 from './page/index3.vue'
import login from './page/login.vue'
import home from './page/home.vue'
import goods_detail from './page/goods_detail.vue'
import settlement from './page/app-settlement.vue'
import order from './page/app-order.vue'
import backstage from './page/bs-index.vue'
import backstage_goods from './page/backstage/bs-goods.vue'
import notFound from './page/404.vue'
// 要告诉 vue 使用 vueRouter
Vue.use(VueRouter);

let routes = [{
    path: '/',
    component: index,
},
{
    path: '/index',
    component: index3,
},
{
    path: '/goods',
    component: goods_detail,
},
{
    path: '/login',
    component: login,
},
{
    path: '/settlement',
    component: settlement,
},
{
    path: '/order',
    component: order,
},
{
    path: '/backstage',
    component: backstage,
    children: [
        { path: 'goods', component: backstage_goods },
    ]
},
{
    path: '/404',
    component: notFound,
},
{
    path: '/home',
    component: home,
},

];
var router = new VueRouter({
    mode: 'history',
    routes
})
export default router;