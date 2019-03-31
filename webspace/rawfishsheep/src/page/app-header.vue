<template>
  <div>
    <div class="header-container">
      <div class="header-top">
        <div class="container">
          <dir class="row">
            <div class="col-6">
              <div class>111</div>
            </div>
            <div class="col-6">
              <div class="float-right">
                <ul class="nav">
                  <li class="nav-item" v-for="(item,i) in head_bar.items" :key="i">
                    <a :href="item.link" class="nav-link text-white">{{ item.message }}</a>
                  </li>
                </ul>
              </div>
            </div>
          </dir>
        </div>
      </div>
      <div></div>
    </div>header123
  </div>
</template>

<style lang="scss">
.header-container {
  height: 30px;
  color: aliceblue;
  background-color: black;
}

</style>


<script>
export default {
  name: "app-header",
  data() {
    return {
      head_bar: {
        items: [
          { message: "xxx", link: "/" },
          { message: "登录", link: "/login" },
          { message: "注册", link: "/register" }
        ]
      }
    };
  }
};
</script>

