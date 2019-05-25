<template>
  <div class="body">
    <el-dialog title="新增收货地址" :visible.sync="addAddressButtonVisible" width="40%">
      <span>新增收货地址</span>

      <span slot="footer" class="dialog-footer">
        <el-button @click="addAddressButtonVisible=false">取 消</el-button>
        <el-button
          type="primary"
          :loading="addAddressButtonLoading"
          @click="addAddressButtonVisible=false;addAddressButtonLoading=true;"
        >确 定</el-button>
      </span>
    </el-dialog>
    <div class="table-top">
      <cart></cart>
      <hr>
      <div v-loading="this.$store.state.cartlock">
        <div v-for="(cart, id) in this.$store.state.cartList" :key="id">
          <el-row :gutter="20" class="pull-center">
            <el-col :span="6" class="line pull-left">
              <img :src="cart.goods.picture_url" style="height: 5rem;">
              {{ cart.name }}
            </el-col>
            <el-col :span="6">¥ {{ cart.goods.price }}</el-col>
            <el-col :span="6">
              <el-input-number
                v-model="cart.amount"
                :min="1"
                :max="100"
                :step="1"
                label="选择数量"
                @change="Public.changeCartAmount(cart.goods.id,cart.amount)"
              ></el-input-number>
            </el-col>
            <el-col :span="6">
              <!-- <el-button type="success" icon="el-icon-plus" circle></el-button> -->
              <el-button
                type="danger"
                icon="el-icon-delete"
                circle
                @click="Public.removeFromCartList(cart.goods.id)"
              ></el-button>
            </el-col>
          </el-row>
          <hr>
        </div>
      </div>
      <div class="settlement-inf">
        <!-- 选择收货地址： -->
        <el-card class="box-card">
          <div slot="header" class="clearfix">
            <span>收货信息</span>
            <el-button
              style
              class="totalprice"
              type="text"
            >总价：¥ {{ Number(this.$store.state.totalPrice).toFixed(2)}}</el-button>
          </div>
          <el-row class="pull-center">
            <el-col :span="4">收货地址</el-col>
            <el-col :span="16" :offset="2">
              <el-autocomplete
                popper-class="my-autocomplete"
                v-model="address"
                :fetch-suggestions="querySearch"
                placeholder="请选择收货地址"
                @select="handleSelect"
                style=" width: 100%;"
              >
                <i class="el-icon-edit el-input__icon" slot="suffix" @click="handleIconClick"></i>
                <template slot-scope="{ item }">
                  <div class="name">{{ item.value }}</div>
                  <span class="addr">{{ item.address }}</span>
                </template>
              </el-autocomplete>
            </el-col>
            <el-col :span="2">
              <el-button type="text" @click="addAddressButtonVisible = true">新增</el-button>
            </el-col>
          </el-row>
          <br>
          <el-row class="pull-center">
            <el-col :span="4">收货时间</el-col>
            <el-col :span="16" :offset="2">
              <el-time-select
                placeholder="选择收货时间"
                v-model="datetime"
                :picker-options="{start: '07:00',step: '00:30',end: '20:00'}"
                style="width:100%"
              ></el-time-select>
            </el-col>
            <el-col :span="2"></el-col>
          </el-row>
          <br>
          <el-row class="pull-center">
            <el-col :span="4">付款方式</el-col>
            <el-col :span="16" :offset="2">
              <el-select v-model="payment" clearable placeholder="选择付款方式" style="width:100%">
                <el-option
                  v-for="item in payments"
                  :key="item.value"
                  :label="item.label"
                  :value="item.value"
                ></el-option>
              </el-select>
            </el-col>
            <el-col :span="2"></el-col>
          </el-row>
          <br>
          <br>
          <el-row class="pull-center">
            <el-col :span="8" :offset="8">
              <router-link to="/order">
                <el-button type="primary" style="width:100%">提交订单</el-button>
              </router-link>
            </el-col>
          </el-row>
          <br>

          <!-- <div v-for="o in 4" :key="o" class="text item">{{'列表内容 ' + o }}</div> -->
        </el-card>

        <hr>
      </div>
    </div>
  </div>
</template>
<style lang="scss" scoped>
.body {
  margin-left: 10%;
  margin-right: 10%;
}
.table-top {
  margin-top: 1rem;
}
.settlement-inf {
  margin-top: 2rem;
  margin-left: 5%;
  margin-right: 5%;
}
.my-autocomplete {
  li {
    line-height: normal;
    padding: 7px;
    .name {
      text-overflow: ellipsis;
      overflow: hidden;
    }
    .addr {
      font-size: 12px;
      color: #b4b4b4;
    }

    .highlighted .addr {
      color: #ddd;
    }
  }
}
.totalprice {
  float: right;
  padding: 3px 0;
  font-size: 1.3rem;
}
</style>


<script>
import cart from "@/components/settlement/st-cart.vue";
import create_address from "@/components/settlement/st-create_address.vue";
import manage_address from "@/components/settlement/st-manage_address.vue";

export default {
  name: "app-settlement",
  components: {
    cart: cart,
    create_address: create_address,
    manage_address: manage_address
  },
  data() {
    return {
      loading: true,
      addAddressButtonVisible: false,
      addAddressButtonLoading: false,
      address: "",
      addressList: [],
      payment: "",
      payments: [
        {
          value: "货到付款",
          label: "货到付款"
        },
        {
          value: "支付宝",
          label: "支付宝"
        },
        {
          value: "微信支付",
          label: "微信支付"
        },
        {
          value: "京东支付",
          label: "京东支付"
        },
        {
          value: "银联钱包",
          label: "银联钱包"
        }
      ],
      datetime: ""
    };
  },
  methods: {
    querySearch(queryString, cb) {
      var addressList = this.addressList;
      var results = queryString
        ? addressList.filter(this.createFilter(queryString))
        : addressList;
      // 调用 callback 返回建议列表的数据
      cb(results);
    },
    createFilter(queryString) {
      return addr => {
        return (
          addr.value.toLowerCase().indexOf(queryString.toLowerCase()) === 0
        );
      };
    },
    loadAll() {
      return [
        {
          value: "华东理工大学（奉贤校区）",
          address: "上海市奉贤区海思路999号"
        },
        { value: "三全鲜食（北新泾店）", address: "上海市长宁区新渔路144号" },
        {
          value: "Hot honey 首尔炸鸡（仙霞路）",
          address: "上海市长宁区淞虹路661号"
        },
        {
          value: "新旺角茶餐厅",
          address: "上海市普陀区真北路988号创邑金沙谷6号楼113"
        },
        { value: "贡茶", address: "上海市长宁区金钟路633号" },
        {
          value: "豪大大香鸡排超级奶爸",
          address: "上海市嘉定区曹安公路曹安路1685号"
        },
        { value: "壹分米客家传统调制米粉(天山店)", address: "天山西路428号" },
        {
          value: "福荣祥烧腊（平溪路店）",
          address: "上海市长宁区协和路福泉路255弄57-73号"
        },
        {
          value: "速记黄焖鸡米饭",
          address: "上海市长宁区北新泾街道金钟路180号1层01号摊位"
        },
        { value: "红辣椒麻辣烫", address: "上海市长宁区天山西路492号" },
        {
          value: "(小杨生煎)西郊百联餐厅",
          address: "长宁区仙霞西路88号百联2楼"
        },
        { value: "阳阳麻辣烫", address: "天山西路389号" },
        {
          value: "南拳妈妈龙虾盖浇饭",
          address: "普陀区金沙江路1699号鑫乐惠美食广场A13"
        }
      ];
    },
    handleSelect(item) {
      console.log(item);
    },
    handleIconClick(ev) {
      console.log(ev);
    }
  },
  mounted() {
    setTimeout(() => {
      if (this.$store.state.cartList.length == 0) {
        this.$message({
          message: "购物车空空如也",
          type: "warning"
        });
        this.$router.go(-1);
      } else {
        this.loading = false;
      }
    }, 500);
    this.addressList = this.loadAll();
    var _this = this;
    // setInterval(function(){console.log(_this.$store.state.cartlock); },50);
  }
};
</script>
