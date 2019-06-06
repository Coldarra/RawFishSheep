<template>
  <div>
    <div style="margin-top:1rem">
      <div>
        <span v-if="orderinfo.status=='unprocessed'">
          <el-steps :active="1" align-center finish-status="success" process-status="finish">
            <el-step title="提交订单" icon="fa fa-2x fa-pencil-square-o" :description="orderinfo.createtime"></el-step>
            <el-step title="待付款" icon="fa fa-2x fa-pulse fa-spinner" :description="orderinfo.paidtime"></el-step>
            <el-step title="商品出库" icon="fa fa-2x fa-envelope-open-o" :description="deliveryinfo.createtime"></el-step>
            <el-step title="等待收货" icon="fa fa-2x fa-truck" :description="deliveryinfo.finishtime"></el-step>
            <el-step title="确认收货" icon="fa fa-2x fa-check-circle-o" :description="orderinfo.finishtime"></el-step>
          </el-steps>
        </span>
        <span v-else-if="orderinfo.status=='processing'||orderinfo.status=='examining'">
          <el-steps :active="2" align-center finish-status="success" process-status="finish">
            <el-step title="提交订单" icon="fa fa-2x fa-pencil-square-o" :description="orderinfo.createtime"></el-step>
            <el-step title="已付款" icon="fa fa-2x fa-credit-card" :description="orderinfo.paidtime"></el-step>
            <el-step title="商品出库" icon="fa fa-2x fa-pulse fa-spinner" :description="deliveryinfo.createtime"></el-step>
            <el-step title="等待收货" icon="fa fa-2x fa-truck" :description="deliveryinfo.finishtime"></el-step>
            <el-step title="确认收货" icon="fa fa-2x fa-check-circle-o" :description="orderinfo.finishtime"></el-step>
          </el-steps>
        </span>
        <span v-else-if="orderinfo.status=='preparing'||orderinfo.status=='delivering'">
          <el-steps :active="3" align-center finish-status="success" process-status="finish">
            <el-step title="提交订单" icon="fa fa-2x fa-pencil-square-o" :description="orderinfo.createtime"></el-step>
            <el-step title="已付款" icon="fa fa-2x fa-credit-card" :description="orderinfo.paidtime"></el-step>
            <el-step title="商品出库" icon="fa fa-2x fa-envelope-open-o" :description="deliveryinfo.createtime"></el-step>
            <el-step title="等待收货" icon="fa fa-2x fa-pulse fa-spinner" :description="deliveryinfo.finishtime"></el-step>
            <el-step title="确认收货" icon="fa fa-2x fa-check-circle-o" :description="orderinfo.finishtime"></el-step>
          </el-steps>
        </span>
        <span v-else-if="orderinfo.status=='delivered'">
          <el-steps :active="4" align-center finish-status="success" process-status="finish">
            <el-step title="提交订单" icon="fa fa-2x fa-pencil-square-o" :description="orderinfo.createtime"></el-step>
            <el-step title="已付款" icon="fa fa-2x fa-credit-card" :description="orderinfo.paidtime"></el-step>
            <el-step title="商品出库" icon="fa fa-2x fa-envelope-open-o" :description="deliveryinfo.createtime"></el-step>
            <el-step title="等待收货" icon="fa fa-2x fa-truck" :description="deliveryinfo.finishtime"></el-step>
            <el-step title="确认收货" icon="fa fa-2x fa-pulse fa-spinner" :description="orderinfo.finishtime"></el-step>
          </el-steps>
        </span>
        <span v-else-if="orderinfo.status=='confirmed'">
          <el-steps :active="5" align-center finish-status="success" process-status="finish">
            <el-step title="提交订单" icon="fa fa-2x fa-pencil-square-o" :description="orderinfo.createtime"></el-step>
            <el-step title="已付款" icon="fa fa-2x fa-credit-card" :description="orderinfo.paidtime"></el-step>
            <el-step title="商品出库" icon="fa fa-2x fa-envelope-open-o" :description="deliveryinfo.createtime"></el-step>
            <el-step title="等待收货" icon="fa fa-2x fa-truck" :description="deliveryinfo.finishtime"></el-step>
            <el-step title="确认收货" icon="fa fa-2x fa-check-circle-o" :description="orderinfo.finishtime"></el-step>
          </el-steps>
        </span>
        <span v-else>
          <el-steps :active="-1" align-center finish-status="success" process-status="finish">
            <el-step title="提交订单" icon="fa fa-2x fa-pencil-square-o" :description="orderinfo.createtime"></el-step>
            <el-step title="已付款" icon="fa fa-2x fa-credit-card" :description="orderinfo.paidtime"></el-step>
            <el-step title="商品出库" icon="fa fa-2x fa-envelope-open-o" :description="deliveryinfo.createtime"></el-step>
            <el-step title="等待收货" icon="fa fa-2x fa-truck" :description="deliveryinfo.finishtime"></el-step>
            <el-step title="确认收货" icon="fa fa-2x fa-check-circle-o" :description="orderinfo.finishtime"></el-step>
          </el-steps>
        </span>
      </div>
    </div>
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
  name: "od-state",
  props: ["orderinfo", "deliveryinfo"],

  data() {
    return {
      orderid: ""
    };
  },
  filters: {
    status_filter: function(status) {
      if (status_mapping.hasOwnProperty(status)) return status_mapping[status];
      else return "";
    }
  },
  mounted() {
    // console.log(this.orderinfo);
    // console.log(this.deliveryinfo);
  }
};
</script>
