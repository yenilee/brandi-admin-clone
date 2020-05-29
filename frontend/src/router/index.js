import Vue from 'vue'
import VueRouter from 'vue-router'
import Login from '../views/Login/Login.vue'
import SignUp from '../views/SignUp/SignUp.vue'
import SellerRegist from '../views/ProductRegist/ProductRegist.vue'
import SellerList from '../views/ProductList/ProductList.vue'
import ProductRegist from '../views/ProductRegist/ProductRegist.vue'
import ProductList from '../views/ProductList/ProductList.vue'

Vue.use(VueRouter)

const routes = [
  {
    path: '/login',
    name: 'Login',
    component: Login
  },
  {
    path: '/SignUp',
    name: 'SignUp',
    component: SignUp
  },
  {
    path: '/SellerRegist',
    name: 'SellerRegist',
    component: SellerRegist
  },
  {
    path: '/SellerList',
    name: 'SellerList',
    component: SellerList
  },
  {
    path: '/ProductRegist',
    name: 'ProductRegist',
    component: ProductRegist
  },
  {
    path: '/ProductList',
    name: 'ProductList',
    component: ProductList
  },
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
