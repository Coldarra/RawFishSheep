<template>
  <div class="margin10">
    <state_page :orderinfo="orderinfo" :deliveryinfo="deliveryinfo"></state_page>
  </div>
</template>

<script>
const status_mapping = {
  unprocessed: "待支付",
  processing: "系统准备中",
  examining: "订单审核中",
  preparing: "备货中",
  delivering: "配送中",
  delivered: "配送完成",
  confirmed: "订单完成"
};
import state_page from "./od-state.vue";

export default {
  name: "od-detail",
  components: {
    state_page
  },
  data() {
    return {
      serialnumber: "",
      orderinfo: {},
      deliveryinfo: {
        createtime: "",
        finishtime: ""
      }
    };
  },
  mounted() {
    function checkstatus(status) {
      // console.log("checkstatus", status);
      var status_array = ["delivering", "delivered", "confirmed"];
      var res = false;
      status_array.forEach(s => {
        // console.log(s, status, s == status);
        if (s == status) res = true;
      });
      return res;
    }
    this.serialnumber = this.$route.params.orderid;
    console.log(this.serialnumber);
    this.$ajax
      .post("/api/order/info", { serialnumber: this.serialnumber })
      .then(res => {
        if (res.data.ret == "0") {
          console.log(res.data.data);
          this.orderinfo = res.data.data.order;
          if (checkstatus(this.orderinfo.status)) {
            this.$ajax
              .post("/api/order/delivery/info", {
                serialnumber: this.serialnumber
              })
              .then(res => {
                if (res.data.ret == "0") {
                  console.log(res.data.data);
                  this.deliveryinfo = res.data.data.delivery;
                } else {
                }
              });
          }
        } else {
          this.$router.go(-1);
        }
      });
  }
};
</script>

