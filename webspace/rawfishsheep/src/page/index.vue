<template>
  <div>
    <slider></slider>
    <feature></feature>
    <products></products>
  </div>
</template>

<script>
import feature from "./index/feature.vue";
import products from "./index/products.vue";
import slider from "./index/slider.vue";
export default {
  name: "index",
  components: {
    feature: feature,
    products: products,
    slider: slider,
  }
};
</script>
