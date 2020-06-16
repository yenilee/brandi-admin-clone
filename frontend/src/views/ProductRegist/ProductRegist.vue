<template>
  <div class="prWrap">
    <div v-if="colorModal" class="wrap"></div>
    <div v-if="sellersModal" class="wrap"></div>
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
            <i class="xi-info">상품을 등록할 셀러를 선택해주세요. (검색 10건)</i>
            <div class="inputBox">
              <div class="text">셀러검색</div>
              <div>
                <div @click="sellersInputModal = !sellersInputModal" class="inputSelect">
                  {{sellerInfo.name? sellerInfo.name: "Select..."}}
                  <input
                    v-if="sellersInputModal === true"
                    type="text"
                    @input="searchSellerList($event.target.value)"
                  />
                  <div v-if="sellersInputModal === true" class="searchResult">
                    <div v-for="seller in sellerList" :key="seller.id">
                      <div
                        class="sellerlist"
                        @click="selectSeller(seller.seller_key_id, seller.seller_name)"
                      >{{searchSeller.length ? seller.seller_name : ""}}</div>
                    </div>
                  </div>
                </div>
              </div>
            </div>
            <div class="titleLine02"></div>
            <div class="sellersBtn">
              <div class="cancel" @click="sellersModal = !sellersModal">닫기</div>
              <div class="selected" @click="sellersModal = !sellersModal">셀러 선택하기</div>
            </div>
          </div>
        </div>
        <!-- 컬러필터모달 -->
        <div v-if="colorModal === 1" class="colorModal">
          <div class="slTitle">색상 선택</div>
          <div class="titleLine"></div>
          <div class="colorBox" v-for="color in colors" :key="color.id">
            <div @click="selectColor(color.id)">
              <img :src="color.image" />
              <div v-model="productDatas.color_filter_id">{{color.name}}</div>
              <div>({{color.eng_name}})</div>

              <div
                v-if="productDatas.color_filter_id === color.id && color.id != 13 || productDatas.color_filter_id === color.id &&  color.id != 16 || productDatas.color_filter_id === color.id &&  color.id != 17 || productDatas.color_filter_id === color.id &&  color.id != 18"
              >
                <i class="xi-check" style="color: white"></i>
              </div>

              <div
                v-if="productDatas.color_filter_id === color.id && productDatas.color_filter_id === color.id &&  color.id === 13 || productDatas.color_filter_id === color.id &&  color.id === 16 || productDatas.color_filter_id === color.id &&  color.id === 17 || productDatas.color_filter_id === color.id &&  color.id === 18"
              >
                <i class="xi-check" style="color: black"></i>
              </div>
            </div>
          </div>
          <div class="titleLine"></div>
          <div style="text-align:center">
            <div class="selected" @click="colorModal = 0">적용</div>
            <div class="cancel" @click="colorModal = 0; productDatas.color_filter_id = 0">취소</div>
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
                  <input
                    type="text"
                    placeholder="셀러검색을 해주세요."
                    v-model="sellerInfo.name"
                    style="cursor: not-allowed !important;"
                    disabled
                  />
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
                      v-model="productDatas.is_onsale"
                      type="radio"
                      id="onSale"
                      :value="1"
                      name="saleStatus"
                    />
                    <label for="onSale">판매</label>
                    <input
                      v-model="productDatas.is_onsale"
                      type="radio"
                      id="noSale"
                      :value="0"
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
                      v-model="productDatas.is_displayed"
                      type="radio"
                      id="displayed"
                      :value="1"
                      name="displayStatus"
                    />
                    <label for="displayed">진열</label>
                    <input
                      v-model="productDatas.is_displayed"
                      type="radio"
                      id="nodisplayed"
                      :value="0"
                      name="displayStatus"
                    />
                    <label for="nodisplayed">미진열</label>
                  </div>
                  <div>
                    <i class="xi-info">미진열 선택시 앱에서 노출되지 않습니다.</i>
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
                      <select
                        v-model="productDatas.first_category_id"
                        @change="getSecondCategory(productDatas.seller_key_id, productDatas.first_category_id)"
                      >
                        <option value="0">1차 카테고리를 선택해 주세요.</option>
                        <option
                          :value="list.id"
                          v-for="list in firstCate"
                          :key="list.id"
                        >{{list.name}}</option>
                      </select>
                    </td>
                  </tr>
                  <tr>
                    <th>2차 카테고리를 선택해 주세요.</th>
                    <td>
                      <select @change="productDatas.second_category_id = $event.target.value">
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
                      v-model="productDatas.is_detail_reference"
                      type="radio"
                      id="detailInfo"
                      :value="1"
                      name="infoState"
                    />
                    <label for="detailInfo">상품상세 참조</label>
                    <input
                      v-model="productDatas.is_detail_reference"
                      type="radio"
                      id="writeInfo"
                      :value="0"
                      name="infoState"
                    />
                    <label for="writeInfo">직접입력</label>
                    <div v-if="productDatas.is_detail_reference === 0" class="detailBox">
                      <div class="inputBox">
                        <div class="inputTitle">제조사(수입사):</div>
                        <input v-model="productDatas.manufacture.manufacturer" type="text" />
                      </div>
                      <div class="inputBox">
                        <div class="inputTitle">제조일자:</div>
                        <input v-model="productDatas.manufacture.manufacture_date" type="text" />
                      </div>
                      <div class="inputBox">
                        <div class="inputTitle">원산지:</div>
                        <select v-model="productDatas.manufacture.origin">
                          <option>기타</option>
                          <option value="중국">중국</option>
                          <option value="한국">한국</option>
                          <option value="베트남">베트남</option>
                        </select>
                      </div>
                    </div>
                  </div>
                </td>
              </tr>
            </tbody>
            <!-- 상품명 -->
            <tbody>
              <tr>
                <th>상품명</th>
                <td>
                  <div class="box">
                    <input type="text" v-model="productDatas.name" />
                    <div>
                      <i class="xi-info">미진열 선택시 앱에서 노출되지 않습니다.</i>
                    </div>
                  </div>
                </td>
              </tr>
            </tbody>
            <!-- 한줄 상품 설명 -->
            <tbody>
              <tr>
                <th>한줄 상품 설명</th>
                <td>
                  <input type="text" v-model="productDatas.simple_description" />
                </td>
              </tr>
            </tbody>
            <!-- 색상필터(썸네일 이미지) -->
            <tbody>
              <tr>
                <th>색상필터(썸네일 이미지)</th>
                <td class="onSaleBox">
                  <div style="width: 40%">
                    <input
                      v-model="colorModal"
                      :value="0"
                      type="radio"
                      id="unuse"
                      name="colorFilter"
                      checked
                    />
                    <label for="unuse">사용안함</label>
                    <input
                      @click="getColors()"
                      v-model="colorModal"
                      :value="1"
                      type="radio"
                      id="using"
                      name="colorFilter"
                    />
                    <label @click="getColors()" for="using">사용</label>
                    <input type="text" />
                  </div>
                </td>
              </tr>
            </tbody>
          </template>
        </v-simple-table>
      </div>
    </div>
    <div class="cmpWrap">
      <div class="cmpTitle">
        <i class="xi-user">옵션 정보</i>
      </div>
      <div class="cmpTable">
        <template>
          <tbody>
            <tr>
              <th>옵션설정</th>
              <td>
                <input type="radio" id="option" checked />
                <label for="option">기본옵션</label>
              </td>
            </tr>
          </tbody>
          <div class="optionTable">
            <tbody>
              <tr>
                <th>옵션정보</th>
                <td>
                  <tbody>
                    <tr>
                      <th>옵션 항목</th>
                      <th>상품 옵션명</th>
                      <th>옵션값 추가/삭제</th>
                    </tr>
                    <tr>
                      <th>색상</th>
                      <td v-for="(color, index) in invenColorsCount" :key="color.id">
                        <div class="optionModal">
                          <div class="text" @click="colorModalHandle(index)">sssdfdsfdsf</div>
                          <input v-if="invenColorsCount[index].state === true" type="text" />
                          <div v-if="invenColorsCount[index].state === true" class="optionList">
                            <p
                              @click="selectOptionColor(optionColor.name,'color')"
                              v-for="optionColor in optionColors"
                              :key="optionColor.id"
                            >{{optionColor.name}}</p>
                          </div>
                        </div>
                      </td>
                      <th>
                        <div @click="plusColorOption()">플러스</div>
                        <div @click="minusColorOption()">마이너스</div>
                      </th>
                    </tr>
                    <tr>
                      <th>사이즈</th>
                      <td v-for="(size, index) in invenSizesCount" :key="size.id">
                        <div class="optionModal">
                          <div class="text" @click="sizeModalHandle(index)">sssdfdsfdsf</div>
                          <input v-if="invenSizesCount[index].state === true" type="text" />
                          <div v-if="invenSizesCount[index].state === true" class="optionList">
                            <p
                              @click="selectOptionColor(optionSize.name,'size')"
                              v-for="optionSize in optionSizes"
                              :key="optionSize.id"
                            >{{optionSize.name}}</p>
                          </div>
                        </div>
                      </td>
                      <th>
                        <div @click="plusSizeOption()">플러스</div>
                        <div @click="minusSizeOption()">마이너스</div>
                      </th>
                    </tr>
                  </tbody>
                </td>
                <td>
                  <tr>
                    <th>재고관리여부</th>
                  </tr>
                  <tr>
                    <td>
                      <input
                        v-model="productDatas.is_displayed"
                        type="radio"
                        id="noinventory"
                        :value="1"
                        name="inventory"
                      />
                      <label for="noinventory">재고 수량 관리 안함</label>
                    </td>
                  </tr>
                  <tr>
                    <td>
                      <input
                        v-model="productDatas.is_displayed"
                        type="radio"
                        id="inventroy"
                        :value="1"
                        name="inventory"
                      />
                      <label for="inventroy">재고 수량 관리</label>
                    </td>
                  </tr>
                </td>
                <p>ㅗㅑㅗㅑ</p>
                <button @click="makingOptions()">button</button>
              </tr>
            </tbody>
          </div>
        </template>
      </div>
    </div>
    <div class="cmpWrap">
      <div class="cmpTitle">
        <i class="xi-user">판매 정보</i>
      </div>
      <div class="cmpTable"></div>
    </div>
    <div>
      <div id="app">
  <v-app id="inspire">
    <div>
      <v-container
        v-for="align in alignments"
        :key="align"
        class="grey lighten-5 mb-6"
      >
        <v-row
          :align="align"
          no-gutters
          style="height: 50px;"
        >
          <v-col
            v-for="n in 3"
            :key="n"
          >
            <v-card
              class="pa-2"
              outlined
              tile
            >
              One of three columns
            </v-card>
          </v-col>
        </v-row>
      </v-container>
  
      <v-container class="grey lighten-5">
        <v-row
          no-gutters
          style="height: 50px;"
        >
          <v-col
            v-for="align in alignments"
            :key="align"
            :align-self="align"
          >
            <v-card
              class="pa-2"
              outlined
              tile
            >
              One of three columns
            </v-card>
          </v-col>
        </v-row>
      </v-container>
    </div>
  </v-app>
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

      sellersModal: false,
      sellersInputModal: false,
      sellerList: [],
      sellerInfo: { id: "", name: "" },
      searchSeller: "",

      firstCate: [],
      secondCate: [],

      colorModal: 0,

      colors: [],

      invenColorsCount: [{ state: false }],
      invenSizesCount: [{ state: false }],

      optionColorModal: false,
      optionColors: [],
      optionSizes: [],
      allOptions: { color: [], size: [] },
      makingOptionsData: [],

      productDatas: {
        seller_key_id: "",
        is_onsale: 1,
        is_displayed: 1,
        first_category_id: "0",
        second_category_id: "",
        is_detail_reference: 1,
        manufacture: {
          manufacturer: "",
          manufacture_date: "",
          origin: "한국"
        },
        name: "",
        simple_description: "",
        color_filter_id: 0
        // details: "뛰어다닐 수 있어요",
        // options: [
        //   {
        //     size_id: 5,
        //     color_id: 4,
        //     quantity: 88
        //   },
        //   {
        //     size_id: 6,
        //     color_id: 1,
        //     quantity: 3
        //   }
        // ],
        // wholesale_price: 30000,
        // price: 68000,
        // discount_rate: 10,
        // discount_start: "2020-06-01 08:30:00",
        // discount_end: "2020-06-03 23:59:59",
        // maximum_quantity: 1000,
        // minimum_quantity: 40,
        // tags: ["태그88", "태그97", "태그94"]
      }
    };
  },
  mounted: function() {
    // this.getListDatas();
    this.getOptionColors();
  },
  methods: {
    sellersModalHandle: function() {
      this.sellersInputModal
        ? (this.sellersMdaol = false)
        : (this.sellersInputModal = false);
    },
    makingOptions: function() {
      for (let i = 0; i <= this.allOptions.color.length - 1; i++) {
        for (let j = 0; j <= this.allOptions.size.length - 1; j++) {
          this.makingOptionsData.push({
            color: this.allOptions.color[i],
            size: this.allOptions.size[j]
          });
        }
      }
    },
    selectOptionColor: function(name, option) {
      option === "color"
        ? this.allOptions.color.push(name)
        : this.allOptions.size.push(name);
    },
    colorModalHandle: function(index) {
      this.invenColorsCount[index].state = !this.invenColorsCount[index].state;
    },
    sizeModalHandle: function(index) {
      this.invenSizesCount[index].state = !this.invenSizesCount[index].state;
    },

    getOptionColors: function() {
      axios
        .get(`${YE_URL}/product-options`, {
          headers: {
            Authorization: localStorage.access_token
          }
        })
        .then(response => {
          this.optionColors = response.data.page_info.option_color;
          this.optionSizes = response.data.page_info.option_size;
        });
      // axios.get(`${URL}/test.json`).then(response => {
      //   console.log("here is test Data >>>>", response);
      //   this.optionSizes = response.data.size;
      //   this.optionColors = response.data.color;
      // });
    },
    minusSizeOption: function() {
      this.invenSizesCount.splice(this.invenSizesCount.length - 1, 1);
    },
    plusSizeOption: function() {
      this.invenSizesCount.push({ state: false });
    },
    minusColorOption: function() {
      this.invenColorsCount.splice(this.invenColorsCount.length - 1, 1);
    },
    plusColorOption: function() {
      this.invenColorsCount.push({ state: false });
    },

    selectColor: function(id) {
      this.productDatas.color_filter_id = id;
    },
    getColors: function() {
      axios
        .get(`${YE_URL}/product-color-filter`, {
          headers: {
            Authorization: localStorage.access_token
          }
        })
        .then(response => {
          this.colors = response.data.color_filters;
        });
    },

    //셀러 검색창에서 검색결과의 아이디를 클릭하면, 해당 아이디의 텍스트와 고유 id를 data에 저장합니다.
    //getFirstCategory라는 카테고리 리스트를 수신하는 함수에 셀러의 고유 id를 인자로 보내며 실행합니다.
    selectSeller: function(id, name) {
      this.sellerInfo.name = name;
      this.productDatas.seller_key_id = id;
      this.getFirstCategory(id);
      // event.stopPropagation();
    },

    //1차 카테고리를 선택하면 해당 옵션에 2차카테고리를 받아옵니다.
    getSecondCategory: function(keyId, cateId) {
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
          this.secondCate = response.data.second_categories;
        });
    },

    //셀러 검색 후, 선택된 셀러의 속성에 따라 1차카테고리 리스트가 달라지므로,
    //selectSeller함수에서 셀러 고유 id를 받아 1차 카테고리 리스트를 받아옵니다.
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
    //셀러 검색창에 입력된 텍스트들을 실시간으로 받아, 해당 텍스트가 포함된 셀러 리스트를 받아옵니다.
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
    //상품 수정페이지로 진입시, 기존의 상품 정보들을 받아옵니다.
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
  .wrap {
    position: absolute;
    top: -100px;
    left: 0;
    width: 100vw;
    height: 200vh;
    opacity: 50%;
    background-color: gray;
    z-index: 5;
  }

  .v-data-table {
    background-color: #eee;
  }

  .sellersModal {
    position: fixed;
    background-color: white;
    top: 40%;
    left: 40%;
    z-index: 10;
    width: 450px;
    height: 240px;
    border-radius: 5px;

    .cancel {
      border: 1px solid lightgray;
      cursor: pointer;
      &:hover {
        background-color: lightgray;
      }
    }
    .selected {
      color: #fff;
      background-color: #5bc0de;
      border-color: #46b8da;
      cursor: pointer;
      &:hover {
        background-color: #46b8da;
      }
    }

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
      width: 100%;
      height: 1px;
    }

    .inputBox {
      display: flex;
      margin: 20px 0 0 0;
      width: 100%;
      height: 30px;
      z-index: 30;
      .text {
        display: inline-block;
        color: black;
        margin-right: 100px;
        font-size: 13px;
      }
      input {
        margin-top: 0px;
        width: 100%;
        z-index: 40;
      }
    }

    .inputSelect {
      width: 240px;

      padding: 10px;
      border: 1px solid lightgray;
      border-radius: 5px;
      color: gray;
      background-color: white;
      z-index: 15;
    }
    .searchResult {
      height: 130px;
      border: 1px solid lightgray;
      overflow: auto;
      .sellerlist {
        &:hover {
          background-color: lightgray;
        }
      }
    }
  }
  .titleLine02 {
    margin-top: 20px;
    margin-bottom: 20px;
    border: 1px solid lightgray;
    width: 100%;
    height: 1px;
  }
  .sellersBtn {
    width: 100%;
    display: flex;
    justify-content: flex-end;
    font-size: 13px;
    font-weight: 600;
    div {
      margin: 0 15px;
      padding: 8px 10px;
      border-radius: 5px;
    }
  }

  .colorModal {
    position: fixed;
    top: 20%;
    left: 40%;
    width: 500px;
    height: 500px;
    background-color: white;
    padding: 40px;
    z-index: 10;
    .cancel {
      display: inline-block;
      border-radius: 5px;
      border: 1px solid lightgray;
      margin-top: 10px;
      padding: 8px 10px;
      cursor: pointer;
      &:hover {
        background-color: lightgray;
      }
    }
    .selected {
      display: inline-block;
      border-radius: 5px;
      color: #fff;
      background-color: #5bc0de;
      border-color: #46b8da;
      margin-top: 10px;
      padding: 8px 10px;
      margin-right: 10px;
      cursor: pointer;
      &:hover {
        background-color: #46b8da;
      }
    }

    .colorBox {
      position: relative;
      display: inline-block;
      width: 80px;
      text-align: center;
      margin: 1px;
      &:hover {
        background-color: lightgray;
      }
    }
    .slTitle {
      margin: 20px 0;
      font-size: 18px !important;
      color: gray !important;
    }
    .titleLine {
      border: 1px solid lightgray;
      width: 100%;
      height: 1px;
    }
    .xi-check {
      position: absolute;
      top: 10px;
      left: 32px;
    }
  }

  .categoryBox {
    margin-bottom: 10px;
    tr {
      width: 100%;
      height: 100%;
      border: 1px solid lightgray;
    }
    th {
      background-color: white;
      width: 100vw;
      text-align: left;
      font-size: 14px;
      font-weight: 600;
      border: unset;
    }
    select {
      background-color: white;
      border: 1px solid lightgray;
      padding-left: 3px;
      border-radius: 3px;
      width: 100%;
      height: 34px;
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

  .detailBox {
    .inputBox {
      display: flex;
      margin: 20px 0;
      .inputTitle {
        width: 100px;
      }
      input,
      select {
        width: 250px;
      }
      select {
        background-color: white;
        border: 1px solid lightgray;
        border-radius: 3px;
        padding-left: 5px;
      }
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

  .optionModal {
    width: 100%;
    height: 30px;
    input {
      width: 100%;
      position: relative;
    }
    .optionList {
      position: absolute;
      width: 100px;
      height: 100px;
      background-color: white;
      overflow: scroll;
    }
    p {
      &:hover {
        background-color: #eee;
      }
    }
  }
  input:focus {
    outline: 1px solid gray;
  }
  select:focus {
    outline: 1px solid gray;
  }
  .box {
    width: 100%;
    .xi-info {
      font-size: 12px;
      margin-top: 10px;
      color: #1e90ff;
    }
  }
  .xi-info {
    font-size: 12px;
    margin-top: 10px;
    color: #1e90ff;
  }
}
</style>