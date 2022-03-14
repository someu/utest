<template>
  <el-menu class="menu" :collapse="menuCollapse">
    <template v-for="(subMenu, index) in menu">
      <el-sub-menu
        :index="index"
        :key="`${index}_menu`"
        v-if="subMenu.children && subMenu.children.length"
      >
        <template #title>
          <el-icon v-if="subMenu.icon">
            <component :is="subMenu.icon"></component>
          </el-icon>
          <span>{{ subMenu.title }}</span>
        </template>

        <el-menu-item
          v-for="(child, cIndex) in subMenu.children"
          :index="`${index}_${cIndex}`"
          :key="cIndex"
        >
          <el-icon v-if="child.icon">
            <component :is="child.icon"></component>
          </el-icon>
          <span>{{ child.title }}</span>
        </el-menu-item>
      </el-sub-menu>
      <el-menu-item :index="index" :key="`${index}_item`" v-else>
        <el-icon v-if="subMenu.icon">
          <component :is="subMenu.icon"></component>
        </el-icon>
        <span>{{ subMenu.title }}</span>
      </el-menu-item>
    </template>
  </el-menu>
</template>

<script>
import {
  ElMenu,
  ElSubMenu,
  ElMenuItem,
  ElMenuItemGroup,
  ElIcon,
} from "element-plus";

import {
  Location,
  Document,
  Menu as IconMenu,
  Setting,
} from "@element-plus/icons-vue";

export default {
  components: {
    ElMenu,
    ElSubMenu,
    ElMenuItem,
    ElMenuItemGroup,
    ElIcon,

    Location,
    Document,
    IconMenu,
    Setting,
  },
  computed: {
    menu() {
      return [
        {
          title: "项目管理",
          icon: "setting",
        },
        {
          title: "用例管理",
          icon: "setting",
        },
        {
          title: "系统设置",
          icon: "setting",
        },
      ];
    },
    menuCollapse() {
      return this.$store.state.global.menuCollapse;
    },
  },
  methods: {},
};
</script>

<style lang="less" scoped>
.menu {
}
</style>
