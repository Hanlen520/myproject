import Vue from 'vue/dist/vue.js';
import Router from 'vue-router'
import Login from '@/components/Login'
import UpdateUrl from '@/components/UpdateUrl'
import DeleteUrl from '@/components/DeleteUrl'
import AddUrl from '@/components/AddUrl'
import CaseList from '@/components/CaseList'
import AddCase from '@/components/AddCase'
import CaseSuiteList from '@/components/CaseSuiteList'

Vue.use(Router);

export default new Router({
  routes: [
    {
      path: '/login',
      name: 'Login',
      component: Login
    },
    {
      path: '/update_url/:id',
      name: 'UpdateUrl',
      component: UpdateUrl
    },
    {
      path: '/add-url/',
      name: 'AddUrl',
      component: AddUrl
    },
    {
      path: '/case_list/',
      name: 'CaseList',
      component: CaseList,
    },
    {
      path: '/add_cases/',
      name: 'AddCase',
      component: AddCase,
    },
    {
      path: '/case_suite_list/',
      name: 'CaseSuiteList',
      component: CaseSuiteList,
    },

  ],
  mode: 'history'
})

