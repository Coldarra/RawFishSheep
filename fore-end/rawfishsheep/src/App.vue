<template>
  <div id="app">
    <app-header v-if="headerVisible"></app-header>
    <router-view></router-view>
    <app-footer></app-footer>
  </div>
</template>

<script>
import Header from "@/components/app-header.vue";
import Footer from "@/components/app-footer.vue";

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
        // console.log(this.$route.path.indexOf("backstage"));
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
// .el-message,
// .el-notification {
//   display: -webkit-inline-box;
// }
</style>