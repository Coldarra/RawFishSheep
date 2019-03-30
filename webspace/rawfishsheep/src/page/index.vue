<template>
    <span>

        <div>
            <div class="mainblank"></div>
            <div class="mainnvabar">
                <nav class="navbar navbar-expand-lg navbar-light bg-navbar">
                    <a class="navbar-brand" href="/"> <i> i-Sharing </i></a>
                    <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarSupportedContent" aria-controls="navbarSupportedContent"
                        aria-expanded="false" aria-label="Toggle navigation">
                        <span class="navbar-toggler-icon"></span>
                    </button>

                    <div class="collapse navbar-collapse" id="navbarSupportedContent">
                        <ul class="navbar-nav mr-auto">
                            <li class="nav-item" id="nav-index">
                                <a class="nav-link" href="/">首页</a>
                            </li>

                            <li class="nav-item" id="nav-upload">
                                <a class="nav-link" href="/file/upload">上传文件</a>
                            </li>
                            <li class="nav-item" id="nav-course">
                                <a class="nav-link" href="/course">课程中心</a>
                            </li>
                            <li class="nav-item" id="nav-history">
                                <a class="nav-link" href="/history">历史记录</a>
                            </li>
                            <li class="nav-item" id="nav-ocr">
                                <a class="nav-link" href="/ocr">文字识别</a>
                            </li>
                            <li class="nav-item" id="nav-filebox">
                                <a class="nav-link disabled" href="#" onclick="FLAlert('warning','功能开发中请耐心等待')">文件库</a>
                            </li>
                        </ul>

                        <div class="my-2 my-lg-0">
                            <ul class="navbar-nav mr-auto userinfo">
                                
                                <div class="d-none d-lg-block">
                                    <li class="nav-item dropdown message" id="message" style="display: none;">
                                        <a class="nav-link" href="#" id="navbarDropdown" role="button" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">
                                            <i class="fa fa-bell color-orange" id="bell"></i>
                                            <span class="badge badge-pill align-text-bottom " id="unreadmessagecount"></span>
                                        </a>
                                        <div class="dropdown-menu messageframe" aria-labelledby="navbarDropdown">
                                            <div id="unreadmessageframe"></div>
                                            <div class="dropdown-divider"></div>
                                            <div class="messagecontent">
                                                <a class="showall" href="">查看全部</a>
                                                <!-- | <a class="allread" href="#">全部已读</a> -->
                                            </div>
                                        </div>
                                    </li>
                                </div>

                                <li class="nav-item dropdown active userinfo" id="dropmenu" display="block">

                                    <a class="nav-link dropdown-toggle" href="#" id="navbarDropdown" role="button" data-toggle="dropdown" aria-haspopup="true"
                                        aria-expanded="false">
                                        <!-- <img alt="image" class="img-thumbnail" src="/static/img/head/{{request.session.headid}}.png" > -->
                                        <!-- <i class="fa fa-user-plus" aria-hidden="true"></i>&nbsp;&nbsp; -->
                                        <!-- {{request.session.username}} -->
                                    </a>
                                    <div class="dropdown-menu userinfoframe" aria-labelledby="navbarDropdown">
                                        <a class="dropdown-item" href="/user"><i class="fa fa-info-circle fa-fw"></i>&nbsp;个人信息</a>
                                        <a class="dropdown-item" href="/history"><i class="fa fa-print fa-fw"></i>&nbsp;提交记录</a>

                                        <div class="dropdown-divider"></div>
                                        <a class="dropdown-item" href="/logout"><i class="fa fa-user-times fa-fw" aria-hidden="true"></i>&nbsp;退出登录</a>
                                    </div>
                                </li>

                                <li class="nav-item">
                                    <a class="btn btn-outline-primary" href="/user/login"><i class="fa fa-key fa-fw" aria-hidden="true"></i>登录</a>
                                </li>
                                &nbsp;
                                <li class="nav-item">
                                    <a class="btn btn-outline-primary" href="/user/register"><i class="fa fa-location-arrow fa-fw"
                                            aria-hidden="true"></i>注册</a>
                                </li>
                            </ul>
                        </div>
                    </div>
                </nav>
            </div>
        </div>
    
    </span>
</template>

<script>
  export default {
    name: 'index'
  }
</script>

