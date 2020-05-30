<template>
  <div>
    <div class="text">
      | 상호 : (주)브랜디 | 주소 : (06223) 서울특별시 강남구 테헤란로 32길 26 청송빌딩 | 사업자등록번호 : 220-88-93187 | 통신판매업신고 : 2016-서울강남-00359호 | 이메일 : help@brandi.co.kr
      2018 © brandi inc.
    </div>
    <div class="toTop">
      <i class="xi-angle-up" @click="toTop()"></i>
    </div>
  </div>
</template>

<script>
export default {
  methods: {
    toTop: function() {
      window.scrollTo({
        top: 0,
        behavior: "smooth"
      });
    }
  }
};
</script>

<style lang="scss" scoped>
div {
  width: 100%;
  height: 49px;
  background-color: #363636;
  color: lightgray;
  display: flex;
  justify-content: space-between;
  align-items: center;
  .text {
    width: 939px;
    font-size: 12px;
    margin-left: 30px;
  }
  .toTop {
    display: flex;
    justify-content: center;
    align-items: center;
    width: 30px;
    height: 30px;
    border-radius: 50px;
    border: 1px solid #45484c;
    background-color: #45484c;
    margin-right: 30px;
    text-align: center;
    color: gray;
    cursor: pointer;
  }
}
</style>