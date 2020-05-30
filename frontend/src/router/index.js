import Vue from 'vue'
import VueRouter from 'vue-router'
import Login from '../views/Login/Login.vue'
import SignUp from '../views/SignUp/SignUp.vue'
import Main from '../views/Main.vue'
import Product from '../components/Product.vue'
import ProductList from '../components/Product/ProductList.vue'
import ProductRegist from '../components/Product/ProductRegist.vue'
import Seller from '../components/Seller.vue'
import SellerList from '../components/Seller/SellerList.vue'
import SellerRegist from '../components/Seller/SellerRegist.vue'

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
          },
          {
            path: 'sellerregist',
            component: SellerRegist,
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
