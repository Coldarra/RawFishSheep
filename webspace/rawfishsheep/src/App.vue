<template>
  <div id="app">
    <app-header v-if="headerVisible"></app-header>
    <router-view></router-view>
    <app-footer></app-footer>
  </div>
</template>

<script>
import Header from "./page/app-header.vue";
import Footer from "./page/app-footer.vue";
export default {
  name: "App",
  components: {
    "app-header": Header,
    "app-footer": Footer
  },
  data() {
    return {
      headerVisible: true
    };
  },
  watch: {
    $route: "toggleHeader"
  },
  methods: {
    toggleHeader() {
      if (this.$route.path.indexOf("backstage") != -1) {
        this.headerVisible = false;
        console.log(this.$route.path.indexOf("backstage"));
      } else {
        this.headerVisible = true;
      }
    }
  },
  mounted() {
    this.toggleHeader();
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