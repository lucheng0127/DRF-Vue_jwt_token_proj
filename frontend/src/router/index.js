import Vue from 'vue'
import Router from 'vue-router'

import Login from '../components/login/Login.vue'
import Home from '../components/home/Home.vue'

Vue.use(Router)

const router = new Router({
  routes: [
    {
      path: '/login',
      name: 'login',
      component: Login
    },
    {
      path: '',
      name: 'home',
      component: Home
    }
  ]
})

export default router
