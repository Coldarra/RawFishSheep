<template>
  <div class="head_background">
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
                    <router-link :to="item.link" class="nav-link text-white">{{ item.message }}</router-link>
                  </li>
                </ul>
              </div>
            </div>
            <div class="clearfix"></div>
          </dir>
        </div>
      </div>
      <div class="container">
        <div class="row">
          <div class="col-4 header-phone d-none d-lg-block">
            <i class="fa fa-mobile"></i> + 1016 1750
          </div>
          <div class="col-4 logo-block">
            <!-- Header Logo -->
            <div class="logo">
              <a title="Freshia Basket" href="/">
                <img alt="Freshia" src="../assets/images/logo1.png">
              </a>
            </div>
            <!-- End Header Logo -->
          </div>

          <div class="col-3 offset-1 d-none d-lg-block">
            <div class="search-box">
              <form action="cat" method="POST" id="search_mini_form" name="Categories">
                <input
                  type="text"
                  placeholder="Search entire store here..."
                  value="Search"
                  maxlength="70"
                  name="search"
                  id="search"
                  class="search-block"
                >
                <button type="button" class="search-btn-bg">
                  <i class="fa fa-search search-icon"></i>&nbsp;
                </button>
              </form>
            </div>
          </div>
        </div>
      </div>
      <div></div>
    </div>
    <nav>
      <div class="container">
        <div class="mm-toggle-wrap">
          <div class="mm-toggle">
            <i class="fa fa-align-justify"></i>
            <span class="mm-label">Menu</span>
          </div>
        </div>
      </div>
    </nav>header
  </div>
</template>

<style lang="scss">
// #header {
//   background: #000 url("../images/footer-bg.jpg") no-repeat center center;
//   height: 187px;
// }
.head_background {
  background: url("../assets/images/footer-bg.jpg") no-repeat center center;
  height: 187px;
}
.header-container {
  height: auto;
  color: aliceblue;
  .header-top {
    padding: 2px 0px 10px 0px;
    background: #111;
    height: 40px;
  }
  .header-phone {
    font-size: 20px;
    color: #fff;
    font-family: "Rubik", sans-serif;
    padding-top: 34px;
    font-weight: normal;
    line-height: 32px;
  }
  .logo-block {
    text-align: center;
    .logo {
      vertical-align: middle;
      text-align: center;
      display: inline-block;
      margin-top: 27px;
      margin-bottom: 20px;
    }
  }
  .search-box {
    margin: auto;
    right: 0px;
    background: none;
    border-radius: 3px;
    margin: 30px 0px;
    border: none;
    border: 2px rgba(255, 255, 255, 0.9) solid;
    .search-block {
      margin: 0;
      width: 200px;
      font-size: 13px;
      height: 45px;
      color: #fff;
      padding: 0 20px;
      background: none;
      outline: none;
      border: none;
      letter-spacing: 0.5px;
      font-weight: 300;
      color: rgba(255, 255, 255, 0.9);
    }
    .search-btn-bg {
      position: absolute;
      padding: 6px 3px;
      cursor: pointer;
      display: inline-block;
      background: none;
      position: absolute;
      outline: none;
      box-shadow: none;
      border: none;
      height: 45px;
      right: 15px;
      font-size: 20px;
      border-left: none;
      padding-left: 14px;
      width: 45px;
      border-radius: 3px;

      .search-icon {
        font-size: 16px;
        color: #59b210;
      }
    }
  }
}

form {
  display: block;
  margin-top: 0em;
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

