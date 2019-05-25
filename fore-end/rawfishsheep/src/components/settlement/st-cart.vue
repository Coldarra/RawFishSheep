<template>
  <div>
    <div v-loading="this.$store.state.cartLock">
      <div v-for="(cart, id) in this.$store.state.cartList" :key="id">
        <el-row :gutter="20" class="pull-center">
          <el-col :span="6" class="line pull-left">
            <img :src="cart.goods.picture_url" style="height: 5rem;">
            {{ cart.name }}
          </el-col>
          <el-col :span="6">¥ {{ cart.goods.price }}</el-col>
          <el-col :span="6">
            <el-input-number
              v-model="cart.amount"
              :min="1"
              :max="100"
              :step="1"
              label="选择数量"
              @change="Public.changeCartAmount(cart.goods.id,cart.amount)"
            ></el-input-number>
          </el-col>
          <el-col :span="6">
            <!-- <el-button type="success" icon="el-icon-plus" circle></el-button> -->
            <el-button
              type="danger"
              icon="el-icon-delete"
              circle
              @click="Public.removeFromCartList(cart.goods.id)"
            ></el-button>
          </el-col>
        </el-row>
        <hr>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "st-cart",
  data() {
    return {};
  },
  mounted() {
    // setInterval(() => {
    //   console.log(this.$store.state.cartLock);
    // }, 200);
  }
};
</script>

