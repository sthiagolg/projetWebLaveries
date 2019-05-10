import Vue from 'vue'
import Router from 'vue-router'

import Auth from '@/components/pages/Auth.vue'
import Laveries from '@/components/pages/Laveries.vue'
import Home from '@/components/pages/Home.vue'
import B from '@/components/pages/batiments/B.vue'
import Menu from '@/components/pages/Menu.vue'

Vue.use(Router)

export default new Router({
  mode: 'history',
  base: process.env.BASE_URL,
  routes: [
    {
      path: '/laveries',
      name: 'Laveries',
      component: Laveries
    },
    
    {
      path: '/auth',
      name: 'Auth',
      component: Auth
    },
    {
      path: '/',
      name: 'Home',
      component: Home
    },
    {
      path: '/laveries/B',
      name: 'B',
      component: B
    }
  ]
})