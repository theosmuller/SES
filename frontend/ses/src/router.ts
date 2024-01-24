import { createRouter, createWebHistory, RouteRecordRaw } from 'vue-router';
import Login from './components/Login.vue';

const routes: Array<RouteRecordRaw> = [
  { path: '/login', component: { render: () => Login } },
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;
