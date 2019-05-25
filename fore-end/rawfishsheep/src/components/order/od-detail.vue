<template>
  <div class="margin10">
    <!-- {{this.$route.params.orderid}} -->

    <el-card class="box-card">
      <div slot="header" class="clearfix">
        <span>卡片名称</span>
      </div>
      <div class></div>
    </el-card>
  </div>
</template>

<script>
export default {
  name: "od-detail",
  orderid: "",
  orderinfo: {},
  data() {
    return {};
  },
  mounted() {
    this.orderid = this.$route.params.orderid;
    this.$ajax.post("/api/order/info", { order_id: this.orderid }).then(res => {
      if (res.data.ret == "0") {
        console.log(res.data.data);
        this.orderinfo = res.data.data.order;
      }
    });
  }
};
</script>

