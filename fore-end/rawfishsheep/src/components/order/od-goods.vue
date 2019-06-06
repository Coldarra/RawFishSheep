<template>
  <div style="margin-top:1rem">
    <template>
      <el-table :data="orderinfo.detail" stripe style="width: 100%">
        <el-table-column label="商品信息" min-width="200">
          <template slot-scope="scope">
            <div class="line">
              <img :src="scope.row.goods.picture_url" style="height: 5rem;width: 5rem;">
              &nbsp;&nbsp;{{ scope.row.goods.name }}
            </div>
          </template>
        </el-table-column>
        <el-table-column label="单价" prop="price" min-width="75">
          <template slot-scope="scope">¥ {{ scope.row.price }}</template>
        </el-table-column>
        <el-table-column label="数量" prop="amount" min-width="75"></el-table-column>
        <el-table-column label="总价" min-width="100">
          <template slot-scope="scope">¥ {{ (Number(scope.row.price)*Number(scope.row.amount)).toFixed(2) }}</template>
        </el-table-column>
        <el-table-column label="操作" min-width="100">
          <template slot-scope="scope">
            <el-button type="text" style="color:#F56C6C" icon="el-icon-warning-outline" @click=";">申请售后</el-button>
            <br>
            <el-button type="text" icon="el-icon-copy-document" @click="Public.addToCartList(scope.row.goods_id)">加入购物车</el-button>
          </template>
        </el-table-column>
      </el-table>
    </template>
  </div>
</template>


<script>
export default {
  name: "od-goods",
  props: ["orderinfo"],
  data() {
    return {
      orderid: ""
    };
  },
  mounted() {
    // console.log(this.orderinfo);
  }
};
</script>
