<template>
  <div>
    <el-row :gutter="20" class="pull-center">
      <el-col :span="6">
        &nbsp;
        <i class="el-icon-tickets"></i>&nbsp;商品
      </el-col>
      <el-col :span="6">
        &nbsp;
        <i class="el-icon-date"></i>&nbsp;单价
      </el-col>
      <el-col :span="6">
        &nbsp;
        <i class="el-icon-edit-outline"></i>&nbsp;数量
      </el-col>
      <el-col :span="6">
        &nbsp;
        <i class="el-icon-setting"></i>
        &nbsp;选项
      </el-col>
    </el-row>
  </div>
</template>

<script>
export default {
  name: "st-cart",
  data() {
    return {};
  }
};
</script>

