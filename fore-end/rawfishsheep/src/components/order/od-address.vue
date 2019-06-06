<template>
  <div class="margin5">
    <el-row :gutter="20">
      <el-col :span="12">
        <el-row :gutter="20">
          <el-col :span="8">收货人:</el-col>
          <el-col :span="12">{{orderinfo.receiver.name}}</el-col>
        </el-row>
        <el-row :gutter="20">
          <el-col :span="8">地址:</el-col>
          <el-col :span="12">{{orderinfo.receiver.address}}</el-col>
        </el-row>
        <el-row :gutter="20">
          <el-col :span="8">手机号码:</el-col>
          <el-col :span="12">{{orderinfo.receiver.phonenumber}}</el-col>
        </el-row>
      </el-col>
      <el-col :span="12">
        <el-row :gutter="20">
          <el-col :span="8">配送方式:</el-col>
          <el-col :span="12">普通快递</el-col>
        </el-row>
        <el-row :gutter="20">
          <el-col :span="8">运费:</el-col>
          <el-col :span="12">¥ 0.00</el-col>
        </el-row>
      </el-col>
    </el-row>
  </div>
</template>

<script>
export default {
  //   name: "od-address",
  props: ["orderinfo", "deliveryinfo"],
  data() {
    return {
      orderid: ""
    };
  },
  mounted() {
    console.log(this.orderinfo);
  }
};
</script>
