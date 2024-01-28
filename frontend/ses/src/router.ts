import { createRouter, createWebHistory, RouteRecordRaw } from 'vue-router';
import Login from './views/LoginPage.vue';
import Home from './views/HomePage.vue';
import Admin from './views/AdminPage.vue';
import Cookies from 'js-cookie';

const routes: Array<RouteRecordRaw> = [
  {
    path: '/home',
    name: 'Home',
    component: Home
  },
  {
    path: '/login',
    name: 'Login',
    component: Login
  },
  {
    path: '/admin',
    name:'Admin Tools',
    component: Admin
  }
];


const router = createRouter({
  history: createWebHistory(),
  routes,
});

router.beforeEach((to, from, next) => {
  const isAuthenticated = Cookies.get('auth'); // replace this with real authentication check
  if (to.path !== '/login' && !isAuthenticated) next({ path: '/login' })
  else next()
})

export default router;