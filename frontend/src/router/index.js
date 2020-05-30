import Vue from 'vue'
import VueRouter from 'vue-router'
import Login from '../views/Login/Login.vue'
import SignUp from '../views/SignUp/SignUp.vue'
import Main from '../views/Main.vue'
import Product from '../components/Product/Product.vue'
import ProductList from '../components/Product/ProductList.vue'
import ProductRegist from '../components/Product/ProductRegist.vue'

Vue.use(VueRouter)

const routes = [
  {
    path: '/login',
    name: 'Login',
    component: Login
  },
  {
    path: '/signUp',
    name: 'SignUp',
    component: SignUp
  },
  {
    path: '/main',
    name: 'Main',
    component: Main,
    children: [
      {
        path: 'product',
        name: 'product',
        component: Product,
        children: [
          {
            path: 'productlist',
            name: 'productlist',
            component: ProductList
          },
          {
            path: 'productregist',
            name: 'productregist',
            component: ProductRegist
          }
        ]
      }
    ],
  }

]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
