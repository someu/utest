import { createRouter, createWebHistory } from "vue-router";
import Layout from "@/views/Layout/index.vue";

const routes = [
  {
    path: "/",
    component: Layout,
  },
];

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes,
});

export default router;
