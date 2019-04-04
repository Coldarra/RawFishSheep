<template>
  <el-container id="products">
    <el-row type="flex" justify="center" style="width: 100%">
      <el-col :span="20">
          <h3 style="float: left;background-color: #59B210; border-radius: 4px; padding: 1px 20px">产品</h3>
          <el-tabs
            v-model="activeName">
            <el-tab-pane v-for="(item, index) in paneName" :key="index" :label="item.label" :name="item.name">
              <el-row>
                <el-col :span="6" v-for="(i, id) in new_products[index]" :key="id">
                  <el-card shadow="never">
                    <img :src="i[0]" alt="" style="width: 100%">
                    <el-button type="text">{{ i[1] }}</el-button>
                    <el-rate v-model="i[3]"></el-rate>
                    <div>{{ i[2] }}</div>
                    <el-button type="danger" plain>加入购物车</el-button>
                  </el-card>
                </el-col>
              </el-row>
            </el-tab-pane>
          </el-tabs>
      </el-col>
    </el-row>
  </el-container>
</template>

<script>
export default {
  name: 'products',
  data () {
    return {
      activeName: 'first',
      paneName: [
        {label: '新鲜水果', name: 'first'},
        {label: '海鲜水产', name: 'second'},
        {label: '精选肉类', name: 'third'},
        {label: '冷冻饮食', name: 'fourth'},
        {label: '蔬菜蛋品', name: 'fifth'}
      ],
      value1: null,
      new_products: [
        {
          item1: [require('../../assets/products-images/product1.jpg'), 'a', '123￥', 0],
          item2: [require('../../assets/products-images/product2.jpg'), 'b', '123￥', 1],
          item3: [require('../../assets/products-images/product3.jpg'), 'c', '123￥', 2],
          item4: [require('../../assets/products-images/product4.jpg'), 'd', '123￥', 3]
        },
        {
          item1: [require('../../assets/products-images/product5.jpg'), 'a', '123￥', 4],
          item2: [require('../../assets/products-images/product6.jpg'), 'b', '123￥', 5],
          item3: [require('../../assets/products-images/product7.jpg'), 'c', '123￥', 0.5],
          item4: [require('../../assets/products-images/product8.jpg'), 'd', '123￥', 1.5]
        },
        {
          item1: [require('../../assets/products-images/product9.jpg'), 'a', '123￥', 2.5],
          item2: [require('../../assets/products-images/product10.jpg'), 'b', '123￥', 3.5],
          item3: [require('../../assets/products-images/product11.jpg'), 'c', '123￥', 4.5],
          item4: [require('../../assets/products-images/product12.jpg'), 'd', '123￥', 0.7]
        },
        {
          item1: [require('../../assets/products-images/product13.jpg'), 'a', '123￥', 1.7],
          item2: [require('../../assets/products-images/product14.jpg'), 'b', '123￥', 2.7],
          item3: [require('../../assets/products-images/product5.jpg'), 'c', '123￥', 3.7],
          item4: [require('../../assets/products-images/product16.jpg'), 'd', '123￥', 4.7]
        },
        {
          item1: [require('../../assets/products-images/product7.jpg'), 'a', '123￥', 5],
          item2: [require('../../assets/products-images/product6.jpg'), 'b', '123￥', 4],
          item3: [require('../../assets/products-images/product5.jpg'), 'c', '123￥', 3],
          item4: [require('../../assets/products-images/product11.jpg'), 'd', '123￥', 2]
        }
      ]
    }
  },
  methods: {
    handleClick (tab, event) {
      console.log(tab, event)
    }
  }
}
</script>

<style>
#products {
  margin-bottom: 20px;
}

.el-tabs__nav {
  float: right;
}
.el-tabs__nav-scroll {
  border-bottom: 5px #59B210;
}

.el-tabs__active-bar {
  background-color: #59B210;
}

.el-tabs__item:hover {
  color: #59B210;
}

.el-tabs__item.is-active {
  color: #59B210;
}
</style>
