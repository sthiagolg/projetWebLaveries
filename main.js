import Vue from 'vue'
import './plugins/vuetify'
import App from './App.vue'
import router from "./index.js"
import Vuetify from 'vuetify'
import 'vuetify/dist/vuetify.min.css'
import VueSession from 'vue-session'


Vue.use(Vuetify)
Vue.use(VueSession)

Vue.config.productionTip = false

var vm = new Vue({
  router,
  render: h => h(App),
  
}).$mount('#app')

/*new Vue({
  router,
  render: h => h(B),
}).$mount('#B')*/
//vm.item = 'thiago'
