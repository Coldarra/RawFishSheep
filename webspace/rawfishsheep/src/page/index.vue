<template>
  <div id="body">
    <slider class="unit"></slider>
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
import feature from "./index/feature.vue";
import products from "./index/products.vue";
import slider from "./index/slider.vue";
export default {
  name: "index",
  components: {
    feature: feature,
    products: products,
    slider: slider
  }
};
</script>
