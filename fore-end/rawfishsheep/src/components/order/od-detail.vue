<template>
  <div>{{this.$route.params.orderid}}</div>
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
    this.$ajax.get("/api/order/info", { orderid: this.order }).then(res => {
      if (res.data.ret == "0") {
        console.log(res.data.data);
        this.orderinfo = res.data.data.order;
      }
    });
  }
};
</script>

