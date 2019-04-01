<template>
  <div id="mainpage">
    <div class="container">
      <div id="slideshow" class="container">
        <div class="row">
          <div class="col-md-9">
            <div id="itemRecommend" class="carousel" data-ride="carousel" style="height: auto">
              <div class="carousel-inner m-100 h-100">
                <div class="carousel-item active" data-interval="1000">
                  <img src="../assets/images/slide-img1.jpg" alt="" class="d-blcok w-100">
                </div>
                <div class="carousel-item" data-interval="1000">
                  <img src="../assets/images/slide-img2.jpg" alt="" class="d-blcok w-100">
                </div>
                <div class="carousel-item" data-interval="1000">
                  <img src="../assets/images/slide-img1.jpg" alt="" class="d-blcok w-100">
                </div>
              </div>
              <a href="#itemRecommend" class="carousel-control-prev" role="button" data-slide="prev">
                <span class="carousel-control-prev-icon" aria-hidden="true"></span>
                <span class="sr-only">Previous</span>
              </a>
              <a href="#itemRecommend" class="carousel-control-next" role="button" data-slide="next">
                <span class="carousel-control-next-icon" aria-hidden="true"></span>
                <span class="sr-only">Next</span>
              </a>
            </div>
          </div>
          <div class="col-md-3">
            <div class="card text-center slide shadow-sm p-3 mb-5 bg-white rounded">
              <img src="../assets/products-images/product1.jpg" alt="" class="card-img-top d-block w-100">
              <div class="card-body">
                <h5 class="card-title"><a href="#">洋葱</a></h5>
                <div class="text-center" style="padding-bottom: 10px"><span
                  class="badge badge-warning"><strong>评分</strong></span></div>
                <button type="button" class="btn btn-success">加入购物车</button>
              </div>
            </div>
          </div>
        </div>
      </div>
      <div id="feature" class="container">
        <div class="row">
          <div class="col-md-3">
            <div class="card text-white bg-truck">
              <div class="card-body text-left">
                <i class="fa fa-truck fa-3x"></i>
                <span class="content">
                啊啊发啊士大夫撒
              </span>
              </div>
            </div>
          </div>
          <div class="col-md-3">
            <div class="card text-white bg-phone">
              <div class="card-body text-left">
                <i class="fa fa-phone fa-3x"></i>
                <span class="content">
                啊啊发啊士大夫撒
              </span>
              </div>
            </div>
          </div>
          <div class="col-md-3">
            <div class="card text-white bg-dollar">
              <div class="card-body text-left">
                <i class="fa fa-dollar fa-3x"></i>
                <span class="content">
                啊啊发啊士大夫撒
              </span>
              </div>
            </div>
          </div>
          <div class="col-md-3">
            <div class="card text-white bg-briefcase">
              <div class="card-body text-left">
                <i class="fa fa-briefcase fa-3x"></i>
                <span class="content">
                啊啊发啊士大夫撒
              </span>
              </div>
            </div>
          </div>
        </div>
      </div>
      <div id="products" class="container shadow-sm p-3 mb-5 bg-white rounded">
        <nav class="navbar navbar-light">
          <span class="navbar-brand text-white rounded">RawFishSheep</span>
          <ul class="nav nav-pills justify-content-end" id="pills-tab" role="tablist">
            <li class="nav-item">
              <a class="nav-link active" id="pills-a-tab" data-toggle="pill" href="#pills-a" role="tab"
                 aria-controls="pills-a" aria-selected="true">aaa</a>
            </li>
            <li class="nav-item">
              <a class="nav-link" id="pills-b-tab" data-toggle="pill" href="#pills-b" role="tab" aria-controls="pills-b"
                 aria-selected="false">bbb</a>
            </li>
            <li class="nav-item">
              <a class="nav-link" id="pills-c-tab" data-toggle="pill" href="#pills-c" role="tab" aria-controls="pills-c"
                 aria-selected="false">ccc</a>
            </li>
            <li class="nav-item">
              <a class="nav-link" id="pills-d-tab" data-toggle="pill" href="#pills-d" role="tab" aria-controls="pills-d"
                 aria-selected="false">ddd</a>
            </li>
          </ul>
        </nav>
        <div class="tab-content" id="pills-tabContent">
          <div class="tab-pane fade show active" id="pills-a" role="tabpanel" aria-labelledby="pills-a-tab">
            <div class="row no-gutters">
              <div class="col-lg-3 col-md-3 col-sm-4 col-xs-6">
                <div class="card text-center slide shadow-sm p-3 mb-5 bg-white rounded">
                  <img src="../assets/products-images/product1.jpg" alt="" class="card-img-top d-block w-100">
                  <div class="card-body">
                    <h5 class="card-title"><a href="#">洋葱</a></h5>
                    <div class="text-center" style="padding-bottom: 10px"><span
                      class="badge badge-warning"><strong>评分</strong></span></div>
                    <button type="button" class="btn btn-success">加入购物车</button>
                  </div>
                </div>
              </div>
              <div class="col-lg-3 col-md-3 col-sm-4 col-xs-6">
                <div class="card text-center slide shadow-sm p-3 mb-5 bg-white rounded">
                  <img src="../assets/products-images/product1.jpg" alt="" class="card-img-top d-block w-100">
                  <div class="card-body">
                    <h5 class="card-title"><a href="#">洋葱</a></h5>
                    <div class="text-center" style="padding-bottom: 10px"><span
                      class="badge badge-warning"><strong>评分</strong></span></div>
                    <button type="button" class="btn btn-success">加入购物车</button>
                  </div>
                </div>
              </div>
              <div class="col-lg-3 col-md-3 col-sm-4 col-xs-6">
                <div class="card text-center slide shadow-sm p-3 mb-5 bg-white rounded">
                  <img src="../assets/products-images/product1.jpg" alt="" class="card-img-top d-block w-100">
                  <div class="card-body">
                    <h5 class="card-title"><a href="#">洋葱</a></h5>
                    <div class="text-center" style="padding-bottom: 10px"><span
                      class="badge badge-warning"><strong>评分</strong></span></div>
                    <button type="button" class="btn btn-success">加入购物车</button>
                  </div>
                </div>
              </div>
              <div class="col-lg-3 col-md-3 col-sm-4 col-xs-6">
                <div class="card text-center slide shadow-sm p-3 mb-5 bg-white rounded">
                  <img src="../assets/products-images/product1.jpg" alt="" class="card-img-top d-block w-100">
                  <div class="card-body">
                    <h5 class="card-title"><a href="#">洋葱</a></h5>
                    <div class="text-center" style="padding-bottom: 10px"><span
                      class="badge badge-warning"><strong>评分</strong></span></div>
                    <button type="button" class="btn btn-success">加入购物车</button>
                  </div>
                </div>
              </div>
            </div>
          </div>
          <div class="tab-pane fade" id="pills-b" role="tabpanel" aria-labelledby="pills-b-tab">
            <div class="row no-gutters">
              <div class="col-lg-3 col-md-3 col-sm-4 col-xs-6">
                <div class="card text-center slide shadow-sm p-3 mb-5 bg-white rounded">
                  <img src="../assets/products-images/product1.jpg" alt="" class="card-img-top d-block w-100">
                  <div class="card-body">
                    <h5 class="card-title"><a href="#">洋葱</a></h5>
                    <div class="text-center" style="padding-bottom: 10px"><span
                      class="badge badge-warning"><strong>评分</strong></span></div>
                    <button type="button" class="btn btn-success">加入购物车</button>
                  </div>
                </div>
              </div>
              <div class="col-lg-3 col-md-3 col-sm-4 col-xs-6">
                <div class="card text-center slide shadow-sm p-3 mb-5 bg-white rounded">
                  <img src="../assets/products-images/product1.jpg" alt="" class="card-img-top d-block w-100">
                  <div class="card-body">
                    <h5 class="card-title"><a href="#">洋葱</a></h5>
                    <div class="text-center" style="padding-bottom: 10px"><span
                      class="badge badge-warning"><strong>评分</strong></span></div>
                    <button type="button" class="btn btn-success">加入购物车</button>
                  </div>
                </div>
              </div>
              <div class="col-lg-3 col-md-3 col-sm-4 col-xs-6">
                <div class="card text-center slide shadow-sm p-3 mb-5 bg-white rounded">
                  <img src="../assets/products-images/product1.jpg" alt="" class="card-img-top d-block w-100">
                  <div class="card-body">
                    <h5 class="card-title"><a href="#">洋葱</a></h5>
                    <div class="text-center" style="padding-bottom: 10px"><span
                      class="badge badge-warning"><strong>评分</strong></span></div>
                    <button type="button" class="btn btn-success">加入购物车</button>
                  </div>
                </div>
              </div>
              <div class="col-lg-3 col-md-3 col-sm-4 col-xs-6">
                <div class="card text-center slide shadow-sm p-3 mb-5 bg-white rounded">
                  <img src="../assets/products-images/product1.jpg" alt="" class="card-img-top d-block w-100">
                  <div class="card-body">
                    <h5 class="card-title"><a href="#">洋葱</a></h5>
                    <div class="text-center" style="padding-bottom: 10px"><span
                      class="badge badge-warning"><strong>评分</strong></span></div>
                    <button type="button" class="btn btn-success">加入购物车</button>
                  </div>
                </div>
              </div>
            </div>
          </div>
          <div class="tab-pane fade" id="pills-c" role="tabpanel" aria-labelledby="pills-c-tab">
            <div class="row no-gutters">
              <div class="col-lg-3 col-md-3 col-sm-4 col-xs-6">
                <div class="card text-center slide shadow-sm p-3 mb-5 bg-white rounded">
                  <img src="../assets/products-images/product1.jpg" alt="" class="card-img-top d-block w-100">
                  <div class="card-body">
                    <h5 class="card-title"><a href="#">洋葱</a></h5>
                    <div class="text-center" style="padding-bottom: 10px"><span
                      class="badge badge-warning"><strong>评分</strong></span></div>
                    <button type="button" class="btn btn-success">加入购物车</button>
                  </div>
                </div>
              </div>
              <div class="col-lg-3 col-md-3 col-sm-4 col-xs-6">
                <div class="card text-center slide shadow-sm p-3 mb-5 bg-white rounded">
                  <img src="../assets/products-images/product1.jpg" alt="" class="card-img-top d-block w-100">
                  <div class="card-body">
                    <h5 class="card-title"><a href="#">洋葱</a></h5>
                    <div class="text-center" style="padding-bottom: 10px"><span
                      class="badge badge-warning"><strong>评分</strong></span></div>
                    <button type="button" class="btn btn-success">加入购物车</button>
                  </div>
                </div>
              </div>
              <div class="col-lg-3 col-md-3 col-sm-4 col-xs-6">
                <div class="card text-center slide shadow-sm p-3 mb-5 bg-white rounded">
                  <img src="../assets/products-images/product1.jpg" alt="" class="card-img-top d-block w-100">
                  <div class="card-body">
                    <h5 class="card-title"><a href="#">洋葱</a></h5>
                    <div class="text-center" style="padding-bottom: 10px"><span
                      class="badge badge-warning"><strong>评分</strong></span></div>
                    <button type="button" class="btn btn-success">加入购物车</button>
                  </div>
                </div>
              </div>
              <div class="col-lg-3 col-md-3 col-sm-4 col-xs-6">
                <div class="card text-center slide shadow-sm p-3 mb-5 bg-white rounded">
                  <img src="../assets/products-images/product1.jpg" alt="" class="card-img-top d-block w-100">
                  <div class="card-body">
                    <h5 class="card-title"><a href="#">洋葱</a></h5>
                    <div class="text-center" style="padding-bottom: 10px"><span
                      class="badge badge-warning"><strong>评分</strong></span></div>
                    <button type="button" class="btn btn-success">加入购物车</button>
                  </div>
                </div>
              </div>
            </div>
          </div>
          <div class="tab-pane fade" id="pills-d" role="tabpanel" aria-labelledby="pills-d-tab">
            <div class="row no-gutters">
              <div class="col-lg-3 col-md-3 col-sm-4 col-xs-6">
                <div class="card text-center slide shadow-sm p-3 mb-5 bg-white rounded">
                  <img src="../assets/products-images/product1.jpg" alt="" class="card-img-top d-block w-100">
                  <div class="card-body">
                    <h5 class="card-title"><a href="#">洋葱</a></h5>
                    <div class="text-center" style="padding-bottom: 10px"><span
                      class="badge badge-warning"><strong>评分</strong></span></div>
                    <button type="button" class="btn btn-success">加入购物车</button>
                  </div>
                </div>
              </div>
              <div class="col-lg-3 col-md-3 col-sm-4 col-xs-6">
                <div class="card text-center slide shadow-sm p-3 mb-5 bg-white rounded">
                  <img src="../assets/products-images/product1.jpg" alt="" class="card-img-top d-block w-100">
                  <div class="card-body">
                    <h5 class="card-title"><a href="#">洋葱</a></h5>
                    <div class="text-center" style="padding-bottom: 10px"><span
                      class="badge badge-warning"><strong>评分</strong></span></div>
                    <button type="button" class="btn btn-success">加入购物车</button>
                  </div>
                </div>
              </div>
              <div class="col-lg-3 col-md-3 col-sm-4 col-xs-6">
                <div class="card text-center slide shadow-sm p-3 mb-5 bg-white rounded">
                  <img src="../assets/products-images/product1.jpg" alt="" class="card-img-top d-block w-100">
                  <div class="card-body">
                    <h5 class="card-title"><a href="#">洋葱</a></h5>
                    <div class="text-center" style="padding-bottom: 10px"><span
                      class="badge badge-warning"><strong>评分</strong></span></div>
                    <button type="button" class="btn btn-success">加入购物车</button>
                  </div>
                </div>
              </div>
              <div class="col-lg-3 col-md-3 col-sm-4 col-xs-6">
                <div class="card text-center slide shadow-sm p-3 mb-5 bg-white rounded">
                  <img src="../assets/products-images/product1.jpg" alt="" class="card-img-top d-block w-100">
                  <div class="card-body">
                    <h5 class="card-title"><a href="#">洋葱</a></h5>
                    <div class="text-center" style="padding-bottom: 10px"><span
                      class="badge badge-warning"><strong>评分</strong></span></div>
                    <button type="button" class="btn btn-success">加入购物车</button>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
      <div id="bestsell" class="container">
        <div class="row no-gutters">
          <div class="col-3">
            <div class="card text-center slide shadow-sm p-3 mb-5 bg-white rounded">
              <div class="card-body">
                <div class="card-title" style="background: #e31837; color: white;text-align: left">销量最高</div>
                <img src="../assets/products-images/product1.jpg" alt="" class="card-img-top d-block w-100">
                <div class="text-center" style="padding-bottom: 10px">
                  <span class="badge badge-warning"><strong>大促销。。。</strong></span>
                </div>
                <!--<button type="button" class="btn btn-success">加入购物车</button>-->
                <a href="#" style="text-align: left"><div class="card-title">查看全部</div></a>
              </div>
            </div>
          </div>
          <div class="col-9">
            <div class="row no-gutters">
              <div class="col-3">
                <div class="card text-center slide shadow-sm p-3 mb-5 bg-white rounded">
                  <img src="../assets/products-images/product1.jpg" alt="" class="card-img-top d-block w-100">
                  <div class="card-body">
                    <h5 class="card-title"><a href="#">洋葱</a></h5>
                    <div class="text-center" style="padding-bottom: 10px"><span
                      class="badge badge-warning"><strong>评分</strong></span></div>
                    <button type="button" class="btn btn-success">加入购物车</button>
                  </div>
                </div>
              </div>
              <div class="col-3">
                <div class="card text-center slide shadow-sm p-3 mb-5 bg-white rounded">
                  <img src="../assets/products-images/product1.jpg" alt="" class="card-img-top d-block w-100">
                  <div class="card-body">
                    <h5 class="card-title"><a href="#">洋葱</a></h5>
                    <div class="text-center" style="padding-bottom: 10px"><span
                      class="badge badge-warning"><strong>评分</strong></span></div>
                    <button type="button" class="btn btn-success">加入购物车</button>
                  </div>
                </div>
              </div>
              <div class="col-3">
                <div class="card text-center slide shadow-sm p-3 mb-5 bg-white rounded">
                  <img src="../assets/products-images/product1.jpg" alt="" class="card-img-top d-block w-100">
                  <div class="card-body">
                    <h5 class="card-title"><a href="#">洋葱</a></h5>
                    <div class="text-center" style="padding-bottom: 10px"><span
                      class="badge badge-warning"><strong>评分</strong></span></div>
                    <button type="button" class="btn btn-success">加入购物车</button>
                  </div>
                </div>
              </div>
              <div class="col-3">
                <div class="card text-center slide shadow-sm p-3 mb-5 bg-white rounded">
                  <img src="../assets/products-images/product1.jpg" alt="" class="card-img-top d-block w-100">
                  <div class="card-body">
                    <h5 class="card-title"><a href="#">洋葱</a></h5>
                    <div class="text-center" style="padding-bottom: 10px"><span
                      class="badge badge-warning"><strong>评分</strong></span></div>
                    <button type="button" class="btn btn-success">加入购物车</button>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
  export default {
    name: 'page'
  }
</script>

<style scoped>
  #itemRecommend {
    height: 100%;
  }

  .row {
    display: -webkit-box;
    display: -webkit-flex;
    display: -ms-flexbox;
    display: flex;
    flex-wrap: wrap;
  }

  .carousel .item {
    height: 500px;
    background-color: #777;
  }

  .carousel-inner > .item > img {
    position: absolute;
    top: 0;
    left: 0;
    min-width: 100%;
    height: 500px;
  }

  .bg-truck {
    background: #685c88;
  }

  .bg-phone {
    background: #94d7fb;
  }

  .bg-dollar {
    background: #fc9cc4;
  }

  .bg-briefcase {
    background: #e31837;
  }

  .content {
    display: block;
    text-align: left;
    margin-left: 70px;
    border-left: 1px rgba(255, 255, 255, 0.5) solid;
    padding-left: 25px;
    font-weight: 500
  }

  .fa {
    float: left;
  }

  #products {
    margin-top: 25px;
  }

  .no-gutters {
    margin-right: 0;
    margin-left: 0;
  }

  .navbar-light {
    border-bottom: #59b210;
  }

  .navbar-brand {
    background: #59b210;
    /*margin: auto;*/
    font-weight: 500;
    font-size: 22px;
    letter-spacing: 1px;
    font-family: 'Rubik', sans-serif;
    text-transform: uppercase;
    color: #fff;
    text-align: left;
    padding: 15px 15px;
  }

  #pills-tabContent {
    border-top: #59b210;
  }
</style>
