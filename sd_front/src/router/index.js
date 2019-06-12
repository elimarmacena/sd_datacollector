import Vue from 'vue'
import Router from 'vue-router'
import HelloWorld from '@/components/HelloWorld'
import OwnerForm from '@/components/OwnerForm'
import IntervalDaysForm from '@/components/IntervalDaysForm'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'HelloWorld',
      component: HelloWorld
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
