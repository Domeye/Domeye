<template>
  <div>
    <span>123</span>
    <ul>
      <li class="test1"><a href="">test1</a></li>
      <li class="test2"><a href="">test2</a></li>
      <li class="test3"><a href="">test3</a></li>
      <li class="test4"><a href="">test4</a></li>
    </ul>
  </div>
</template>

<script>
  export default {
    name: "test"
  }
</script>

<style lang="scss" scoped>
 $test: #f00;
  div{
    color: $test
  }
  $i: 3;
  @while($i > 0){
    .test#{$i}{
      overflow: hidden;
    }
    $i: $i - 1;
  }
</style>
