import Vue from 'vue'
import Router from 'vue-router'
import UserInfo from '@/components/UserInfo'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'UserInfo',
      component: UserInfo
    }
  ]
})
