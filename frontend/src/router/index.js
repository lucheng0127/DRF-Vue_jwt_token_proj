import Vue from 'vue'
import Router from 'vue-router'

import login from '../components/login/login.vue'
import userInfo from '../components/userInfo/userInfo.vue'
import thesisList from '../components/thesis/thesisList.vue'

Vue.use(Router)

export default new Router({
// const router = new VueRouter({
  routes: [
    {
      path: '/login',
      component: login
    },
    {
      path: '/user-info',
      component: userInfo
    },
    {
      path: '/thesis-list',
      component: thesisList
    }
  ]
})

// router.beforeEach(function (to, from, next) {
//   if (sessionStorage.getItem('auth-token')==null || sessionStorage.getItem('auth-token')==undefined || sessionStorage.getItem('auth-token')=='') {
//     this.path.replace('/login');
//   } else {
//     next();
//   }
// })
