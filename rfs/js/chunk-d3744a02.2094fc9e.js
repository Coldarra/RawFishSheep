(window["webpackJsonp"]=window["webpackJsonp"]||[]).push([["chunk-d3744a02"],{"503a":function(e,t,s){"use strict";var a=s("bde3"),r=s.n(a);r.a},bde3:function(e,t,s){},c851:function(e,t,s){"use strict";s.r(t);var a=function(){var e=this,t=e.$createElement,s=e._self._c||t;return s("div",{staticClass:"body"},[s("el-dialog",{attrs:{title:"新增收货地址",visible:e.addAddressButtonVisible,width:"50%"},on:{"update:visible":function(t){e.addAddressButtonVisible=t}}},[s("el-form",{ref:"addressForm",attrs:{model:e.addressForm,"status-icon":"",rules:e.addressRules,"label-width":"100px"}},[s("el-form-item",{attrs:{label:"收货人",prop:"name"}},[s("el-input",{model:{value:e.addressForm.name,callback:function(t){e.$set(e.addressForm,"name",t)},expression:"addressForm.name"}})],1),s("el-form-item",{attrs:{label:"手机号",prop:"phonenumber"}},[s("el-input",{attrs:{autocomplete:"off"},model:{value:e.addressForm.phonenumber,callback:function(t){e.$set(e.addressForm,"phonenumber",t)},expression:"addressForm.phonenumber"}})],1),s("el-form-item",{attrs:{label:"地址",prop:"address"}},[s("el-input",{attrs:{autocomplete:"off"},model:{value:e.addressForm.address,callback:function(t){e.$set(e.addressForm,"address",t)},expression:"addressForm.address"}})],1),s("el-form-item",{attrs:{label:"详情",prop:"detail"}},[s("el-input",{attrs:{autocomplete:"off"},model:{value:e.addressForm.detail,callback:function(t){e.$set(e.addressForm,"detail",t)},expression:"addressForm.detail"}})],1),s("el-form-item",[s("el-button",{attrs:{type:"success",plain:""},on:{click:function(t){return e.submitForm("addressForm")}}},[e._v("保存并使用")]),s("el-button",{on:{click:function(t){return e.resetForm("addressForm")}}},[e._v("重置")])],1),s("span",{staticClass:"dialog-footer",attrs:{slot:"footer"},slot:"footer"},[s("el-button",{on:{click:function(t){e.addAddressButtonVisible=!1}}},[e._v("取 消")]),s("el-button",{attrs:{type:"primary",loading:e.addAddressButtonLoading},on:{click:function(t){e.addAddressButtonVisible=!1,e.addAddressButtonLoading=!0}}},[e._v("确 定")])],1)],1)],1),s("div",{directives:[{name:"loading",rawName:"v-loading",value:e.pageLoading,expression:"pageLoading"}],staticClass:"table-top"},[s("cart"),s("hr"),s("el-collapse-transition",[s("div",{directives:[{name:"show",rawName:"v-show",value:e.settlementShow,expression:"settlementShow"},{name:"loading",rawName:"v-loading",value:e.settlementLoading,expression:"settlementLoading"}],staticClass:"settlement-inf"},[s("el-card",{staticClass:"box-card"},[s("div",{staticClass:"clearfix",attrs:{slot:"header"},slot:"header"},[s("span",[e._v("收货信息")]),s("el-button",{staticClass:"totalprice",attrs:{type:"text"}},[e._v("总价：¥ "+e._s(Number(this.$store.state.totalPrice).toFixed(2)))])],1),s("el-form",{ref:"orderForm",attrs:{model:e.orderForm,"status-icon":"",rules:e.orderRules}},[s("el-form-item",{attrs:{label:"收货地址",prop:"address"}},[s("el-row",{staticClass:"pull-center"},[s("el-col",{attrs:{span:18,offset:2}},[s("el-select",{staticStyle:{width:"100%"},attrs:{filterable:"",placeholder:"请选择收货地址"},model:{value:e.orderForm.address,callback:function(t){e.$set(e.orderForm,"address",t)},expression:"orderForm.address"}},e._l(e.addressList,function(t){return s("el-option-group",{key:t.label,staticClass:"my-option",attrs:{label:t.label}},e._l(t.addresses,function(t){return s("el-option",{key:t.id,attrs:{label:t.detail+" "+t.name+" "+t.phonenumber,value:t.id}},[s("div",{staticClass:"name"},[e._v(e._s(t.name))]),s("div",{staticClass:"addr"},[e._v(e._s(t.phonenumber)+" "+e._s(t.address)+" "+e._s(t.detail))])])}),1)}),1)],1),s("el-col",{attrs:{span:2,offset:1}},[s("el-button",{attrs:{type:"text"},on:{click:function(t){e.addAddressButtonVisible=!0}}},[e._v("新增")])],1)],1)],1),s("br"),s("el-form-item",{attrs:{label:"付款方式",prop:"payment"}},[s("el-row",{staticClass:"pull-center"},[s("el-col",{attrs:{span:18,offset:2}},[s("el-select",{staticStyle:{width:"100%"},attrs:{clearable:"",placeholder:"选择付款方式"},model:{value:e.orderForm.payment,callback:function(t){e.$set(e.orderForm,"payment",t)},expression:"orderForm.payment"}},e._l(e.payments,function(e){return s("el-option",{key:e.value,attrs:{label:e.label,value:e.value}})}),1)],1)],1)],1),s("br"),s("br"),s("el-row",{staticClass:"pull-center"},[s("el-col",{attrs:{span:8,offset:8}},[s("el-button",{staticStyle:{width:"100%"},attrs:{type:"primary"},on:{click:function(t){return e.SubmitOrder("orderForm")}}},[e._v("提交订单")])],1)],1),s("br")],1)],1),s("hr")],1)])],1)],1)},r=[],n=(s("ac6a"),function(){var e=this,t=e.$createElement,s=e._self._c||t;return s("div",[s("el-row",{staticClass:"pull-center",attrs:{gutter:20}},[s("el-col",{attrs:{span:6}},[e._v("\n       \n      "),s("i",{staticClass:"el-icon-tickets"}),e._v(" 商品\n    ")]),s("el-col",{attrs:{span:6}},[e._v("\n       \n      "),s("i",{staticClass:"el-icon-date"}),e._v(" 单价\n    ")]),s("el-col",{attrs:{span:6}},[e._v("\n       \n      "),s("i",{staticClass:"el-icon-edit-outline"}),e._v(" 数量\n    ")]),s("el-col",{attrs:{span:6}},[e._v("\n       \n      "),s("i",{staticClass:"el-icon-setting"}),e._v("\n       选项\n    ")])],1),s("hr"),s("div",{directives:[{name:"loading",rawName:"v-loading",value:this.$store.state.cartLock,expression:"this.$store.state.cartLock"}]},e._l(this.$store.state.cartList,function(t,a){return s("div",{key:a},[s("el-row",{staticClass:"pull-center",attrs:{gutter:20}},[s("el-col",{staticClass:"line pull-left",attrs:{span:6}},[e._v("\n            \n          "),s("img",{staticStyle:{height:"5rem",width:"5rem"},attrs:{src:t.goods.picture_url}}),e._v("\n          "+e._s(t.name)+"\n        ")]),s("el-col",{attrs:{span:6}},[e._v("¥ "+e._s(t.goods.price))]),s("el-col",{attrs:{span:6}},[s("el-input-number",{attrs:{min:1,max:100,step:1,label:"选择数量"},on:{change:function(s){return e.Public.changeCartAmount(t.goods.id,t.amount)}},model:{value:t.amount,callback:function(s){e.$set(t,"amount",s)},expression:"cart.amount"}})],1),s("el-col",{attrs:{span:6}},[s("el-button",{attrs:{type:"danger",icon:"el-icon-delete",circle:""},on:{click:function(s){e.Public.removeFromCartList(t.goods.id),e.deletecheck()}}})],1)],1),s("hr")],1)}),0)],1)}),l=[],o={name:"st-cart",data:function(){return{}},methods:{deletecheck:function(){var e=this;0!=this.$store.state.cartList.length&&setTimeout(function(){e.$message({message:"购物车为空，正在返回首页",type:"info"}),setTimeout(function(){e.$router.push("/")},500)},500)}},mounted:function(){}},d=o,i=s("2877"),c=Object(i["a"])(d,n,l,!1,null,null,null),u=c.exports,m=function(){var e=this,t=e.$createElement,s=e._self._c||t;return s("div")},p=[],f={name:"st-create_address",props:{addAddressButtonVisible:!1,addAddressButtonLoading:!1},data:function(){return{}}},b=f,g=Object(i["a"])(b,m,p,!1,null,null,null),v=g.exports,h=function(){var e=this,t=e.$createElement,s=e._self._c||t;return s("div")},_=[],F={name:"st-manage_address",data:function(){return{}}},y=F,w=Object(i["a"])(y,h,_,!1,null,null,null),x=w.exports,$={name:[{required:!0,min:2,max:10,message:"请输入收货人姓名",trigger:"blur"}],phonenumber:[{required:!0,min:11,max:11,message:"请输入11位手机号",trigger:"blur"}],address:[{required:!0,min:11,max:11,message:"请输入",trigger:"blur"}],detail:[{required:!0,min:11,max:11,message:"请输入",trigger:"blur"}]},k={address:[{required:!0,message:"请选择收货地址",trigger:"blur"}],payment:[{required:!0,message:"请选择支付方式",trigger:"blur"}]},L=[{value:"alipay",label:"支付宝"},{value:"wechat",label:"微信支付"},{value:"jdpay",label:"京东支付"},{value:"unionpay",label:"银联钱包"}],C={name:"",phonenumber:"",address:"",detail:""},A={default_address:{label:"默认地址",addresses:[]},other_address:{label:"其他地址",addresses:[]}},B={address:"",payment:""},S={name:"app-settlement",components:{cart:u,addr_create:v,addr_manage:x},data:function(){return{pageLoading:!0,settlementShow:!1,settlementLoading:!1,addAddressButtonVisible:!1,addAddressButtonLoading:!1,addressForm:C,addressRules:$,addressList:A,payments:L,orderRules:k,orderForm:B}},methods:{submitForm:function(e){},resetForm:function(e){this.$refs[e].resetFields()},SubmitOrder:function(e){var t=this;this.$refs[e].validate(function(e){e&&(t.settlementLoading=!0,t.$ajax.post("/api/order/append",{address_id:t.orderForm.address,paymentname:t.orderForm.payment}).then(function(e){if("0"==e.data.ret){t.settlementLoading=!1,t.Public.fillCartList(),t.$message({message:"订单创建成功",type:"success"});var s=e.data.data.order.serialnumber;t.$router.push("/order/"+s)}}))})},getAddress:function(){var e=this;this.$ajax.post("/api/user/address/all").then(function(t){if(console.log("res:",t),"0"==t.data.ret){var s=t.data.data.address,a=[],r=[];s.forEach(function(e){"0"==e.status?a.push(e):r.push(e)}),e.addressList.default_address.addresses=a,e.addressList.other_address.addresses=r,console.log(e.addressList)}})}},mounted:function(){this.getAddress(),0!=this.$store.state.cartList.length?(this.pageLoading=!1,this.settlementShow=!0):0==this.$store.state.cartLock&&(this.$message({message:"购物车空空如也",type:"warning"}),this.$router.go(-1))}},j=S,V=(s("503a"),Object(i["a"])(j,a,r,!1,null,"824291c8",null));t["default"]=V.exports}}]);
//# sourceMappingURL=chunk-d3744a02.2094fc9e.js.map