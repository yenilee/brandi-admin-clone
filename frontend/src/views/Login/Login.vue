<template>
  <div>
    <div class="container">
      <div class="logo"></div>
      <LoginBox />
    </div>
    <LoginFooter />
  </div>
</template>

<script>
import LoginBox from "./LoginBox";
import SignUpBox from "../SignUp/SignUpBox";
import LoginFooter from "./LoginFooter";

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
</style>
