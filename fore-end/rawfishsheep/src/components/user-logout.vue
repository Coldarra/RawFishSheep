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
    this.$message({
      message: "退出成功",
      type: "success"
    });
    this.Public.clearAll();
  }
};
</script>
