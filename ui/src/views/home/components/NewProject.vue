<template>
  <el-form label-width="60px" class="project-form">
    <el-form-item label="名称">
      <el-input v-model="name" placeholder="请填写项目名称"></el-input>
    </el-form-item>
    <el-form-item label="地址">
      <el-input v-model="url" placeholder="请填写项目地址"></el-input>
    </el-form-item>
    <el-form-item label="描述">
      <el-input v-model="description" placeholder="请填写项目描述"></el-input>
    </el-form-item>
    <el-form-item label="地址">
      <el-input v-model="address" placeholder="请填写项目地址"></el-input>
    </el-form-item>
  </el-form>
</template>

<script>
import { ElForm } from "element-plus";
export default {
  components: {
    ElForm,
  },
};
</script>

<style lang="less" scoped>
.project-form {
//   width: 520px;
}
</style>
