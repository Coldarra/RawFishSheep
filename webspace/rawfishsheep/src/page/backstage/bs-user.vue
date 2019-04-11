<template>
  <div id="bs-user">
    <el-container>
      <el-table :data="tableData" height="100%" border style="width: 100%">
        <el-table-column fixed prop="userName" label="用户名" width="150"></el-table-column>
        <el-table-column prop="userID" label="用户ID" width="120"></el-table-column>
        <el-table-column prop="permission" label="用户类型" width="120"></el-table-column>
        <el-table-column prop="province" label="省份" width="120"></el-table-column>
        <el-table-column prop="city" label="市区" width="200"></el-table-column>
        <el-table-column prop="address" label="地址" width="300"></el-table-column>
        <el-table-column fixed="right" label="操作" width="100">
          <template slot-scope="scope">
            <el-button @click="handleClick(scope.row)" type="text" size="small">查看</el-button>
            <el-button type="text" size="small">编辑</el-button>
          </template>
        </el-table-column>
      </el-table>
    </el-container>
  </div>
</template>

<style lang="scss" scoped>
</style>


<script>
export default {
  name: "bs-user",
  data() {
    return {
      tableData: [
        {
          userName: "admin111",
          userID: "10001",
          permission: "管理员",
          province: "上海",
          city: "奉贤区",
          address: "上海市奉贤区海思路 999 号"
        },
        {
          userName: "admin222",
          userID: "10002",
          permission: "管理员",
          province: "上海",
          city: "奉贤区",
          address: "上海市奉贤区海思路 999 号"
        },
        {
          userName: "admin333",
          userID: "10003",
          permission: "管理员",
          province: "上海",
          city: "奉贤区",
          address: "上海市奉贤区海思路 999 号"
        },
        {
          userName: "王小鼠",
          userID: "20001",
          permission: "会员",
          province: "上海",
          city: "奉贤区",
          address: "上海市奉贤区海思路 999 号"
        },
        {
          userName: "王小牛",
          userID: "20002",
          permission: "会员",
          province: "上海",
          city: "奉贤区",
          address: "上海市奉贤区海思路 999 号"
        },
        {
          userName: "王小虎",
          userID: "20003",
          permission: "会员",
          province: "上海",
          city: "奉贤区",
          address: "上海市奉贤区海思路 999 号"
        },
        {
          userName: "赵钱孙",
          userID: "30001",
          permission: "普通用户",
          province: "上海",
          city: "奉贤区",
          address: "上海市奉贤区海思路 999 号"
        },
        {
          userName: "李周吴",
          userID: "30002",
          permission: "普通用户",
          province: "上海",
          city: "奉贤区",
          address: "上海市奉贤区海思路 999 号"
        },
        {
          userName: "郑王",
          userID: "30003",
          permission: "普通用户",
          province: "上海",
          city: "奉贤区",
          address: "上海市奉贤区海思路 999 号"
        },
        {
          userName: "李白",
          userID: "40001",
          permission: "配送员",
          province: "上海",
          city: "奉贤区",
          address: "上海市奉贤区海思路 999 号"
        },
        {
          userName: "杜甫",
          userID: "40002",
          permission: "配送员",
          province: "上海",
          city: "奉贤区",
          address: "上海市奉贤区海思路 999 号"
        },
        {
          userName: "白居易",
          userID: "40003",
          permission: "配送员",
          province: "上海",
          city: "奉贤区",
          address: "上海市奉贤区海思路 999 号"
        }
      ]
    };
  },
  methods: {
    handleClick(row) {
      console.log(row);
    }
  }
};
</script>
