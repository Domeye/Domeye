<template>
  <div class="navbar">
    <div class="navbar-brand">
      <a class="navbar-brand-a" href="/">
        <span>Domeye</span>
      </a>
    </div>
    <div class="navbar-main">
      <ul class="navbar-left">
        <li class="navbar-left-item">
          <router-link to="/">首页</router-link>
        </li>
        <li class="navbar-left-item">
          <router-link to="/website">网站</router-link>
        </li>
        <li class="navbar-left-item">
          <router-link to="/address">地址</router-link>
        </li>
        <li class="navbar-left-item">
          <router-link to="/data">数据</router-link>
        </li>
        <li class="navbar-left-item">
          <router-link to="/report">报告</router-link>
        </li>
        <li class="navbar-left-item">
          <router-link to="/test">测一测</router-link>
        </li>
      </ul>
      <!-- <ul class="navbar-right" v-show="!isLogin">
        <li><router-link to="/register">注册</router-link></li>
        <li><span class="divider">|</span></li>
        <li><router-link to="/login">登录</router-link></li>
      </ul>
      <ul class="navbar-right" v-show="isLogin">
        <li>
          <span class="nav-text">你好，{{ userName }}</span>
        </li>
        <li><span class="divider">|</span></li>
        <li><router-link to="/admin">进入后台</router-link></li>
        <li><span class="divider">|</span></li>
        <li><router-link to="/logout">退出登录</router-link></li>
      </ul> -->
    </div>
  </div>
</template>

<script>
export default {
  name: "HeadNav",
  components: {},
  data() {
    return {
      isLogin: false,
      userName: "",
    };
  },
};
</script>

<style lang="scss" scoped>
@import "~@/assets/style/reset.css";
.navbar {
  display: flex;
  height: 100%;
  align-items: center;
  background-color: rgb(0, 0, 0);
  color: rgb(255, 255, 255);
  .navbar-brand {
    flex: 2;
    text-align: center;
    .navbar-brand-a {
      span {
        color: rgb(98, 118, 207);
        font-size: 17px;
        font-weight: bold;
      }
    }
  }
  .navbar-main {
    flex: 20;
    display: flex;
    .navbar-left {
      //float: left;
      // margin-left
      flex: 7;
      display: flex;
      text-align: center;
      padding-inline-start: 20px;
      a:link {
        color: rgb(255, 255, 255);
      }
      li {
        padding: 0 18px 0 18px;
        .router-link-exact-active {
          text-shadow: 2px 2px 1.5px rgb(179, 178, 178);
        }
        a:visited {
          color: rgb(255, 255, 255);
        }
        a:hover {
          color: rgb(212, 212, 212);
        }
      }
      li:first-child {
        padding-left: 18px;
      }
    }
    // .navbar-right {
    //   // float: right;
    //   flex: 1;
    //   display: flex;
    //   margin-right: 20px;
    //   li {
    //     padding: 0 8px 0 8px;
    //     a:link {
    //       color: rgb(255, 255, 255);
    //     }
    //     a:visited {
    //       color: rgb(255, 255, 255);
    //     }
    //   }
    //   li:last-of-type {
    //     padding-right: 28px;
    //   }
    // }
  }
}
</style>
