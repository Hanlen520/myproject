// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import App from './App'

import axios from 'axios'
import VueRouter from 'vue-router'
import Login from './components/Login'
import Url from './components/Url'
import AddUrl from './components/AddUrl'
import UpdateUrl from './components/UpdateUrl'
import CaseList from './components/CaseList'
import AddCase from './components/AddCase'
import UpdateCase from './components/UpdateCase'
import CaseSuiteList from './components/CaseSuiteList'
import AddCaseSuite from './components/AddCaseSuite'
import UpdateCaseSuite from './components/UpdateCaseSuite'
import Register from './components/Register'
import UserList from './components/UserList'
import AddUser from './components/AddUser'
import UpdateUser from './components/UpdateUser'
import ResetPwd from './components/ResetPwd'
import ElementUI from 'element-ui'

import 'element-ui/lib/theme-chalk/index.css'

Vue.use(ElementUI);

Vue.use(VueRouter);


Vue.config.productionTip = false;


axios.defaults.withCredentials = true;
Vue.prototype.$bus = new Vue();


axios.defaults.baseURL = "http://127.0.0.1:8000/";
axios.defaults.headers.post['Content-Type'] = 'application/json; charset=UTF-8';
axios.defaults.headers.get['Content-Type'] = 'application/json; charset=UTF-8';
axios.defaults.headers.put['Content-Type'] = 'application/json; charset=UTF-8';
axios.defaults.headers.delete['Content-Type'] = 'application/json; charset=UTF-8';
if (localStorage.token !== '') {

  axios.defaults.headers.post['Authorization'] = "JWT " + localStorage.token;

  axios.defaults.headers.get['Authorization'] = "JWT " + localStorage.token;

  axios.defaults.headers.put['Authorization'] = "JWT " + localStorage.token;

  axios.defaults.headers.delete['Authorization'] = "JWT " + localStorage.token;
}


const router = new VueRouter({
  mode: 'history',
  base: __dirname,
  linkActiveClass: "mui-active",
  routes: [
    {path: "/login/", component: Login},
    {
      path: "/url_list/", meta: {
        requireAuth: true,  // 添加该字段，表示进入这个路由是需要登录的
      }, component: Url
    },
    {path: "/case_list/", component: CaseList},
    {path: "/add_cases/", component: AddCase},
    {path: "/add_url/", component: AddUrl},
    {path: "/update_url/:id", component: UpdateUrl},
    {path: "/update_case/:id", component: UpdateCase},
    {path: "/case_suite_list/", component: CaseSuiteList},
    {path: "/add_case_suite/", component: AddCaseSuite},
    {path: "/update_case_suite/:id", component: UpdateCaseSuite},
    {path: "/register/", component: Register},
    {path: "/user_list/", component: UserList},
    {path: "/add_user/", component: AddUser},
    {path: "/update_user/:id", component: UpdateUser},
    {path: "/reset_pwd/:id", component: ResetPwd},
  ]
});


Vue.prototype.$axios = axios;


/* eslint-disable no-new */
new Vue({
  router,
  template: `
    <div id="app">
    <router-view></router-view>
    </div>
  `

}).$mount("#app")


