<template>
  <div class="signUpBox">
    <p>셀러회원 가입</p>
    <hr />
    <img class="signUpBanner" src="http://sadmin.brandi.co.kr/include/img/seller_join_top_2.png" />
    <p>가입 정보</p>

    <!-- id check input -->
    <input
      v-model="id.value"
      v-bind:class="{ defaultInput: id.state, warningInput: !id.state }"
      placeholder="아이디"
      @keyup="idCheck()"
    />
    <div
      v-bind:class="{ defaultText: id.state || id.value.length > 0, warningText: id.state || id.value.length == 0}"
    >필수 입력 항목입니다.</div>
    <div
      v-bind:class="{ defaultText: id.state || id.value.length == 0, warningText: !id.state && id.value.length >= 1}"
    >아이디는 5~20글자의 영문, 숫자, 언더바, 하이픈만 사용 가능하며 시작 문자는 영문 또는 숫자입니다.</div>

    <!-- pw check input -->
    <input
      type="password"
      v-model="pw.value"
      v-bind:class="{ defaultInput: pw.state, warningInput: !pw.state }"
      placeholder="비밀번호"
      @keyup="pwCheck()"
      class="defaultInput"
    />
    <div
      v-bind:class="{ defaultText: pw.state || pw.value.length > 0, warningText: pw.state || pw.value.length == 0}"
    >필수 입력 항목입니다.</div>
    <div
      v-bind:class="{ defaultText: pw.state || pw.value.length == 0, warningText: !pw.state && pw.value.length >= 1}"
    >비밀번호는 8~20글자의 영문대소문자, 숫자, 특수문자를 조합해야 합니다.</div>

    <!-- rePw recheck input -->
    <input
      type="password"
      v-model="rePw.value"
      v-bind:class="{ defaultInput: rePw.state, warningInput: !rePw.state }"
      placeholder="비밀번호 재입력"
    />
    <div
      v-bind:class="{ defaultText: rePw.value.length == 0 || pw.value === rePw.value, warningText: pw.value !== rePw.value}"
    >비밀번호가 일치하지 않습니다.</div>

    <!-- ph check input -->
    <div class="signUpManager">
      <p>담당자 정보</p>
      <p>(*실제 샵을 운영하시는 분)</p>
    </div>
    <input
      v-model="ph.value"
      v-bind:class="{ defaultInput: ph.state, warningInput: !ph.state }"
      placeholder="핸드폰번호"
      @keyup="phCheck()"
    />
    <div v-bind:class="{ defaultText: ph.state, warningText: !ph.state}">올바른 정보를 입력해주세요.</div>
    <i class="xi-info">입점 신청 후 브랜디 담당자가 연락을 드릴 수 있으니 정확한 정보를 기입해주세요.</i>

    <!-- info check input -->
    <div class="radioList">
      <p>셀러정보</p>
      <div class="radioBox">
        <v-radio-group v-model="sellerInfo" :mandatory="false">
          <v-radio label="쇼핑몰" value="radio-1"></v-radio>
          <v-radio label="마켓" value="radio-2"></v-radio>
          <v-radio label="로드샵" value="radio-3"></v-radio>
          <v-radio label="디자이너 브랜드" value="radio-4"></v-radio>
          <v-radio label="제너럴 브랜드" value="radio-5"></v-radio>
          <v-radio label="네셔널 브랜드" value="radio-6"></v-radio>
          <v-radio label="기타" value="radio-7"></v-radio>
        </v-radio-group>
      </div>
    </div>

    <!-- name check input -->
    <input
      v-model="sellerName.value"
      v-bind:class="{ defaultInput: sellerName.state, warningInput: !sellerName.state }"
      placeholder="셀러명(상호)"
      @keyup="nameCheck()"
    />
    <div
      v-bind:class="{ defaultText: sellerName.state || sellerName.value.length > 0 , warningText: sellerName.value.length == 0 || !sellerName.state}"
    >필수 입력 항목입니다.</div>
    <div
      v-bind:class="{ defaultText: sellerName.value >= 0 || sellerName.state, warningText: !sellerName.state}"
    >한글,영문,숫자만 입력해주세요.</div>

    <!-- engName check input -->
    <input
      v-model="sellerEngName.value"
      v-bind:class="{ defaultInput: sellerEngName.state, warningInput: !sellerEngName.state }"
      placeholder="영문 셀러명 (영문상호)"
      @keyup="engNameCheck()"
    />
    <div
      v-bind:class="{ defaultText: sellerEngName.state || sellerEngName.value.length > 0 , warningText: sellerEngName.value.length == 0 || !sellerEngName.state}"
    >필수 입력 항목입니다.</div>
    <div
      v-bind:class="{ defaultText: sellerEngName.value >= 0 || sellerEngName.state, warningText: !sellerEngName.state}"
    >셀러 영문명은 소문자만 입력가능합니다.</div>

    <!-- tel check input -->
    <input
      v-model="serviceTel.value"
      v-bind:class="{ defaultInput: serviceTel.state, warningInput: !serviceTel.state }"
      placeholder="고객센터 전화번호"
      @keyup="telCheck()"
      class="defaultInput"
    />
    <div
      v-bind:class="{ defaultText: serviceTel.state || serviceTel.value.length > 0 , warningText: serviceTel.value.length == 0 || !serviceTel.state}"
    >필수 입력 항목입니다.</div>
    <div
      v-bind:class="{ defaultText: serviceTel.value >= 0 || serviceTel.state, warningText: !serviceTel.state}"
    >고객센터 전화번호는 숫자와 하이픈만 입력가능합니다.</div>

    <!-- url check input -->
    <input
      v-model="serviceUrl.value"
      v-bind:class="{ defaultInput: serviceUrl.state, warningInput: !serviceUrl.state }"
      placeholder="사이트 URL"
      @keyup="urlCheck()"
    />
    <div
      v-bind:class="{ defaultText: serviceUrl.state || serviceUrl.value.length > 0 , warningText: serviceUrl.value.length == 0 || !serviceUrl.state}"
    >필수 입력 항목입니다.</div>
    <div
      v-bind:class="{ defaultText: serviceUrl.value >= 0 || serviceUrl.state, warningText: !serviceUrl.state}"
    >올바른 주소를 입력해주세요. (ex. http://www.brandi.co.kr)</div>

    <div class="signUpBtnBox">
      <!-- 신청 클릭 하면 패치로 포스트 해보자 -->
      <div class="signUpApply">신청</div>
      <div class="signUpCancel">
        <router-link to="/login">취소</router-link>
      </div>
    </div>
  </div>
</template>

<script>
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
      id: { value: "", state: true },
      pw: { value: "", state: true },
      rePw: { value: "", state: true },
      ph: { value: "", state: true },
      sellerInfo: { value: "", state: true },
      sellerName: { value: "", state: true },
      sellerEngName: { value: "", state: true },
      serviceTel: { value: "", state: true },
      serviceUrl: { value: "", state: true }
    };
  },
  methods: {
    //확인 후, 백엔드로 전송할 value값과 state값을 수정한다.
    idCheck: function() {
      /^[A-Za-z0-9]([-_]?[0-9a-zA-Z--_]){4,20}$/.test(this.id.value)
        ? (this.id.state = true)
        : (this.id.state = false);
    },
    //확인 후, 백엔드로 전송할 pw value값과 state값을 수정한다.
    pwCheck: function() {
      /^(?=.*[A-Za-z])(?=.*\d)(?=.*[$@$!%*#?&])[A-Za-z\d$@$!%*#?&]{8,20}$/.test(
        this.pw.value
      )
        ? ((this.pw.state = true), console.log(pw.state))
        : ((this.pw.state = false), console.log(pw.state));
    },
    //확인 후, 백엔드로 전송할 ph value, state
    phCheck: function() {
      /^\d{3}-\d{3,4}-\d{4}$/.test(this.ph.value)
        ? (this.ph.state = true)
        : (this.ph.state = false);
    },
    //확인 후, 백엔드로 전송할 상호명 value, state
    nameCheck: function() {
      /^[ㄱ-ㅣ가-힣-0-9A-Za-z]([0-9ㄱ-ㅣ가-힣A-Za-z]){0,20}$/.test(
        this.sellerName.value
      )
        ? (this.sellerName.state = true)
        : (this.sellerName.state = false);
    },

    //확인 후, 백엔드로 전송할 영문 상호명 value, state
    engNameCheck: function() {
      /^[a-z]*$/.test(this.sellerEngName.value)
        ? (this.sellerEngName.state = true)
        : (this.sellerEngName.state = false);
    },
    telCheck: function() {
      /(^02.{0}|^01.{1}|[0-9]{4})-([0-9]+)-([0-9]{4})/.test(
        this.serviceTel.value
      )
        ? (this.serviceTel.state = true)
        : (this.serviceTel.state = false);
    },
    urlCheck: function() {
      /(http|https):\/\/(\w+:{0,1}\w*@)?(\S+)(:[0-9]+)?(\/|\/([\w#!:.?+=&%@!\-\/]))?/.test(
        this.serviceUrl.value
      )
        ? (this.serviceUrl.state = true)
        : (this.serviceUrl.state = false);
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