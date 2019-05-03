import Vue from 'vue';
import ElementUI from 'element-ui';
import 'element-ui/lib/theme-chalk/index.css';
import Router from 'vue-router';
import App from './App.vue';
import echarts from 'echarts';
import 'font-awesome/css/font-awesome.min.css';

// import VueAxios from 'vue-axios'
import axios from 'axios'

import global from './global';
// Vue.prototype.GLOBAL = global

Vue.use(ElementUI);
Vue.use(Router);
Vue.use(echarts);
Vue.use(axios);

// router.beforeEach((to, from, next) => {
//   if (to.path == '/login') {
//     sessionStorage.removeItem('user');
//   }
//   let user = JSON.parse(sessionStorage.getItem('user'));
//   console.log(user);
//   console.log(sessionStorage);
  
//   if (!user && to.path != '/login') {
//     next({
//       path: '/login'
//     });
//   } else {
//     next();
//   }
// });

// 引入路由
import router from "./router.js"
new Vue({
  el: '#app',
  router, // 注入到根实例中
  render: h => h(App)
});