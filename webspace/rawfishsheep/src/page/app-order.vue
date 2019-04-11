<template>
  <div id="order">
    <div>
      <el-row class="pull-center" :gutter="20">
        <el-col :span="7">商品信息</el-col>
        <el-col :span="3">总价</el-col>
        <el-col :span="6">收货地址</el-col>
        <el-col :span="5">订单状态</el-col>
        <el-col :span="5">订单操作</el-col>
      </el-row>
      <hr>
      <div v-for="(order, order_index) in orders" :key="order_index">
        <el-row class="pull-center" :gutter="20">
          <el-col :span="7">
            <div v-for="(item, id) in order.goods" :key="id">
              <div v-if="id">
                <br>
              </div>
              <img :src="item.src" style="height: 4rem;">
              {{ item.name }} * {{ item.quantity }}&nbsp;&nbsp;&nbsp;/&nbsp;&nbsp;&nbsp;¥ {{ item.price }}
            </div>
          </el-col>

          <el-col :span="3">
            <div>¥ {{ order.total_price }}</div>
          </el-col>

          <el-col :span="6">{{ order.address }}</el-col>

          <el-col :span="5">
            <div>{{ order.state }}</div>
          </el-col>

          <el-col :span="5">
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
export default {
  name: "app-order",

  data() {
    return {
      logo: require("../assets/images/logo.png"),
      orders: [
        {
          goods: [
            {
              id: 0,
              src: require("../assets/products-images/product11.jpg"),
              name: "草莓",
              price: "3.00",
              quantity: 4
            },
            {
              id: 1,
              src: require("../assets/products-images/product10.jpg"),
              name: "青椒",
              price: "2.00",
              quantity: 2
            }
          ],
          address: "上海市奉贤区海思路999号 华东理工大学（奉贤校区）",
          payment: "货到付款",
          total_price: "16.00",
          state: "配货中",
          seeting: ['<el-button type="primary">确认收货</el-button>']
        },
        {
          goods: [
            {
              id: 0,
              src: require("../assets/products-images/product13.jpg"),
              name: "土豆",
              price: "3.00",
              quantity: 2
            },
            {
              id: 1,
              src: require("../assets/products-images/product16.jpg"),
              name: "葡萄",
              price: "4.00",
              quantity: 4
            },
            {
              id: 2,
              src: require("../assets/products-images/product7.jpg"),
              name: "苹果",
              price: "4.00",
              quantity: 1
            }
          ],
          address: "上海市奉贤区海思路999号 华东理工大学（奉贤校区）",
          payment: "货到付款",
          total_price: "26.00",
          state: "配送中",
          seeting: ["<el-button>评价商品</el-button>"]
        },
        {
          goods: [
            {
              id: 0,
              src: require("../assets/products-images/product6.jpg"),
              name: "香蕉",
              price: "4.00",
              quantity: 3
            },
          ],
          address: "上海市奉贤区海思路999号 华东理工大学（奉贤校区）",
          payment: "货到付款",
          total_price: "12.00",
          state: "已完成",
          seeting: ["<el-button>评价商品</el-button>"]
        }
      ]
    };
  }
};
</script>
