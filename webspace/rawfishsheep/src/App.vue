<template>
  <div id="app">
    <app-header></app-header>
    <router-view></router-view>
    <app-footer></app-footer>
  </div>
</template>

<script>
cartList = [
  {
    src: require("../assets/products-images/product11.jpg"),
    name: "草莓",
    price: "￥3.00",
    quantity: 4
  },
  {
    src: require("../assets/products-images/product10.jpg"),
    name: "青椒",
    price: "￥2.00",
    quantity: 2
  }
];
import Header from "./page/app-header.vue";
import Footer from "./page/app-footer.vue";
export default {
  name: "App",
  components: {
    "app-header": Header,
    "app-footer": Footer
  }
};

// console.log(Header,Footer);
</script>

<style lang="scss">
  
// body {
//     margin-left: 15%;
//     margin-right: 15%;
// }

// #app {
//     position: absolute;
//     top: 0;
//     bottom: 0;
//     width: 100%;
// }

// .el-submenu [class^=fa] {
//     vertical-align: baseline;
//     margin-right: 10px;
// }

// .el-menu-item [class^=fa] {
//     vertical-align: baseline;
//     margin-right: 10px;
// }
</style>