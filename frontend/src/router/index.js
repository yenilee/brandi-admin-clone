import Vue from 'vue'
import VueRouter from 'vue-router'
import Login from '../views/Login/Login.vue'
import SignUp from '../views/SignUp/SignUp.vue'
import Main from '../views/Main.vue'
import Product from '../components/Product'
import ProductList from '../views/ProductList/ProductList'
import ProductRegist from '../views/ProductRegist/ProductRegist'
import Seller from '../components/Seller'
import SellerList from '../views/SellerList/SellerList'
import SellerRegist from '../views/SellerRegist/SellerRegist'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
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
            component: ProductList,
          },
          {
            path: 'productRegist',
            component: ProductRegist,
          },
        ]
      },
      {
        path: 'seller',
        name: 'seller',
        component: Seller,
        children: [
          {
            path: 'sellerlist',
            component: SellerList,
            name: 'sellerlist'
          },
          {
            path: ':id',
            component: SellerRegist,
            name: 'sellerregist'
          },
        ]
      },
    ],
  }

]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
