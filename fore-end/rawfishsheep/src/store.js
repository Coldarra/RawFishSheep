import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    domain: 'http://test.example.com',
    token: null,
    isLogin: false,
    userInfo: {
      username: null,
      level: null,
      userid: null,
    },
    cartList: [],
    totalPrice: 0,
  },
  getters: {
    // totalPrice: state => {
      // let price = 0;
      // state.cartList.forEach(cart => {
      //   price += cart.price;
      // });
      // console.log("price:", price);
      // return price;
    // }
  },
  mutations: {
    updateUserInfo(state, data) {
      // console.log(data);
      state.isLogin = true;
      state.token = data.token;
      // console.log("updateUserInfo:", data.token);
      localStorage.setItem('token', data.token);
      localStorage.setItem('username', data.user.username);
      localStorage.setItem('level', data.user.level);
      state.userInfo = {
        username: data.user.username,
        level: data.user.level,
        userid: data.user.userid,
      };
    },
    clearUserInfo(state) {
      localStorage.removeItem("token");
      localStorage.removeItem('username');
      localStorage.removeItem('level');
      state.isLogin = false;
      state.token = '';
      state.userInfo = {
        username: null,
        level: null,
        userid: null,
      };
    },
    updateCartList(state, newCartList) {
      console.log(newCartList);
      if (typeof (newCartList) == "object") {
        state.cartList = newCartList;
        localStorage.setItem('cartList', JSON.stringify(newCartList));
      }
      if (typeof (newCartList) == "string") {
        localStorage.setItem('cartList', newCartList);
        state.cartList = JSON.parse(newCartList);
      }

      let price = 0;
      state.cartList.forEach(cart => {
        price += Number(cart.price);
      });
      console.log("price:", price);
      state.totalPrice = price;
    },
    appendToCartList(state, goods) { // goodsid, goodsname, price, count
      for (var i = 0; i < state.cartList.length; i++) {
        // console.log(state.cartList[i].goodsid, goods.id);
        if (state.cartList[i].goodsid == goods.id) {
          state.cartList[i].amount = Number(state.cartList[i].amount) + 1;
          localStorage.setItem('cartList', JSON.stringify(state.cartList));
          return;
        }
      }
      goods["amount"] = 1;
      state.cartList.push(goods)
      localStorage.setItem('cartList', JSON.stringify(state.cartList));
    },
    clearCartList(state) {
      state.cartList = [];
      localStorage.removeItem('cartList');
    },
    removeFromCartList(state, goodsid) {
      for (var i = 0; i < state.cartList.length; i++) {
        if (state.cartList[i].goodsid == goodsid) {
          state.cartList.splice(i, 1);
          break;
        }
      }
    }

  },
  actions: {

  }
})
