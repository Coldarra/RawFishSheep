<template>
  <div id="login">
    <div id="loginForm">
      <!-- <h3><div class="">登录</div></h3> -->
      <el-form
        :model="loginForm"
        status-icon
        :rules="loginRules"
        ref="loginForm"
        label-width="100px"
        class="demo-loginForm"
      >
        <el-form-item label="用户名" prop="username">
          <el-input v-model="loginForm.username"></el-input>
        </el-form-item>
        <el-form-item label="密码" prop="password">
          <el-input type="password" v-model="loginForm.password" autocomplete="off"></el-input>
        </el-form-item>
        <el-form-item>
          <el-button type="success" plain @click="submitForm('loginForm')">登录</el-button>
          <el-button @click="resetForm('loginForm')">重置</el-button>
        </el-form-item>
      </el-form>
    </div>
  </div>
</template>

<style scoped>
#login {
  padding-left: 5%;
  padding-right: 5%;
}
#loginForm {
  margin-top: 7rem;
  margin-left: 30%;
  margin-right: 30%;
  margin-bottom: 8rem;
}
</style>

<script>
export default {
  name: "login",
  data() {
    return {
      loginForm: {
        username: "",
        password: ""
      },
      loginRules: {
        username: [
          {
            required: true,
            min: 4,
            max: 20,
            message: "请输入用户名",
            trigger: "blur"
          }
        ],
        password: [
          {
            required: true,
            min: 6,
            max: 16,
            message: "请输入密码",
            trigger: "blur"
          }
        ]
      },
      logo: require("@/assets/images/logo.png")
    };
  },
  methods: {
    submitForm(formName) {
      this.$refs[formName].validate(valid => {
        if (valid) {
          this.$ajax
            .post("/api/user/login", {
              username: this.loginForm.username,
              password: this.loginForm.password
            })
            .then(res => {
              // console.log(res);
              // console.log(this.$router);
              if (res.data.ret == "0") {
                this.$store.commit("updateUserInfo", res.data.data);
                this.$message({
                  message: "登录成功",
                  type: "success"
                });
                if (this.$route.query.redirect) {
                  this.$router.push({
                    path: decodeURIComponent(this.$route.query.redirect)
                  });
                } else {
                  this.$router.go(-1);
                }
              } else {
              }
            });
        } else {
          console.log("error submit!!");
          return false;
        }
      });
    },
    resetForm(formName) {
      this.$refs[formName].resetFields();
    }
  },
  mounted() {
    if (this.$store.state.isLogin) {
      this.$router.go(-1);
    }
  }
};
</script>
