<template>
  <div class="margin10">
    <el-card class="box-card">
      <div slot="header" class="clearfix">
        <span>{{this.$route.params.orderid}}</span>
        <hr>
        <el-steps :active="3" align-center finish-status="success" process-status="finish">
          <el-step
            title="提交订单"
            icon="fa fa-2x fa-pencil-square-o"
            description="2019/05/23 23:15:59"
          ></el-step>
          <el-step title="付款成功" icon="fa fa-2x fa-credit-card" description="2019/05/23 23:15:59"></el-step>
          <el-step title="商品出库" icon="fa fa-2x fa-envelope-open-o" description="2019/05/23 23:15:59"></el-step>
          <el-step title="配送中" icon="fa fa-2x fa-pulse fa-spinner" description="2019/05/23 23:15:59"></el-step>
          <!-- <el-step title="配送中" icon="fa fa-2x fa-truck" description="2019/05/23 23:15:59"></el-step> -->
          <el-step
            title="确认收货"
            icon="fa fa-2x fa-check-circle-o"
            description="2019/05/23 23:15:59"
          ></el-step>
          <!-- <el-step
            title="确认收货"
            icon="fa fa-2x fa-pulse fa-spinner"
            description="2019/05/23 23:15:59"
          ></el-step> -->
        </el-steps>
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

