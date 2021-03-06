import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    domain: 'http://test.example.com',
    token: '',
    isLogin: false,
    userInfo: {
      username: null,
      level: null,
      userid: null,
    },
    cartList: [],
  },
  getters: {
    totalPrice: state => {
      let price = 0;
      state.cartList.forEach(cart => {
        price += cart.price;
      });
      return price;
    }
  },
  mutations: {
    updateUserInfo(state, data) {
      state.isLogin = true;
      state.token = data.token;
      console.log("updateUserInfo:", data.token);
      
      localStorage.setItem('token', data.token);
      state.userInfo = {
        username: data.user.username,
        level: data.user.level,
        userid: data.user.userid,
      };
    },
    clearUserInfo(state){
      localStorage.setItem("token", "");
      state.isLogin = false;
      state.token = '';
      state.userInfo = {
        username: null,
        level: null,
        userid: null,
      };
    },
    updateCartList(state, newCartList) {
      state.cartList = newCartList;
    },
    appendToCartList(state, goods) { // goodsid, goodsname, price, count
      state.cartList.forEach(cart => {
        if (cart.goodsid == goods.goodsid) {
          cart.count += goods.count;
          return;
        }
      });
      state.cartList.push({
        "goodsid": goods.goodsid,
        "goodsname": goods.goodsname,
        "price": goods.price,
        "count": goods.count,
      })
    },
    clearCartList(state){
      state.cartList = [];
    },
    removeFromCartList(state, goodsid){
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
