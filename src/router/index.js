import {createRouter, createWebHistory} from 'vue-router'
import Home from '../pages/Home.vue'

const routes = [
  {
    path: '/',
    component: Home
  }
]

const router = new createRouter({
  history: createWebHistory(),
  routes
})


export default router
