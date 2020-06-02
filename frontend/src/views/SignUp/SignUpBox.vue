<template>
  <div class="signUpBox">
    <p>셀러회원 가입</p>
    <hr />
    <img class="signUpBanner" src="http://sadmin.brandi.co.kr/include/img/seller_join_top_2.png" />
    <p>가입 정보</p>

    <!-- user check input -->
    <input
      v-model="user.value"
      v-bind:class="{ defaultInput: user.state, warningInput: !user.state }"
      placeholder="아이디"
      @keyup="idCheck()"
    />
    <div
      v-bind:class="{ defaultText: user.state || user.value.length > 0, warningText: user.state || user.value.length == 0}"
    >필수 입력 항목입니다.</div>
    <div
      v-bind:class="{ defaultText: user.state || user.value.length == 0, warningText: !user.state && user.value.length >= 1}"
    >아이디는 5~20글자의 영문, 숫자, 언더바, 하이픈만 사용 가능하며 시작 문자는 영문 또는 숫자입니다.</div>

    <!-- password check input -->
    <input
      type="password"
      v-model="password.value"
      v-bind:class="{ defaultInput: password.state, warningInput: !password.state }"
      placeholder="비밀번호"
      @keyup="pwCheck()"
      class="defaultInput"
    />
    <div
      v-bind:class="{ defaultText: password.state || password.value.length > 0, warningText: password.state || password.value.length == 0}"
    >필수 입력 항목입니다.</div>
    <div
      v-bind:class="{ defaultText: password.state || password.value.length == 0, warningText: !password.state && password.value.length >= 1}"
    >비밀번호는 8~20글자의 영문대소문자, 숫자, 특수문자를 조합해야 합니다.</div>

    <!-- rePw recheck input -->
    <input
      type="password"
      v-model="rePw.value"
      v-bind:class="{ defaultInput: rePw.state, warningInput: !rePw.state }"
      placeholder="비밀번호 재입력"
    />
    <div
      v-bind:class="{ defaultText: rePw.value.length == 0 || password.value === rePw.value, warningText: password.value !== rePw.value}"
    >비밀번호가 일치하지 않습니다.</div>

    <!-- phone_number check input -->
    <div class="signUpManager">
      <p>담당자 정보</p>
      <p>(*실제 샵을 운영하시는 분)</p>
    </div>
    <input
      v-model="phone_number.value"
      v-bind:class="{ defaultInput: phone_number.state, warningInput: !phone_number.state }"
      placeholder="핸드폰번호"
      @keyup="phCheck()"
    />
    <div
      v-bind:class="{ defaultText: phone_number.state, warningText: !phone_number.state}"
    >올바른 정보를 입력해주세요.</div>
    <i class="xi-info">입점 신청 후 브랜디 담당자가 연락을 드릴 수 있으니 정확한 정보를 기입해주세요.</i>

    <!-- info check input -->
    <div class="radioList">
      <p>셀러정보</p>
      <div class="radioBox">
        <v-radio-group v-model="seller_attribute_id.value" :mandatory="false">
          <v-radio label="쇼핑몰" value="1"></v-radio>
          <v-radio label="마켓" value="2"></v-radio>
          <v-radio label="로드샵" value="3"></v-radio>
          <v-radio label="디자이너 브랜드" value="4"></v-radio>
          <v-radio label="제너럴 브랜드" value="5"></v-radio>
          <v-radio label="네셔널 브랜드" value="6"></v-radio>
          <v-radio label="기타" value="7"></v-radio>
        </v-radio-group>
      </div>
    </div>

    <!-- name check input -->
    <input
      v-model="name.value"
      v-bind:class="{ defaultInput: name.state, warningInput: !name.state }"
      placeholder="셀러명(상호)"
      @keyup="nameCheck()"
    />
    <div
      v-bind:class="{ defaultText: name.state || name.value.length > 0 , warningText: name.value.length == 0 || !name.state}"
    >필수 입력 항목입니다.</div>
    <div
      v-bind:class="{ defaultText: name.value >= 0 || name.state, warningText: !name.state}"
    >한글,영문,숫자만 입력해주세요.</div>

    <!-- engName check input -->
    <input
      v-model="eng_name.value"
      v-bind:class="{ defaultInput: eng_name.state, warningInput: !eng_name.state }"
      placeholder="영문 셀러명 (영문상호)"
      @keyup="engNameCheck()"
    />
    <div
      v-bind:class="{ defaultText: eng_name.state || eng_name.value.length > 0 , warningText: eng_name.value.length == 0 || !eng_name.state}"
    >필수 입력 항목입니다.</div>
    <div
      v-bind:class="{ defaultText: eng_name.value >= 0 || eng_name.state, warningText: !eng_name.state}"
    >셀러 영문명은 소문자만 입력가능합니다.</div>

    <!-- tel check input -->
    <input
      v-model="service_number.value"
      v-bind:class="{ defaultInput: service_number.state, warningInput: !service_number.state }"
      placeholder="고객센터 전화번호"
      @keyup="telCheck()"
      class="defaultInput"
    />
    <div
      v-bind:class="{ defaultText: service_number.state || service_number.value.length > 0 , warningText: service_number.value.length == 0 || !service_number.state}"
    >필수 입력 항목입니다.</div>
    <div
      v-bind:class="{ defaultText: service_number.value >= 0 || service_number.state, warningText: !service_number.state}"
    >고객센터 전화번호는 숫자와 하이픈만 입력가능합니다.</div>

    <!-- url check input -->
    <input
      v-model="site_url.value"
      v-bind:class="{ defaultInput: site_url.state, warningInput: !site_url.state }"
      placeholder="사이트 URL"
      @keyup="urlCheck()"
    />
    <div
      v-bind:class="{ defaultText: site_url.state || site_url.value.length > 0 , warningText: site_url.value.length == 0 || !site_url.state}"
    >필수 입력 항목입니다.</div>
    <div
      v-bind:class="{ defaultText: site_url.value >= 0 || site_url.state, warningText: !site_url.state}"
    >올바른 주소를 입력해주세요. (ex. http://www.brandi.co.kr)</div>

    <div class="signUpBtnBox">
      <!-- 신청 클릭 하면 패치로 포스트 해보자 -->
      <div class="signUpApply" @click="signUpClick()">신청</div>
      <div class="signUpCancel">
        <router-link to="/login">취소</router-link>
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";
export default {
  name: "SignUpBox",
  mounted: function() {
    window.scrollTo({
      top: 0,
      behavior: "smooth"
    });
  },
  data() {
    return {
      user: { value: "", state: true },
      password: { value: "", state: true },
      rePw: { value: "", state: true },
      phone_number: { value: "", state: true },
      seller_attribute_id: { value: "", state: true },
      name: { value: "", state: true },
      eng_name: { value: "", state: true },
      service_number: { value: "", state: true },
      site_url: { value: "", state: true }
    };
  },
  methods: {
    //확인 후, 백엔드로 전송할 value값과 state값을 수정한다.
    idCheck: function() {
      /^[A-Za-z0-9]([-_]?[0-9a-zA-Z--_]){4,20}$/.test(this.user.value)
        ? (this.user.state = true)
        : (this.user.state = false);
    },
    //확인 후, 백엔드로 전송할 password value값과 state값을 수정한다.
    pwCheck: function() {
      /^(?=.*[A-Za-z])(?=.*\d)(?=.*[$@$!%*#?&])[A-Za-z\d$@$!%*#?&]{8,20}$/.test(
        this.password.value
      )
        ? ((this.password.state = true), console.log(password.state))
        : ((this.password.state = false), console.log(password.state));
    },
    //확인 후, 백엔드로 전송할 phone_number value, state
    phCheck: function() {
      /^\d{3}-\d{3,4}-\d{4}$/.test(this.phone_number.value)
        ? (this.phone_number.state = true)
        : (this.phone_number.state = false);
    },
    //확인 후, 백엔드로 전송할 상호명 value, state
    nameCheck: function() {
      /^[ㄱ-ㅣ가-힣-0-9A-Za-z]([0-9ㄱ-ㅣ가-힣A-Za-z]){0,20}$/.test(
        this.name.value
      )
        ? (this.name.state = true)
        : (this.name.state = false);
    },

    //확인 후, 백엔드로 전송할 영문 상호명 value, state
    engNameCheck: function() {
      /^[a-z]*$/.test(this.eng_name.value)
        ? (this.eng_name.state = true)
        : (this.eng_name.state = false);
    },
    telCheck: function() {
      /(^02.{0}|^01.{1}|[0-9]{4})-([0-9]+)-([0-9]{4})/.test(
        this.service_number.value
      )
        ? (this.service_number.state = true)
        : (this.service_number.state = false);
    },
    urlCheck: function() {
      /(http|https):\/\/(\w+:{0,1}\w*@)?(\S+)(:[0-9]+)?(\/|\/([\w#!:.?+=&%@!\-\/]))?/.test(
        this.site_url.value
      )
        ? (this.site_url.state = true)
        : (this.site_url.state = false);
    },
    signUpClick: function() {
      axios
        .post("http://192.168.7.40:5000/sign-up", {
          method: "POST",
          user: this.user.value,
          seller_attribute_id: this.seller_attribute_id.value,
          password: this.password.value,
          phone_number: this.phone_number.value,
          name: this.name.value,
          eng_name: this.eng_name.value,
          service_number: this.service_number.value,
          site_url: this.site_url.value,
          end_date: this.end_date
        })
        .then(response => {
          alert("성공");
        });
    },
    radios: function() {}
  }
};
</script>

<style lang="scss">
.signUpBox {
  width: 470px !important;
  height: 937px;
  margin: 0 auto;
  padding: 20px 30px 15px 30px;
  background-color: #ffffff !important  ;
  display: flex;
  flex-direction: column;
  p:nth-of-type(1) {
    margin-top: 20px;
    font-size: 24px;
    font-weight: 300 !important;
    text-align: center;
    background-color: #ffffff;
  }
  hr {
    position: relative;
    margin: 20px 0;
  }
  .signUpBanner {
    width: 408px;
    height: 45px;
    margin: 0 auto 40px auto;
  }
  p:nth-of-type(2) {
    margin-bottom: 20px;
    font-size: 22px;
    font-weight: 300;
    background-color: #ffffff;
  }
  .signUpManager {
    display: flex;
    flex-direction: row;
    align-items: flex-end;
    margin-bottom: 20px;
    p {
      margin: 0;
      font-weight: 300;
    }
    p:nth-of-type(1) {
      font-size: 22px;
      margin-right: 10px;
    }
    p:nth-of-type(2) {
      font-size: 16px;
      color: rgb(30, 144, 255);
    }
  }
  .xi-info {
    display: inline;
    font-size: 12px;
    font-weight: 500;
    color: rgb(30, 144, 255);
    letter-spacing: 1px;
    word-spacing: -7px;
    background-color: #ffffff;
  }

  .radioList {
    p {
      text-align: left;
      font-size: 24px;
      font-weight: 300 !important;
    }
    .radioBox {
      background-color: #ffffff;
      div {
        display: inline-block;
        margin-right: 10px;
      }
      label {
        font-size: 14px;
      }
    }
  }
  .signUpBtnBox {
    display: flex;
    flex-direction: row;
    justify-content: center;
    background-color: #ffffff;
    div {
      padding: 10px 10px;
      color: #ffffff;
      font-size: 14px;
      font-weight: 400;
      cursor: pointer;
    }
    .signUpApply {
      width: 50px;
      height: 35px;
      background-color: #31b1d5;
      border-top-left-radius: 4px;
      border-bottom-left-radius: 4px;
    }
    .signUpCancel {
      width: 50px;
      height: 35px;
      background-color: #c9302c;
      border: 1px solid red;
      border-top-right-radius: 4px;
      border-bottom-right-radius: 4px;
    }
  }
}
</style>