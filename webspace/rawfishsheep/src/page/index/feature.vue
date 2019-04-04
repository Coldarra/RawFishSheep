<template>
  <el-container>
    <el-row type="flex" justify="center" style="width: 100%;">
      <el-col :span="20">
        <el-row>
          <el-row>
            <el-col :span="4">
                <el-card shadow="never" style="height: 100%">
                  <el-alert type="error" :closable="false" style="width: 100%">
                    <span style="font-size: 12px">销量最高</span>
                    <el-button type="danger" class="el-icon-arrow-left" size="small" @click="prev"></el-button>
                    <el-button type="danger" class="el-icon-arrow-right" size="small" @click="next"></el-button>
                  </el-alert>
                  <img src="../../assets/products-images/product1.jpg" alt="" style="width: 100%">
                  <div style="border: 3px solid #4fa10b; border-radius: 4px">
                    今日购买，75折！
                  </div>
                  <el-button type="text info" style="float: left">查看全部</el-button>
                </el-card>
            </el-col>
            <el-col :span="5" v-for="(item, index) in products" :key="index">
              <el-card v-show="display[index]" style="height:100%">
                <img :src="item.src" :alt="item.name" style="width: 100%">
                <el-button type="text">{{ item.name }}</el-button>
                <el-rate v-model="item.rates"></el-rate>
                <div>{{ item.price }}</div>
                <el-button type="danger" plain>加入购物车</el-button>
              </el-card>
            </el-col>
          </el-row>
        </el-row>
      </el-col>
    </el-row>
  </el-container>
</template>

<script>
export default {
  name: 'feature',
  data () {
    return {
      products: [
        { src: require('../../assets/products-images/product9.jpg'), name: '胡萝卜', price: '1￥', rates: 2.5 },
        { src: require('../../assets/products-images/product10.jpg'), name: '青椒', price: '2￥', rates: 3.5 },
        { src: require('../../assets/products-images/product11.jpg'), name: '草莓', price: '3￥', rates: 4.5 },
        { src: require('../../assets/products-images/product13.jpg'), name: '土豆', price: '4￥', rates: 1.7 },
        { src: require('../../assets/products-images/product14.jpg'), name: 'b', price: '5￥', rates: 2.7 },
        { src: require('../../assets/products-images/product12.jpg'), name: 'd', price: '6￥', rates: 0.7 }
      ],
      display: [true, true, true, true, false, false]
    }
  },
  methods: {
    prev: function () {
      let t = this.display.shift()
      this.display.push(t)
    },
    next: function () {
      let t = this.display.pop()
      this.display.unshift(t)
    }
  }
}
</script>

<style>
  .el-button--small, .el-button--small.is-round {
    padding: 0 0;
  }
</style>
