<template>
<div class="login-page-container">
    <el-form :model="ruleForm" :rules="rules" ref="ruleForm" label-position="left" label-width="0px" class="demo-ruleForm login-container">
        <h3 class="title">系统登录</h3>
        <el-form-item prop="account">
            <el-input type="text" v-model="ruleForm.account" auto-complete="off" placeholder="账号"></el-input>
        </el-form-item>
        <el-form-item prop="checkPass">
            <el-input type="password" v-model="ruleForm.checkPass" auto-complete="off" placeholder="密码"></el-input>
        </el-form-item>
        <el-checkbox v-model="checked" checked class="remember">记住密码</el-checkbox>
        <!-- <a href="/home">home</a> -->
        <el-form-item style="width:100%;">
            <el-button type="primary" style="width:100%;" @click="handleSubmit2" :loading="logining">登录</el-button>
        </el-form-item>
    </el-form>
</div>
</template>
 
<script>
export default {
    props: {
    },
    data() {
        return {
            logining: false,
            ruleForm: {
                account: 'admin',
                checkPass: '123456'
            },
            rules: {
                account: [{
                        required: true,
                        message: '请输入账号',
                        trigger: 'blur'
                    },
                    //{ validator: validaePass }
                ],
                checkPass: [{
                        required: true,
                        message: '请输入密码',
                        trigger: 'blur'
                    },
                    //{ validator: validaePass2 }
                ]
            },
            checked: true
        };
    },
    methods: {
        handleSubmit2(ev) {
            var _this = this;
            _this.$refs.ruleForm.validate((valid) => {
                if (valid) {
                    _this.logining = true;
                    var loginParams = {
                        username: this.ruleForm.account,
                        password: this.ruleForm.checkPass
                    };
                    if (loginParams.username == "admin" && loginParams.password == "123456") {
                        _this.logining = false;
                        sessionStorage.setItem('user', JSON.stringify(loginParams));
                        _this.$router.push({ path: '/menutab' });
                    } else {
                        _this.logining = false;
                        _this.$alert('用户名或密码错误！', '提示信息', {
                            confirmButtonText: '确定'
                        });
                    }
                } else {
                    console.log('error submit!!');
                    return false;
                }
            });
        }
    }
}
</script>

<style scoped>
.login-container {
    -webkit-border-radius: 5px;
    border-radius: 5px;
    -moz-border-radius: 5px;
    background-clip: padding-box;
    margin: 5rem auto;
    width: 350px;
    padding: 35px 35px 15px;
    background: #fff;
    border: 1px solid #eaeaea;
    box-shadow: 0 0 25px #cac6c6;
}

label.el-checkbox.remember {
    margin: 0px 0px 35px 0px;
}
</style>