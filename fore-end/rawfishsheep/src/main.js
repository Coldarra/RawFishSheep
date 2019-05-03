import Vue from 'vue'
import App from './App.vue'
import store from './store'
import router from './router'

import ElementUI from 'element-ui';
import 'element-ui/lib/theme-chalk/index.css';
import 'font-awesome/css/font-awesome.min.css';

// import VueAxios from 'vue-axios'
import axios from 'axios'


Vue.use(ElementUI);
Vue.use(router);
// Vue.use(axios);

Vue.prototype.$ajax = axios;

Vue.config.productionTip = false;

new Vue({
  store,
  router,
  render: h => h(App)
}).$mount('#app')

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
    if (to.meta.requireAuth) {
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
          duration: 0,
        });
      }
    }
    else {
      next();
    }
})
