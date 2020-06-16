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
                    @click="$event.stopPropagation()"
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
            <div @click="selectColor(color.id, color.image, color.name)">
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

            <!-- 판매여부 -->

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

            <!--진열 여부 -->

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

            <!-- 카테고리 -->

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

            <!-- 상품 정보 고시 -->

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

            <!-- 상품명 -->

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

            <!-- 한줄 상품 설명 -->

            <tr>
              <th>한줄 상품 설명</th>
              <td>
                <input type="text" v-model="productDatas.simple_description" />
              </td>
            </tr>

            <!-- 상세 상품 설명 -->
            <tr>
              <th>상세 상품 설명</th>
              <td class="editorBox">
                <vue-editor v-model="productDatas.details"></vue-editor>
              </td>
            </tr>
            <!-- 색상필터(썸네일 이미지) -->

            <tr>
              <th>색상필터(썸네일 이미지)</th>
              <td class="onSaleBox">
                <div style="width: 100%">
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
                  <input class="colorInput" type="text" disabled :value="selectedColor[2]" />
                  <div>
                    <i
                      class="xi-info"
                    >베스트 탭, 카테고리 페이지 및 검색페이지의 필터에 적용되며, 선택하지 않으실 경우 색상필터를 사용한 검색결과에 노출되지 않습니다.</i>
                  </div>
                  <div>
                    <i class="xi-info">썸네일 이미지의 1개 색상만 선택 가능하며, 뷰티 및 다이어트 카테고리의 상품의 경우 선택하실 수 없습니다.</i>
                  </div>
                </div>
              </td>
            </tr>
          </template>
        </v-simple-table>
      </div>
    </div>
    <div class="cmpWrap">
      <div class="cmpTitle">
        <i class="xi-user">옵션 정보</i>
      </div>
      <div class="cmpTable">
        <v-simple-table>
          <template v-slot:default>
            <tr>
              <th>옵션설정</th>
              <td>
                <input style="width: 10px; margin-right: 10px" type="radio" id="option" checked />
                <label for="option">기본옵션</label>
              </td>
            </tr>

            <!-- 옵션정보 테이블 시작 -->

            <tr class="optionTable" style="background-color: white !important">
              <th>옵션정보</th>
              <td class="tdBox">
                <v-simple-table>
                  <template v-slot:default>
                    <thead>
                      <tr class="headColor">
                        <th class="headTh" style="width: 20%;">옵션 항목</th>
                        <th class="headTh">상품 옵션명</th>
                        <th class="headTh" style="width: 20%;">옵션값 추가/삭제</th>
                      </tr>
                    </thead>

                    <tr class="thColor" style="background-color: white !important">
                      <th class="thLine">색상</th>
                      <td v-for="(color, index) in invenColorsCount" :key="color.id">
                        <div class="optionModal">
                          <div class="textDiv" @click="colorModalHandle(index)">
                            <div
                              class="textBox"
                            >{{allOptions.color[index]?allOptions.color[index] : "색상 옵션을 선택해 주세요."}}</div>
                            <input
                              @click=" $event.stopPropagation()"
                              v-if="invenColorsCount[index].state === true"
                              type="text"
                            />
                            <div v-if="invenColorsCount[index].state === true" class="optionList">
                              <p
                                class="listText"
                                @click="selectOptionColor(optionColor.name,'color',index)"
                                v-for="optionColor in optionColors"
                                :key="optionColor.id"
                              >{{optionColor.name}}</p>
                            </div>
                          </div>
                        </div>
                      </td>
                      <th class="thLine">
                        <div
                          v-if="invenColorsCount.length > 1"
                          class="icon"
                          @click="minusColorOption()"
                        >
                          <i class="xi-minus"></i>
                        </div>
                        <div class="icon" @click="plusColorOption()">
                          <i class="xi-plus"></i>
                        </div>
                      </th>
                    </tr>
                    <tr class="thColor" style="background-color: white !important">
                      <th>사이즈</th>
                      <td
                        style="border-bottom: 1px solid lightgray; border-top-width: 0;"
                        v-for="(size, index) in invenSizesCount"
                        :key="size.id"
                      >
                        <div class="optionModal">
                          <div class="textDiv" @click="sizeModalHandle(index)">
                            <div
                              class="textBox"
                            >{{allOptions.size[index]?allOptions.size[index] : "사이즈 옵션을 선택해 주세요."}}</div>
                            <input v-if="invenSizesCount[index].state === true" type="text" />
                            <div v-if="invenSizesCount[index].state === true" class="optionList">
                              <p
                                class="listText"
                                @click="selectOptionColor(optionSize.name,'size',index)"
                                v-for="optionSize in optionSizes"
                                :key="optionSize.id"
                              >{{optionSize.name}}</p>
                            </div>
                          </div>
                        </div>
                      </td>
                      <th>
                        <div
                          class="icon"
                          v-if="invenSizesCount.length > 1"
                          @click="minusSizeOption()"
                        >
                          <i class="xi-minus"></i>
                        </div>
                        <div class="icon" @click="plusSizeOption()">
                          <i class="xi-plus"></i>
                        </div>
                      </th>
                    </tr>
                  </template>
                </v-simple-table>
              </td>
              <!-- <td>
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
              </td>-->
              <div class="optionSelected" @click="makingOptions()">
                <i class="xi-check">적용</i>
              </div>
              <v-simple-table class="reusltTableWrap">
                <template v-slot:default>
                  <tr class="resultTable">
                    <th class="resultTableTh">
                      <v-simple-table>
                        <template v-slot:default>
                          <tr>
                            <th class="headTh" style="background-color:#eee;" colspan="2">상품 정보 옵션</th>
                            <th class="headTh" style="background-color:#eee;" rowspan="2">일반 재고</th>
                            <th class="headTh" style="background-color:#eee;" rowspan="2"></th>
                          </tr>
                          <tr>
                            <th class="headTh">색상</th>
                            <th class="headTh">사이즈</th>
                          </tr>
                          <tr
                            style="background-color:#eee"
                            v-for="(option, index) in makingOptionsData"
                            :key="option.id"
                          >
                            <th>{{option.color}}</th>
                            <th>{{option.size}}</th>
                            <th class="invenControl">
                              <input :name="`inven${index}`" id="noInven" type="radio" />
                              <label :for="`inven${index}`">재고관리 안함</label>

                              <input :name=" `inven${index}`" id="inven" type="radio" />

                              <label :for="`inven${index}`">
                                <input v-model="makingOptionsData[index].quantity" type="text" />개
                              </label>
                            </th>
                            <th>dsfl</th>
                          </tr>
                        </template>
                      </v-simple-table>
                    </th>
                  </tr>
                  <div style="background-color:white;">
                    <i class="xi-info">도매처옵션명 조합은 최대 100자까지 표시됩니다.</i>
                  </div>
                </template>
              </v-simple-table>
            </tr>
          </template>
        </v-simple-table>
      </div>
    </div>
    <div class="cmpWrap">
      <div class="cmpTitle">
        <i class="xi-user">판매 정보</i>
      </div>
      <div class="cmpTable">
        <div @click="test01">전송버튼</div>
      </div>
    </div>

    <!-- 판매정보 시작 -->

    <!-- 등록 취소 버튼 -->
    <v-col class="text-center">
      <div class="my-2">
        <v-btn class="enroll-button">등록</v-btn>
      </div>
      <div class="my-2">
        <v-btn class="cancle-button">취소</v-btn>
      </div>
    </v-col>
  </div>
</template>

<script>
import axios from "axios";
import { VueEditor } from "vue2-editor";
import { URL, SJ_URL, YE_URL } from "../../config/urlConfig";

export default {
  components: {
    VueEditor
  },
  data() {
    return {
      infoDatas: [],
      content: "",

      sellersModal: false,
      sellersInputModal: false,
      sellerList: [],
      sellerInfo: { id: "", name: "" },
      searchSeller: "",

      firstCate: [],
      secondCate: [],

      colorModal: 0,
      colors: [],
      selectedColor: [],

      invenColorsCount: [{ state: false }],
      invenSizesCount: [{ state: false }],

      optionColorModal: false,
      optionColors: [],
      optionSizes: [],
      allOptions: { color: [], size: [] },
      makingOptionsData: [],
      invenState: null,
      test: 0,

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
        color_filter_id: 0,
        details: "",
        options: this.makingOptionsData
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
    test01: function() {
      axios
        .post(
          `${YE_URL}/product`,
          {
            seller_key_id: this.productDatas.seller_key_id,
            is_onsale: this.productDatas.is_onsale,
            is_displayed: this.productDatas.is_displayed,
            color_filter_id: this.productDatas.color_filter_id,
            first_category_id: this.productDatas.first_category_id,
            second_category_id: Number(this.productDatas.second_category_id),
            is_detail_reference: this.productDatas.is_detail_reference,
            manufacture: {
              manufacturer: this.productDatas.manufacture.manufacturer,
              manufacture_date: this.productDatas.manufacture.manufacture_date,
              origin: this.productDatas.manufacture.origin
            },
            name: this.productDatas.name,
            simple_description: this.productDatas.simple_description,
            details: "겨울",
            color_filter_id: this.productDatas.color_filter_id,
            options: [
              {
                size: "XL",
                color: "White",
                quantity: 30
              },
              {
                size: "L",
                color: "White",
                quantity: 30
              }
            ],
            wholesale_price: 5000,
            price: 20000,
            discount_rate: 50,
            discount_start: "2020-06-16 00:00:00",
            discount_end: "2020-06-16 23:59:59",
            maximum_quantity: 20,
            minimum_quantity: 2,
            tags: ["코트", "따듯한 코트"]
          },
          {
            headers: {
              Authorization: localStorage.access_token
            }
          }
        )
        .then(response => {
          console.log(response);
        })
        .catch(error => {
          console.log(error.response.data.message);
        });
    },
    sellersModalHandle: function() {
      this.sellersInputModal
        ? (this.sellersMdaol = false)
        : (this.sellersInputModal = false);
    },
    makingOptions: function() {
      this.makingOptionsData = [];
      for (let i = 0; i <= this.allOptions.color.length - 1; i++) {
        for (let j = 0; j <= this.allOptions.size.length - 1; j++) {
          this.makingOptionsData.push({
            color: this.allOptions.color[i],
            size: this.allOptions.size[j],
            quantity: null
          });
        }
      }
    },
    selectOptionColor: function(name, option, index) {
      if (option === "color" && this.allOptions.color.length === 0) {
        this.allOptions.color.push(name);
      } else if (option === "color" && this.allOptions.color[index]) {
        const colorCheck = this.allOptions.color.filter(colorInfo => {
          return colorInfo === name;
        });
        colorCheck.length != 0
          ? alert(`이미 선택된 옵션입니다.`)
          : (this.allOptions.color[index] = name);
      } else if (option === "color" && this.allOptions.color.length != 0) {
        const colorCheck = this.allOptions.color.filter(colorInfo => {
          return colorInfo === name;
        });
        colorCheck.length != 0
          ? alert(`이미 선택된 옵션입니다.`)
          : this.allOptions.color.push(name);
      }

      if (option === "size" && this.allOptions.size.length === 0) {
        this.allOptions.size.push(name);
      } else if (option === "size" && this.allOptions.size[index]) {
        const sizeCheck = this.allOptions.size.filter(sizeInfo => {
          return sizeInfo === name;
        });
        sizeCheck.length != 0
          ? alert(`이미 선택된 옵션입니다.`)
          : (this.allOptions.size[index] = name);
      } else if (option === "size" && this.allOptions.size.length != 0) {
        const sizeCheck = this.allOptions.size.filter(sizeInfo => {
          return sizeInfo === name;
        });
        sizeCheck.length != 0
          ? alert(`이미 선택된 옵션입니다.`)
          : this.allOptions.size.push(name);
      }
      // option === "color"
      //   ? this.allOptions.color.push(name)
      //   : this.allOptions.size.push(name);
    },
    colorModalHandle: function(index) {
      this.invenColorsCount[index].state = !this.invenColorsCount[index].state;
    },
    sizeModalHandle: function(index) {
      this.invenSizesCount[index].state = !this.invenSizesCount[index].state;
    },

    getOptionColors: function() {
      // axios
      //   .get(`${YE_URL}/product-options`, {
      //     headers: {
      //       Authorization: localStorage.access_token
      //     }
      //   })
      //   .then(response => {
      //     this.optionColors = response.data.option_color;
      //     this.optionSizes = response.data.option_size;
      //   });
      axios.get(`${URL}/test.json`).then(response => {
        console.log("here is test Data >>>>", response);
        this.optionSizes = response.data.size;
        this.optionColors = response.data.color;
      });
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

    selectColor: function(id, img, name) {
      this.productDatas.color_filter_id = id;
      this.selectedColor.push(id, img, name);
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

  .editorBox {
    display: block !important;
  }
  .quillWrapper {
    background-color: white;
  }
  td {
    padding: 20px !important;
  }
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
    background-color: #fafafa;
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
    .v-data-table table {
      width: 100%;
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
  .optionSelected {
    display: inline-block;

    color: #fff;
    background-color: #5bc0de;
    border-color: #46b8da;
    font-weight: 900;
    font-size: 15px;
    cursor: pointer;
    &:hover {
      background-color: #46b8da;
    }
    border-radius: 3px;
    padding: 8px 12px;
    margin-left: 20px;
    margin-bottom: 10px;
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
    .colorInput {
      width: 30%;
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

  .optionTable {
    border: 1px solid lightgray;
    .tdBox {
      .v-data-table {
        border: 1px solid lightgray;
        border-radius: 3px;
      }
      .headTh:nth-child(2) {
        border: 1px solid lightgray !important;
        border-top-width: 0 !important;
        border-bottom-width: 0 !important;
      }
      .thColor {
        background-color: white;
        td {
          border: 1px solid lightgray !important;
          border-bottom-width: 0 !important;
        }
        .icon {
          display: inline-block;
          width: 25px;
          padding: 5px;
          text-align: center;
          margin-right: 20px;
          border: 1px solid lightgray;
          border-radius: 3px;
        }
        i {
          color: black;
          font-weight: 900;
          font-size: 13px;
          cursor: pointer;
          &:hover {
            color: gray;
          }
        }
      }
      .thLine {
        border: 1px solid lightgray !important;
        border-left-width: 0 !important;
        border-right-width: 0 !important;
      }
      th {
        border: 0 !important;
      }
      td {
        border: 0 !important;
      }
    }
    .optionModal {
      .textBox {
        text-align: center;
        width: 80%;
        margin: 0 !important;
        cursor: pointer;
      }
      input {
        width: 100%;
      }
      .optionList {
        margin: 0;
        display: inline-block;
        width: 100%;
        height: 100px;
        background-color: white;
        overflow: scroll;
        text-align: center;
        font-size: 14px;
        font-weight: 400;
        .listText {
          margin-top: 10px;
          cursor: pointer;
          &:hover {
            background-color: #eee;
          }
        }
      }
      .textBox {
        text-align: center;
        width: unset;
        font-size: 14px;
        margin-bottom: 10px !important;
      }
      .textDiv {
        border: 1px solid lightgray;
        padding: 10px;
        text-align: left;
        font-size: 13px;
      }
    }

    .reusltTableWrap {
      .v-data-table {
        margin: 20px 0;
        border: 1px solid lightgray !important;
      }
      .xi-info {
        margin-left: 20px;

        background-color: white;
      }
    }
    .resultTable {
      .resutlTableTh {
        border: 0 !important;
      }
      th {
        background-color: white;
      }
      .headTh {
        background-color: #eee;
      }
      .invenControl {
        display: flex;
        width: 100%;
        align-items: center;
        input {
          width: unset;
          margin-right: 5px;
        }
        label {
          margin: 0 30px 0 10px;
        }
      }
    }

    .headTh {
      font-size: 14px;
      font-weight: 600;
      color: black;
    }
    div:first-child {
      width: 100%;
    }
    .headColor {
      background-color: #eee;
    }
  }
  * {
    // border: 1px solid red;
  }
  .ProductRegist {
    tr th {
      // border : 1px solid #ddd;
      text-align: center;
    }
    td {
      padding: 10px;
      border: 0.3px solid #ddd;
      background-color: white;
    }
    .td-border {
      // border:  0.3px solid #ddd;
    }
    .page_content {
      width: 100%;
      height: 100%;
      background-color: white;
      margin-top: 20px;
      .page_title {
        background-color: #eee;
        padding: 10px 10px 2px 10px;
        font-size: 20px;
        small {
          font-size: 14px;
          letter-spacing: 0px;
          font-weight: 300;
          color: #888;
        }
      }
      .page_bar {
        border: 0;
        padding: 0px;
        background-color: #eee;
        margin-bottom: 25px;
        padding-left: 10px;
        padding-right: 20px;
      }
      .page_ul {
        display: flex;
        justify-content: flex-start;
        padding: 8px;
        margin: 0;
        list-style: none;
      }
      .portlet {
        .portlet-title {
          background-color: #eee;
          border-radius: 4px 4px 0 0;
          padding: 10px 10px 2px 10px;
          height: 50px;
        }
        .caption {
          color: #333;
          display: flex;
          justify-content: flex-start;
          font-size: 16px;
          line-height: 16px;
          font-weight: 400;
          margin: 0;
          padding: 0;
          margin-top: 1px;
        }
      }
      .modal-color {
        background-color: white;
        color: red;
      }
      .modal-form {
        display: flex;
        justify-content: center;
        background-color: white;
      }

      label {
        display: flex;
        margin: 10px;
      }
      .seller-search {
        display: flex;

        .seller-search-input {
          background-color: white;
          width: 150px;
          margin: auto;
        }
        .seller-search2 {
          cursor: not-allowed;
          background-color: #eeeeee;
          width: 250px;
          border: none;
        }
      }

      .row {
        margin-right: -15px;
        margin-left: -15px;

        .table-in-portlet {
          width: 100%;
        }
        .align-middle {
          background-color: #f9f9f9;
          .font-color-red {
            color: red !important;
          }
          input[type="button"] {
            -webkit-appearance: button;
            cursor: pointer;
          }
        }
        .radio-list {
          display: flex;
          align-items: center;
        }
        .font-color-blue {
          font-size: 13px;
          color: #1e90ff !important;
          margin-top: 5px;
        }
        .font-color-red {
          color: red !important;
        }
        .table-category {
          zoom: 1;
          position: static;
          width: 500px;
          background-color: #f9f9f9;
        }
        .radio {
          display: flex;
        }
        .input-directly {
          height: 300px;
        }
        .manufacture-day {
          display: flex;
          justify-content: flex-start;
          align-items: center;
        }

        .company-name {
          margin-top: 10px;
          background-color: white;
          border: 1px solid #888;
          width: 400px;
          background-color: white;
          border: 1px solid #888;
        }
        .origin {
          width: 400px;
        }
        .form-selectd {
          border: 1px solid #888;
          background-color: white;
          width: 300px;
        }
        .form-control {
          border: 1px solid #888;
        }
        .color-filter {
          // border: 1px solid #ddd;
          width: 200px;
        }
        .one-line {
          width: 100%;
          background-color: white;
          border: 1px solid #888;
        }
        #preview {
          display: flex;
          justify-content: center;
          align-items: center;
        }
        #preview img {
          max-width: 100%;
          max-height: 500px;
        }
        .picker-box {
          margin-right: 30px;
        }
      }
      .li-tag {
        margin-top: 15px;
      }
      .age-filter {
        background-color: white;
        width: 200px;
        height: 12px;
        border-radius: 15px;
      }
      .ckeditor {
        display: block;
        // border: 1px solid #ddd;
        border-radius: 4px;
        padding: 0 3px;
        background: #eee;
      }
      .vertical-align-middle {
        height: unset;
        background-color: #eee !important;
      }
      .bd-top {
        font-size: 14px;
        font-weight: 600;
        background-color: #eee !important;
      }
      .style-filter-label {
        display: flex;
        justify-content: flex-start;
      }
      .default-info-left {
        background-color: #eee;
        text-align: center;
      }
      .td-wholesale {
        display: flex;
      }
      .tr-wholesale {
        border: 1px solid rgb(221, 221, 221);
      }
      .input-group {
        width: 240px !important;
        background-color: white;
        border-radius: 10px;
        margin-left: 10px;
      }
      .wholesale {
        position: relative;
        z-index: 2;
        float: left;
        width: 100%;
        margin-left: 10px;
      }
      .input-group-addon {
        margin-left: 10px;
        border-color: #e5e5e5;
        min-width: 39px;
        margin-top: 10px;
      }
      .seller-info-input {
        border: 1px solid #eee;
      }
      .td-background {
        background-color: white;
      }
      .discount-label {
        width: 120px;
      }
      .discount-div {
        background-color: #f9f9f9;
      }
      .discount-persent {
        background-color: #e5e5e5;
      }
      .discount-button {
        color: #fff;
        background-color: #3071a9;
        border-color: #285e8e;
        border-radius: 10px;
        width: 124px;
        height: 34px;
        margin: 15px;
      }
      .discount-input {
        width: 100px;
        margin-left: 10px;
        border: 1px solid #ddd;
      }
      .discount-rate {
        display: flex;
      }
      .minimum-amount {
        cursor: not-allowed;
        background-color: #eeeeee;
        width: 100px;
        height: 34px;
      }
      .stock-div {
        display: flex;
      }
      .stock-amount {
        margin-left: 20px;
      }
      .text-center {
        display: flex;
        justify-content: center;
      }

      .inspire {
        height: 50px;
      }
      .modal-input {
        border: 1px solid red;
      }
      .enroll-button {
        background-color: #5cb85c !important;
        color: white;
      }
      .cancle-button {
        margin-left: 5px;
        background-color: #d9534f !important;
        color: white;
      }
      .apply-button {
        background-color: #5bc0de !important;
        color: white;
        margin-bottom: 10px;
      }
      .product-option-info {
        text-align: center;
      }
      .style-filter-span {
        margin-left: 20px;
      }
    }
  }
}
</style>