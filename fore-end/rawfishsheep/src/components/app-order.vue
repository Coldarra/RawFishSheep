<template>
  <div id="order">
    <!-- <div :v-if="false">
      <el-row class="pull-center" :gutter="20">
        <el-col :span="8">商品信息</el-col>
        <el-col :span="2">总价</el-col>
        <el-col :span="6">收货地址</el-col>
        <el-col :span="4">订单状态</el-col>
        <el-col :span="4">订单操作</el-col>
      </el-row>
      <hr>
      <div v-for="(order, index) in orderList" :key="index">
        <el-row :gutter="20">
          <el-col :span="8">
            <div v-for="(item, id) in order.detail" :key="id">
              <p>
                <img :src="item.goods.picture_url" style="height: 3rem;width: 3rem;">
                {{ item.goods.name }} × {{ item.amount }}
              </p>
            </div>
          </el-col>

          <el-col :span="2">
            <div>¥ {{ order.total_price }}</div>
          </el-col>

          <el-col :span="6">{{ order.address }}</el-col>

          <el-col :span="4">
            <div>{{ order.status }}</div>
          </el-col>

          <el-col :span="4">
            <div v-if="order.state=='配货中'">
              <el-button type>订单详情</el-button>
              <div style="margin-top:0.5rem;"></div>
              <el-button type="danger">取消订单</el-button>
            </div>
            <div v-if="order.state=='配送中'">
              <el-button type>订单详情</el-button>
              <div style="margin-top:0.5rem;"></div>
              <el-button type="primary">确认收货</el-button>
            </div>
            <div v-else-if="order.state=='已完成'">
              <el-button type>订单详情</el-button>
              <div style="margin-top:0.5rem;"></div>
              <el-button type="success">评价订单</el-button>
            </div>
          </el-col>
        </el-row>

        <hr>
      </div>
      <br>
    </div>-->

    <div>
      <template>
        <el-table
          v-loading="loading"
          :data="orderList.filter(data => !search || data.detail.name.includes(search))"
          style="width: 100%"
        >
          <el-table-column label="商品信息" min-width="200">
            <template slot-scope="scope">
              <p v-for="(item, i) in scope.row.detail" :key="i" style="white-space: nowrap;">
                <img :src="item.goods.picture_url" style="height: 3rem;width: 3rem;">
                {{ item.goods.name }} × {{ item.amount }}
              </p>
            </template>
          </el-table-column>
          <el-table-column label="总价" prop="totalprice" min-width="75"></el-table-column>
          <el-table-column label="收货地址" prop="address" min-width="200"></el-table-column>
          <el-table-column label="状态">
            <template slot-scope="scope">{{ scope.row.status | get_status }}</template>
          </el-table-column>
          <el-table-column align="right" min-width="200">
            <template slot="header" slot-scope="scope">
              <el-input v-model="search" size="mini" placeholder="输入关键字搜索"/>
            </template>
            <template slot-scope="scope">
              <el-button v-if="scope.row.status=='delivering'" size="mini" type="primary">确认收货</el-button>
              <el-button v-else-if="scope.row.status=='delivered'" size="mini" type="success">评价订单</el-button>
              <el-button v-else size="mini" type="danger">取消订单</el-button>
              <el-button size="mini">订单详情</el-button>
            </template>
          </el-table-column>
        </el-table>
      </template>
    </div>
  </div>
</template>

<style lang="scss" scoped>
#order {
  margin-left: 10%;
  margin-right: 10%;
  margin-top: 2rem;
}
</style>


<script>
var status_mapping = {
  processing: "准备中",
  examining: "审核中",
  preparing: "备货中",
  delivering: "配送中",
  delivered: "配送完成",
  confirmed: "订单完成"
};
export default {
  name: "app-order",

  data() {
    return {
      loading: true,
      logo: require("@/assets/images/logo.png"),
      search: "",
      orderList: [
        {
          id: 6,
          user: "test",
          address: "上海市奉贤区海思路999号",
          totalprice: 300,
          discount: 1,
          createtime: "2019/04/13 18:14:12",
          finishtime: "",
          paymentname: "货到付款",
          isrefund: "0",
          isdelete: "0",
          status: "2",
          detail: [
            {
              id: 1,
              order: 6,
              goods_id: 1,
              amount: 1,
              goods: {
                id: 1,
                goods_id: 1,
                category: "null",
                name: "法兰西大粗黄瓜",
                unit: "根",
                status: "1",
                price: "1.00",
                remain: 1000,
                picture_url: "/static/img/goods/1.jpg",
                isdelete: "0"
              },
              price: "3.00",
              isdelete: "0"
            }
          ]
        },
        {
          id: 8,
          user: "test",
          address: "上海市奉贤区海思路999号",
          totalprice: 300,
          discount: 1,
          createtime: "2019/04/13 18:19:30",
          finishtime: "",
          paymentname: "货到付款",
          isrefund: "0",
          isdelete: "0",
          status: "2",
          detail: [
            {
              id: 3,
              order: 8,
              goods_id: 1,
              goods: {
                id: 1,
                goods_id: 1,
                category: "null",
                name: "法兰西大粗黄瓜",
                unit: "根",
                status: "1",
                price: "1.00",
                remain: 1000,
                picture_url: "/static/img/goods/1.jpg",
                isdelete: "0"
              },
              price: "3.00",
              isdelete: "0"
            }
          ]
        },
        {
          id: 9,
          user: "test",
          address: "上海市奉贤区海思路999号",
          totalprice: 300,
          discount: 1,
          createtime: "2019/04/13 18:20:36",
          finishtime: "",
          paymentname: "货到付款",
          isrefund: "0",
          isdelete: "0",
          status: "4",
          detail: [
            {
              id: 4,
              order: 9,
              goods_id: 1,
              goods: {
                id: 1,
                goods_id: 1,
                category: "null",
                name: "法兰西大粗黄瓜",
                unit: "根",
                status: "1",
                price: "1.00",
                remain: 1000,
                picture_url: "/static/img/goods/1.jpg",
                isdelete: "0"
              },
              price: "3.00",
              isdelete: "0"
            }
          ]
        },
        {
          id: 9,
          user: "test",
          address: "上海市奉贤区海思路999号",
          totalprice: 300,
          discount: 1,
          createtime: "2019/04/13 18:20:36",
          finishtime: "",
          paymentname: "货到付款",
          isrefund: "0",
          isdelete: "0",
          status: "4",
          detail: [
            {
              id: 4,
              order: 9,
              goods_id: 1,
              goods: {
                id: 1,
                goods_id: 1,
                category: "null",
                name: "法兰西大粗黄瓜",
                unit: "根",
                status: "1",
                price: "1.00",
                remain: 1000,
                picture_url: "/static/img/goods/1.jpg",
                isdelete: "0"
              },
              price: "3.00",
              isdelete: "0"
            }
          ]
        },
        {
          id: 9,
          user: "test",
          address: "上海市奉贤区海思路999号",
          totalprice: 300,
          discount: 1,
          createtime: "2019/04/13 18:20:36",
          finishtime: "",
          paymentname: "货到付款",
          isrefund: "0",
          isdelete: "0",
          status: "4",
          detail: [
            {
              id: 4,
              order: 9,
              goods_id: 1,
              goods: {
                id: 1,
                goods_id: 1,
                category: "null",
                name: "法兰西大粗黄瓜",
                unit: "根",
                status: "1",
                price: "1.00",
                remain: 1000,
                picture_url: "/static/img/goods/1.jpg",
                isdelete: "0"
              },
              price: "3.00",
              isdelete: "0"
            }
          ]
        }
      ]
    };
  },
  method: {
    get_status(status) {
      console.log(status);
      return this.status_mapping[status];
    }
  },
  filters: {
    get_status: function(status) {
      // var status_mapping = {
      //   processing: "准备中",
      //   examining: "审核中",
      //   preparing: "备货中",
      //   delivering: "配送中",
      //   delivered: "配送完成",
      //   confirmed: "订单完成"
      // };
      return status_mapping[status];
    }
  },
  mounted() {
    this.$ajax.get("/api/order/all").then(res => {
      if (res.data.ret == "0") {
        this.loading = false;
        this.orderList = res.data.data.order;
        console.log(this.orderList);
      }
    });
  }
};
</script>
