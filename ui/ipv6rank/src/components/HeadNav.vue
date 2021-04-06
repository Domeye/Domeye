<template>
  <div class="headnav">
    <ul>
      <li><router-link to="/home">IPv6Rank</router-link></li>
      <li><router-link to="/website">网站</router-link></li>
      <li><router-link to="/address">地址</router-link></li>
      <li><router-link to="/statistics">统计</router-link></li>
      <li><router-link to="/blog">博客</router-link></li>
      <li><router-link to="/download">下载</router-link></li>
    </ul>
    <!-- <div class="login">
      <router-link to="/">登录</router-link>
      <span>|</span>
      <router-link to="/">注册</router-link>
    </div> -->
  </div>
</template>

<style lang="scss" scoped>
@import "~@/assets/css/reset.css";
.headnav {
  display: flex;
  height: 40px;
  align-items: center;
  font-size: 13px;
  ul {
    flex: 9;
    display: flex;
    margin-left: 20px;
    li {
      margin-right: 30px;
      color: #222;
      font-family: Arial, sans-serif;
    }
    li:first-of-type {
      font-size: 14px;
      font-weight: bold;
    }
    li:first-of-type a.router-link-exact-active {
      text-shadow: 2px 2px 1.5px rgb(179, 178, 178);
    }
  }
  .login {
    flex: 1;
    display: flex;
    justify-content: center;
    font-family: Arial, sans-serif;
    a:first-of-type {
      margin: auto 7%;
    }
    a:last-of-type {
      margin: auto 7%;
    }
  }
  a:hover {
    color: rgb(109, 109, 109);
  }
}
</style>