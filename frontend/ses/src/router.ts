import { createRouter, createWebHistory, RouteRecordRaw } from 'vue-router';
import Login from './views/LoginPage.vue';

const routes: Array<RouteRecordRaw> = [
  {
    path: '/',
    name: 'Home',
    component: Login
  },
  {
    path: '/login',
    name: 'Login',
    component: Login
  }
];


const router = createRouter({
  history: createWebHistory(),
  routes,
});

router.beforeEach((to, from, next) => {
  const isAuthenticated = false; // replace this with real authentication check
  if (to.path !== '/login' && !isAuthenticated) next({ path: '/login' })
  else next()
})

export default router;