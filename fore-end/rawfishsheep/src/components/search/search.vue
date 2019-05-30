<template>
  <div id="search">
    <el-container>
      <el-container style="border: 1px solid #eee; width: 77%">
        <el-aside style="border-right: green; width: 15%">
          <el-card
            :body-style="{ padding: '0px', height: '100%' }"
            style="height: 100%; background: #f3f3f3"
          >
            <div class="vertical-center">筛选：</div>
          </el-card>
        </el-aside>
        <el-container>
          <el-main>
            <div style="margin: 0% 18%" class="line">
              <div v-for="(items, id) in category" :key="id">
                <el-radio-group v-model="radio[id]">
                  <el-radio-button
                    v-for="(bitem, bid) in items"
                    :key="bid"
                    :label="bitem.label"
                    @click.native.prevent="showChildCategory(bitem.children, bitem.level, bitem.label)"
                  ></el-radio-button>
                </el-radio-group>

              </div>
            </div>
          </el-main>
          <el-aside>
            <div class="vertical-center">
              <div>
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
              </div>
            </div>
          </el-aside>
        </el-container>
      </el-container>
      <el-container v-show="searchAlert" style="margin: 20px">
        <div>
          <el-alert title="提示" type="error" description="抱歉，没有符合筛选条件的商品" effect="dark" show-icon></el-alert>
        </div>
      </el-container>
      <el-main id="gridShow" v-show="visible" style="width: 80%">
        <el-row v-for="r in row" :key="r" :gutter="20" style="margin-bottom: 10px">
          <el-col :span="6" v-for="(item, id) in gridGoods[r]" :key="id">
            <el-card :body-style="{ padding: '0px' }" shadow="hover">
              <img :src="item.picture_url" class="image" style="width: 235px; height: 235px">
              <div style="padding: 14px;">
                <div style="text-align:left; color:#e4393c">{{ item.price }}￥</div>
                <div style="text-align:left">
                  <el-link :underline="false">{{ item.name }}</el-link>
                </div>
                <div style="text-align:left">
                  <el-tag :type="tags[item.category]">{{ item.category }}</el-tag>
                </div>
                <!-- <el-rate v-model="rates" disabled show-score style="text-align:left"></el-rate> -->
                <div style="text-align:left">库存 ：{{ item.remain }}{{ item.unit }}</div>
                <div>
                  <el-button
                    type="text"
                    icon="el-icon-shopping-cart-full"
                    @click="Public.addToCartList(item.goods_id)"
                  >加入购物车</el-button>
                </div>
              </div>
            </el-card>
          </el-col>
        </el-row>
      </el-main>
      <el-main id="listShow" v-show="!visible" style="width: 80%">
        <el-card
          v-for="(item, id) in listGoods"
          :key="id"
          :body-style="{ padding: '0px', height: '50%' }"
          style="margin-bottom: 10px"
          shadow="hover"
        >
          <div>
            <div style="display: inline">
              <img :src="item.picture_url" class="image" style="width: 235px; height: 235px">
            </div>
            <div style="display: inline-block">
              <div style="text-align:left">
                <el-link :underline="false">{{ item.name }}</el-link>
              </div>
              <el-rate v-model="rates" disabled show-score style="text-align:center"></el-rate>
              <div style="text-align:left; color:#e4393c">{{ item.price }}￥</div>
              <div style="text-align:left">
                <el-tag type="warning">{{ item.category }}</el-tag>
              </div>
              <div style="text-align:left">
                <div style="text-align:left">库存 ：{{ item.remain }}{{ item.unit }}</div>
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
.vertical-center {
  height: 100%;
  font-weight: bold;
  text-align: center;
  display: flex;
  align-items: center;
  justify-content: center;
}
</style>

<script>
export default {
  name: "search",
  data() {
    return {
      totalGoods: [],
      goods: [],
      listGoods: [],
      gridGoods: [],
      category: [],
      row: [],
      tags: {
        蔬菜: "success",
        水果: "info",
        海鲜: "warning",
        肉类: "danger",
        熟食: "",
        其他: ""
      },
      allCategory: {},
      filterCategory: [],
      searchResult: 0,
      pageSize: 8,
      visible: true,
      searchAlert: false,
      rates: 3.3,
      currentPage: 1,
      radio: [],
    };
  },
  created: function() {
    this.getSearchResult();
    // this.Public.getCategory();

    // let f = this.getCategory;
    this.Public.getCategory().then((result) => {
      console.log("F SUCCESS", result)
      this.getCategory(result);
      // f();
    }).catch(function (error) {
      console.log("F ERROR", error);
    })
    // setTimeout(() => {
    //   this.getCategory();
    // }, 100);
    // this.getCategory();
    // this.category = this.$store.state.category;
  },
  mounted: function() {
    this.category = this.$store.state.category;
  },
  methods: {
    handleCurrentChange(val) {
      console.log(`当前页: ${val}`);
      this.currentPage = val;
      this.changePages(val);
    },
    changeShow(i) {
      this.visible = i === "1";
      // if (i === "1") {
      //   this.visible = true;
      // } else {
      //   this.visible = false;
      // }
    },
    getSearchResult() {
      this.$ajax
        .post("/api/goods/all", {})
        .then(res => {
          if (res.data.ret == "0") {
            this.totalGoods = res.data.data.goods;
            this.goods = res.data.data.goods;
            this.searchResult = this.goods.length;
            // console.log(res);
            this.handleCurrentChange(1);
          }
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
        for (
          let j = 0;
          j < 4 && index < tempGoods.length && cnt <= pageSize;
          j++
        ) {
          if (index >= tempGoods.length) break;
          this.listGoods.push(tempGoods[index]);
          tempArray.push(tempGoods[index++]);
          cnt++;
        }
        this.gridGoods.push(tempArray);
      }
      // console.log("gridGoods:", this.gridGoods);
      // console.log("listGoods:", this.listGoods);
    },
    // getCategory() {
    //   this.$ajax
    //     .post("/api/goods/category/all", {})
    //     .then(res => {
    //       if (res.data.ret == "0") {
    //         let temp = res.data.data.category;
    //         this.category = [];
    //         this.category.push(temp);

    //         console.log("res", res);
    //         this.getCategoryTree(temp);
    //       }
    //     })
    //     .catch(error => {
    //       console.log(error);
    //     });
    // },
    getCategory(ctg) {
      this.category = [];
      this.category.push(ctg);
      this.getCategoryTree(ctg);
      // this.category.push(ctg);
      console.log("SEARCH.VUE, GETCATEGORY", this.category);
    },
    getCategoryTree(ctg) {
      let tempAllCategory = {};
      addCtg(ctg, "top");

      this.allCategory = tempAllCategory;
      console.log("allcategory:", this.allCategory);

      function addCtg(child, parent) {
        for (let i = 0; i < child.length; i++) {
          tempAllCategory[child[i].label] = parent;

          if ("children" in child[i]) {
            addCtg(child[i].children, child[i].label);
          }
        }
      }
    },
    showChildCategory(val, level, ctg) {
      // console.log("val", val);
      while (this.category.length > level) {
        this.category.pop();
      }

      let tempAllCategory = this.allCategory;
      let tcategory = this.category;
      let tradio = [];

      addRadio(ctg);
      function addRadio(ctg) {
        if (tempAllCategory[ctg] != "top") {
          addRadio(tempAllCategory[ctg]);
        }
        tradio.push(ctg);
      }

      // console.log("tradio", tradio);
      this.radio = tradio;
      // console.log("radio:", this.radio);

      let tempCtg = [];
      tempCtg.push(ctg);
      tempCtg = addCtg(val, tempCtg);

      // console.log("tempCtg", tempCtg);
      this.filterCategory = tempCtg;

      let tempGoods = this.totalGoods;
      this.goods = [];
      for (let i = 0; i < tempGoods.length; i++) {
        if (tempCtg.indexOf(tempGoods[i].category) > -1) {
          // console.log(i, tempGoods[i]);
          this.goods.push(tempGoods[i]);
        }
      }

      // console.log("this.goods", this.goods);
      this.$forceUpdate();
      this.changePages(this.currentPage);

      this.searchAlert = this.goods.length === 0 ? true : false;
      // console.log('seachalter', this.searchAlert);
      this.searchResult = this.goods.length;

      if (val === undefined) return;
      this.category.push(val);

      function addCtg(child, temp) {
        if (child === undefined) return temp;
        for (let i = 0; i < child.length; i++) {
          temp.push(child[i].label);

          if ("children" in child[i]) {
            addCtg(child[i].children, temp);
          }
        }
        return temp;
      }
    },
    test() {
      this.category = this.$store.state.category;
    }
  }
};
</script>
