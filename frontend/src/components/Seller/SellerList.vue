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
      <div class="tableOut">
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
                        v-model="manager_infos_phone_number"
                        type="text"
                      />
                    </td>
                    <td>
                      <input v-on:keyup.enter="search()" v-model="manager_infos_email" type="text" />
                    </td>
                    <td>
                      <input v-on:keyup.enter="search()" v-model="detail_attribute" type="text" />
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
                    <td>{{ item.seller_actions }}</td>
                  </tr>
                </tbody>
              </div>
            </template>
          </v-simple-table>
        </template>
      </div>
    </div>
  </div>
</template>
 


<script>
// sellerlist에 들어갈 header들을 config에서 관리하고 import 했습니다.
import { sellerListHeaders } from "../../config/SellerListDatas";
import axios from "axios";

export default {
  data() {
    return {
      headers: sellerListHeaders,
      infoDatas: [],
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
    axios
      .get("http://localhost:8080/test.json")
      .then(response => (this.infoDatas = response.data.seller_list));
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
    input {
      width: 100%;
      border: 1px solid lightgray;

      border-radius: 3px;
    }
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
      margin: 0 15px;
    }
    .tableOut {
      min-width: 1169px;
      overflow: auto;
      border: 1px solid lightgray;
      .tableIn {
        white-space: nowrap;
        min-width: 100%;
        padding: 0 !important;
        height: unset !important;
      }
    }
  }
  th,
  td {
    text-align: left;
    height: 39px !important;
    padding: 8px;
  }
  th {
    font-weight: 600;
    color: black !important;
    font-size: 13px !important;
    background-color: #eee;
  }
}
</style>