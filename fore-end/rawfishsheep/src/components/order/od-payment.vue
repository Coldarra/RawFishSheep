<template>
  <div>
    <div class="pull-center">
      <el-button type="text" style="font-size:1rem">立即支付</el-button>
    </div>
    <div id="qrcode"></div>
  </div>
</template>

<script>
import QRCode from "qrcodejs2";
export default {
  name: "od-payment",
  props: ["orderinfo"],
  data() {
    return {
      orderid: ""
    };
  },
  methods: {
    qrcode() {
      let url = window.location.href;
      // console.log(url);
      let qrcode = new QRCode("qrcode", {
        width: 132,
        height: 132,
        text: url + "/pay", // 二维码地址
        colorDark: "#000",
        colorLight: "#fff"
      });
    }
  },
  mounted() {
    this.qrcode();
    // this.orderid = this.$route.params.orderid;
    // this.$ajax.post("/api/order/info", { order_id: this.orderid }).then(res => {
    //   if (res.data.ret == "0") {
    //     console.log(res.data.data);
    //     this.orderinfo = res.data.data.order;
    //   }
    // });
  }
};
</script>
