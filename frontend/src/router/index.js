import Vue from 'vue'
import Router from 'vue-router'

import Login from '../components/login/Login.vue'
import Home from './home'

Vue.use(Router)

const router = new Router({
  routes: [
    {
      path: '/login',
      component: Login
    },
    Home
  ]
})

router.beforeEach((to, from, next) => {
  if (to.path !== '/login') {
    if (sessionStorage.getItem('auth-token')) {
      console.log('用户已经登录')
      next()
    } else {
      console.log('用户未登录')
      next('/login')
    }
  } else {
    console.log('当前页面是登录页面')
    next()
  }
})

export default router
