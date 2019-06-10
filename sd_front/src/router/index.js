import Vue from 'vue'
import Router from 'vue-router'
import HelloWorld from '@/components/HelloWorld'
import TemperatureForm from '@/components/TemperatureForm'
import OwnerForm from '@/components/OwnerForm'
import IntervalDaysForm from '@/components/IntervalDaysForm'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/a',
      name: 'HelloWorld',
      component: HelloWorld
    },
    {
      path: '/temperatureForm',
      name: 'TemperatureForm',
      component: TemperatureForm
    },
    {
      path: '/ownerForm',
      name: 'OwnerForm',
      component: OwnerForm
    },
    {
      path: '/intervalDaysForm',
      name: 'IntervalDaysForm',
      component: IntervalDaysForm
    }
  ]
})
