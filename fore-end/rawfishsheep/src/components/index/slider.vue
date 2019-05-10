<template>
  <div>
    <el-carousel indicator-position="none" :interval="2500" height="30rem">
      <el-carousel-item>
        <a href="#">
          <div class="banner-image banner-image1"></div>
        </a>
      </el-carousel-item>
      <el-carousel-item>
        <a href="#">
          <div class="banner-image banner-image2"></div>
        </a>
      </el-carousel-item>
    </el-carousel>

    <el-row :gutter="30" class="fabox">
      <el-col :span="6" :xs="12" class="box">
        <div class="truck">
          <div class="box-container">
            <i class="fa fa-truck"></i>&nbsp;&nbsp;|&nbsp;&nbsp;全场29元包邮
          </div>
        </div>
      </el-col>

      <el-col :span="6" :xs="12" class="box">
        <div class="phone">
          <div class="box-container">
            <i class="fa fa-phone"></i>&nbsp;&nbsp;|&nbsp;&nbsp;+ 1016 1750
          </div>
        </div>
      </el-col>

      <el-col :span="6" :xs="12" class="box">
        <div class="wechat">
          <div class="box-container">
            <i class="fa fa-wechat"></i>&nbsp;&nbsp;|&nbsp;&nbsp;移动支付
          </div>
        </div>
      </el-col>
      <el-col :span="6" :xs="12" class="box">
        <div class="ontime">
          <div class="box-container">
            <i class="fa fa-clock-o"></i>&nbsp;&nbsp;|&nbsp;&nbsp;3天质保
          </div>
        </div>
      </el-col>
    </el-row>
  </div>
</template>

<script>
export default {
  name: "slider",
  data() {
    return {
      slidePic: [
        { src: require("@/assets/images/slide-img1.jpg") },
        { src: require("@/assets/images/slide-img2.jpg") }
      ]
    };
  }
};
</script>

<style lang="scss" scoped>
.bannerImg {
  width: 100%;
}
.banner-image {
  width: 100%;
  height: 100%;
  background-repeat: no-repeat;
  background-size: cover;
  background-attachment: scroll;
  background-position: bottom center;
  /* background-size: 300px 200px;  */
  background-color: transparent;
}
.banner-image1 {
  background-image: url(http://cdn.cs161.cn/rfs/img/slide-img1.jpg);
}
.banner-image2 {
  background-image: url(http://cdn.cs161.cn/rfs/img/slide-img2.jpg);
}

.fabox {
  margin-top: 1rem;
  margin-bottom: 1rem;
  font-size: 1.3rem;
  color: white;
  font-family: "Microsoft YaHei";
  i {
    font-size: 2rem;
    vertical-align: middle;
  }
  .box {
    margin-bottom: 1rem;
  }

  .box-container {
    margin-left: 1rem;
    margin-right: 1rem;
    white-space: nowrap;
  }
  .box-border {
    border-left: 1px rgba(255, 255, 255, 0.5) solid;
  }

  .truck {
    border-block-start: 1rem;
    border-radius: 4px;
    background: #685c88;
    min-height: 4rem;
    display: flex;
    align-items: center;
  }
  .phone {
    border-radius: 4px;
    background: #94d7fb;
    min-height: 4rem;
    display: flex;
    align-items: center;
  }
  .wechat {
    border-radius: 4px;
    background: #fc9cc4;
    min-height: 4rem;
    display: flex;
    align-items: center;
  }
  .ontime {
    border-radius: 4px;
    background: #c2e7b0;
    min-height: 4rem;
    display: flex;
    align-items: center;
  }
}
</style>
