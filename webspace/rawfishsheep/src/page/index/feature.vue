<template>
<div id="feature">
  <el-container>
    <el-row >
      <h3 class="new">- 最新上市 -</h3>
    </el-row>
  </el-container>
  <el-container>
    <el-row type="flex" :gutter="20" justify="center" class="pull-center">
      <!-- <el-col :span="4">
                <el-card shadow="never" style="height: 100%">
                  <el-alert type="error" :closable="false" style="width: 100%">
                    <span style="font-size: 2em">最新上市</span>
                  </el-alert>
                  <img src="../../assets/products-images/product1.jpg" alt="" style="width: 100%">
                  <div style="border: 3px solid #4fa10b; border-radius: 4px">
                    今日购买，75折！
                  </div>
                  <el-button type="text info" style="float: left">查看全部</el-button>
                </el-card>
      </el-col>-->
      <el-col :span="6" v-for="(item, index) in products" :key="index">
        <el-card style="height:100%">
          <img :src="item.src" :alt="item.name" style="width: 100%">
          <el-button type="text">{{ item.name }}</el-button>
          <el-rate v-model="item.rates" disabled></el-rate>
          <div class="price">{{ item.price }}</div>
          <el-button type="success" plain>加入购物车</el-button>
        </el-card>
      </el-col>
    </el-row>
  </el-container>
  </div>
</template>

<style scoped>
.el-button--small,
.el-button--small.is-round {
  padding: 0 0;
}
#feature {
  margin-bottom: 2rem;
  margin-left: 5%;
  margin-right: 5%;
}
.new{
  font-family:"Microsoft YaHei";
  margin-top: 2rem;
  margin-bottom: 1rem;
}
</style>
<script>
export default {
  name: "feature",
  data() {
    return {
      products: [
        {
          src: require("../../assets/products-images/product9.jpg"),
          name: "胡萝卜",
          price: "￥1.00",
          rates: 4.5
        },
        {
          src: require("../../assets/products-images/product10.jpg"),
          name: "青椒",
          price: "￥2.00",
          rates: 5.0
        },
        {
          src: require("../../assets/products-images/product11.jpg"),
          name: "草莓",
          price: "￥3.00",
          rates: 4.5
        },
        {
          src: require("../../assets/products-images/product13.jpg"),
          name: "土豆",
          price: "￥4.00",
          rates: 4.7
        }
      ],
      
    };
  },
  methods: {}
};
</script>

