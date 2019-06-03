<template>
  <div class="body">
    <el-dialog title="新增收货地址" :visible.sync="addAddressButtonVisible" width="50%">
      <!-- <span>新增收货地址</span> -->
      <el-form
        :model="addressForm"
        status-icon
        :rules="addressRules"
        ref="addressForm"
        label-width="100px"
      >
        <el-form-item label="收货人" prop="name">
          <el-input v-model="addressForm.name"></el-input>
        </el-form-item>
        <el-form-item label="手机号" prop="phonenumber">
          <el-input v-model="addressForm.phonenumber" autocomplete="off"></el-input>
        </el-form-item>
        <el-form-item label="地址" prop="address">
          <el-input v-model="addressForm.address" autocomplete="off"></el-input>
        </el-form-item>
        <el-form-item label="详情" prop="detail">
          <el-input v-model="addressForm.detail" autocomplete="off"></el-input>
        </el-form-item>
        <el-form-item>
          <el-button type="success" plain @click="submitForm('addressForm')">保存并使用</el-button>
          <el-button @click="resetForm('addressForm')">重置</el-button>
        </el-form-item>

        <span slot="footer" class="dialog-footer">
          <el-button @click="addAddressButtonVisible=false">取 消</el-button>
          <el-button
            type="primary"
            :loading="addAddressButtonLoading"
            @click="addAddressButtonVisible=false;addAddressButtonLoading=true;"
          >确 定</el-button>
        </span>
      </el-form>
    </el-dialog>
    <div class="table-top" v-loading="pageLoading">
      <cart></cart>
      <hr>
      <el-collapse-transition>
        <div class="settlement-inf" v-show="settlementShow" v-loading="settlementLoading">
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
            <el-form :model="orderForm" status-icon :rules="orderRules" ref="orderForm">
              <el-form-item label="收货地址" prop="address">
                <el-row class="pull-center">
                  <el-col :span="18" :offset="2">
                    <el-select
                      v-model="orderForm.address"
                      filterable
                      placeholder="请选择收货地址"
                      style=" width: 100%;"
                    >
                      <el-option-group
                        v-for="group in addressList"
                        :key="group.label"
                        :label="group.label"
                        class="my-option"
                      >
                        <el-option
                          v-for="item in group.addresses"
                          :key="item.id"
                          :label="item.detail + ' ' + item.name + ' ' + item.phonenumber + ''"
                          :value="item.id"
                        >
                          <div class="name">{{ item.name }}</div>

                          <div
                            class="addr"
                          >{{ item.phonenumber }} {{ item.address }} {{ item.detail }}</div>
                        </el-option>
                      </el-option-group>
                    </el-select>
                  </el-col>
                  <el-col :span="2" :offset="1">
                    <el-button type="text" @click="addAddressButtonVisible = true">新增</el-button>
                  </el-col>
                </el-row>
              </el-form-item>

              <br>

              <el-form-item label="付款方式" prop="payment">
                <el-row class="pull-center">
                  <el-col :span="18" :offset="2">
                    <el-select
                      v-model="orderForm.payment"
                      clearable
                      placeholder="选择付款方式"
                      style="width:100%"
                    >
                      <el-option
                        v-for="item in payments"
                        :key="item.value"
                        :label="item.label"
                        :value="item.value"
                      ></el-option>
                    </el-select>
                  </el-col>
                  <!-- <el-col :span="2" :offset="1"></el-col> -->
                </el-row>
              </el-form-item>

              <br>
              <br>
              <el-row class="pull-center">
                <el-col :span="8" :offset="8">
                  <el-button
                    type="primary"
                    style="width:100%"
                    @click="SubmitOrder('orderForm')"
                  >提交订单</el-button>
                </el-col>
              </el-row>
              <br>
            </el-form>
          </el-card>

          <hr>
        </div>
      </el-collapse-transition>
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
.my-option {
  li {
    line-height: normal !important;
    height: auto !important;
    padding: 7px;
    .name {
      padding-left: 20px;
      text-overflow: ellipsis;
      overflow: hidden;
    }
    .addr {
      padding-left: 20px;
      font-size: 12px;
      white-space: normal;
      color: #b4b4b4;
    }

    .highlighted .addr {
      color: #ddd;
    }
  }
  li .selected {
    .name {
      color: inherit !important;
      font-weight: bold;
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
import addr_create from "@/components/settlement/addr-create.vue";
import addr_manage from "@/components/settlement/addr-manage.vue";

const addressRules = {
  name: [
    {
      required: true,
      min: 2,
      max: 10,
      message: "请输入收货人姓名",
      trigger: "blur"
    }
  ],
  phonenumber: [
    {
      required: true,
      min: 11,
      max: 11,
      message: "请输入11位手机号",
      trigger: "blur"
    }
  ],
  address: [
    {
      required: true,
      min: 11,
      max: 11,
      message: "请输入",
      trigger: "blur"
    }
  ],
  detail: [
    {
      required: true,
      min: 11,
      max: 11,
      message: "请输入",
      trigger: "blur"
    }
  ]
};
const orderRules = {
  address: [
    {
      required: true,
      message: "请选择收货地址",
      trigger: "blur"
    }
  ],
  payment: [
    {
      required: true,
      message: "请选择支付方式",
      trigger: "blur"
    }
  ]
};
const payments = [
  {
    value: "alipay",
    label: "支付宝"
  },
  {
    value: "wechat",
    label: "微信支付"
  },
  {
    value: "jdpay",
    label: "京东支付"
  },
  {
    value: "unionpay",
    label: "银联钱包"
  }
];
export default {
  name: "app-settlement",
  components: {
    cart: cart,
    addr_create: addr_create,
    addr_manage: addr_manage
  },
  data() {
    return {
      pageLoading: true,
      settlementShow: false,
      settlementLoading: false,
      addAddressButtonVisible: false,
      addAddressButtonLoading: false,
      addressForm: {
        name: "",
        phonenumber: "",
        address: "",
        detail: ""
      },
      addressRules: addressRules,

      addressList: {
        default_address: { label: "默认地址", addresses: [] },
        other_address: { label: "其他地址", addresses: [] }
      },
      payments: payments,
      orderRules: orderRules,
      orderForm: {
        address: "",
        payment: ""
      }
    };
  },
  methods: {
    submitForm(Form) {},
    resetForm(Form) {
      this.$refs[Form].resetFields();
    },
    SubmitOrder(Form) {
      this.$refs[Form].validate(valid => {
        if (valid) {
          this.settlementLoading = true;
          this.$ajax
            .post("/api/order/append", {
              address_id: this.orderForm.address,
              paymentname: this.orderForm.payment
            })
            .then(res => {
              if (res.data.ret == "0") {
                this.settlementLoading = false;
                this.Public.fillCartList();
                this.$message({
                  message: "订单创建成功",
                  type: "success"
                });
                const serialnumber = res.data.data.order.serialnumber;
                // console.log(res.data.data.order);
                this.$router.push("/order/" + serialnumber);
              }
            });
        }
      });
    },
    getAddress() {
      this.$ajax.post("/api/user/address/all").then(res => {
        console.log("res:", res);
        if (res.data.ret == "0") {
          const address = res.data.data.address;
          // console.log("Address:", address);
          var default_address = [],
            other_address = [];
          address.forEach(addr => {
            // console.log(addr);
            if (addr.status == "0") default_address.push(addr);
            else other_address.push(addr);
          });
          this.addressList.default_address.addresses = default_address;
          this.addressList.other_address.addresses = other_address;
          console.log(this.addressList);
        }
      });
    }
  },
  mounted() {
    this.getAddress();
    this.pageLoading = false;
    this.settlementShow = true;
    // var timer = setInterval(() => {
    //   console.log(
    //     this.$store.state.cartList.length,
    //     this.$store.state.cartLock
    //   );

    //   if (this.$store.state.cartList.length != 0) {
    //     this.pageLoading = false;
    //     this.settlementShow = true;
    //     clearInterval(timer);
    //   } else if (this.$store.state.cartLock == false) {
    //     this.$message({
    //       message: "购物车空空如也",
    //       type: "warning"
    //     });
    //     this.$router.go(-1);
    //     clearInterval(timer);
    //   }
    // }, 100);

  }
};
</script>
