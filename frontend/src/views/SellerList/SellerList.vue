<template>
  <div class="tableContainer">
    <div class="slTitleBox">
      <div class="slTitle">셀러 계정 관리</div>
      <div class="slSubTitle">셀러 회원 목록 / 관리</div>
      <div></div>
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
                      <input
                        @keydown="() => lengthCheck(0)"
                        v-on:keyup.enter="search()"
                        v-model="searchDatas[0].id"
                        type="text"
                      />
                    </td>
                    <td>
                      <input
                        @keydown="() => lengthCheck(1)"
                        v-on:keyup.enter="search()"
                        v-model="searchDatas[1].id"
                        type="text"
                      />
                    </td>
                    <td>
                      <input
                        @keydown="() => lengthCheck(2)"
                        v-on:keyup.enter="search()"
                        v-model="searchDatas[2].id"
                        type="text"
                      />
                    </td>
                    <td>
                      <input
                        @keydown="() => lengthCheck(3)"
                        v-on:keyup.enter="search()"
                        v-model="searchDatas[3].id"
                        type="text"
                      />
                    </td>
                    <td>
                      <input
                        @keydown="() => lengthCheck(4)"
                        v-on:keyup.enter="search()"
                        v-model="searchDatas[4].id"
                        type="text"
                      />
                    </td>
                    <td>
                      <select
                        class="sellerStatus"
                        @click="() => lengthCheck(7)"
                        v-model="searchDatas[7].id"
                      >
                        <option value>선택</option>
                        <option value="1">입점대기</option>
                        <option value="2">입점</option>
                        <option value="5">퇴점</option>
                        <option value="4">퇴점대기</option>
                        <option value="3">휴점</option>
                      </select>
                    </td>
                    <td>
                      <input
                        @keydown="() => lengthCheck(5)"
                        v-on:keyup.enter="search()"
                        v-model="searchDatas[5].id"
                        type="text"
                      />
                    </td>

                    <td>
                      <input
                        @keydown="() => lengthCheck(6)"
                        v-on:keyup.enter="search()"
                        v-model="searchDatas[6].id"
                        type="text"
                      />
                    </td>
                    <td>
                      <select
                        class="sellerStatus"
                        @click="() => lengthCheck(8)"
                        v-model="searchDatas[8].id"
                      >
                        <option value>선택</option>
                        <option value="1">쇼핑몰</option>
                        <option value="2">마켓</option>
                        <option value="3">로드샵</option>
                        <option value="4">디자이너브랜드</option>
                        <option value="5">제너럴브랜드</option>
                        <option value="6">내셔널브랜드</option>
                        <option value="7">뷰티</option>
                      </select>
                    </td>
                    <td></td>

                    <td></td>
                    <td></td>
                    <td class="actionBtns">
                      <div class="searchBtn" @click="search()">Search</div>
                      <div class="resetBtn" @click="reset()">Reset</div>
                    </td>
                  </tr>

                  <tr v-for="item in infoDatas" :key="item.id">
                    <!-- 아이디를 클릭하면 해당 아이디의 수정페이지로 넘어간다. -->
                    <td>{{ item.id }}</td>
                    <td
                      @click="() => idClick(item.seller_key_id)"
                      class="sellerIdText"
                    >{{ item.seller_id}}</td>
                    <td>{{ item.seller_eng_name }}</td>
                    <td>{{ item.seller_kor_name }}</td>
                    <td>{{ item.manager_name }}</td>
                    <td>{{ item.status_name}}</td>
                    <td>{{ item.manager_phone_number }}</td>
                    <td>{{ item.manager_email }}</td>
                    <td>{{ item.seller_attribute_name }}</td>
                    <td>{{ item.number_of_product }}</td>
                    <td>{{ item.site_url }}</td>
                    <td>{{ item.created_at }}</td>
                    <td>
                      <!-- 클릭하면 상태를 post 하고, Post 처리가 된 뒤의 action 버튼들을 get 해야한다. -->
                      <div
                        class="statusBtnBox"
                        v-for="action in item.actions_by_status"
                        :key="action"
                      >
                        <button
                          style="background-color: #5bc0de; border-color: #46b8da;"
                          v-if="action === '입점 승인'"
                          @click="() => actionClick(action,item.seller_key_id)"
                        >{{action}}</button>
                        <button
                          style="background-color: #d9534f;border-color: #d43f3a;"
                          v-if="action === '입점 거절' || action === '퇴점 신청 처리' || action === '퇴점 확정 처리'"
                          @click="() => actionClick(action,item.seller_key_id)"
                        >{{action}}</button>
                        <button
                          style="background-color: #f0ad4e; border-color: #eea236;"
                          v-if="action === '휴점 신청'"
                          @click="() => actionClick(action,item.seller_key_id)"
                        >{{action}}</button>
                        <button
                          style="background-color: #5cb85c; border-color: #4cae4c;"
                          v-if="action === '퇴점 철회 처리' || action === '휴점 해제'"
                          @click="() => actionClick(action,item.seller_key_id)"
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
          <select name id>
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
import { URL, SJ_URL, YE_URL } from "../../config/urlConfig";

export default {
  data() {
    return {
      headers: sellerListHeaders,
      infoDatas: [],
      usersData: null,
      pagesData: null,
      searchDatas: [
        { name: "sellers.id", id: "", state: false },
        { name: "seller_keys.user", id: "", state: false },
        { name: "sellers.eng_name", id: "", state: false },
        { name: "sellers.name", id: "", state: false },
        { name: "supervisor_infos.name", id: "", state: false },
        { name: "supervisor_infos.phone_number", id: "", state: false },
        { name: "supervisor_infos.email", id: "", state: false },
        { name: "seller_status.id", id: "", state: false },
        { name: "seller_attributes.id", id: "", state: false }
      ],
      dates: ["2020-06-03", "2020-06-24"]
    };
  },
  //로컬에 목업데이터를 위치해놓고, 해당 데이터들을 get하고 있습니다.
  mounted: function() {
    this.getListDatas();
  },

  methods: {
    lengthCheck: function(index) {
      this.searchDatas[index].id.length == 0
        ? (this.searchDatas[index].state = false)
        : (this.searchDatas[index].state = true);
    },
    getListDatas: function() {
      axios
        .get(`${YE_URL}/sellers`, {
          // .get(`${URL}/sellerList.json`, {
          headers: {
            Authorization: localStorage.access_token
          }
        })
        .then(response => {
          this.infoDatas = response.data.sellers;
          this.usersData = response.data.number_of_sellers;
          this.pagesData = response.data.number_of_pages;
          console.log(response);
        });
    },
    idClick: function(id) {
      // console.log("url data >>>> ", this.$route.query.page);
      // this.$router.push(`/main/seller/sellerregist:${id}`);
      this.$router.push({ name: "sellerregist", params: { id: id } });
    },
    actionClick: function(action, id) {
      if (
        action === "입점 승인" ||
        action === "입점 거절" ||
        action === "휴점 해제"
      ) {
        if (confirm(`${action} 하시겠습니까?`) == true) {
          this.actionBtnChange(action, id);
        }
      }

      if (
        action === "휴점 신청" ||
        action === "퇴점 철회 처리" ||
        action === "퇴점 신청 처리"
      ) {
        if (
          confirm(
            `${action} 시 셀러의 모든 상품이 미진열/미판매로 전환 되고,상품 관리를 할 수 없게 됩니다. ${action} 하시겠습니까?`
          ) === true
        ) {
          this.actionBtnChange(action, id);
        }
      }
    },
    actionBtnChange: function(action, id) {
      axios
        .put(
          `${YE_URL}/action`,
          {
            user: id,
            action_type: action
          },

          {
            headers: {
              Authorization: localStorage.access_token
            }
          }
        )
        .then(response => {
          console.log(response);
          if (response.status === 200) {
            alert("정상처리 되었습니다.");
          }
        })
        .catch(error => {
          console.log(error.response.data.message);
        })
        .then(response => {
          this.getListDatas();
        });
    },
    search: function() {
      let queryString = [];
      //이 곳에서 serachDatas의 내용을 post에 실어 백엔드에 보내준다.
      //그 다음에 바로 해당 내용들을 get해서 리스트에 뿌려주어야 한다.
      // console.log("url data >>>> ", this.$route.query.page);
      // this.$router.push("sellers?seller_attributes.name=쇼핑몰");
      // axios.get(`${YE_URL}/sellers`);
      // alert(this.searchDatas.id);
      this.searchDatas.filter(item => {
        item.state && item.id.length != 0
          ? queryString.push(`${item.name}=${item.id}&`)
          : "";
      });
      axios
        .get(`${YE_URL}/sellers?${queryString.join("")}`, {
          headers: {
            Authorization: localStorage.access_token
          }
        })
        .then(response => {
          this.infoDatas = response.data.sellers;
          this.usersData = response.data.number_of_sellers;
          this.pagesData = response.data.number_of_pages;
          console.log(response);
        });
    },
    reset: function() {
      this.searchDatas.map(item => {
        item.id = "";
      });
      this.search();
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

    .sellerIdText {
      color: #0d638f;

      &:hover {
        cursor: pointer;
        text-decoration: underline;
      }
    }

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
    .actionBtns {
      div {
        border: 1px solid red;
        padding: 5px 10px;
        font-size: 13px;
        line-height: 1.5;
        border-radius: 3px;
        font-weight: 800;
        display: inline-block;
        text-align: center;
        white-space: nowrap;
        vertical-align: middle;
        cursor: pointer;
        margin-right: 10px;
      }
      .searchBtn {
        color: #fff;
        background-color: #f0ad4e;
        border-color: #eea236;
      }
      .resetBtn {
        color: #fff;
        background-color: #d9534f;
        border-color: #d43f3a;
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