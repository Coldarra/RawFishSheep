<template>
  <div id="header">
    <el-row type="flex" justify="center" :gutter="20" class="header-bar">
      <div class>123</div>
      <div class>123</div>
      <div class>123</div>
      <div class>123</div>
    </el-row>

    <el-header>
      <el-menu
        :default-active="activeIndex"
        class="el-menu24emo pull-center"
        mode="horizontal"
        @select="handleSelect"
      >
        <el-menu-item class="pull-left">
          <i>
            <i class="fa fa-home fa-2x"></i>
          </i>
        </el-menu-item>
        <el-menu-item index="0">生🐟鱼🐑羊</el-menu-item>
        <!-- <el-menu-item index="1">商品中心</el-menu-item> -->
        <el-submenu index="2">
          <template slot="title">商品分类</template>
          <el-menu-item index="2-1">分类1</el-menu-item>
          <el-menu-item index="2-2">分类2</el-menu-item>
          <el-menu-item index="2-3">分类3</el-menu-item>
          <el-submenu index="2-4">
            <template slot="title">分类4</template>
            <el-menu-item index="2-4-1">选项1</el-menu-item>
            <el-menu-item index="2-4-2">选项2</el-menu-item>
            <el-menu-item index="2-4-3">选项3</el-menu-item>
          </el-submenu>
        </el-submenu>
        <el-menu-item index="3" disabled>消息中心</el-menu-item>
        <el-menu-item index="4">
          <a href="https://www.ele.me" target="_blank">订单管理</a>
        </el-menu-item>

        <el-submenu index="5" class="pull-right">
          <template slot="title">
            <i class="fa fa-shopping-cart fa-2x"></i>
          </template>
          <el-menu-item index="2-1">商品1</el-menu-item>
          <el-menu-item index="2-2">商品2</el-menu-item>
          <el-menu-item index="2-3">商品3</el-menu-item>
        </el-submenu>
      </el-menu>
    </el-header>
  </div>
</template>

<style scoped>
.pull-left {
  float: left;
}
.pull-right {
  float: right;
}
.pull-center{
    display: flex;
    justify-content: space-around;
}
.header-bar {
  height: 100px;
}
</style>


<script>
export default {
  name: "app-header",

  data() {
    return {
      clientHeight: "",
      activeIndex: "0"
    };
  },
  methods: {
    handleSelect(key, keyPath) {
      console.log(key, keyPath);
    }
  }
};
</script>