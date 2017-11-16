import Vue from 'vue'
import Router from 'vue-router'

import login from '../components/login/login.vue'
import userInfo from '../components/userInfo/userInfo.vue'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/login',
      component: login
    },
    {
      path: '/user-info',
      component: userInfo
    }
  ]
})
