<template>
    <el-container>
      <el-main>
        <el-carousel indicator-position="none" :interval="500" height="600px">
          <el-carousel-item v-for="(item, index) in slidePic" :key="index">
            <a href="#"><img class="bannerImg" :src="item.src" alt=""></a>
          </el-carousel-item>
        </el-carousel>
      </el-main>
    </el-container>
</template>

<script>
export default {
  name: 'slider',
  data () {
    return {
      slidePic: [
        { src: require('../../assets/images/slide-img1.jpg') },
        { src: require('../../assets/images/slide-img2.jpg') },
        { src: require('../../assets/images/blog-img1.jpg') },
        { src: require('../../assets/images/blog-img2.jpg') }
      ]
    }
  }
}
</script>

<style scoped>
.bannerImg {
  width: 100%;
}
</style>
