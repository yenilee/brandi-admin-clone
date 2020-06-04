<template>
  <div class="srContainer">
    <div class="srTitleBox">
      <div class="srTitle">셀러 정보 관리</div>
      <div class="srSubTitle">셀러 정보 조회 / 수정</div>
    </div>
    <div class="srCategory">
      <i class="xi-home">
        회원 관리
        <i class="xi-angle-right-min">셀러 정보 관리</i>
        <i class="xi-angle-right-min">셀러 정보 조회 / 수정</i>
      </i>
    </div>
  </div>
</template>

<script>
export default {};
</script>

<style lang="scss" scoped>
.srContainer {
  margin-top: 35px;
  .srTitleBox {
    padding: 0 20px;
    display: flex;
    align-items: flex-end;
    margin-bottom: 20px;

    .srTitle {
      font-size: 28px;
      color: #666;
      margin-right: 10px;
      font-weight: 300;
    }
    .srSubTitle {
      font-size: 14px;
      color: #666;
      font-weight: 300;
    }
  }
  .srCategory {
    width: 100%;
    height: 44px;
    font-size: 13px;
    display: flex;
    align-items: center;
    background-color: #eee;
    padding-left: 20px;
    margin-bottom: 10px;
  }
}
</style>