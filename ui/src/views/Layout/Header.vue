<template>
  <div class="header">
    <div class="menu-action" @click="triggerMenuCollapse">
      <el-icon v-if="menuCollapse"><expand /></el-icon>
      <el-icon v-else><fold /></el-icon>
    </div>
  </div>
</template>

<script>
import { ElIcon } from "element-plus";
import { Fold, Expand } from "@element-plus/icons-vue";

export default {
  components: {
    ElIcon,
    Fold,
    Expand,
  },
  computed: {
    menuCollapse() {
      return this.$store.state.global.menuCollapse;
    },
  },
  methods: {
    triggerMenuCollapse() {
      this.$store.commit("global/triggerMenuCollapse");
    },
  },
};
</script>

<style lang="less" scoped>
.header {
  height: 60px;
  display: flex;
  align-items: center;

  .menu-action {
    font-size: 18px;
  }
}
</style>
