import Vue from 'vue'
import Router from 'vue-router'

import Login from '../components/login/Login.vue'
import Home from './home'

Vue.use(Router)

const router = new Router({
  routes: [
    {
      path: '/login',
      name: 'login',
      component: Login
    },
    Home
  ]
})

export default router
