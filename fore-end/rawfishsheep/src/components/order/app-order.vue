<template>
  <div id="orderlist">
    <div>
      <template>
        <el-table
          v-loading="this.$store.state.cartListLock"
          :data="this.$store.state.orderList"
          style="width: 100%"
        >
          <el-table-column label="商品信息" min-width="200">
            <template slot-scope="scope">
              <p v-for="(item, i) in scope.row.detail" :key="i" class="line">
                <img :src="item.goods.picture_url" style="height: 3rem;width: 3rem;">
                {{ item.goods.name }} × {{ item.amount }}
              </p>
            </template>
          </el-table-column>
          <el-table-column label="总价" prop="totalprice" min-width="75"></el-table-column>
          <el-table-column label="收货地址" prop="address" min-width="200"></el-table-column>
          <el-table-column label="下单时间" prop="createtime" min-width="180"></el-table-column>
          <el-table-column label="状态" min-width="100">
            <template slot-scope="scope">
              <div class="line">{{ scope.row.status | status_filter }}</div>
            </template>
          </el-table-column>
          <el-table-column align="right" min-width="200">
            <template slot="header">
              <el-input v-model="search" size="mini" placeholder="输入关键字搜索"/>
            </template>
            <template slot-scope="scope">
              <div style="margin-top:0.2rem;margin-bottom:0.2rem;">
                <el-button
                  v-if="scope.row.status=='processing' || scope.row.status=='examining'"
                  size="mini"
                  type="danger"
                >取消订单</el-button>
                <el-button
                  v-else-if="scope.row.status=='delivering'"
                  size="mini"
                  type="primary"
                >确认收货</el-button>
                <el-button v-else-if="scope.row.status=='delivered'" size="mini" type="primary">确认收货</el-button>
                <el-button v-else-if="scope.row.status=='confirmed'" size="mini" type="success">评价订单</el-button>
                <el-button size="mini" @click="jumpToDetail( scope.row.id.toString() )">订单详情</el-button>
              </div>
            </template>
          </el-table-column>
        </el-table>
      </template>
    </div>
  </div>
</template>

<style lang="scss" scoped>
#orderlist {
  margin-left: 10%;
  margin-right: 10%;
  // margin-top: 2rem;
}
</style>


<script>
const status_mapping = {
  processing: "系统准备中",
  examining: "订单审核中",
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
      // logo: require("@/assets/images/logo.png"),
      search: ""
    };
  },
  methods: {
    jumpToDetail(orderid) {
      console.log(orderid);
      this.$router.push("/order/" + orderid);
    }
  },
  filters: {
    status_filter: function(status) {
      if (status_mapping.hasOwnProperty(status)) return status_mapping[status];
      else return "";
    },
    search_data: function(orderList) {
      return orderList.filter(
        data => !this.search || data.detail.name.includes(this.search)
      );
    }
  },
  mounted() {
    this.Public.fillOrderList();
  }
};
</script>
