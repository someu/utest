<template>
  <el-container class="basic-layout">
    <el-aside width="200px" class="basic-layout_aside"> </el-aside>
    <el-container>
      <el-header class="basic-layout_header"> </el-header>
      <el-main class="basic-layout_main">
        <slot></slot>
      </el-main>
    </el-container>
  </el-container>
</template>

<script>
import { ElContainer, ElAside, ElHeader, ElMain } from "element-plus";
export default {
  components: {
    ElContainer,
    ElAside,
    ElHeader,
    ElMain,
  },
  computeds: {
    menus() {
      return [];
    },
  },
};
</script>

<style lang="less">
.basic-layout {
}
</style>
