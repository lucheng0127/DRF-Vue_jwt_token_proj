import Vue from 'vue'
import iView from 'iview'
import axios from 'axios'
import 'iview/dist/styles/iview.css'

import App from './App'
import router from './router'

Vue.config.productionTip = false
Vue.use(iView)
Vue.use(axios)

/* eslint-disable no-new */
new Vue({
  el: '#app',
  router,
  template: '<App/>',
  components: { App }
})
