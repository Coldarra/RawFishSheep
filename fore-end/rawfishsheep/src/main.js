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
Vue.use(axios);

Vue.prototype.$ajax = axios;

Vue.config.productionTip = false;

new Vue({
  store,
  router,
  render: h => h(App)
}).$mount('#app')
