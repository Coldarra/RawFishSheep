<template>
  <div id="logout"></div>
</template>


<script>
export default {
  name: "logout",
  data() {
    return {};
  },
  mounted() {
    this.$router.push("/");
    this.$ajax.post("/api/user/logout").then(res => {
      if (res.data.ret == "0") {
        this.$message({
          message: "退出成功",
          type: "success"
        });
        this.Public.clearAll();
      }
    });
  }
};
</script>
