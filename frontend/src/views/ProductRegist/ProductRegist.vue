<template>
  <div class="prWrap">
    <div class="slTitleBox">
      <div class="slTitle">상품 등록</div>
      <div class="slSubTitle">상품 정보 등록</div>
    </div>
    <div class="slCategory">
      <i class="xi-home">
        상품 관리
        <i class="xi-angle-right-min">상품 관리</i>
        <i class="xi-angle-right-min">상품 등록</i>
      </i>
    </div>
    <div class="cmpWrap">
      <div class="cmpTitle">
        <i class="xi-user">기본 정보</i>
      </div>
      <div class="cmpTable">
        <!-- 셀러검색모달 -->
        <div v-if="sellersModal === true" class="sellersModal">
          <div class="slTitleBox">
            <div class="slTitle">셀러 선택</div>
            <div class="titleLine"></div>
            <i class="xi-info">미판매 선택시 앱에서 Sold Out으로 표시됩니다.</i>
            <div class="inputBox">
              <div class="text">셀러검색</div>
              <div>
                <div class="inputSelect">{{sellerInfo.name? sellerInfo.name: "Select"}}</div>
                <input type="text" @input="searchSellerList($event.target.value)" />
                <div class="searchResult">
                  <div v-for="seller in sellerList" :key="seller.id">
                    <div
                      @click="selectSeller(seller.seller_key_id, seller.seller_name)"
                    >{{searchSeller.length ? seller.seller_name : ""}}</div>
                  </div>
                </div>
                <div>선택</div>
              </div>
            </div>
          </div>
        </div>
        <v-simple-table>
          <template>
            <!-- 테이블 시작 영역 -->
            <!-- 셀러 상태 테이블 -->
            <tbody>
              <tr class="sellerSelect">
                <th>셀러 선택</th>
                <td>
                  <input type="text" placeholder="셀러검색을 해주세요." v-model="sellerInfo.name" />
                  <div @click="sellersModal = !sellersModal" class="btn">셀러검색</div>
                </td>
              </tr>
            </tbody>
            <!-- 판매여부 -->
            <tbody>
              <tr>
                <th>판매여부</th>
                <td class="onSaleBox">
                  <div>
                    <input
                      v-model="infoDatas.is_onsale"
                      type="radio"
                      id="onSale"
                      value="1"
                      name="saleStatus"
                    />
                    <label for="onSale">판매</label>
                    <input
                      v-model="infoDatas.is_onsale"
                      type="radio"
                      id="noSale"
                      value="0"
                      name="saleStatus"
                    />
                    <label for="noSale">미판매</label>
                  </div>
                  <div>
                    <i class="xi-info">미판매 선택시 앱에서 Sold Out으로 표시됩니다.</i>
                  </div>
                </td>
              </tr>
            </tbody>
            <!--진열 여부 -->
            <tbody>
              <tr>
                <th>진열여부</th>
                <td class="onSaleBox">
                  <div>
                    <input
                      v-model="infoDatas.is_displayed"
                      type="radio"
                      id="displayed"
                      value="1"
                      name="displayStatus"
                    />
                    <label for="displayed">진열</label>
                    <input
                      v-model="infoDatas.is_displayed"
                      type="radio"
                      id="nodisplayed"
                      value="0"
                      name="displayStatus"
                    />
                    <label for="nodisplayed">미진열</label>
                  </div>
                  <div>
                    <i class="xi-info">미판매 선택시 앱에서 Sold Out으로 표시됩니다.</i>
                  </div>
                </td>
              </tr>
            </tbody>
            <!-- 카테고리 -->
            <tbody>
              <tr>
                <th>카테고리</th>
                <td class="categoryBox">
                  <tr>
                    <th>1차 카테고리</th>
                    <td>
                      <select v-model="selectedFirst" @change="get(sellerInfo.id, selectedFirst)">
                        <option>1차 카테고리</option>
                        <option
                          :value="list.id"
                          v-for="list in firstCate"
                          :key="list.id"
                        >{{list.name}}</option>
                      </select>
                    </td>
                  </tr>
                  <tr>
                    <th>2차 카테고리</th>
                    <td>
                      <select>
                        <option>2차 카테고리</option>
                        <option
                          :value="list.id"
                          v-for="list in secondCate"
                          :key="list.id"
                        >{{list.name}}</option>
                      </select>
                    </td>
                  </tr>
                </td>
              </tr>
            </tbody>
            <!-- 상품 정보 고시 -->
            <tbody>
              <tr>
                <th>상품 정보 고시</th>
                <td class="onSaleBox">
                  <div>
                    <input
                      v-model="infoDatas.is_onsale"
                      type="radio"
                      id="detailInfo"
                      value="1"
                      name="infoState"
                    />
                    <label for="detailInfo">상품상세 참조</label>
                    <input
                      v-model="infoDatas.is_onsale"
                      type="radio"
                      id="writeInfo"
                      value="0"
                      name="infoState"
                    />
                    <label for="writeInfo">직접입력</label>
                  </div>
                </td>
              </tr>
            </tbody>
          </template>
        </v-simple-table>
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";
import { URL, SJ_URL, YE_URL } from "../../config/urlConfig";

export default {
  data() {
    return {
      infoDatas: [],
      sellerList: [],
      sellerInfo: { id: "", name: "" },
      firstCate: [],
      selectedFirst: "",
      secondCate: [],
      selectedSecond: "",
      sellersModal: false,
      searchSeller: "",
      selectedSeller: ""
    };
  },
  mounted: function() {
    // this.getListDatas();
  },
  methods: {
    selectSeller: function(id, name) {
      this.searchSeller = id;
      this.sellerInfo.id = id;
      this.sellerInfo.name = name;
      this.getFirstCategory(id);
    },
    get: function(keyId, cateId) {
      axios
        .get(
          `${YE_URL}/product/second-category?seller_key_id=${keyId}&first_category_id=${cateId}`,
          {
            headers: {
              Authorization: localStorage.access_token
            }
          }
        )
        .then(response => {
          console.log("here", response.data.second_categories);
          this.secondCate = response.data.second_categories;
        });
    },
    getFirstCategory: function(id) {
      axios
        .get(`${YE_URL}/product/first-category?seller_key_id=${id}`, {
          headers: {
            Authorization: localStorage.access_token
          }
        })
        .then(response => {
          this.firstCate = response.data.first_category;
        });
    },
    searchSellerList: function(e) {
      this.searchSeller = e;
      axios
        .get(`${YE_URL}/sellers-for-master?name=${this.searchSeller}`, {
          headers: {
            Authorization: localStorage.access_token
          }
        })
        .then(response => {
          this.sellerList = response.data.seller_list;
        })
        .catch(error => {
          error.respons.status === 500 ? (this.sellerList = "") : "";
        });
    },
    getListDatas: function() {
      axios
        .get(`${YE_URL}/product/2`, {
          headers: {
            Authorization: localStorage.access_token
          }
        })
        .then(response => {
          this.infoDatas = response.data.product_detail;
        });
    }
  }
};
</script>

<style lang="scss" scoped>
.prWrap {
  padding-top: 35px;

  .sellersModal {
    position: fixed;

    top: 40%;
    left: 40%;
    border: 1px solid red;
    background-color: white;
    width: 500px;
    height: 300px;
    .slTitleBox {
      display: flex;
      flex-direction: column;
      align-items: flex-start;
    }
    .slTitle {
      margin: 20px 0;
      font-size: 18px !important;
      color: black !important;
    }
    .titleLine {
      border: 1px solid lightgray;
      width: 80%;
      height: 1px;
    }
    .xi-info {
      font-size: 12px;
      margin-top: 20px;
      color: #1e90ff;
    }

    .inputBox {
      display: flex;
      margin: 20px 0 0 0;
      width: 100%;
      height: 30px;
      .text {
        display: inline-block;
        color: black;
        margin-right: 10px;
      }
      input {
        margin-top: 0px;
        width: 100%;
      }
    }

    .inputSelect {
      width: 100%;
      padding-left: 10px;
      padding-top: 5px;
      border: 1px solid lightgray;
    }
    .searchResult {
      height: 130px;
      border: 1px solid lightgray;
      overflow: auto;
    }
  }

  .categoryBox {
    margin-bottom: 10px;
    th,
    td {
      border: 1px solid lightgray;
      height: 100%;
    }
    select {
      width: 100%;
      height: 20px;
    }
  }

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
  .cmpWrap {
    border: 1px solid lightgray;
    border-radius: 3px;
    margin: 10px;

    .cmpTitle {
      height: 39px;
      background-color: #eee;
      color: #333;
      font-size: 18px;
      line-height: 16px;
      font-weight: 400;
      padding: 10px 20px;
    }
  }

  .sellerSelect {
    .btn {
      margin-left: 20px;
    }
  }

  .onSaleBox {
    display: flex;
    flex-direction: column;
    div:first-child {
      margin-bottom: 20px;
    }

    input {
      width: 10px;
      margin-right: 10px;
    }
    label {
      margin-right: 10px;
    }
    i {
      color: #1e90ff;
      display: block;
    }
  }

  .btn {
    color: #fff;
    background-color: #5cb85c;
    border-color: #4cae4c;

    display: inline-block;
    padding: 6px 12px;
    margin-bottom: 0;
    font-size: 14px;
    font-weight: 400;
    line-height: 1.42857143;
    text-align: center;
    white-space: nowrap;
    vertical-align: middle;
    cursor: pointer;
    -webkit-user-select: none;
    -moz-user-select: none;
    -ms-user-select: none;
    user-select: none;
    background-image: none;
    border: 1px solid transparent;
    border-radius: 4px;
  }
}
</style>