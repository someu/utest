<template>
  <el-container class="utest-layout">
    <el-aside class="utest-layout_aside">
      <u-test-menu></u-test-menu>
    </el-aside>
    <el-container>
      <el-header class="utest-layout_header">
        <u-test-header></u-test-header>
      </el-header>
      <el-main class="utest-layout_main">
        <transition>
          <router-view></router-view>
        </transition>
      </el-main>
    </el-container>
  </el-container>
</template>

<script>
import { ElContainer, ElAside, ElHeader, ElMain } from "element-plus";
import Menu from "./Menu.vue";
import Header from "./Header.vue";

export default {
  components: {
    ElContainer,
    ElAside,
    ElHeader,
    ElMain,
    UTestMenu: Menu,
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

  &_aside {
    display: flex;
    flex-direction: column;

    .el-menu {
      flex: 1;
    }
  }

  &_aside {
    width: auto;
  }

  &_header {
    border-bottom: 1px solid #ccc;
  }
}
</style>
