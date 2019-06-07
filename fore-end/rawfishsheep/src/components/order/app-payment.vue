<template>
  <div class="margin10" v-loading="loading">
    <el-card class="box-card" style="height:40vh;">
      <div slot="header" class="clearfix">
        <div class>
          <span class="pull-left" style="font-size:1rem;">{{this.$route.params.orderid}}</span>
          <span class="pull-right">
            <!-- <el-button type="text" style="font-size:1.2rem">{{orderinfo.status|status_filter}}</el-button> -->
          </span>
        </div>
      </div>
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
  delivered: "确认收货",
  confirmed: "订单完成"
};
export default {
  name: "app-payment",
  data() {
    return {
      loading: true,
      orderid: "",
      orderinfo: {}
    };
  },
  filters: {
    status_filter: function(status) {
      if (status_mapping.hasOwnProperty(status)) return status_mapping[status];
      else return "";
    }
  },
  methods: {},
  mounted() {
    this.orderid = this.$route.params.orderid;

    // this.$ajax
    //   .post("/api/order/info", { serialnumber: this.orderid })
    //   .then(res => {
    //     if (res.data.ret == "0") {
    //       console.log(res.data.data);
    //       this.orderinfo = res.data.data.order;
    //     }
    //   });

    this.$message({
      message: "支付中，请稍等",
      type: "info"
    });
    setTimeout(() => {
      this.$ajax
        .post("/api/order/pay", { serialnumber: this.orderid })
        .then(res => {
          if (res.data.ret == "0") {
            this.$message({
              message: "支付成功",
              type: "success"
            });
            this.loading = false;
            console.log(res.data.msg);
          } else {
            setTimeout(() => {
              this.$router.push("/");
            }, 1000);
          }
        });
    }, 2000);
  }
};
</script>
