<template>
  <div id="page">
    <div class="bg">
      <el-container>
        <el-header height="40px">
          <el-row :gutter="0" style="width: 100%">
            <el-col :span="20">
              &ensp;
            </el-col>
            <el-col :span="4">
              <el-button type="text" style="color: #FFF;">账户</el-button>
              <el-button type="text" style="color: #FFF;">结账</el-button>
              <el-button type="text" style="color: #FFF;">登录</el-button>
            </el-col>
          </el-row>
        </el-header>
      </el-container>

      <el-container>
        <el-aside style="font-size: 22px; color: #fff;">
          &ensp;
        </el-aside>
        <el-main style="font-size: 42px; color: #fff; top: 20px;    text-align: center;">
          生🐟鱼🐏羊
        </el-main>
        <el-main>
          <el-form>
            <el-input class="header-search" style="width: 22vw;" placeholder="请输入内容" clearable></el-input>
          </el-form>
        </el-main>
      </el-container>
      <el-container>
        <el-aside width="5%"></el-aside>
        <!--<el-main>-->
        <el-menu mode="horizontal" style="width: 100%; height: 150%;margin: 0 auto;float:left;" background-color="#59b210">
          <el-menu-item index="1" style="background: #e31837;">
              <i class="fa fa-home fa-2x" style="color:white;text-align:center;"></i>
          </el-menu-item> 
        </el-menu>
        <el-menu mode="horizontal" >
          <el-menu-item index="2" :center=true>AAA</el-menu-item>
          <el-menu-item index="3" :center=true>BBB</el-menu-item>
          <el-menu-item index="4" :center=true>CCC</el-menu-item>
          <el-menu-item index="5" :center=true>DDDDDDD</el-menu-item>
        </el-menu>
        <el-menu mode="horizontal" >
          <el-menu-item index="6" style="background: #4fa10b;float:right;">
            <i class="fa fa-shopping-cart fa-2x" style="color:white;text-align:center;"></i>
          </el-menu-item>
        </el-menu>
        <!--</el-main>-->
        <el-aside width="5%"></el-aside>
      </el-container>
    </div>
    <div id="item-slideshow">
      <el-container style="margin: 0 100px 0 100px">
        <el-main style="width: 75%; box-shadow: 0 2px 12px 0 rgba(0, 0, 0, 0.1)">
          <el-carousel height="420px">
            <el-carousel-item v-for="item in 4" :key="item">
              <a href="#"><img src="../assets/images/slide-img1.jpg" alt="slides"/></a>
            </el-carousel-item>
          </el-carousel>
        </el-main>
        <el-container direction="vertical" style="width: 25%; box-shadow: 0 2px 12px 0 rgba(0, 0, 0, 0.1)">
          <el-main>
            <a href="#"><img src="../assets/products-images/product16.jpg" alt="" height="280px" width="280px"/></a>
            <!--<div class="hot-label hot-top-left">Hot</div>-->
            <el-main style="padding: 0 0">
              <a href="#">葡萄</a>
            </el-main>
            <el-main>
              <!-- <el-rate
                v-model="value2"
                :colors="['#99A9BF', '#F7BA2A', '#FF9900']">
              </el-rate> -->
            </el-main>
            <el-main style="padding: 0 0">
              <span>125,000$</span>
            </el-main>
            <el-main>
              <el-button type="success">成功按钮</el-button>
            </el-main>
          </el-main>
        </el-container>
      </el-container>
    </div>
    <div id="feature-box">
      <el-container style="margin: 20px 100px 20px 100px">
        <el-row :gutter="20" style="width: 100%">
          <el-col :span="6">
            <el-card shadow="always" body-style="color:white; background-color:#685c88">
              快速
            </el-card>
          </el-col>
          <el-col :span="6">
            <el-card shadow="always" body-style="color:white; background-color:#94d7fb">
              新鲜
            </el-card>
          </el-col>
          <el-col :span="6">
            <el-card shadow="always" body-style="color:white; background-color:#fc9cc4">
              及时
            </el-card>
          </el-col>
          <el-col :span="6">
            <el-card shadow="always" body-style="color:white; background-color:#e31837">
              优惠
            </el-card>
          </el-col>
        </el-row>
      </el-container>
    </div>
    <div id="new-product">
      <el-container style="margin: 0 100px 0 100px; height: 550px; box-shadow: 0 2px 12px 0 rgba(0, 0, 0, 0.1)">
        <el-header style="float: right">
          <el-tabs>
            <el-tab-pane label="aaa" name="first" style="height: 550px">
              <el-container direction="vertical" style="height: 450px">
                <el-row :gutter="0">
                  <el-col :span="6">
                    <el-main>
                      <a href="#"><img src="../assets/products-images/product16.jpg" alt="" height="280px" width="280px"/></a>
                      <!--<div class="hot-label hot-top-left">Hot</div>-->
                      <el-main style="padding: 0 0">
                        <a href="#">葡萄</a>
                      </el-main>
                      <el-main>
                        <el-rate
                          v-model="value2"
                          :colors="['#99A9BF', '#F7BA2A', '#FF9900']">
                        </el-rate>
                      </el-main>
                      <el-main style="padding: 0 0">
                        <span>125,000$</span>
                      </el-main>
                      <el-main>
                        <el-button type="success">成功按钮</el-button>
                      </el-main>
                    </el-main>
                  </el-col>
                  <el-col :span="6">
                    <el-main>
                      <a href="#"><img src="../assets/products-images/product16.jpg" alt="" height="280px" width="280px"/></a>
                      <!--<div class="hot-label hot-top-left">Hot</div>-->
                      <el-main style="padding: 0 0">
                        <a href="#">葡萄</a>
                      </el-main>
                      <el-main>
                        <el-rate
                          v-model="value2"
                          :colors="['#99A9BF', '#F7BA2A', '#FF9900']">
                        </el-rate>
                      </el-main>
                      <el-main style="padding: 0 0">
                        <span>125,000$</span>
                      </el-main>
                      <el-main>
                        <el-button type="success">成功按钮</el-button>
                      </el-main>
                    </el-main>
                  </el-col>
                  <el-col :span="6">
                    <el-main>
                      <a href="#"><img src="../assets/products-images/product16.jpg" alt="" height="280px" width="280px"/></a>
                      <!--<div class="hot-label hot-top-left">Hot</div>-->
                      <el-main style="padding: 0 0">
                        <a href="#">葡萄</a>
                      </el-main>
                      <el-main>
                        <el-rate
                          v-model="value2"
                          :colors="['#99A9BF', '#F7BA2A', '#FF9900']">
                        </el-rate>
                      </el-main>
                      <el-main style="padding: 0 0">
                        <span>125,000$</span>
                      </el-main>
                      <el-main>
                        <el-button type="success">成功按钮</el-button>
                      </el-main>
                    </el-main>
                  </el-col>
                  <el-col :span="6">
                    <el-main>
                      <a href="#"><img src="../assets/products-images/product16.jpg" alt="" height="280px" width="280px"/></a>
                      <!--<div class="hot-label hot-top-left">Hot</div>-->
                      <el-main style="padding: 0 0">
                        <a href="#">葡萄</a>
                      </el-main>
                      <el-main>
                        <el-rate
                          v-model="value2"
                          :colors="['#99A9BF', '#F7BA2A', '#FF9900']">
                        </el-rate>
                      </el-main>
                      <el-main style="padding: 0 0">
                        <span>125,000$</span>
                      </el-main>
                      <el-main>
                        <el-button type="success">成功按钮</el-button>
                      </el-main>
                    </el-main>
                  </el-col>
                </el-row>
              </el-container>
            </el-tab-pane>
            <el-tab-pane label="bbb" name="second" style="height: 550px">
              <el-container direction="vertical" style="height: 450px">
                <el-row :gutter="0">
                  <el-col :span="6">
                    <el-main>
                      <a href="#"><img src="../assets/products-images/product1.jpg" alt="" height="280px" width="280px"/></a>
                      <!--<div class="hot-label hot-top-left">Hot</div>-->
                      <el-main style="padding: 0 0">
                        <a href="#">葡萄</a>
                      </el-main>
                      <el-main>
                        <el-rate
                          v-model="value2"
                          :colors="['#99A9BF', '#F7BA2A', '#FF9900']">
                        </el-rate>
                      </el-main>
                      <el-main style="padding: 0 0">
                        <span>125,000$</span>
                      </el-main>
                      <el-main>
                        <el-button type="success">成功按钮</el-button>
                      </el-main>
                    </el-main>
                  </el-col>
                  <el-col :span="6">
                    <el-main>
                      <a href="#"><img src="../assets/products-images/product1.jpg" alt="" height="280px" width="280px"/></a>
                      <!--<div class="hot-label hot-top-left">Hot</div>-->
                      <el-main style="padding: 0 0">
                        <a href="#">葡萄</a>
                      </el-main>
                      <el-main>
                        <el-rate
                          v-model="value2"
                          :colors="['#99A9BF', '#F7BA2A', '#FF9900']">
                        </el-rate>
                      </el-main>
                      <el-main style="padding: 0 0">
                        <span>125,000$</span>
                      </el-main>
                      <el-main>
                        <el-button type="success">成功按钮</el-button>
                      </el-main>
                    </el-main>
                  </el-col>
                  <el-col :span="6">
                    <el-main>
                      <a href="#"><img src="../assets/products-images/product1.jpg" alt="" height="280px" width="280px"/></a>
                      <!--<div class="hot-label hot-top-left">Hot</div>-->
                      <el-main style="padding: 0 0">
                        <a href="#">葡萄</a>
                      </el-main>
                      <el-main>
                        <el-rate
                          v-model="value2"
                          :colors="['#99A9BF', '#F7BA2A', '#FF9900']">
                        </el-rate>
                      </el-main>
                      <el-main style="padding: 0 0">
                        <span>125,000$</span>
                      </el-main>
                      <el-main>
                        <el-button type="success">成功按钮</el-button>
                      </el-main>
                    </el-main>
                  </el-col>
                  <el-col :span="6">
                    <el-main>
                      <a href="#"><img src="../assets/products-images/product1.jpg" alt="" height="280px" width="280px"/></a>
                      <!--<div class="hot-label hot-top-left">Hot</div>-->
                      <el-main style="padding: 0 0">
                        <a href="#">葡萄</a>
                      </el-main>
                      <el-main>
                        <el-rate
                          v-model="value2"
                          :colors="['#99A9BF', '#F7BA2A', '#FF9900']">
                        </el-rate>
                      </el-main>
                      <el-main style="padding: 0 0">
                        <span>125,000$</span>
                      </el-main>
                      <el-main>
                        <el-button type="success">成功按钮</el-button>
                      </el-main>
                    </el-main>
                  </el-col>
                </el-row>
              </el-container>
            </el-tab-pane>
            <el-tab-pane label="ccc" name="third" style="height: 550px">
              <el-container direction="vertical" style="height: 450px">
                <el-row :gutter="0">
                  <el-col :span="6">
                    <el-main>
                      <a href="#"><img src="../assets/products-images/product2.jpg" alt="" height="280px" width="280px"/></a>
                      <!--<div class="hot-label hot-top-left">Hot</div>-->
                      <el-main style="padding: 0 0">
                        <a href="#">葡萄</a>
                      </el-main>
                      <el-main>
                        <el-rate
                          v-model="value2"
                          :colors="['#99A9BF', '#F7BA2A', '#FF9900']">
                        </el-rate>
                      </el-main>
                      <el-main style="padding: 0 0">
                        <span>125,000$</span>
                      </el-main>
                      <el-main>
                        <el-button type="success">成功按钮</el-button>
                      </el-main>
                    </el-main>
                  </el-col>
                  <el-col :span="6">
                    <el-main>
                      <a href="#"><img src="../assets/products-images/product12.jpg" alt="" height="280px" width="280px"/></a>
                      <!--<div class="hot-label hot-top-left">Hot</div>-->
                      <el-main style="padding: 0 0">
                        <a href="#">葡萄</a>
                      </el-main>
                      <el-main>
                        <el-rate
                          v-model="value2"
                          :colors="['#99A9BF', '#F7BA2A', '#FF9900']">
                        </el-rate>
                      </el-main>
                      <el-main style="padding: 0 0">
                        <span>125,000$</span>
                      </el-main>
                      <el-main>
                        <el-button type="success">成功按钮</el-button>
                      </el-main>
                    </el-main>
                  </el-col>
                  <el-col :span="6">
                    <el-main>
                      <a href="#"><img src="../assets/products-images/product2.jpg" alt="" height="280px" width="280px"/></a>
                      <!--<div class="hot-label hot-top-left">Hot</div>-->
                      <el-main style="padding: 0 0">
                        <a href="#">葡萄</a>
                      </el-main>
                      <el-main>
                        <el-rate
                          v-model="value2"
                          :colors="['#99A9BF', '#F7BA2A', '#FF9900']">
                        </el-rate>
                      </el-main>
                      <el-main style="padding: 0 0">
                        <span>125,000$</span>
                      </el-main>
                      <el-main>
                        <el-button type="success">成功按钮</el-button>
                      </el-main>
                    </el-main>
                  </el-col>
                  <el-col :span="6">
                    <el-main>
                      <a href="#"><img src="../assets/products-images/product12.jpg" alt="" height="280px" width="280px"/></a>
                      <!--<div class="hot-label hot-top-left">Hot</div>-->
                      <el-main style="padding: 0 0">
                        <a href="#">葡萄</a>
                      </el-main>
                      <el-main>
                        <el-rate
                          v-model="value2"
                          :colors="['#99A9BF', '#F7BA2A', '#FF9900']">
                        </el-rate>
                      </el-main>
                      <el-main style="padding: 0 0">
                        <span>125,000$</span>
                      </el-main>
                      <el-main>
                        <el-button type="success">成功按钮</el-button>
                      </el-main>
                    </el-main>
                  </el-col>
                </el-row>
              </el-container>
            </el-tab-pane>
            <el-tab-pane label="ddd" name="fourth" style="height: 550px">
              <el-container direction="vertical" style="height: 450px">
                <el-row :gutter="0">
                  <el-col :span="6">
                    <el-main>
                      <a href="#"><img src="../assets/products-images/product3.jpg" alt="" height="280px" width="280px"/></a>
                      <!--<div class="hot-label hot-top-left">Hot</div>-->
                      <el-main style="padding: 0 0">
                        <a href="#">葡萄</a>
                      </el-main>
                      <el-main>
                        <el-rate
                          v-model="value2"
                          :colors="['#99A9BF', '#F7BA2A', '#FF9900']">
                        </el-rate>
                      </el-main>
                      <el-main style="padding: 0 0">
                        <span>125,000$</span>
                      </el-main>
                      <el-main>
                        <el-button type="success">成功按钮</el-button>
                      </el-main>
                    </el-main>
                  </el-col>
                  <el-col :span="6">
                    <el-main>
                      <a href="#"><img src="../assets/products-images/product3.jpg" alt="" height="280px" width="280px"/></a>
                      <!--<div class="hot-label hot-top-left">Hot</div>-->
                      <el-main style="padding: 0 0">
                        <a href="#">葡萄</a>
                      </el-main>
                      <el-main>
                        <el-rate
                          v-model="value2"
                          :colors="['#99A9BF', '#F7BA2A', '#FF9900']">
                        </el-rate>
                      </el-main>
                      <el-main style="padding: 0 0">
                        <span>125,000$</span>
                      </el-main>
                      <el-main>
                        <el-button type="success">成功按钮</el-button>
                      </el-main>
                    </el-main>
                  </el-col>
                  <el-col :span="6">
                    <el-main>
                      <a href="#"><img src="../assets/products-images/product3.jpg" alt="" height="280px" width="280px"/></a>
                      <!--<div class="hot-label hot-top-left">Hot</div>-->
                      <el-main style="padding: 0 0">
                        <a href="#">葡萄</a>
                      </el-main>
                      <el-main>
                        <el-rate
                          v-model="value2"
                          :colors="['#99A9BF', '#F7BA2A', '#FF9900']">
                        </el-rate>
                      </el-main>
                      <el-main style="padding: 0 0">
                        <span>125,000$</span>
                      </el-main>
                      <el-main>
                        <el-button type="success">成功按钮</el-button>
                      </el-main>
                    </el-main>
                  </el-col>
                  <el-col :span="6">
                    <el-main>
                      <a href="#"><img src="../assets/products-images/product3.jpg" alt="" height="280px" width="280px"/></a>
                      <!--<div class="hot-label hot-top-left">Hot</div>-->
                      <el-main style="padding: 0 0">
                        <a href="#">葡萄</a>
                      </el-main>
                      <el-main>
                        <el-rate
                          v-model="value2"
                          :colors="['#99A9BF', '#F7BA2A', '#FF9900']">
                        </el-rate>
                      </el-main>
                      <el-main style="padding: 0 0">
                        <span>125,000$</span>
                      </el-main>
                      <el-main>
                        <el-button type="success">成功按钮</el-button>
                      </el-main>
                    </el-main>
                  </el-col>
                </el-row>
              </el-container>
            </el-tab-pane>
          </el-tabs>
        </el-header>
      </el-container>
    </div>
    <div id="best-sell" style="margin-top: 30px">
      <el-container style="margin: 0 100px 0 100px; height: 550px; box-shadow: 0 2px 12px 0 rgba(0, 0, 0, 0.1)">
        <el-header style="float: right">
          <el-tabs>
            <el-tab-pane label="aaa" name="first" style="height: 550px">
              <el-container direction="vertical" style="height: 450px">
                <el-row :gutter="0">
                  <el-col :span="6">
                    <el-main>
                      <a href="#"><img src="../assets/products-images/product16.jpg" alt="" height="280px" width="280px"/></a>
                      <!--<div class="hot-label hot-top-left">Hot</div>-->
                      <el-main style="padding: 0 0">
                        <a href="#">葡萄</a>
                      </el-main>
                      <el-main>
                        <el-rate
                          v-model="value2"
                          :colors="['#99A9BF', '#F7BA2A', '#FF9900']">
                        </el-rate>
                      </el-main>
                      <el-main style="padding: 0 0">
                        <span>125,000$</span>
                      </el-main>
                      <el-main>
                        <el-button type="success">成功按钮</el-button>
                      </el-main>
                    </el-main>
                  </el-col>
                  <el-col :span="6">
                    <el-main>
                      <a href="#"><img src="../assets/products-images/product16.jpg" alt="" height="280px" width="280px"/></a>
                      <!--<div class="hot-label hot-top-left">Hot</div>-->
                      <el-main style="padding: 0 0">
                        <a href="#">葡萄</a>
                      </el-main>
                      <el-main>
                        <el-rate
                          v-model="value2"
                          :colors="['#99A9BF', '#F7BA2A', '#FF9900']">
                        </el-rate>
                      </el-main>
                      <el-main style="padding: 0 0">
                        <span>125,000$</span>
                      </el-main>
                      <el-main>
                        <el-button type="success">成功按钮</el-button>
                      </el-main>
                    </el-main>
                  </el-col>
                  <el-col :span="6">
                    <el-main>
                      <a href="#"><img src="../assets/products-images/product16.jpg" alt="" height="280px" width="280px"/></a>
                      <!--<div class="hot-label hot-top-left">Hot</div>-->
                      <el-main style="padding: 0 0">
                        <a href="#">葡萄</a>
                      </el-main>
                      <el-main>
                        <el-rate
                          v-model="value2"
                          :colors="['#99A9BF', '#F7BA2A', '#FF9900']">
                        </el-rate>
                      </el-main>
                      <el-main style="padding: 0 0">
                        <span>125,000$</span>
                      </el-main>
                      <el-main>
                        <el-button type="success">成功按钮</el-button>
                      </el-main>
                    </el-main>
                  </el-col>
                  <el-col :span="6">
                    <el-main>
                      <a href="#"><img src="../assets/products-images/product16.jpg" alt="" height="280px" width="280px"/></a>
                      <!--<div class="hot-label hot-top-left">Hot</div>-->
                      <el-main style="padding: 0 0">
                        <a href="#">葡萄</a>
                      </el-main>
                      <el-main>
                        <el-rate
                          v-model="value2"
                          :colors="['#99A9BF', '#F7BA2A', '#FF9900']">
                        </el-rate>
                      </el-main>
                      <el-main style="padding: 0 0">
                        <span>125,000$</span>
                      </el-main>
                      <el-main>
                        <el-button type="success">成功按钮</el-button>
                      </el-main>
                    </el-main>
                  </el-col>
                </el-row>
              </el-container>
            </el-tab-pane>
            <el-tab-pane label="bbb" name="second" style="height: 550px">
              <el-container direction="vertical" style="height: 450px">
                <el-row :gutter="0">
                  <el-col :span="6">
                    <el-main>
                      <a href="#"><img src="../assets/products-images/product1.jpg" alt="" height="280px" width="280px"/></a>
                      <!--<div class="hot-label hot-top-left">Hot</div>-->
                      <el-main style="padding: 0 0">
                        <a href="#">葡萄</a>
                      </el-main>
                      <el-main>
                        <el-rate
                          v-model="value2"
                          :colors="['#99A9BF', '#F7BA2A', '#FF9900']">
                        </el-rate>
                      </el-main>
                      <el-main style="padding: 0 0">
                        <span>125,000$</span>
                      </el-main>
                      <el-main>
                        <el-button type="success">成功按钮</el-button>
                      </el-main>
                    </el-main>
                  </el-col>
                  <el-col :span="6">
                    <el-main>
                      <a href="#"><img src="../assets/products-images/product1.jpg" alt="" height="280px" width="280px"/></a>
                      <!--<div class="hot-label hot-top-left">Hot</div>-->
                      <el-main style="padding: 0 0">
                        <a href="#">葡萄</a>
                      </el-main>
                      <el-main>
                        <el-rate
                          v-model="value2"
                          :colors="['#99A9BF', '#F7BA2A', '#FF9900']">
                        </el-rate>
                      </el-main>
                      <el-main style="padding: 0 0">
                        <span>125,000$</span>
                      </el-main>
                      <el-main>
                        <el-button type="success">成功按钮</el-button>
                      </el-main>
                    </el-main>
                  </el-col>
                  <el-col :span="6">
                    <el-main>
                      <a href="#"><img src="../assets/products-images/product1.jpg" alt="" height="280px" width="280px"/></a>
                      <!--<div class="hot-label hot-top-left">Hot</div>-->
                      <el-main style="padding: 0 0">
                        <a href="#">葡萄</a>
                      </el-main>
                      <el-main>
                        <el-rate
                          v-model="value2"
                          :colors="['#99A9BF', '#F7BA2A', '#FF9900']">
                        </el-rate>
                      </el-main>
                      <el-main style="padding: 0 0">
                        <span>125,000$</span>
                      </el-main>
                      <el-main>
                        <el-button type="success">成功按钮</el-button>
                      </el-main>
                    </el-main>
                  </el-col>
                  <el-col :span="6">
                    <el-main>
                      <a href="#"><img src="../assets/products-images/product1.jpg" alt="" height="280px" width="280px"/></a>
                      <!--<div class="hot-label hot-top-left">Hot</div>-->
                      <el-main style="padding: 0 0">
                        <a href="#">葡萄</a>
                      </el-main>
                      <el-main>
                        <el-rate
                          v-model="value2"
                          :colors="['#99A9BF', '#F7BA2A', '#FF9900']">
                        </el-rate>
                      </el-main>
                      <el-main style="padding: 0 0">
                        <span>125,000$</span>
                      </el-main>
                      <el-main>
                        <el-button type="success">成功按钮</el-button>
                      </el-main>
                    </el-main>
                  </el-col>
                </el-row>
              </el-container>
            </el-tab-pane>
            <el-tab-pane label="ccc" name="third" style="height: 550px">
              <el-container direction="vertical" style="height: 450px">
                <el-row :gutter="0">
                  <el-col :span="6">
                    <el-main>
                      <a href="#"><img src="../assets/products-images/product2.jpg" alt="" height="280px" width="280px"/></a>
                      <!--<div class="hot-label hot-top-left">Hot</div>-->
                      <el-main style="padding: 0 0">
                        <a href="#">葡萄</a>
                      </el-main>
                      <el-main>
                        <el-rate
                          v-model="value2"
                          :colors="['#99A9BF', '#F7BA2A', '#FF9900']">
                        </el-rate>
                      </el-main>
                      <el-main style="padding: 0 0">
                        <span>125,000$</span>
                      </el-main>
                      <el-main>
                        <el-button type="success">成功按钮</el-button>
                      </el-main>
                    </el-main>
                  </el-col>
                  <el-col :span="6">
                    <el-main>
                      <a href="#"><img src="../assets/products-images/product12.jpg" alt="" height="280px" width="280px"/></a>
                      <!--<div class="hot-label hot-top-left">Hot</div>-->
                      <el-main style="padding: 0 0">
                        <a href="#">葡萄</a>
                      </el-main>
                      <el-main>
                        <el-rate
                          v-model="value2"
                          :colors="['#99A9BF', '#F7BA2A', '#FF9900']">
                        </el-rate>
                      </el-main>
                      <el-main style="padding: 0 0">
                        <span>125,000$</span>
                      </el-main>
                      <el-main>
                        <el-button type="success">成功按钮</el-button>
                      </el-main>
                    </el-main>
                  </el-col>
                  <el-col :span="6">
                    <el-main>
                      <a href="#"><img src="../assets/products-images/product2.jpg" alt="" height="280px" width="280px"/></a>
                      <!--<div class="hot-label hot-top-left">Hot</div>-->
                      <el-main style="padding: 0 0">
                        <a href="#">葡萄</a>
                      </el-main>
                      <el-main>
                        <el-rate
                          v-model="value2"
                          :colors="['#99A9BF', '#F7BA2A', '#FF9900']">
                        </el-rate>
                      </el-main>
                      <el-main style="padding: 0 0">
                        <span>125,000$</span>
                      </el-main>
                      <el-main>
                        <el-button type="success">成功按钮</el-button>
                      </el-main>
                    </el-main>
                  </el-col>
                  <el-col :span="6">
                    <el-main>
                      <a href="#"><img src="../assets/products-images/product12.jpg" alt="" height="280px" width="280px"/></a>
                      <!--<div class="hot-label hot-top-left">Hot</div>-->
                      <el-main style="padding: 0 0">
                        <a href="#">葡萄</a>
                      </el-main>
                      <el-main>
                        <el-rate
                          v-model="value2"
                          :colors="['#99A9BF', '#F7BA2A', '#FF9900']">
                        </el-rate>
                      </el-main>
                      <el-main style="padding: 0 0">
                        <span>125,000$</span>
                      </el-main>
                      <el-main>
                        <el-button type="success">成功按钮</el-button>
                      </el-main>
                    </el-main>
                  </el-col>
                </el-row>
              </el-container>
            </el-tab-pane>
            <el-tab-pane label="ddd" name="fourth" style="height: 550px">
              <el-container direction="vertical" style="height: 450px">
                <el-row :gutter="0">
                  <el-col :span="6" style="border-left: 1px solid gray; border-bottom: 2px solid; border-right: 1px solid; border-top: 3px solid green">
                    <el-main>
                      <a href="#"><img src="../assets/products-images/product3.jpg" alt="" height="280px" width="280px"/></a>
                      <!--<div class="hot-label hot-top-left">Hot</div>-->
                      <el-main style="padding: 0 0">
                        <a href="#">葡萄</a>
                      </el-main>
                      <el-main>
                        <el-rate
                          v-model="value2"
                          :colors="['#99A9BF', '#F7BA2A', '#FF9900']">
                        </el-rate>
                      </el-main>
                      <el-main style="padding: 0 0">
                        <span>125,000$</span>
                      </el-main>
                      <el-main>
                        <el-button type="success">成功按钮</el-button>
                      </el-main>
                    </el-main>
                  </el-col>
                  <el-col :span="6" style="border-left: 1px solid gray; border-bottom: 2px solid; border-right: 1px solid; border-top: 3px solid green">
                    <el-main>
                      <a href="#"><img src="../assets/products-images/product3.jpg" alt="" height="280px" width="280px"/></a>
                      <!--<div class="hot-label hot-top-left">Hot</div>-->
                      <el-main style="padding: 0 0">
                        <a href="#">葡萄</a>
                      </el-main>
                      <el-main>
                        <el-rate
                          v-model="value2"
                          :colors="['#99A9BF', '#F7BA2A', '#FF9900']">
                        </el-rate>
                      </el-main>
                      <el-main style="padding: 0 0">
                        <span>125,000$</span>
                      </el-main>
                      <el-main>
                        <el-button type="success">成功按钮</el-button>
                      </el-main>
                    </el-main>
                  </el-col>
                  <el-col :span="6" style="border-left: 1px solid gray; border-bottom: 2px solid; border-right: 1px solid; border-top: 3px solid green">
                    <el-main>
                      <a href="#"><img src="../assets/products-images/product3.jpg" alt="" height="280px" width="280px"/></a>
                      <!--<div class="hot-label hot-top-left">Hot</div>-->
                      <el-main style="padding: 0 0">
                        <a href="#">葡萄</a>
                      </el-main>
                      <el-main>
                        <el-rate
                          v-model="value2"
                          :colors="['#99A9BF', '#F7BA2A', '#FF9900']">
                        </el-rate>
                      </el-main>
                      <el-main style="padding: 0 0">
                        <span>125,000$</span>
                      </el-main>
                      <el-main>
                        <el-button type="success">成功按钮</el-button>
                      </el-main>
                    </el-main>
                  </el-col>
                  <el-col :span="6" style="border-left: 1px solid gray; border-bottom: 2px solid; border-right: 1px solid; border-top: 3px solid green">
                    <el-main>
                      <a href="#"><img src="../assets/products-images/product3.jpg" alt="" height="280px" width="280px"/></a>
                      <!--<div class="hot-label hot-top-left">Hot</div>-->
                      <el-main style="padding: 0 0">
                        <a href="#">葡萄</a>
                      </el-main>
                      <el-main>
                        <el-rate
                          v-model="value2"
                          :colors="['#99A9BF', '#F7BA2A', '#FF9900']">
                        </el-rate>
                      </el-main>
                      <el-main style="padding: 0 0">
                        <span>125,000$</span>
                      </el-main>
                      <el-main>
                        <el-button type="success">成功按钮</el-button>
                      </el-main>
                    </el-main>
                  </el-col>
                </el-row>
              </el-container>
            </el-tab-pane>
          </el-tabs>
        </el-header>
      </el-container>
    </div>
  </div>
</template>

<script>
  export default {
    name: 'index'
  }
</script>

<style scoped>
  .bg {
    background: #000 url(../assets/images/footer-bg.jpg) no-repeat center center;
    height: 187px;
  }

  .header-search {
    padding: 3px 6px;
    width: 170px;
    /*color: rgba(255,255,255,0.9);*/
    background-color: transparent;
  }

  #item-slideshow {
    margin-top: 50px;
  }

  .hot-label {
    font-size: 10px;
    color: #fff;
    background: #927fc5;
    text-transform: uppercase;
    padding: 7px 10px 4px 10px;
    text-align: center;
    display: block;
    position: absolute;
    top: 0px;
    font-weight: bold;
    letter-spacing: 1px;
    border-radius: 2px;
    right: 0;
  }

  .hot-label.hot-top-right {
    right: 0;
    left: auto;
  }
</style>
