<template>
  <div id="search">
    <el-container>
      <el-header>
        <el-link
          icon="el-icon-s-grid"
          :underline="false"
          @click="changeShow('1')"
          style="font-size:30px"
        ></el-link>
        <el-link
          icon="el-icon-s-unfold"
          :underline="false"
          @click="changeShow('2')"
          style="font-size:30px"
        ></el-link>
      </el-header>
      <el-main id="gridShow" v-show="visible" style="width: 80%">
        <el-row
          v-for="r in row"
          :key="r"
          type="flex"
          :gutter="20"
          justify="center"
          class="pull-center"
          style="margin-bottom: 10px"
        >
          <el-col :span="6" v-for="g in gridGoods[r]" :key="g.id">
            <el-card :body-style="{ padding: '0px' }" shadow="hover">
              <img
                src="../../assets/products-images/product9.jpg"
                class="image"
                style="width: 235px; height: 235px"
              >
              <div style="padding: 14px;">
                <div style="text-align:left; color:#e4393c">{{ g.price }}￥</div>
                <div style="text-align:left">
                  <el-link :underline="false">{{ g.name }}</el-link>
                </div>
                <div style="text-align:left">
                  <el-tag type="warning">{{ g.category }}</el-tag>
                </div>
                <!-- <el-rate v-model="rates" disabled show-score style="text-align:left"></el-rate> -->
                <div style="text-align:left">
                  <el-tag type="danger">库存</el-tag>
                  ：{{ g.remain }}{{ g.unit }}
                </div>
                <div>
                  <el-button type="text" icon="el-icon-shopping-cart-full">加入购物车</el-button>
                </div>
              </div>
            </el-card>
          </el-col>
        </el-row>
      </el-main>
      <el-main id="listShow" v-show="!visible" style="width: 80%">
        <el-card
          v-for="g in listGoods"
          :key="g.id"
          :body-style="{ padding: '0px', height: '50%' }"
          style="margin-bottom: 10px"
          shadow="hover"
        >
          <div>
            <div style="display: inline">
              <img
                src="../../assets/products-images/product9.jpg"
                class="image"
                style="width: 235px; height: 235px"
              >
            </div>
            <div style="display: inline-block">
              <div style="text-align:left">
                <el-link :underline="false">{{ g.name }}</el-link>
              </div>
              <el-rate v-model="rates" disabled show-score style="text-align:center"></el-rate>
              <div style="text-align:left; color:#e4393c">{{ g.price }}￥</div>
              <div style="text-align:left">
                <el-tag type="warning">{{ g.category }}</el-tag>
              </div>
              <div style="text-align:left">
                <el-tag type="danger">库存</el-tag>
                ：{{ g.remain }}{{ g.unit }}
              </div>
              <div style="text-align:center">
                <el-button type="text" icon="el-icon-shopping-cart-full">加入购物车</el-button>
              </div>
            </div>
          </div>
        </el-card>
      </el-main>
      <el-footer>
        <el-pagination
          @current-change="handleCurrentChange"
          :current-page.sync="currentPage"
          :page-size="pageSize"
          layout="total, prev, pager, next, jumper"
          :total="searchResult"
          :hide-on-single-page="false"
        ></el-pagination>
      </el-footer>
    </el-container>
  </div>
</template>

<style scoped>
.list-goods-name {
}
</style>

<script>
export default {
  name: "search",
  data() {
    return {
      goods: [],
      listGoods: [],
      gridGoods: [],
      row: [],
      searchResult: 0,
      pageSize: 6,
      visible: true,
      rates: 3.3,
      currentPage: 1,
      times: [1, 2, 3, 4]
    };
  },
  created: function() {
    this.getSearchResult();
  },
  methods: {
    handleCurrentChange(val) {
      console.log(`当前页: ${val}`);
      this.changePages(val);
    },
    changeShow(i) {
      if (i === "1") {
        this.visible = true;
      } else {
        this.visible = false;
      }
    },
    getSearchResult() {
      this.$ajax
        .post("/api/goods/all", {})
        .then(response => {
          this.goods = response.data.data.goods;
          this.searchResult = this.goods.length;
          // console.log(response);
          this.handleCurrentChange(1);
        })
        .catch(error => {
          console.log(error);
        });
    },
    changePages(val) {
      // this.listGoods = this.goods;
      let tempGoods = this.goods;
      let pageSize = this.pageSize;
      if (this.row.length !== 0) this.row = [];
      let total = tempGoods.length - pageSize * (val - 1);
      if (total > pageSize) total = pageSize;
      for (let i = 0; i < Math.ceil(total / 4); i++) {
        this.row.push(i);
      }
      // console.log("row", this.row);

      this.listGoods = [];
      this.gridGoods = [];
      let index = pageSize * (val - 1);
      let cnt = 1;
      for (let i = 0; i < this.row.length; i++) {
        let tempArray = [];
        for (let j = 0; j < 4 && index < tempGoods.length && cnt <= pageSize; j++) {
          if (index >= tempGoods.length) break;
          this.listGoods.push(tempGoods[index]);
          tempArray.push(tempGoods[index++]);
          cnt++;
        }
        this.gridGoods.push(tempArray);
      }
      // console.log("gridGoods:", this.gridGoods);
      // console.log("listGoods:", this.listGoods);
    }
  }
};
</script>
