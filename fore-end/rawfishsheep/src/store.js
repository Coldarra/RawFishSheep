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
    updateTotalPrice(state){
      let price = 0;
      console.log(state.cartList);
      
      state.cartList.forEach(cart => {
        console.log(cart);
        price += Number(cart.price) * Number(cart.amount);
      });
      console.log("price:", price);
      state.totalPrice = price;
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
      this.commit("updateTotalPrice");
    },
    appendToCartList(state, goods) { // goods_id, goodsname, price, count
      for (var i = 0; i < state.cartList.length; i++) {
        // console.log(state.cartList[i].goods_id, goods.id);
        if (state.cartList[i].goods_id == goods.id) {
          state.cartList[i].amount = Number(state.cartList[i].amount) + 1;
          localStorage.setItem('cartList', JSON.stringify(state.cartList));
          this.commit("updateTotalPrice");
          return;
        }
      }
      goods["amount"] = 1;
      state.cartList.push(goods)
      localStorage.setItem('cartList', JSON.stringify(state.cartList));
      this.commit("updateTotalPrice");
    },
    clearCartList(state) {
      state.cartList = [];
      localStorage.removeItem('cartList');
      this.commit("updateTotalPrice");
    },
    removeFromCartList(state, goods_id) {
      console.log("removeFromCartList");
      for (var i = 0; i < state.cartList.length; i++) {
        if (state.cartList[i].goods_id == goods_id) {
          state.cartList.splice(i, 1);
          // console.log("removeFromCartList",state.cartList);
          localStorage.setItem('cartList', JSON.stringify(state.cartList));
          this.commit("updateTotalPrice");
          return;
        }
      }
    }

  },
  actions: {

  }
})
