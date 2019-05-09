<template>
  <div id="register">
    <div id="registerForm">
      <!-- <h3><div class="">登录</div></h3> -->
      <el-form
        :model="registerForm"
        status-icon
        :rules="registerRules"
        ref="registerForm"
        label-width="100px"
        class="demo-registerForm"
      >
        <el-form-item label="用户名" prop="username">
          <el-input v-model="registerForm.username"></el-input>
        </el-form-item>
        <el-form-item label="密码" prop="password">
          <el-input type="password" v-model="registerForm.password" autocomplete="off"></el-input>
        </el-form-item>
        <el-form-item label="手机号" prop="phonenumber">
          <el-input type="number" v-model="registerForm.phonenumber"></el-input>
        </el-form-item>
        <el-form-item label="邮箱" prop="email">
          <el-input type="email" v-model="registerForm.email"></el-input>
        </el-form-item>

        <el-form-item>
          <el-button type="success" plain @click="submitForm('registerForm')">登录</el-button>
          <el-button @click="resetForm('registerForm')">重置</el-button>
        </el-form-item>
      </el-form>
    </div>
  </div>
</template>

<style scoped>
#register {
  padding-left: 5%;
  padding-right: 5%;
}
#registerForm {
  margin-top: 5rem;
  margin-left: 30%;
  margin-right: 30%;
  margin-bottom: 3rem;
}
</style>

<script>
export default {
  name: "register",
  data() {
    return {
      registerForm: {
        username: "",
        password: ""
      },
      registerRules: {
        username: [
          {
            required: true,
            message: "请输入用户名",
            trigger: "blur"
          },
          {
            min: 4,
            max: 20,
            message: "请输入正确长度的用户名",
            trigger: "blur"
          }
        ],
        password: [
          {
            required: true,
            message: "请输入密码",
            trigger: "blur"
          },
          {
            min: 6,
            max: 16,
            message: "请输入正确长度的密码",
            trigger: "blur"
          }
        ],
        phonenumber: [
          {
            required: true,
            trigger: "blur",
            message: "请输入手机号"
          },
          {
            min: 11,
            max: 11,
            trigger: "blur",
            message: "请输入11位手机号"
          }
        ],
        email: [
          {
            required: true,
            type: "email",
            message: "请输入正确的邮箱",
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
            .post("/api/user/register", {
              username: this.registerForm.username,
              password: this.registerForm.password,
              phonenumber: this.registerForm.phonenumber,
              email: this.registerForm.email
            })
            .then(
              res => {
                // console.log(res);
                // console.log(this.$router);
                if (res.data.ret == "0") {
                  this.$message({
                    message: "注册成功",
                    type: "success"
                  });
                  // this.$store.commit("updateUserInfo", res.data.data.user);
                  if (this.$route.query.redirect) {
                    this.$router.push({
                      path: decodeURIComponent(this.$route.query.redirect)
                    });
                  } else {
                    this.$router.go(-1);
                  }
                }
              },
              res => {}
            );
        } else {
          console.log("error submit!!");
          return false;
        }
      });
    },
    resetForm(formName) {
      this.$refs[formName].resetFields();
    }
  }
};
</script>
