<template>
  <div id="bs-goods">
    <el-table :data="tableData" class="goods-table" height="100%" style="width: 100%;">
      <el-table-column align="center" fixed label="商品图片" prop="name">
        <template slot-scope="scope">
          <img :src="scope.row.src" alt style="height:3rem;">
        </template>
      </el-table-column>
      <el-table-column fixed label="商品名称" prop="name"></el-table-column>
      <el-table-column label="成本价" prop="cost"></el-table-column>
      <el-table-column label="售价" prop="price"></el-table-column>
      <el-table-column label="库存" prop="stock"></el-table-column>
      <el-table-column label="销量" prop="sales"></el-table-column>
      <el-table-column align="center">
        <template slot="header">
          <div class="add-goods-button">
            <el-button icon="el-icon-circle-plus-outline" @click="show_addGoodsButton = true">添加商品</el-button>
          </div>
        </template>
        <template slot-scope="scope">
          <div>
            <el-button size="mini" @click="handleEdit(scope.$index, scope.row)">修改商品</el-button>
            <br>
            <el-button size="mini" type="danger" @click="handleDelete(scope.$index, scope.row)">删除商品</el-button>
          </div>
        </template>
      </el-table-column>
    </el-table>
    <el-dialog
      title="添加商品"
      :visible.sync="show_addGoodsButton"
      width="50%"
      :before-close="handleClose"
    >
      <!-- <span>这是添加商品页面</span> -->
      <el-row>
        <el-col :span="4">商品名称</el-col>
        <el-col :span="20">
          <el-input v-model="new_goods_name" placeholder="商品名称"></el-input>
        </el-col>
      </el-row>
      <br>
      <el-row>
        <el-col :span="4">商品分类</el-col>
        <el-col :span="20">
          <el-radio-group v-model="new_goods_category" size="medium">
            <el-radio-button label="蔬菜"></el-radio-button>
            <el-radio-button label="水果"></el-radio-button>
            <el-radio-button label="海鲜"></el-radio-button>
            <el-radio-button label="肉类"></el-radio-button>
            <el-radio-button label="其他"></el-radio-button>
          </el-radio-group>
          <!-- <el-radio v-model="new_goods_category" label="1">蔬菜</el-radio>
          <el-radio v-model="new_goods_category" label="2">水果</el-radio>
          <el-radio v-model="new_goods_category" label="3">海鲜</el-radio>
          <el-radio v-model="new_goods_category" label="4">肉类</el-radio>
          <el-radio v-model="new_goods_category" label="5">其他</el-radio>-->
        </el-col>
      </el-row>
      <br>
      <el-row>
        <el-col :span="4">商品售价/元</el-col>
        <el-col :span="20">
          <el-input-number v-model="new_goods_price" controls-position="right" :min="1" :max="1000"></el-input-number>
        </el-col>
      </el-row>
      <br>
      <el-row>
        <el-col :span="4">商品进价/元</el-col>
        <el-col :span="8">
          <el-input-number v-model="new_goods_cost" controls-position="right" :min="1" :max="1000"></el-input-number>
        </el-col>
        <el-col :span="4">进货数量</el-col>
        <el-col :span="8">
          <el-input-number
            v-model="new_goods_remain"
            controls-position="right"
            :min="1"
            :max="1000"
          ></el-input-number>
        </el-col>
      </el-row>
      <br>
      <el-row>
        <el-col :span="4">商品图片</el-col>
        <el-col :span="20">
          <el-upload class="upload-demo" drag action="/" multiple>
            <i class="el-icon-upload"></i>
            <div class="el-upload__text">
              将图片拖到此处，或
              <em>点击上传</em>
            </div>
            <div class="el-upload__tip" slot="tip">只能上传jpg/png文件，且不超过1024kb</div>
          </el-upload>
        </el-col>
      </el-row>

      <span slot="footer" class="dialog-footer">
        <el-button @click="dialogVisible = false">取 消</el-button>
        <el-button type="primary" @click="dialogVisible = false">确 定</el-button>
      </span>
    </el-dialog>
  </div>
</template>


<style lang="scss" scoped>
// .goods-table {
//   // margin-right:1rem;
//   // margin-left:1rem;
// }
// .add-goods-button {
//   //   margin-right: 1rem;
//   //   margin-left: 1rem;
// }
</style>


<script>
export default {
  name: "bs-goods",
  data() {
    return {
      tableData: [
        {
          name: "四川春见耙耙柑",
          cost: "￥84.80",
          price: "￥94.80",
          stock: "18273",
          sales: "39821",
          src: require("../../assets/products-images/product11.jpg")
        },
        {
          name: "广西沃柑",
          cost: "￥19.90",
          price: "￥29.90",
          stock: "18273",
          sales: "39821",
          src: require("../../assets/products-images/product10.jpg")
        },
        {
          name: "新疆阿克苏苹果",
          cost: "￥88.00",
          price: "￥98.00",
          stock: "18273",
          sales: "39821",
          src: require("../../assets/products-images/product9.jpg")
        },
        {
          name: "智利轮切三文鱼排",
          cost: "￥49.90",
          price: "￥59.90",
          stock: "18273",
          sales: "39821",
          src: require("../../assets/products-images/product8.jpg")
        },
        {
          name: "越南巴沙鱼柳",
          cost: "￥12.90",
          price: "￥22.90",
          stock: "18273",
          sales: "39821",
          src: require("../../assets/products-images/product7.jpg")
        },
        {
          name: "冷冻阿拉斯加狭鳕鱼柳",
          cost: "￥10.90",
          price: "￥19.90",
          stock: "18273",
          sales: "39821",
          src: require("../../assets/products-images/product6.jpg")
        },
        {
          name: "澳洲厚切肥牛片",
          cost: "￥70.00",
          price: "￥79.00",
          stock: "18273",
          sales: "39821",
          src: require("../../assets/products-images/product5.jpg")
        },
        {
          name: "澳洲羊排",
          cost: "￥58.00",
          price: "￥68.00",
          stock: "18273",
          sales: "39821",
          src: require("../../assets/products-images/product4.jpg")
        },
        {
          name: "四川春见耙耙柑",
          cost: "￥84.80",
          price: "￥94.80",
          stock: "18273",
          sales: "39821",
          src: require("../../assets/products-images/product3.jpg")
        },
        {
          name: "四川春见耙耙柑",
          cost: "￥84.80",
          price: "￥94.80",
          stock: "18273",
          sales: "39821",
          src: require("../../assets/products-images/product2.jpg")
        },
        {
          name: "巴西进口鸡翅中",
          cost: "￥30.00",
          price: "￥36.00",
          stock: "18273",
          sales: "39821",
          src: require("../../assets/products-images/product1.jpg")
        }
      ],
      show_addGoodsButton: false,
      new_goods_name: "",
      new_goods_category: "",
      new_goods_remain: 1,
      new_goods_price: 1,
      new_goods_cost: 1,
      new_goods_category_options: []
    };
  },
  methods: {
    handleEdit(index, row) {
      console.log(index, row);
    },
    handleDelete(index, row) {
      console.log(index, row);
    }
  }
};
</script>