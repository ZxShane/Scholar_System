import Vue from 'vue'
import Router from 'vue-router'
import CreateNewcase from '@/components/CreateNewcase'
import ShowAllScholar from '@/components/ShowAllScholar'
import Load from '@/components/Load'
import AllGrade from '@/components/AllGrade'
import CheckActivity from '@/components/CheckActivity'
import CheckScholar from '@/components/CheckScholar'
import InHospital from '@/components/InHospital'
import Classevaluate from '@/components/Class_evaluate'
import info from '@/components/info'
import apply_scholar from '@/components/Apply_Scholar'
import PersonalInfo from '@/components/PersonalInfo'
import AddMajorGrade from '@/components/AddMajorGrade'
Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'Load',
      component: Load
    },
    {
      path: '/createnewcase',
      name: 'CreateNewcase',
      component: CreateNewcase
    },
    {
      path: '/showallscholar',
      name: 'ShowAllScholar',
      component: ShowAllScholar
    },
    {
      path: '/allgrade',
      name: 'AllGrade',
      component: AllGrade
    },
    {
      path: '/checkactivity',
      name: 'CheckActivity',
      component: CheckActivity
    },
    {
      path: '/checkscholar',
      name: 'CheckScholar',
      component: CheckScholar
    },
    {
      path: '/inhospital',
      name: 'Inhospital',
      component: InHospital
    },
    {
      path: '/evaluate',
      name: 'Classevaluate',
      component: Classevaluate
    },
    {
      path: '/info',
      name: 'Info',
      component: info
    },
    {
      path: '/apply_scholar',
      name: 'Apply_scholar',
      component: apply_scholar
    },{
      path:'/personalinfo',
      name:'PersonalInfo',
      component:PersonalInfo
    },
    {
      path:'/addmajorgrade',
      name:AddMajorGrade,
      component:AddMajorGrade
    }
  ]
})


