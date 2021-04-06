<template>
  <div class="list">
    <div class="title">
      <span>快 速 链 接</span>
    </div>
    <ul>
      <li>
        <div class="subtitle first-subtitle">
          <router-link to="/statistics">default 1</router-link>
        </div>
        <ul>
          <li class="real-link">
            <i class="el-icon-arrow-right"></i>
            <router-link to="/statistics/one/1">default 1-1</router-link>
          </li>
          <li class="real-link">
            <i class="el-icon-arrow-right"></i>
            <router-link to="/statistics/one/2">list 1-2</router-link>
          </li>
        </ul>
      </li>
      <li>
        <div class="subtitle">
          <router-link to="/statistics/two">list 2</router-link>
        </div>
        <ul>
          <li class="real-link">
            <i class="el-icon-arrow-right"></i>
            <router-link to="/statistics/two/1">list 2-1</router-link>
          </li>
          <li class="real-link">
            <i class="el-icon-arrow-right"></i>
            <router-link to="/statistics/two/2">list 2-2</router-link>
          </li>
          <li class="real-link">
            <i class="el-icon-arrow-right"></i>
            <router-link to="/statistics/two/3">list 2-3</router-link>
          </li>
        </ul>
      </li>
    </ul>
  </div>
</template>

<script>
export default {
  name: 'StatisticsList',
}
</script>

<style lang="scss" scoped>
@import "~@/assets/css/reset.css";
.list {
  margin: 15px 30px auto 25px;
  flex-grow: 0;  // 不会占据容器中的剩余空间
  flex-shrink: 0;  // 不会收缩变小以适应容器
  flex-basis: 150px;
  height: 350px;
  border: 1px solid rgb(22, 22, 110);
  .title {
    border: 1px solid white;
    //width: 148px;
    background: rgb(22, 22, 110);
    color: white;
    height: 30px;
    display: flex;
    justify-content: center;
    align-items: center;
    //font-size: 14px;
  }
  .subtitle {
    font-weight: bold;
    margin: 12px auto 4px 11px;
    .router-link-active {
      text-shadow: none;
    }
  }
  .first-subtitle {
    margin-top: 7px;
  }
  .real-link {
    margin-left: 11px;
    margin-bottom: 5px;
    i {
      font-size: 12px;
      margin-right: 3px;
    }
  }
}
</style>