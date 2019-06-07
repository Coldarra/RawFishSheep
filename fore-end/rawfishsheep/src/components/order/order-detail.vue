<template>
  <div class="margin10">
    <el-card class="box-card">
      <div slot="header" class="clearfix">
        <div class>
          <span class="pull-left" style="font-size:1rem;">{{this.$route.params.orderid}}</span>
          <span class="pull-right">
            <el-button type="text" style="font-size:1.2rem">{{orderinfo.status|status_filter}}</el-button>
          </span>
        </div>
      </div>
      <state_page :orderinfo="orderinfo" :deliveryinfo="deliveryinfo"></state_page>
      <hr>
      <span v-if="orderinfo.status=='unprocessed'">
        <payment_page :orderinfo="orderinfo"></payment_page>
        <hr>
      </span>
      <address_page :orderinfo="orderinfo" :deliveryinfo="deliveryinfo"></address_page>
      <hr>
      <goods_page :orderinfo="orderinfo"></goods_page>
    </el-card>
  </div>
</template>

<script>
const status_mapping = {
  unprocessed: "订单待支付",
  processing: "系统准备中",
  examining: "订单审核中",
  preparing: "备货中",
  delivering: "配送中",
  delivered: "配送完成",
  confirmed: "订单完成"
};
import state_page from "./od-state.vue";
import goods_page from "./od-goods.vue";
import address_page from "./od-address.vue";
import payment_page from "./od-payment.vue";

export default {
  name: "order-detail",
  components: {
    state_page,
    goods_page,
    address_page,
    payment_page
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
  filters: {
    status_filter: function(status) {
      if (status_mapping.hasOwnProperty(status)) return status_mapping[status];
      else return "";
    }
  },
  methods: {
    checkStatus(status) {
      // console.log("checkstatus", status);
      var status_array = ["delivering", "delivered", "confirmed"];
      var res = false;
      status_array.forEach(s => {
        // console.log(s, status, s == status);
        if (s == status) res = true;
      });
      return res;
    },
    getOrderInfo() {
      this.$ajax
        .post("/api/order/info", { serialnumber: this.serialnumber })
        .then(res => {
          if (res.data.ret == "0") {
            console.log(res.data.data);
            this.orderinfo = res.data.data.order;
            if (this.checkStatus(this.orderinfo.status)) {
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
  },

  mounted() {
    this.serialnumber = this.$route.params.orderid;
    console.log(this.serialnumber);
    // this.getOrderInfo();
    const _this = this;
    _this.getOrderInfo();
    setInterval(function() {
      _this.getOrderInfo();
    }, 5000);
  }
};
</script>

