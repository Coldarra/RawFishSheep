<template>
  <div id="header" class>
    <el-row :gutter="0" class="top-bar pull-center">
      <el-col :span="6" :offset="1">上海市 奉贤区 海湾旅游区 海思路 999号</el-col>
      <el-col :span="1"></el-col>
      <el-col :span="13" class="pull-right">
        <span
          v-show="this.$store.state.isLogin"
          class="color-green"
        >{{ this.$store.state.userInfo.username }}</span>
        <span v-show="this.$store.state.isLogin">&nbsp;&nbsp;&nbsp;</span>
        <router-link v-show="this.$store.state.isLogin" to="/logout" class="color-black">我的账户</router-link>
        <span v-show="this.$store.state.isLogin">&nbsp;&nbsp;&nbsp;</span>
        <router-link v-show="this.$store.state.isLogin" to="/logout" class="color-black">历史订单</router-link>
        <span v-show="this.$store.state.isLogin">&nbsp;&nbsp;&nbsp;</span>
        <router-link v-show="this.$store.state.isLogin" to="/logout" class="color-black">退出登录</router-link>
        
        <span v-show="this.$store.state.userInfo.level=='admin'">&nbsp;&nbsp;&nbsp;</span>
        <router-link
          v-show="this.$store.state.userInfo.level=='admin'"
          to="/backstage/dashboard"
          class="color-black"
        >后台管理</router-link>
        <span v-show="this.$store.state.userInfo.level=='admin'">&nbsp;&nbsp;&nbsp;</span>
        <span v-show="!this.$store.state.isLogin">
          联系电话:
          <i class="el-icon-mobile-phone"></i>+ 1016 1750
        </span>
      </el-col>
      <el-col :span="1"></el-col>
    </el-row>

    <el-row :gutter="20" class="header-bar pull-center" v-show="show_headmenu">
      <el-col :span="7" class="login-button-box">
        <div v-show="!this.$store.state.isLogin">
          <router-link to="/login">
            <el-button type size="medium" round>登录</el-button>
          </router-link>
          <router-link to="/register">
            <el-button type size="medium" round>注册</el-button>
          </router-link>
        </div>
        <div v-show="this.$store.state.isLogin"></div>
      </el-col>
      <el-col :span="2"></el-col>
      <el-col :span="6">
        <img :src="logo" style="height: 100%">
      </el-col>
      <el-col :span="6" :offset="1">
        <el-input
          class="search-box"
          placeholder="搜索商品"
          prefix-icon="el-icon-search"
          v-model="input"
        ></el-input>
      </el-col>
      <el-col :span="2"></el-col>
    </el-row>

    <el-header>
      <el-menu
        :default-active="$route.path"
        class="pull-center"
        mode="horizontal"
        @select="handleSelect"
        v-if="show_headmenu"
        router
      >
        <el-menu-item class="pull-left">
          <router-link to="/">
            <i class="fa fa-home fa-2x"></i>
          </router-link>
        </el-menu-item>
        <el-menu-item index="/">生🐟鱼🐑羊</el-menu-item>
        <!-- <el-menu-item index="1">商品中心</el-menu-item> -->
        <el-submenu index="2">
          <template slot="title">商品分类</template>
          <el-submenu index="2-1">
            <template slot="title">新鲜水果</template>
            <el-menu-item index="2-1-1">苹果</el-menu-item>
            <el-menu-item index="2-1-2">香蕉</el-menu-item>
            <el-menu-item index="2-1-3">草莓</el-menu-item>
          </el-submenu>
          <el-menu-item index="2-2">海鲜水产</el-menu-item>
          <el-menu-item index="2-3">精选肉类</el-menu-item>
          <el-menu-item index="2-4">冷冻饮食</el-menu-item>
          <el-menu-item index="2-5">蔬菜蛋品</el-menu-item>
        </el-submenu>
        <el-menu-item index="3" disabled>消息中心</el-menu-item>
        <el-menu-item index="/order">订单管理</el-menu-item>

        <el-submenu index="5" class="pull-right">
          <template slot="title">
            <i class="fa fa-shopping-cart fa-2x"></i>
          </template>
          <el-menu-item v-for="(item, index) in cartList" :key="index">
            <img :src="item.src" style="height: 2rem;">
            {{ item.name }} / {{ item.price }} / 数量: {{ item.quantity }}
          </el-menu-item>
          <el-menu-item class>
            共计: ¥16.00
            <router-link to="/settlement" class="pull-right settle">立即结算</router-link>
          </el-menu-item>
        </el-submenu>
      </el-menu>
    </el-header>
  </div>
</template>

<style lang="scss">
.pull-left {
  float: left;
  text-align: left;
}
.pull-right {
  float: right;
  text-align: right;
}
.pull-center {
  display: flex;
  align-items: center;
  justify-content: space-around;
  text-align: center;
}
.vertical-center {
  //   display: flex;
  //   align-items: center;
  vertical-align: text-top;
}
.color-black {
  color: black;
}
.price {
  margin-top: 1rem;
  margin-bottom: 0.2rem;
}
.search-box {
  .el-input__inner:focus {
    border-color: #67c23a;
    outline: 0;
  }
}
.login-button-box {
  .el-button:active {
    color: #67c23a;
    border-color: #67c23a;
    outline: 0;
  }
  .el-button:focus,
  .el-button:hover {
    color: #67c23a;
    border-color: #c2e7b0;
    background-color: #f0f9eb;
  }
}
</style>

<style scoped>
.top-bar {
  margin-left: 3%;
  margin-right: 3%;
  height: 2rem;
  font-size: 0.8rem;
  margin-top: 0rem;
  margin-bottom: 0rem;
  background: #f5f6f3;
  /* height: 50px; */
}
.header-bar {
  margin-top: 0.6rem;
  margin-bottom: 0.1rem;
}
.settle {
  color: black;
}
</style>



<script>
// import axios from "axios";

export default {
  name: "app-header",
  //   props: {
  //     cartList: this.cartList
  //   },
  data() {
    return {
      show_headmenu: true,
      logo: require("@/assets/images/logo.png"),
      clientHeight: "",
      activeIndex: "0",
      input: "",
      cartList: [
        {
          src: require("@/assets/products-images/product11.jpg"),
          name: "草莓",
          price: "￥3.00",
          quantity: 4
        },
        {
          src: require("@/assets/products-images/product10.jpg"),
          name: "青椒",
          price: "￥2.00",
          quantity: 2
        }
      ]
    };
  },
  methods: {
    handleSelect(key, keyPath) {
      console.log(key, keyPath);
    }
  },
  mounted() {
    // this.$message({
    //   message: "lalala",
    //   type: "warning",
    //   duration: 0
    // });
    // this.$notify({
    //   title:"title",
    //   message: "lalala",
    //   type: "warning",
    //   duration: 0
    // });
    // this.$ajax.get("/api/user/").then(
    //   res => {
    //     console.log(res);
    //   },
    //   res => {
    //     console.info("调用失败");
    //   }
    // );
  }
};
</script>
