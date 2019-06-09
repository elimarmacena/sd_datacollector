import Vue from 'vue'
import Router from 'vue-router'
import HelloWorld from '@/components/HelloWorld'
import TemperatureForm from '@/components/TemperatureForm'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'HelloWorld',
      component: HelloWorld
    },
    {
      path: '/temperatureForm',
      name: 'TemperatureForm',
      component: TemperatureForm
    }
  ]
})
