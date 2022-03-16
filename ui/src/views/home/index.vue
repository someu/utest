<template>
  <div class="home">
    <h1 class="title">项目列表</h1>
    <div class="actions">
      <el-button class="new" type="primary" @click="newProject">
        <el-icon><plus /></el-icon>
        新建项目
      </el-button>
      <el-input
        class="search"
        v-model="search"
        placeholder="过滤"
        suffix-icon="search"
      ></el-input>
    </div>
    <div class="projects">
      <div class="project" v-for="project in projects" :key="project.id">
        <img :src="project.img" />
        <div class="info">
          <div class="title">{{ project.name }}</div>
          <div class="created">{{ project.startAt }}</div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { h } from "vue";
import { ElButton, ElInput, ElIcon, ElMessageBox } from "element-plus";
import { Plus } from "@element-plus/icons-vue";
import NewProject from "./components/NewProject.vue";

export default {
  components: {
    ElButton,
    ElInput,
    ElIcon,
    Plus,
  },
  state() {
    return {
      search: "",
    };
  },
  computed: {
    projects() {
      return [
        {
          id: "",
          img: "",
          name: "",
          startAt: "",
          status: "",
        },
      ];
    },
  },
  methods: {
    newProject() {
      ElMessageBox({
        title: "新建项目",
        message: h(NewProject, {}, null),
        showCancelButton: true,
        confirmButtonText: "确认",
        cancelButtonText: "取消",
      });
    },
  },
};
</script>

<style lang="less" scoped>
.home {
  .title {
    font-size: 24px;
    font-weight: bold;
    margin: 24px 0;
  }
  .actions {
    margin-top: 36px;

    display: flex;
    align-items: center;
    justify-content: space-between;

    .search {
      max-width: 300px;
    }
  }
}
</style>
