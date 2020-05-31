<template>
  <div class="tableContainer">
    <div class="slTitleBox">
      <div class="slTitle">셀러 계정 관리</div>
      <div class="slSubTitle">셀러 회원 목록 / 관리</div>
    </div>
    <div class="slCategory">
      <i class="xi-home">
        회원 관리
        <i class="xi-angle-right-min">셀러 계정 관리</i>
        <i class="xi-angle-right-min">셀러 회원 리스트</i>
      </i>
    </div>
    <div class="tableBox">
      <div class="tableTitle">
        <i class="xi-list-dot"></i>
        <div>셀러 회원 리스트</div>
      </div>
      <div class="tableScroll">
        <template>
          <v-data-table
            :headers="headers"
            :items="desserts"
            :items-per-page="10"
            class="elevation-1"
          ></v-data-table>
        </template>
      </div>
    </div>
  </div>
</template>


<script>
export default {
  data() {
    return {
      headers: [
        { text: "번호", value: "name" },
        { text: "셀러이아디", value: "calories" },
        { text: "영문이름", value: "iron" },
        { text: "한글이름", value: "iron" },
        { text: "회원번호", value: "iron" },
        { text: "담당자이름", value: "iron" },
        { text: "셀러상태", value: "iron" },
        { text: "담당자연락처", value: "iron" },
        { text: "담당자이메일", value: "calories" },
        { text: "셀러속성", value: "iron" },
        { text: "상품개수", value: "iron" },
        { text: "URL", value: "protein" },
        { text: "등록일시", value: "iron" },
        { text: "Actions", value: "iron" }
      ],
      desserts: [
        {
          name: "1",
          calories: 159,
          fat: 9.0,
          carbs: 24,
          protein: <input type="text" />,
          iron: "naver.com"
        }
      ]
    };
  }
};
</script>
<style lang="scss" scoped>
.tableContainer {
  padding-top: 35px;
  width: 100%;
  .slTitleBox {
    padding: 0 20px;
    display: flex;
    align-items: flex-end;
    margin-bottom: 20px;

    .slTitle {
      font-size: 28px;
      color: #666;
      margin-right: 10px;
      font-weight: 300;
    }
    .slSubTitle {
      font-size: 14px;
      color: #666;
      font-weight: 300;
    }
  }
  .slCategory {
    width: 100%;
    height: 44px;
    font-size: 13px;
    display: flex;
    align-items: center;
    background-color: #eee;
    padding-left: 20px;
    margin-bottom: 10px;
  }
  .tableBox {
    border: 1px solid #d3d3d3;
    background-color: white;
    margin: 0 15px;
    .tableTitle {
      display: flex;
      align-items: center;
      height: 42px;

      background-color: #eee;
      font-size: 16px;
      color: #333;
    }
    .xi-list-dot {
      font-size: 18px;
      margin: 0 8px;
    }
    .tableScroll {
      width: 1169px;
      overflow: auto !important;

      border: 1px solid lightgray;
      .elevation-1 {
        min-width: 1200px;
        margin: 40px 5px;
        border: 1px solid green;
      }
    }
  }
}
</style>