<template>
  <div>
    <div class="container">
      <div class="logo"></div>
      <LoginBox />
    </div>
    <Footer />
  </div>
</template>

<script>
import LoginBox from "./LoginBox";
import SignUpBox from "../SignUp/SignUpBox";
import LoginFooter from "./Footer";

export default {
  components: {
    LoginBox,
    SignUpBox,
    LoginFooter
  }
};
</script>

<style lang="scss" scoped>
.container {
  width: 100% !important;
  margin: 75px auto 0 auto !important;
  padding: 0 !important;
  background-color: #fafafa;

  .logo {
    width: 360px;
    height: 82px;
    margin: 0 auto;
    background-image: url("http://sadmin.brandi.co.kr/include/img/logo_seller_admin_1.png");
    background-size: 130px 52px;
    background-repeat: no-repeat;
    background-position: center;
  }
}
.LoginFooter {
  width: 100vw;
  height: 74px;
  margin-top: 50px;
  padding-top: 30px;
  font-size: 12px;
  color: #999ba2;
  text-align: center;
  background-color: #35363a;
  div {
    margin-bottom: 5px;
    background-color: #35363a;
  }
}
</style>
