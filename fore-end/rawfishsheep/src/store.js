import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

const order_example = {
  id: 6,
  user: "test",
  address: "上海市奉贤区海思路999号",
  totalprice: 300,
  discount: 1,
  createtime: "2019/04/13 18:14:12",
  finishtime: "",
  paymentname: "货到付款",
  isrefund: "0",
  isdelete: "0",
  status: "confirmed",
  detail: [
    {
      id: 1,
      order: 6,
      goods_id: 1,
      amount: 1,
      goods: {
        id: 1,
        goods_id: 1,
        category: "null",
        name: "法兰西大粗黄瓜",
        unit: "根",
        status: "1",
        price: "1.00",
        remain: 1000,
        picture_url: "/static/img/goods/1.jpg",
        isdelete: "0"
      },
      price: "¥ 3.00",
      isdelete: "0"
    }
  ]
};

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
    searchbox:"",
    searchRegExp: /$/,
    cartLock: false,
    cartList: [],
    orderListLock: true,
    orderList: [
      order_example,
      order_example,
      order_example,
      order_example,
      order_example,
      order_example
    ],
    totalPrice: 0,
    category: []
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
    lockcart(state) {
      state.cartLock = true;
      // console.log("lock cart", state.lock);
    },
    unlockcart(state) {
      state.cartLock = false;
      // console.log("unlock cart", state.lock);
    },
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
      state.cartLock = false;
      state.orderListLock = true;
      state.token = '';
      state.userInfo = {
        username: null,
        level: null,
        userid: null,
      };
    },
    updateTotalPrice(state) {
      var price = 0;
      console.log(state.cartList);
      state.cartList.forEach(cart => {
        // console.log(cart);
        price += Number(cart.price) * Number(cart.amount);
      });
      console.log("price:", price);
      state.totalPrice = price;
      this.commit('unlockcart')
    },
    updateOrderList(state, orderList){
      function sortOrderList(a, b) {
        return b.id - a.id;
      }
      console.log("updateOrderList");
      orderList.sort(sortOrderList);
      state.orderList = orderList;
      state.orderListLock=false;
    },
    updateCartList(state, newCartList) {
      function sortCartList(a, b) {
        return a.id - b.id;
      }
      if (typeof (newCartList) == "object") {
        newCartList.sort(sortCartList);
        console.log("sort end");
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
      localStorage.setItem('cartList', JSON.stringify(state.cartList));
      this.commit("updateTotalPrice");
    },
    removeFromCartList(state, goods_id) {
      this.commit("lockcart");
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
    },
    setCategory(state, ctg) {
      state.category = ctg;
      console.log("STORE.JS", ctg);
      // this.commit("updateCategory");
    },
    setSearchBox(state,content){
      state.searchbox = content;
      console.log("setSearchBox", content);
    },
    setSearchRegExp(state, regExp){
      state.searchRegExp = regExp;
      console.log("setSearchBox", regExp);
    }
  },
  actions: {

  }
})
