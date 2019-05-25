<template>
  <div id="body">
    <slider class="unit"></slider>
    <el-row :gutter="20">
      <el-col :span="6" :offset="3">
        <el-button :plain="true" @click="Public.addToCartList(1)">添加法兰西大粗黄瓜</el-button>
      </el-col>
      <el-col :span="6">
        <el-button :plain="true" @click="Public.addToCartList(2)">添加德国大香肠</el-button>
      </el-col>
      <el-col :span="6">
        <el-button :plain="true" @click="Public.addToCartList(3)">添加新西兰大香蕉</el-button>
      </el-col>
    </el-row>
    <feature class="unit"></feature>
    <products class="unit"></products>
  </div>
</template>

<style scoped>
#body {
  padding-left: 5%;
  padding-right: 5%;
}
.unit {
  padding-top: 1rem;
  padding-bottom: 1rem;
}
</style>

<script>
import feature from "@/components/index/feature.vue";
import products from "@/components/index/products.vue";
import slider from "@/components/index/slider.vue";
export default {
  name: "index",
  components: {
    feature: feature,
    products: products,
    slider: slider
  }
};
</script>
