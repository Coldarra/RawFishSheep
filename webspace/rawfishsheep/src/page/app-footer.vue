<template>
  <div id="footer">
    <div class="foothr">
     <hr>
    </div>
    <div class="footer">
      <div class="pull-center">
        <img :src="logo" style="height: 100%">
        <div>
          <i>Copyright © RawFishSheep 2019 All rights reserved</i>
        </div>
      </div>
    </div>
  </div>
</template>

<style lang="scss" scoped>
.foothr {
  margin-left: 3%;
  margin-right: 3%;
}
.footer {
  margin-top: 3rem;
  margin-left: 10%;
  margin-right: 10%;
  margin-bottom: 2rem;
  i {
    color: #b4b4b4;
  }
}
</style>


<script>
export default {
  name: "app-footer",

  data() {
    return {
      logo: require("../assets/images/logo.png")
    };
  }
};
</script>
