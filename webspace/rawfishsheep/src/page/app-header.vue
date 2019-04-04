<template>
  <div id="header">
    <el-header>

        <!-- <el-row :gutter="20">
          <el-col :span="6">
            <div class>123</div>
          </el-col>
          <el-col :span="6">
            <div class>123</div>
          </el-col>
          <el-col :span="6">
            <div class>123</div>
          </el-col>
          <el-col :span="6">
            <div class>123</div>
          </el-col>
        </el-row> -->
    

            <el-menu
              :default-active="activeIndex"
              class="el-menu24emo"
              mode="horizontal"
              @select="handleSelect"
            >
            <el-menu-item style="width:50px"><i>LOGO</i></el-menu-item>
              <el-menu-item index="0">生🐟鱼🐑羊</el-menu-item>
              <el-menu-item index="1">处理中心</el-menu-item>
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
            </el-menu>


    </el-header>
  </div>
</template>

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