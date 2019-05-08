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
    },
    checkLogin() {
      var token = localStorage.getItem("token");
      console.log("localStorage", token);
      if (token && this.$store.state.isLogin == false) {
        this.$ajax
          .post("/api/user/token", {
            token: token
          })
          .then(res => {
            if (res.data.ret == "0") {
              this.$store.commit("updateUserInfo", res.data.data);
            } else {
              this.$store.commit("clearUserInfo");
            }
          });
      }
    }
  },
  mounted() {
    this.toggleHeader();
    this.checkLogin();
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