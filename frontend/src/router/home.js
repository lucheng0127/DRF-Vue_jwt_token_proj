import Home from '../components/home/Home.vue'
import Thesis from '../components/thesis/Thesis.vue'
import ImportThesis from '../components/thesis/ImportThesis.vue'
import ThesisDetail from '../components/thesis/ThesisDetail.vue'
import Notify from '../components/notify/Notify.vue'
import Settings from '../components/settings/Settings.vue'

export default {
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
      path: 'thesis/:thesis_id',
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
