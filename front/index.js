import Vue from 'vue'
import Router from 'vue-router'

import Auth from '@/components/pages/Auth.vue'
import Laveries from '@/components/pages/Laveries.vue'
import Home from '@/components/pages/Home.vue'
import B from '@/components/pages/batiments/B.vue'
import D from '@/components/pages/batiments/D.vue'
import G from '@/components/pages/batiments/G.vue'
import I from '@/components/pages/batiments/I.vue'
import E from '@/components/pages/batiments/E.vue'
import F from '@/components/pages/batiments/F.vue'
import H from '@/components/pages/batiments/H.vue'


import informerProbleme from '@/components/pages/informerProbleme.vue'
import Admin from '@/components/pages/Admin.vue'

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
    },
    {
      path: '/informerProbleme',
      name: 'informerProbleme',
      component: informerProbleme
    },
    {
      path: '/admin',
      name: 'Admin',
      component: Admin
    },
    {
        path: '/laveries/D',
        name: 'D',
        component: D
      },
    {
        path: '/laveries/G',
        name: 'G',
        component: G
      },
    {
        path: '/laveries/H',
        name: 'H',
        component: H
      },
    {
        path: '/laveries/I',
        name: 'I',
        component: I
      },
    {
        path: '/laveries/E',
        name: 'E',
        component: E
      },
    {
        path: '/laveries/F',
        name: 'F',
        component: F
      }
  ]
})
