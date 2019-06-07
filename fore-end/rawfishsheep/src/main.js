import Vue from "vue";
import App from "./App.vue";
import store from "./store";
import router from "./router";

import ElementUI from "element-ui";
import "element-ui/lib/theme-chalk/index.css";
import "font-awesome/css/font-awesome.min.css";

// import VueAxios from 'vue-axios'
import axios from "axios";
import qs from "qs";
axios.defaults.headers.post["Content-Type"] =
  "application/x-www-form-urlencoded";

Vue.use(ElementUI);
Vue.use(router);
// Vue.use(qs);
// Vue.use(axios);

Vue.prototype.$ajax = axios;
Vue.prototype.$qs = qs;

Vue.config.productionTip = false;

if (process.env.NODE_ENV === "production")
  axios.defaults.baseURL = "http://coldarra.cn:8848/";
// else
//   axios.defaults.baseURL = 'http://127.0.0.1/';

axios.interceptors.request.use(
  function (config) {
    // console.log(config.data);
    var token = localStorage.getItem("token");
    // console.log("token:",token);

    if (token) {
      config.headers.common["Authorization"] = token;
    }
    config.data = qs.stringify(config.data);
    console.log(config.data);
    return config;
  },
  function (error) {
    return Promise.reject(error);
  }
);
axios.interceptors.response.use(
  function (res) {
    console.log(res);
    if (res.data.ret != "0") {
      switch (res.data.ret) {
        case "10":
          // store.commit("clearUserInfo");
          router.push({
            path: "/login",
            querry: { redirect: router.currentRoute.fullPath } //从哪个页面跳转
          });
          break;
        default:
          break;
      }
      Vue.prototype.$message({
        message: res.data.msg,
        type: "warning"
        // duration: 0,
      });
    }
    else{
      setTimeout(() => {
        if (store.state.isLogin == false)
          Vue.prototype.Public.checkLogin();
      }, 1500);
    }
    return res;
  },
  function () {
    Vue.prototype.$message({
      message: "服务器请求失败",
      type: "error"
      // duration: 0,
    });
  }
);

router.beforeEach((to, from, next) => {
  if (to.meta.requireAdmin) {
    if (localStorage.getItem("level") == "admin") next();
    else {
      next({
        path: "/"
      });
      Vue.prototype.$message({
        message: "无此权限",
        type: "error"
      });
    }
  } else if (to.meta.requireLogin) {
    console.log("localStorage:", localStorage.getItem("username"));
    if (localStorage.getItem("username")) {
      next();
    } else {
      next({
        path: "/login",
        query: { redirect: to.fullPath }
      });
      Vue.prototype.$message({
        message: "请先登录",
        type: "warning"
        // duration: 0,
      });
    }
  } else {
    next();
  }
});

Vue.prototype.Public = {
  checkLogin() {
    const token = localStorage.getItem("token");
    console.log("localStorage", token);
    if (token || store.state.isLogin) {
      axios
        .post("/api/user/token", {
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
    console.log("fillCartList");
    store.commit("lockcart");
    const token = localStorage.getItem("token");
    const cartList = localStorage.getItem("cartList");
    if (!token) {
      //如果未登录
      if (cartList) {
        //从localStorage中取出cartList
        store.commit("updateCartList", cartList);
      }
    } else {
      axios.post("/api/cart/all").then(res => {
        if (res.data.ret == "0") {
          store.commit("updateCartList", res.data.data.cart);
        }
      });
    }
  },
  fillOrderList() {
    axios.post("/api/order/all").then(res => {
      if (res.data.ret == "0") {
        const orderList = res.data.data.order;
        store.commit("updateOrderList", orderList);
        Vue.prototype.$message({
          message: "订单已更新",
          type: "success"
        });
      }
    });
  },
  synchronizeCartList() {
    console.log("synchronizeCartList");
    const token = localStorage.getItem("token");
    const cartList = JSON.parse(localStorage.getItem("cartList"));
    if (token) {
      console.log(cartList);
      if (cartList) {
        cartList.forEach((cart, index) => {
          axios
            .post("/api/cart/append", {
              goods_id: cart.goods_id,
              amount: cart.amount
            })
            .then(res => {
              if (res.data.ret != "0") {
                Vue.prototype.$message({
                  message: "商品" + cart.name + "同步失败",
                  type: "warning"
                });
              }
              if (index == cartList.length - 1) this.fillCartList();
            });
        });
      }
    } else {
      Vue.prototype.$message({
        message: "无效登录信息，请重新登录",
        type: "error"
      });
    }
    this.fillCartList();
  },
  clearAll() {
    store.commit("clearUserInfo");
    store.commit("clearCartList");
  },
  addToCartList(goods_id, amount = 1) {
    console.log("addToCartList", goods_id, amount);
    const token = localStorage.getItem("token");
    if (!token) {
      axios
        .post("/api/goods/info", {
          goods_id: goods_id
        })
        .then(res => {
          if (res.data.ret == "0") {
            store.commit("appendToCartList", res.data.data.goods);
            Vue.prototype.$message({
              message: "商品成功加入购物车",
              type: "success"
            });
          }
        });
    } else {
      store.commit("lockcart");
      axios
        .post("/api/cart/append", { goods_id: goods_id, amount: amount })
        .then(res => {
          if (res.data.ret == "0") {
            Vue.prototype.$message({
              message: "商品成功加入购物车",
              type: "success"
            });
            this.fillCartList();
          }
        });
    }
  },
  changeCartAmount(goods_id, amount) {
    console.log("changeCartAmount", goods_id, amount);
    store.commit("lockcart");
    const token = localStorage.getItem("token");
    if (token) {
      axios
        .post("/api/cart/amount", { goods_id: goods_id, amount: amount })
        .then(res => {
          if (res.data.ret == "0") {
            this.fillCartList();
          } else {
            Vue.prototype.$message({
              message: "商品数量修改失败",
              type: "error"
            });
          }
        });
    } else {
      Vue.prototype.$message({
        message: "未登录",
        type: "error"
      });
    }
  },
  removeFromCartList(goods_id) {
    console.log("removeFromCartList", goods_id);
    store.commit("lockcart");
    const token = localStorage.getItem("token");
    if (!token) {
      store.commit("removeFromCartList", goods_id);
    } else {
      axios.post("/api/cart/delete", { goods_id: goods_id }).then(res => {
        if (res.data.ret == "0") {
          Vue.prototype.$message({
            message: "商品删除成功",
            type: "success"
          });
          // store.commit("updateCartList", res.data.data.cart);
          this.fillCartList();
        }
      });
    }
  },
  getCategory() {
    // axios
    //   .post("/api/goods/category/all", {})
    //   .then(res => {
    //     if (res.data.ret == "0") {
    //       let temp = res.data.data.category;
    //       store.commit("setCategory", temp);
    //       // this.category = [];
    //       // this.category.push(temp);
    //       console.log("MAIN.JS", temp);
    //       return;
    //     }
    //   })
    //   .catch(error => {
    //     console.log(error);
    //   });

    return new Promise((resolve, reject) => {
      axios
        .post("/api/goods/category/all", {})
        .then(res => {
          if (res.data.ret == "0") {
            let temp = res.data.data.category;
            store.commit("setCategory", temp);
            // this.category = [];
            // this.category.push(temp);
            console.log("MAIN.JS", temp);
            resolve(temp);
          }
        })
        .catch(error => {
          console.log(error);
          reject(error);
        });
    });
  }
};

new Vue({
  store,
  router,
  render: h => h(App)
}).$mount("#app");
