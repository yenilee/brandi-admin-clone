<template>
  <div class="plWrap">
    <div class="slTitleBox">
      <div class="slTitle">상품 관리</div>
    </div>
    <div class="slCategory">
      <i class="xi-home">
        상품 관리
        <i class="xi-angle-right-min">상품 관리</i>
        <i class="xi-angle-right-min">상품 리스트</i>
      </i>
    </div>
    <div class="filterBox">
      <div class="filterDiv">
        <div>조회 기간</div>

        <b-form-datepicker
          v-model="searchPeriod[0].value"
          id="datepicker-placeholder"
          placeholder="클릭해주세요"
          local="kr"
          style="width:180px; font-size: 13px;"
        ></b-form-datepicker>
        <span class="water">~</span>
        <b-form-datepicker
          v-model="searchPeriod[1].value"
          id="datepicker-placeholder2"
          placeholder="클릭해주세요"
          local="kr"
          style="width:180px; font-size: 13px;"
        ></b-form-datepicker>
      </div>
      <div class="filterDiv">
        <div>셀러명</div>
        <div>
          <input type="text" v-model="inputBtn[0].state" placeholder="검색어를 입력하세요." />
          <select v-model="selectBtn[0].name">
            <option value>Select</option>
            <option value="product_name">상품명</option>
            <option value="product_number">상품번호</option>
            <option value="product_code">상품코드</option>
          </select>
          <input v-model="selectBtn[0].state" type="text" placeholder="검색어를 입력하세요." />
        </div>
      </div>
      <div class="filterDiv">
        <div>셀러속성 :</div>
        <div>
          <div></div>
          <div
            v-bind:class="{ btn: !attBtn[0].state, clickedBtn: attBtn[0].state}"
            @click="attAllClick()"
          >전체</div>
          <div
            v-bind:class="{ btn: !attBtn[1].state, clickedBtn: attBtn[1].state}"
            @click="() => attClickCheck(1)"
          >쇼핑몰</div>
          <div
            v-bind:class="{ btn: !attBtn[2].state, clickedBtn: attBtn[2].state}"
            @click="() => attClickCheck(2)"
          >마켓</div>
          <div
            v-bind:class="{ btn: !attBtn[3].state, clickedBtn: attBtn[3].state}"
            @click="() => attClickCheck(3)"
          >로드샾</div>
          <div
            v-bind:class="{ btn: !attBtn[4].state, clickedBtn: attBtn[4].state}"
            @click="() => attClickCheck(4)"
          >디자이너브랜드</div>
          <div
            v-bind:class="{ btn: !attBtn[5].state, clickedBtn: attBtn[5].state}"
            @click="() => attClickCheck(5)"
          >제너럴브랜드</div>
          <div
            v-bind:class="{ btn: !attBtn[6].state, clickedBtn: attBtn[6].state}"
            @click="() => attClickCheck(6)"
          >내셔널브랜드</div>
          <div
            v-bind:class="{ btn: !attBtn[7].state, clickedBtn: attBtn[7].state}"
            @click="() => attClickCheck(7)"
          >뷰티</div>
        </div>
      </div>
      <div class="flexFilter">
        <div class="filterDiv">
          <div>판매여부 :</div>
          <div>
            <div></div>
            <div
              @click="() => clickCheck(this.twoBtn[0], 3)"
              v-bind:class="{ btn: twoBtn[0].state != 3, clickedBtn: twoBtn[0].state === 3}"
            >전체</div>
            <div
              @click="() => clickCheck(this.twoBtn[0],1)"
              v-bind:class="{ btn: twoBtn[0].state != 1, clickedBtn: twoBtn[0].state === 1}"
            >판매</div>
            <div
              @click="() => clickCheck(this.twoBtn[0],0)"
              v-bind:class="{ btn: twoBtn[0].state != 0, clickedBtn: twoBtn[0].state === 0}"
            >미판매</div>
          </div>
        </div>
        <div class="filterDiv">
          <div>할인여부 :</div>
          <div>
            <div></div>
            <div
              @click="() => clickCheck(this.twoBtn[1], 3)"
              v-bind:class="{ btn: twoBtn[1].state != 3, clickedBtn: twoBtn[1].state === 3}"
            >전체</div>
            <div
              @click="() => clickCheck(this.twoBtn[1],1)"
              v-bind:class="{ btn: twoBtn[1].state != 1, clickedBtn: twoBtn[1].state === 1}"
            >할인</div>
            <div
              @click="() => clickCheck(this.twoBtn[1],0)"
              v-bind:class="{ btn: twoBtn[1].state != 0, clickedBtn: twoBtn[1].state === 0}"
            >미할인</div>
          </div>
        </div>
        <div class="filterDiv">
          <div>진열여부 :</div>
          <div>
            <div></div>
            <div
              @click="() => clickCheck(this.twoBtn[2], 3)"
              v-bind:class="{ btn: twoBtn[2].state != 3, clickedBtn: twoBtn[2].state === 3}"
            >전체</div>
            <div
              @click="() => clickCheck(this.twoBtn[2],1)"
              v-bind:class="{ btn: twoBtn[2].state != 1, clickedBtn: twoBtn[2].state === 1}"
            >진열</div>
            <div
              @click="() => clickCheck(this.twoBtn[2],0)"
              v-bind:class="{ btn: twoBtn[2].state != 0, clickedBtn: twoBtn[2].state === 0}"
            >미진열</div>
          </div>
        </div>
      </div>
      <div class="submitBox">
        <div class="Btn searchBtn" @click="search()">검색</div>
        <div class="Btn resetBtn" @click="reset()">초기화</div>
      </div>
    </div>
    <div class="count">전체 조회건 수 : {{infoDatas.product_count}}</div>
    <div class="tableBox">
      <!-- 테이블 시작 부분입니다.. -->

      <template>
        <v-simple-table>
          <template v-slot:default>
            <div class="tableIn">
              <loading-screen ref="loadingScreen">
                <thead>
                  <tr>
                    <th class="text-left">등록일</th>
                    <th class="text-left">대표이미지</th>
                    <th class="text-left">상품명</th>
                    <th class="text-left">상품코드</th>
                    <th class="text-left">상품번호</th>
                    <th class="text-left">셀러속성</th>
                    <th class="text-left">셀러명</th>
                    <th class="text-left">판매가</th>
                    <th class="text-left">할인가</th>
                    <th class="text-left">판매여부</th>
                    <th class="text-left">진열여부</th>
                    <th class="text-left">할인여부</th>
                  </tr>
                </thead>
                <tbody>
                  <tr v-for="info in infoDatas.products" :key="info.id">
                    <td>{{info.created_at}}</td>
                    <td></td>
                    <td @click="() => idClick(info.product_keys_id)">{{info.name}}</td>
                    <td>{{info.product_code}}</td>
                    <td>{{info.product_keys_id}}</td>
                    <td>{{info.seller_attributes_name}}</td>
                    <td>{{info.user}}</td>
                    <td>{{new Intl.NumberFormat().format(info.price)}}</td>
                    <td>
                      {{new Intl.NumberFormat().format(info.discount_price)}}
                      <div class="discount">{{info.discount_rate ? `(${info.discount_rate}%)` : ""}}</div>
                    </td>
                    <td>{{info.is_onsale ? "판매" : "미판매"}}</td>
                    <td>{{info.is_displayed ? "진열" : "미진열"}}</td>
                    <td>{{info.is_discount ? "할인" : "미할인"}}</td>
                  </tr>
                </tbody>
              </loading-screen>
            </div>
          </template>
        </v-simple-table>
      </template>
    </div>
    <div class="pgCon">
      <div class="pagination">
        <template>
          <div>
            <v-app id="inspire">
              <div class="text-center">
                <v-pagination
                  v-model="page"
                  :length="infoDatas.number_of_pages"
                  @input="pagination"
                  total-visible="10"
                ></v-pagination>
              </div>
            </v-app>
          </div>
        </template>
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";
import "bootstrap/dist/css/bootstrap.css";
import "bootstrap-vue/dist/bootstrap-vue.css";
import { BootstrapVue, IconsPlugin } from "bootstrap-vue";
import LoadingScreen from "vue-loading-screen";
import { URL, YE, YE_URL } from "../../config/urlConfig";
export default {
  components: {
    LoadingScreen
  },
  data() {
    return {
      objects: [],
      number: "",
      page: 1,
      currentPage: 1,
      infoDatas: {},

      searchPeriod: [
        { name: "start_period", value: null },
        { name: "end_period", value: null }
      ],

      searchDatas: [
        { name: "user ", state: "" },
        { name: "product_code", state: 3 },
        { name: "seller_attribute_id", state: 3 }
      ],

      twoBtn: [
        { name: "is_onsale", state: 3 },
        { name: "is_discount", state: 3 },
        { name: "is_displayed", state: 3 }
      ],

      inputBtn: [{ name: "user", state: "" }],

      selectBtn: [{ name: "", state: "" }],

      attCount: 0,
      attBtn: [
        { name: "", state: 1 },
        { name: "seller_attribute_id", state: 0 },
        { name: "seller_attribute_id", state: 0 },
        { name: "seller_attribute_id", state: 0 },
        { name: "seller_attribute_id", state: 0 },
        { name: "seller_attribute_id", state: 0 },
        { name: "seller_attribute_id", state: 0 },
        { name: "seller_attribute_id", state: 0 }
      ],

      query: []
    };
  },
  created() {
    this.$nextTick(() => {
      this.refresh();
    });
  },
  mounted: function() {
    this.getListDatas();
  },
  methods: {
    refresh() {
      const p = new Promise(success => {
        setTimeout(success, 1000);
      });

      this.$refs.loadingScreen.load(p);

      p.then(() => {
        this.objects = [
          { id: 1, name: "Foo" },
          { id: 2, name: "Bar" }
        ];
      });
    },
    idClick: function(id) {
      this.$router.push({ name: "productregist", params: { id: id } });
    },
    pagination: function(page) {
      this.refresh();
      //판매여부, 진열여부, 할인여부
      this.twoBtn.filter(item => {
        item.state < 3 ? this.query.push(`${item.name}=${item.state}&`) : "";
      });
      //셀러명
      this.inputBtn.filter(item => {
        item.state.length > 0
          ? this.query.push(`${item.name}=${item.state}&`)
          : "";
      });
      //상품명, 상품코드, 상품번호
      this.selectBtn.filter(item => {
        item.state.length > 0
          ? this.query.push(`${item.name}=${item.state}&`)
          : "";
      });
      //셀러속성
      this.attBtn.filter(item => {
        item.state ? this.query.push(`${item.name}=${item.state}&`) : "";
      });

      axios
        .get(`${YE_URL}/products?${this.query.join("")}page=${page}`, {
          headers: {
            Authorization: localStorage.access_token
          }
        })
        .then(response => {
          this.infoDatas = response.data;
        });

      //쿼리스트링 초기화
      this.query = [];

      axios
        .get(`${YE_URL}/products?${this.query.join("")}page=${page}`, {
          headers: {
            Authorization: localStorage.access_token
          }
        })
        .then(response => {
          this.infoDatas = response.data;
        });

      //쿼리스트링 초기화
      this.query = [];
    },
    reset: function() {
      //셀러명 select 버튼 초기화
      this.inputBtn[0]["state"] = "";
      this.selectBtn[0]["state"] = "";
      this.attCount = 0;
      //셀러 속성 초기화
      this.attBtn[0]["state"] = 1;
      for (let i = 1; i < this.attBtn.length; i++) {
        this.attBtn[i]["state"] = 0;
      }
      // 판매여부, 할인여부, 진열여부 초기화
      for (let i = 0; i < this.twoBtn.length; i++) {
        this.twoBtn[i]["state"] = 3;
      }
    },
    search: function() {
      this.refresh();
      this.twoBtn.filter(item => {
        item.state < 3 ? this.query.push(`${item.name}=${item.state}&`) : "";
      });

      this.inputBtn.filter(item => {
        item.state.length > 0
          ? this.query.push(`${item.name}=${item.state}&`)
          : "";
      });

      this.selectBtn.filter(item => {
        item.state.length > 0
          ? this.query.push(`${item.name}=${item.state}&`)
          : "";
      });

      this.attBtn.filter(item => {
        item.state ? this.query.push(`${item.name}=${item.state}&`) : "";
      });
      // 검색 버튼을 누르면 무조건 첫번째 페이지로 이동하도록 쿼리스트링
      this.query.push("page=1&");
      axios
        .get(`${YE_URL}/products?${this.query.join("")}`, {
          headers: {
            Authorization: localStorage.access_token
          }
        })
        .then(response => {
          this.infoDatas = response.data;
          this.number = response.data.number_of_pages;
        });

      //pagination 버튼 1로 이동
      this.page = 1;
      //쿼리스트링 초기화
      this.query = [];
    },
    getListDatas: function() {
      axios
        .get(`${YE_URL}/products`, {
          headers: {
            Authorization: localStorage.access_token
          }
        })
        .then(response => {
          this.infoDatas = response.data;
        });
    },
    clickCheck: function(name, stateNumber) {
      if (name.state === stateNumber) {
        name.state = 3;
      } else {
        name.state = stateNumber;
      }
    },
    attAllClick: function() {
      if (!this.attBtn[0].state) {
        this.attBtn[0].state = 1;
        this.attBtn[1].state = 0;
        this.attBtn[2].state = 0;
        this.attBtn[3].state = 0;
        this.attBtn[4].state = 0;
        this.attBtn[5].state = 0;
        this.attBtn[6].state = 0;
        this.attBtn[7].state = 0;

        this.attCount = 0;
      } else if (this.attBtn[0].state) {
        this.attBtn[0].state = 0;
      }
    },
    attClickCheck: function(index) {
      this.attBtn[index].state = index;

      this.attBtn[index].state
        ? (this.attCount = this.attCount + 1)
        : (this.attCount = this.attCount - 1);

      if (this.attCount === 6) {
        this.attCount = 0;
        this.attBtn[0].state = 1;
        this.attBtn[1].state = 0;
        this.attBtn[2].state = 0;
        this.attBtn[3].state = 0;
        this.attBtn[4].state = 0;
        this.attBtn[5].state = 0;
        this.attBtn[6].state = 0;
        this.attBtn[7].state = 0;
      }
      if (this.attCount > 0) {
        this.attBtn[0].state = 0;
      }
    }
  }
};
</script>

<style lang="scss" scoped>
* {
  // border: 1px solid red;
}
.plWrap {
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
  .filterBox {
    margin-top: 15px;
    width: calc(100vw - 335px);
    border: 3px solid #eee;
    margin: 10px;
    padding-left: 10px;
    margin-bottom: 20px;
    background-color: #fafafa;
  }
  .count {
    margin-left: 10px;
  }
  .discount {
    color: red;
    font-size: 12px;
  }
  .filterDiv {
    display: flex;
    padding: 10px 20px;
    font-size: 14px;

    div:first-child {
      margin-right: 30px;
      width: 100px;
      align-self: center;
    }
    .btn {
      display: inline-block;
      padding: 6px 12px;
      margin-right: 10px;
      font-size: 12px;
      font-weight: 400;
      line-height: 1.42857143;
      text-align: center;
      white-space: nowrap;
      vertical-align: middle;
      cursor: pointer;
      user-select: none;
      background-image: none;
      border: 1px solid transparent;
      border-radius: 4px;
      border: 1px solid #eee;
      background-color: white;

      &:hover {
        background-color: #eee;
      }
    }
    .clickedBtn {
      display: inline-block;
      padding: 6px 12px;
      margin-right: 10px;
      font-size: 12px;
      font-weight: 400;
      line-height: 1.42857143;
      text-align: center;
      white-space: nowrap;
      vertical-align: middle;
      cursor: pointer;
      user-select: none;
      background-image: none;
      border: 1px solid transparent;
      border-radius: 4px;
      border: 1px solid #357ebd;
      color: #fff;
      background-color: #428bca;
    }
  }
  .water {
    width: 30px;
    text-align: center;
    padding-top: 5px;
    background-color: #eee;
    font-size: 18px;
  }

  input {
    border: 1px solid lightgray;
    border-radius: 3px;
    width: 180px;
    padding: 6px 12px 6px 33px;
    font-size: 12px;
    font-weight: 500;
    color: #333333;
    margin-right: 40px;
    background-color: white;
  }
  input:focus {
    outline: 1px solid #eee;
  }
  select {
    width: 180px;
    height: 100%;
    border: 1px solid lightgray;
    padding-left: 10px;
    margin-right: 5px;
    border-radius: 3px;
    vertical-align: middle;
    background-color: white;
    font-size: 12px;
  }
  .flexFilter {
    display: grid;
    grid-template-columns: 1fr 1fr;
    align-content: center;
  }
  .submitBox {
    display: flex;
    justify-content: center;

    .Btn {
      display: inline-block;
      padding: 6px 12px;
      margin-bottom: 0;
      font-size: 12px;
      font-weight: 400;
      line-height: 1.42857143;
      text-align: center;
      white-space: nowrap;
      vertical-align: middle;
      cursor: pointer;
      border: 1px solid transparent;
      border-radius: 4px;
      margin: 40px 0;
    }
    .searchBtn {
      color: #fff;
      background-color: #428bca;
      border-color: #357ebd;

      margin-right: 15px;
      &:hover {
        background-color: #357ebd;
      }
    }

    .resetBtn {
      color: #333;
      background-color: white;
      border-color: gray;
      &:hover {
        background-color: #eee;
      }
    }
  }

  .tableBox {
    tr {
      th {
        width: 10%;
      }
    }

    .tableIn {
      width: calc(100vw - 335px);
      overflow: auto;
      white-space: nowrap;
      margin: 10px;
      border: 1px solid lightgray;
      button {
        padding: 5px;
        color: #fff;
        border-radius: 3px;
        margin-left: 5px;
      }
    }
    tr {
      th {
        width: 10%;
      }
    }
    th,
    td {
      text-align: left;
      height: 39px !important;
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
    th {
      width: 100%;

      .page_item {
        font-size: 20px;

        .page_item {
          font-size: 20px;
        }
      }
    }
  }
  .pagination {
    font-size: 20px;
    margin-left: 33%;
  }
  .component-fade-enter-active,
  .component-fade-leave-active {
    transition: opacity 0.3s ease;
  }
  .component-fade-enter,
  .component-fade-leave-active {
    opacity: 0;
  }
  .main {
    position: relative;
    min-height: 50px;
  }
  .loading {
    position: absolute;
    z-index: 1001;
    top: 0;
    left: 0;
    background-color: rgba(230, 233, 236, 0.8);
    cursor: wait;
    height: 100%;
    width: 100%;
    display: flex;
    justify-content: center;
    align-items: center;
  }
  .loading .message {
    background-color: #f4f4f4;
    border-radius: 4px;
    box-shadow: 0 1px 8px rgba(0, 0, 0, 0.15);
    border: solid 1px #bbb;
    padding: 10px 20px;
  }
}
</style>
