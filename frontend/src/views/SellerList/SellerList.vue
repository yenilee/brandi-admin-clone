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
        <div class="leftTitle">
          <i class="xi-list-dot"></i>
          <div>셀러 회원 리스트</div>
        </div>

        <div class="excelBtn">
          <i class="xi-share">액셀 다운로드</i>
        </div>
      </div>

      <div class="tableOut">
        <div class="pageContainer">
          <span>Page</span>
          <button>
            <i class="xi-angle-left-min"></i>
          </button>
          <input type="text" />
          <button>
            <i class="xi-angle-right-min"></i>
          </button>
          <span>of {{pagesData}} | View</span>
          <select name="page">
            <option value="pageNum">10</option>
            <option value="pageNum">20</option>
            <option value="pageNum">50</option>
            <option value="pageNum">150</option>
          </select>
          <span>records Found total {{usersData}} records</span>
        </div>

        <!-- 테이블 시작 부분입니다. -->
        <template>
          <v-simple-table>
            <template v-slot:default>
              <div class="tableIn">
                <thead>
                  <tr>
                    <th class="text-left">번호</th>
                    <th class="text-left">셀러아이디</th>
                    <th class="text-left">영문이름</th>
                    <th class="text-left">한글이름</th>
                    <th class="text-left">회원번호</th>
                    <th class="text-left">담당자이름</th>
                    <th class="text-left">셀러상태</th>
                    <th class="text-left">담당자연락처</th>
                    <th class="text-left">담당자이메일</th>
                    <th class="text-left">셀러속성</th>
                    <th class="text-left">상품개수</th>
                    <th class="text-left">URL</th>
                    <th class="text-left">등록일시</th>
                    <th class="text-left">Actions</th>
                  </tr>
                </thead>
                <tbody>
                  <tr>
                    <td>
                      <input v-on:keyup.enter="search()" v-model="searchDatas.id" type="text" />
                    </td>
                    <td>
                      <input v-on:keyup.enter="search()" v-model="searchDatas.user" type="text" />
                    </td>
                    <td>
                      <input v-on:keyup.enter="search()" v-model="searchDatas.eng_name" type="text" />
                    </td>
                    <td>
                      <input
                        v-on:keyup.enter="search()"
                        v-model="searchDatas.seller_kor_name"
                        type="text"
                      />
                    </td>
                    <td>
                      <input
                        v-on:keyup.enter="search()"
                        v-model="searchDatas.seller_number"
                        type="text"
                      />
                    </td>
                    <td>
                      <input
                        v-on:keyup.enter="search()"
                        v-model="searchDatas.manager_infos_name"
                        type="text"
                      />
                    </td>
                    <td>
                      <select
                        class="sellerStatus"
                        name="sellerStatus"
                        v-model="searchDatas.seller_status"
                      >
                        <option value="status">입점대기</option>
                        <option value="status">입점</option>
                        <option value="status">퇴점</option>
                        <option value="status">퇴점대기</option>
                        <option value="status">휴점</option>
                      </select>
                    </td>
                    <td>
                      <input
                        v-on:keyup.enter="search()"
                        v-model="searchDatas.manager_infos_phone_number"
                        type="text"
                      />
                    </td>
                    <td>
                      <input
                        v-on:keyup.enter="search()"
                        v-model="searchDatas.manager_infos_email"
                        type="text"
                      />
                    </td>
                    <td>
                      <select class="sellerStatus" v-model="searchDatas.detail_attribute">
                        <option value="status">쇼핑몰</option>
                        <option value="status">마켓</option>
                        <option value="status">로드샵</option>
                        <option value="status">디자이너브랜드</option>
                        <option value="status">제너럴브랜드</option>
                        <option value="status">내셔널브랜드</option>
                        <option value="status">뷰티</option>
                      </select>
                    </td>
                    <td></td>
                    <td></td>
                    <!-- 달력이 있어야 할 곳 -->
                    <!-- 달력 -->
                    <td></td>
                  </tr>

                  <tr v-for="item in infoDatas" :key="item.name">
                    <!-- 아이디를 클릭하면 해당 아이디의 수정페이지로 넘어간다. -->
                    <td>{{ item.id }}</td>
                    <td>{{ item.user}}</td>
                    <td>{{ item.eng_name }}</td>
                    <td>{{ item.seller_kor_name }}</td>
                    <td>{{ item.seller_회원번호 }}</td>
                    <td>{{ item.manager_infos_name }}</td>
                    <td>{{ item.seller_status }}</td>
                    <td>{{ item.manager_infos_phone_number }}</td>
                    <td>{{ item.manager_infos_email }}</td>
                    <td>{{ item.detail_attribute }}</td>
                    <td>{{ item.detail_number_of_products }}</td>
                    <td>{{ item.detail_url }}</td>
                    <td>{{ item.created_at }}</td>
                    <td>
                      <!-- 클릭하면 상태를 post 하고, Post 처리가 된 뒤의 action 버튼들을 get 해야한다. -->
                      <div class="statusBtnBox" v-for="action in item.seller_actions" :key="action">
                        <button
                          style="background-color: #5bc0de; border-color: #46b8da;"
                          v-if="action === '입점 승인'"
                        >{{action}}</button>
                        <button
                          style="background-color: #d9534f;border-color: #d43f3a;"
                          v-if="action === '입점 거절' || action === '퇴점 신청 처리' || action === '퇴점 확정 처리'"
                        >{{action}}</button>
                        <button
                          style="background-color: #f0ad4e; border-color: #eea236;"
                          v-if="action === '휴점 신청'"
                        >{{action}}</button>
                        <button
                          style="background-color: #5cb85c; border-color: #4cae4c;"
                          v-if="action === '퇴점 철회 처리' || action === '휴점 해제'"
                        >{{action}}</button>
                      </div>
                    </td>
                  </tr>
                </tbody>
              </div>
            </template>
          </v-simple-table>
        </template>
        <div class="pageContainer">
          <span>Page</span>
          <button>
            <i class="xi-angle-left-min"></i>
          </button>
          <input type="text" />
          <button>
            <i class="xi-angle-right-min"></i>
          </button>
          <span>of {{pagesData}} | View</span>
          <select name="cars" id="cars">
            <option value="volvo">10</option>
            <option value="saab">20</option>
            <option value="opel">50</option>
            <option value="audi">150</option>
          </select>
          <span>records Found total {{usersData}} records</span>
        </div>
      </div>
    </div>
  </div>
</template>
 


<script>
import axios from "axios";
import { sellerListHeaders } from "../../config/SellerListDatas";
import { URL } from "../../config/urlConfig";

export default {
  data() {
    return {
      headers: sellerListHeaders,
      infoDatas: [],
      usersData: null,
      pagesData: null,
      searchDatas: {
        id: "",
        user: "",
        eng_name: "",
        seller_kor_name: "",
        seller_number: "",
        manager_infos_name: "",
        seller_status: "",
        manager_infos_phone_number: "",
        manager_infos_email: "",
        detail_attribute: "",
        created_at: ""
      },
      dates: ["2020-06-03", "2020-06-24"]
    };
  },
  //로컬에 목업데이터를 위치해놓고, 해당 데이터들을 get하고 있습니다.
  mounted: function() {
    axios.get(`${URL}/sellerList.json`).then(response => {
      this.infoDatas = response.data.seller;
      this.usersData = response.data.number_of_sellers;
      this.pagesData = response.data.number_of_pages;
    });
  },
  computed: {
    dateRangeText() {
      return this.dates.join(" ~ ");
    }
  },
  methods: {
    search: function() {
      //이 곳에서 serachDatas의 내용을 post에 실어 백엔드에 보내준다.
      //그 다음에 바로 해당 내용들을 get해서 리스트에 뿌려주어야 한다.
      alert(this.searchDatas.id);
    }
  }
};
</script>
<style lang="scss" scoped>
.tableContainer {
  padding-top: 35px;

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
  .pageContainer {
    display: flex;
    align-items: center;
    font-size: 13px;
    margin: 5px 15px;
    span,
    button,
    input,
    select {
      padding: 8px;
      margin-right: 10px;
      border-radius: 3px;
    }
    button,
    select {
      border: 1px solid lightgray;
    }
    select {
      width: 80px;
    }
    input {
      width: 50px !important;
    }
  }
  .tableBox {
    border: 1px solid #d3d3d3;
    margin: 0 15px;
    border-radius: 5px;

    input,
    .sellerStatus {
      width: 100%;
      border: 1px solid lightgray;
      border-radius: 3px;
    }
    .tableTitle {
      display: flex;
      justify-content: space-between;
      align-items: center;
      height: 42px;

      background-color: #eee;
      font-size: 16px;
      color: #333;
      .leftTitle {
        display: flex;
        align-items: center;
        justify-content: center;
      }
      .excelBtn {
        margin-right: 15px;
        color: #fff;
        background-color: #5cb85c;
        border-color: #4cae4c;
        padding: 4px 10px;
        font-size: 14px;
        font-weight: 800;
        line-height: 1.42857143;
        text-align: center;
        cursor: pointer;
        border-radius: 4px;
      }
    }
    .xi-list-dot {
      font-size: 18px;
      margin: 0 15px;
    }
    .statusBtnBox {
      display: inline;
      font-size: 12px;
    }
    .tableOut {
      min-width: 100%;
      .tableIn {
        width: calc(100vw - 335px);
        overflow: auto;
        white-space: nowrap;
        margin: 0 15px;
        border: 1px solid lightgray;
        button {
          padding: 5px;
          color: #fff;
          border-radius: 3px;
          margin-left: 5px;
        }
      }
    }
  }
  th,
  td {
    text-align: left;
    height: 39px !important;
    padding: 12px 8px 8px 8px;
    border: 1px solid #ddd;
    border-left-width: 0 !important;
    border-bottom-width: 0 !important;
  }
  th {
    font-weight: 600;
    color: black !important;
    font-size: 13px !important;
    background-color: #eee;
  }
  .dateBox {
    border: 1px solid red;
    width: 50%;
    height: 50%;
  }
}
</style>