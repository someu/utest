<template>
  <el-container class="utest-layout">
    <el-header class="utest-layout_header">
      <u-test-header></u-test-header>
    </el-header>
    <el-main class="utest-layout_main">
      <div class="main-wrapper"><router-view></router-view></div>
    </el-main>
  </el-container>
</template>

<script>
import { ElContainer, ElHeader, ElMain } from "element-plus";
import Header from "./Header.vue";

export default {
  components: {
    ElContainer,
    ElHeader,
    ElMain,
    UTestHeader: Header,
  },
  computeds: {
    menus() {
      return [];
    },
  },
};
</script>

<style lang="less" scoped>
.utest-layout {
  height: 100vh;

  &_header {
    border-bottom: 1px solid #ccc;
    padding: 0 48px;
  }

  &_main {
    padding: 0;
  }

  .main-wrapper {
    max-width: 1200px;
    margin: auto;
  }
}
</style>
