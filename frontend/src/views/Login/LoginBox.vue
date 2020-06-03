<template>
  <div class="loginBox">
    <p>셀러 로그인</p>
    <div class="loginContainer">
      <div class="inputBox">
        <input
          v-model="loginValue"
          class="defaultInput"
          placeholder="셀러 아이디"
          v-bind:class="{ defaultInput: loginState, warningInput: !loginState }"
          @keyup="idKeyHandler()"
        />
        <span v-bind:class="{ defaultText: loginState, warningText: !loginState }">아이디를 입력해 주세요.</span>
      </div>

      <div class="inputBox">
        <input
          type="password"
          v-model="passwordValue"
          class="defaultInput"
          placeholder="셀러 비밀번호"
          v-bind:class="{ defaultInput: passwordState, warningInput: !passwordState }"
          @keyup="pwKeyHandler()"
        />
        <span
          v-bind:class="{ defaultText: passwordState, warningText: !passwordState }"
        >비밀번호를 입력해 주세요.</span>
      </div>
      <div class="loginOption">
        <label>
          <input type="checkbox" name="color" value="blue" /> 아이디/비밀번호 기억하기
        </label>
        <i class="xi-search">비밀번호 찾기</i>
      </div>

      <div class="buttonBox">
        <div class="signUpBtn">
          <router-link to="/signup">셀러가입</router-link>
        </div>
        <div class="loginBtn" @click="inputHandler()">로그인</div>
      </div>
    </div>
    <div class="bannerImg"></div>
  </div>
</template>

<script>
import axios from "axios";
import { SJ_URL } from "../../config/urlConfig";
export default {
  data() {
    return {
      loginState: true,
      passwordState: true,
      loginValue: "",
      passwordValue: ""
    };
  },
  mounted: function() {
    window.scrollTo({
      top: 0,
      behavior: "smooth"
    });
  },
  methods: {
    // 로그인 클릭시 실행되는 함수 : 아이디, 비밀번호 문자열 확인 후 0 이면 state false 리턴
    // 이 곳에 아이디, 비밀번호가 맞으면 백으로 아이디, 비밀번호 API POST 할 예정
    inputHandler: function() {
      this.loginValue.length ? "" : (this.loginState = false);
      this.passwordValue.length ? "" : (this.passwordState = false);

      if (this.passwordState && this.loginState) {
        axios
          .post(`${SJ_URL}/sign-in`, {
            method: "POST",
            user: this.loginValue,
            password: this.passwordValue
          })
          .then(response => {
            if (response.data.access_token) {
              localStorage.setItem("access_token", response.data.access_token);
              localStorage.setItem("id", this.loginValue);
              this.$router.push("/main/seller/sellerlist");
            } else {
              alert("아이디 또는 비밀번호가 다릅니다.");
            }
          })
          .catch(err => {
            console.log(err);
          });
      }
    },

    // 이이디 인풋창 입력시 실행되는 함수 : 문자열 길이가 0 보다 크거나 작음을 확인 후 state 변경
    idKeyHandler: function() {
      if (!this.loginState && this.loginValue.length) {
        this.loginState = true;
      } else if (this.loginState && !this.loginValue.length) {
        this.loginState = false;
      }
    },

    // 이이디 인풋창 입력시 실행되는 함수 : 문자열 길이가 0 보다 크거나 작음을 확인 후 state 변경
    pwKeyHandler: function() {
      if (!this.passwordState && this.passwordValue.length) {
        this.passwordState = true;
      } else if (this.passwordState && !this.passwordValue.length) {
        this.passwordState = false;
      }
    }
  }
};
</script>

<style lang="scss">
.loginBox {
  width: 360px;
  height: 543px;
  margin: 0 auto;
  background-color: #ffffff;
  display: flex;
  flex-direction: column;
  .loginContainer {
    padding: 0px 30px 15px 30px;
  }
  .warningInput {
    border-color: #b94a48;
  }
  p {
    margin: 20px 0;
    font-size: 24px;
    font-family: "Open Sans", sans-serif;
    background-color: #ffffff;
    font-weight: 300 !important;
    padding: 20px 30px 0px 30px;
  }
  .inputBox {
    display: flex;
    flex-direction: column;
  }

  .loginOption {
    margin-bottom: 30px;
    display: flex;
    justify-content: space-between;
    font-size: 14px;
    .xi-search {
      color: #296496;
      font-weight: 600;
      cursor: pointer;
      &:hover {
        text-decoration: underline;
      }
    }
  }
  .buttonBox {
    display: flex;
    flex-direction: row;
    justify-content: center;
    background-color: #ffffff;
    div:nth-of-type(1) {
      margin-right: 20px;
    }

    .signUpBtn {
      padding: 10px;
      border: 1px solid;
      border-radius: 5px;
      width: 80px;
      height: 35px;
      font-size: 14px;
      text-align: center;
      color: gray;
      cursor: pointer;
      background-color: #ffffff;
      border-color: lightgrey;
      &:hover {
        background-color: lightgrey;
        border-color: gray;
      }
      a:visited {
        color: black;
      }
    }
    .loginBtn {
      padding: 10px;
      border: 1px solid;
      border-radius: 5px;
      width: 80px;
      height: 35px;
      font-size: 14px;
      text-align: center;
      cursor: pointer;
      background-color: #31b1d5;
      color: #ffffff;
      &:hover {
        background-color: #2a9ebf;
      }
    }
  }
  .bannerImg {
    width: 100%;
    margin-top: 20px;
    height: 120px;
    background-image: url("http://sadmin.brandi.co.kr/include/img/admin_mainbn_helpi.png");
    background-size: contain;
    cursor: pointer;
  }
}
</style>