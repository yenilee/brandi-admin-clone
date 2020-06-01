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
          <select name="cars" id="cars">
            <option value="volvo">10</option>
            <option value="saab">20</option>
            <option value="opel">50</option>
            <option value="audi">150</option>
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
                      <input
                        v-on:keyup.enter="search()"
                        v-model="searchDatas.meta_data_id"
                        type="text"
                      />
                    </td>
                    <td>
                      <input
                        v-on:keyup.enter="search()"
                        v-model="searchDatas.seller_id"
                        type="text"
                      />
                    </td>
                    <td>
                      <input
                        v-on:keyup.enter="search()"
                        v-model="searchDatas.seller_eng_name"
                        type="text"
                      />
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
                      <input
                        v-on:keyup.enter="search()"
                        v-model="searchDatas.seller_status"
                        type="text"
                      />
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
                      <input
                        v-on:keyup.enter="search()"
                        v-model="searchDatas.detail_attribute"
                        type="text"
                      />
                    </td>
                    <td></td>
                    <td></td>
                    <td></td>
                    <td></td>
                  </tr>
                  <tr v-for="item in infoDatas" :key="item.name">
                    <td>{{ item.meta_data_id }}</td>
                    <td>{{ item.seller_id }}</td>
                    <td>{{ item.seller_eng_name }}</td>
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
                      <!-- "seller_actions"의 키를 들고와서 비교에 따라 표현 -->
                      <button v-for="action in item.seller_actions" :key="action">{{ action }}</button>
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
        meta_data_id: "",
        seller_id: "",
        seller_eng_name: "",
        seller_kor_name: "",
        seller_number: "",
        manager_infos_name: "",
        seller_status: "",
        manager_infos_phone_number: "",
        manager_infos_email: "",
        detail_attribute: ""
      }
    };
  },
  //로컬에 목업데이터를 위치해놓고, 해당 데이터들을 get하고 있습니다.
  mounted: function() {
    axios.get(`${URL}/sellerList.json`).then(response => {
      this.infoDatas = response.data.seller_list;
      this.usersData = response.data.number_of_users;
      this.pagesData = response.data.number_of_pages;
    });
  },
  methods: {
    search: function() {
      //이 곳에서 serachDatas의 내용을 post에 실어 백엔드에 보내준다.
      //그 다음에 바로 해당 내용들을 get해서 리스트에 뿌려주어야 한다.
      alert(this.searchDatas.meta_data_id);
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
    background-color: white;
    margin: 0 15px;
    width: calc(100% - 300px);
    border-radius: 5px;

    input {
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
          background-color: #5cb85c;
          border-color: #4cae4c;
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
}
</style>