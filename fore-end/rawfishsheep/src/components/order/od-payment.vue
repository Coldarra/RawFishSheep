<template>
  <div>


  </div>
</template>

<script>
export default {
  name: "od-payment",
  data() {
    return {
      orderid: "",
      orderinfo: {}
    };
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
