import Vue from 'vue'
import App from './App.vue'
import store from './store'
import router from './router'

import ElementUI from 'element-ui';
import 'element-ui/lib/theme-chalk/index.css';
import 'font-awesome/css/font-awesome.min.css';

// import VueAxios from 'vue-axios'
import axios from 'axios'
import qs from 'qs'
axios.defaults.headers.post['Content-Type'] = 'application/x-www-form-urlencoded';


Vue.use(ElementUI);
Vue.use(router);
// Vue.use(qs);
// Vue.use(axios);

Vue.prototype.$ajax = axios;
Vue.prototype.$qs = qs;

Vue.config.productionTip = false;


axios.interceptors.request.use(function (config) {
  // console.log(config.data);
  config.data = qs.stringify(config.data);
  // console.log(config.data);
  return config;
}, function (error) {

  return Promise.reject(error);
});
axios.interceptors.response.use(function (res) {
  console.log(res);
  if (res.data.ret != '0') {
    switch (res.data.ret) {
      case '10':
        router.push({
          path: "/login",
          querry: { redirect: router.currentRoute.fullPath }//从哪个页面跳转
        });
        break;
      default:
        break;
    }
    Vue.prototype.$message({
      message: res.data.msg,
      type: 'warning',
      // duration: 0,
    });
  }

  return res;
}, function (error) {
  // 对响应错误做点什么
  return Promise.reject(error);
});



router.beforeEach((to, from, next) => {
  if (to.meta.requireAdmin) {
    if (store.state.userInfo.level == "admin")
      next()
    else {
      next({
        path: '/',
      });
      Vue.prototype.$message({
        message: '无此权限',
        type: 'error'
      });
    }
  }
  else
    if (to.meta.requireLogin) {
      if (store.state.isLogin) {
        next();
      }
      else {
        next({
          path: '/login',
          query: { redirect: to.fullPath }
        });
        Vue.prototype.$message({
          message: '请先登录',
          type: 'warning',
          // duration: 0,
        });
      }
    }
    else {
      next();
    }
})


new Vue({
  store,
  router,
  render: h => h(App)
}).$mount('#app')
