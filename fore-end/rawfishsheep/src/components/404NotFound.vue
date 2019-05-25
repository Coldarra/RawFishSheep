<template>
  <div id="NotFound" class="pull-center">
    <div class="wrap">
      <div class="line">
        <p></p>
        <p>404</p>
      </div>
      <div class="line">
        <p>404</p>
        <p>NOT</p>
      </div>
      <div class="line">
        <p>NOT</p>
        <p>FOUNT</p>
      </div>
      <div class="line">
        <p>FOUNT</p>
        <p></p>
      </div>
    </div>
  </div>
</template>


<style lang="scss" scoped>
#NotFound {
  margin-right: 10vw;
  display: flex;
  height: 50vh;
  left: -10%;
  justify-content: center;
  align-items: center;
  // background-color: hsl(0, 0%, 15%);
  color: rgb(192, 235, 255);

  p {
    font-family: "Arial";
    font-weight: bold;
    text-transform: uppercase;
    font-size: 58px;
    height: 50px;
    line-height: 50px;
    margin: 0;
    transition: all 0.5s ease-in-out;
  }
  .line {
    position: relative;
    height: 50px;
    overflow: hidden;
  }
  .line:nth-child(odd) {
    transform: skew(60deg, -30deg) scaleY(0.667);
  }
  .line:nth-child(even) {
    transform: skew(0deg, -30deg) scaleY(1.333);
  }
  .line:nth-child(1) {
    left: 0;
  }
  .line:nth-child(2) {
    left: 29px;
  }
  .line:nth-child(3) {
    left: 58px;
  }
  .line:nth-child(4) {
    left: 87px;
  }
  .wrap:hover .line p {
    transform: translate(0, -50px);
  }
}
</style>

<script>
export default {
  name: "NotFound",
  data() {
    return {};
  }
};
</script>

