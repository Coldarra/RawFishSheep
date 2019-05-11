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

if (process.env.NODE_ENV === 'production')
  axios.defaults.baseURL = "http://coldarra.cn:8848/";
// else
//   axios.defaults.baseURL = 'http://127.0.0.1/';

axios.interceptors.request.use(function (config) {
  // console.log(config.data);
  var token = localStorage.getItem("token");
  // console.log("token:",token);

  if (token) {
    config.headers.common['Authorization'] = token;
  }
  config.data = qs.stringify(config.data);
  console.log(config.data);
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
    if (localStorage.getItem("level") == "admin")
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
      console.log("localStorage:", localStorage.getItem("username"));
      if (localStorage.getItem("username")) {
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


Vue.prototype.Public = {
  checkLogin() {
    const token = localStorage.getItem("token");
    console.log("localStorage", token);
    if (token || store.state.isLogin) {
      axios.post("/api/user/token", {
        token: token
      })
        .then(res => {
          if (res.data.ret == "0") {
            store.commit("updateUserInfo", res.data.data);
          } else {
            store.commit("clearUserInfo");
          }
        });
    }
  },
  fillCartList() {
    const token = localStorage.getItem("token");
    const cartList = localStorage.getItem("cartList");
    if (!token) {
      //如果未登录
      if (cartList) {
        //从localStorage中取出cartList
        store.commit("updateCartList", cartList);
      }
    } else {
      axios.get("/api/cart/all").then(res => {
        if (res.data.ret == "0") {
          store.commit("updateCartList", res.data.data.cart);
        }
      });
    }
  },
  synchronizeCartList() {
    const token = localStorage.getItem("token");
    const cartList = localStorage.getItem("cartList");
    if (token) {
      JSON.parse(cartList).forEach(cart => {
        axios.post("/api/cart/append", {
          goods_id: cart.goods_id,
          amount: cart.amount
        }).then(res => {
          if (res.data.ret == "0") {
            store.commit("updateCartList", res.data.data.cart);
          }
          else {
            Vue.prototype.$message({
              message: "商品" + cart.name + '同步失败',
              type: "warning"
            });
          }
        });
      });
    }
  },
  clearAll() {
    store.commit("clearUserInfo");
    store.commit("clearCartList");
  },
  addToCartList(goods_id, amount = 1) {
    const token = localStorage.getItem("token");
    if (!token) {
      axios.get("/api/goods/info", {
        params: {
          goods_id: goods_id
        }
      }).then(res => {
        if (res.data.ret == "0") {
          store.commit("appendToCartList", res.data.data.goods);
        }
      });
    }
    else {
      axios.post("/api/cart/append", { goods_id: goods_id, amount: amount }).then(res => {
        if (res.data.ret == "0") {
          store.commit("updateCartList", res.data.data.cart);
          Vue.prototype.$message({
            message: "商品成功加入购物车",
            type: "success"
          });
        }
      });
    }
  }
}






new Vue({
  store,
  router,
  render: h => h(App)
}).$mount('#app')
