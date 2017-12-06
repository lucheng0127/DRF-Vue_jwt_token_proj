import Vue from 'vue'
import Router from 'vue-router'

import Login from '../components/login/Login.vue'
import Home from '../components/home/Home.vue'
import Thesis from '../components/thesis/Thesis.vue'
import ImportThesis from '../components/thesis/ImportThesis.vue'
import ThesisDetail from '../components/thesis/ThesisDetail.vue'
import Notify from '../components/notify/Notify.vue'
import Settings from '../components/settings/Settings.vue'

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
      component: Home,
      children: [
        {
          path: 'thesis',
          name: 'thesis',
          component: Thesis
        },
        {
          path: 'thesis/:id',
          name: 'thesis-detail',
          component: ThesisDetail
        },
        {
          path: 'import',
          name: 'import',
          component: ImportThesis
        },
        {
          path: '',
          redirect: 'notify'
        },
        {
          path: 'notify',
          name: 'notify',
          component: Notify
        },
        {
          path: 'settings',
          name: 'settings',
          component: Settings
        }
      ]
    }
  ]
})

export default router
