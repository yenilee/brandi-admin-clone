<template>
  <div class="headerContainer">
    <div class="logoBox">
      <div class="headerLogo"></div>
    </div>
    <div class="headerUserInfo">
      <div class="url">https://www.brandi.co.kr/shop/{{user}}</div>
      <div class="urlBtn">My Shop Url 복사하기</div>
      <div class="userBox">
        <div @click="logoutHandle()" class="user">
          {{user}} Logout
          <i class="xi-angle-down-min"></i>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  mounted() {
    if (localStorage.id) {
      this.user = localStorage.id;
    }
  },
  data() {
    return {
      user: ""
    };
  },
  methods: {
    logoutHandle: function() {
      localStorage.removeItem("access_token");
      localStorage.removeItem("id");
      alert(`${this.user}님 로그아웃 하겠습니다.`);
      this.$router.push("/");
    }
  }
};
</script>

<style lang="scss" scoped>
.headerContainer {
  position: fixed;
  display: flex;
  justify-content: space-between;
  align-items: center;
  width: 100vw;
  height: 45px;
  background-color: #883b53;
  font-size: 13px;
  z-index: 5;
  .logoBox {
    display: flex;
    margin-left: 30px;
    .headerLogo {
      width: 100px;
      height: 25px;
      background-size: contain;
      background-image: url("http://sadmin.brandi.co.kr/include/img/logo_2.png");
    }
  }
  .headerUserInfo {
    display: flex;
    flex-direction: row;
    align-items: center;
    margin-right: 30px;
    .url {
      color: lightgray;
      margin-right: 20px;
    }
    .urlBtn {
      background-color: white;
      padding: 4px 10px;
      border-radius: 3px;
      margin-right: 20px;
      cursor: pointer;
    }
    .userBox {
      height: 45px;
      border-left: 1px solid #404347;
      padding-left: 15px;
      display: flex;
      align-items: center;
      .user {
        color: lightgray;
        padding: 12px 10px 0px 10px;
        height: 45px;
        cursor: pointer;
        &:hover {
          background-color: #404347;
        }
      }
    }
  }
}
</style>