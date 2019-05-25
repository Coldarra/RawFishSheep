<template>
  <div id="bs">
    <el-row>
      <el-col :span="4">
        <el-menu
          :default-active="$route.path"
          class="bs-menu"
          @open="handleOpen"
          @close="handleClose"
          id="profile-bar"
          router
        >
          <div class="pull-center" id="profile-logo">
            <img :src="logo" style="height: 100%">
          </div>
          <el-submenu index="/backstage">
            <template slot="title">
              <i class="el-icon-location"></i>
              <span>报表</span>
            </template>
            <el-menu-item-group>
              <template slot="title">仪表盘</template>
              <el-menu-item index="/backstage/dashboard">仪表盘</el-menu-item>
              <el-menu-item index="/backstage/dashboard2">销售报表</el-menu-item>
            </el-menu-item-group>
            <el-menu-item-group title="订单报表">
              <el-menu-item index="1-3">选项3</el-menu-item>
            </el-menu-item-group>
            <el-submenu index="1-4">
              <template slot="title">选项4</template>
              <el-menu-item index="1-4-1">选项1</el-menu-item>
            </el-submenu>
          </el-submenu>

          <el-menu-item index="/backstage/goods">
            <i class="el-icon-menu"></i>
            <span slot="title">商品管理</span>
          </el-menu-item>
          <el-menu-item index="/backstage/c" disabled>
            <i class="el-icon-document"></i>
            <span slot="title">仓库管理</span>
          </el-menu-item>
          <el-menu-item index="/backstage/user">
            <i class="el-icon-news"></i>
            <span slot="title">会员管理</span>
          </el-menu-item>
          <el-menu-item index="/backstage/setting">
            <i class="el-icon-setting"></i>
            <span slot="title">设置</span>
          </el-menu-item>
          <br>
          <el-menu-item index="/">
            <i class="el-icon-back"></i>
            <span>返回</span>
          </el-menu-item>
        </el-menu>
        <div class="bs-menu-blank">&nbsp;</div>
      </el-col>
      <el-col :span="20">
        <div id="bs-content">
          <router-view></router-view>
        </div>
      </el-col>
    </el-row>
  </div>
</template>

<style lang="scss" scoped>
#bs {
  background-color: #f6f7fb;
}
#bs-content {
  margin-left: 3rem;
  margin-right: 3rem;
  margin-top: 1rem;
  margin-bottom: 3rem;
}
.bs-menu {
  position: fixed;
  z-index: 999;
  min-width: 250px;
}
.bs-menu-blank {
  z-index: -999;
  min-width: 250px;
}
</style>
<style lang="scss">
#profile-bar {
  min-height: 50rem;
  //   margin-left: 10%;
  //   margin-right: 10%;
  #profile-logo {
    margin-top: 1rem;
    margin-bottom: 1rem;
  }
  //   .el-menu-item-group__title {
  //     color: #e9e9eb;
  //   }
  //   .el-menu-item i {
  //     color: #ffc060;
  //   }
  //   .el-submenu__title i {
  //     color: #ffc060;
  //   }
}
</style>



<script>
export default {
  name: "bs-index",

  data() {
    return {
      logo: require("@/assets/images/logo.png")
    };
  },
  methods: {
    handleOpen() {},
    handleClose() {}
  }
};
</script>
