<template >
  <div>
    <!-- 기본 정보 시작 영역 -->
    <div class="cmpWrap">
      <div class="cmpTitle">
        <i class="xi-user">기본 정보</i>
      </div>
      <div class="cmpTable">
        <v-simple-table>
          <template>
            <!-- 테이블 시작 영역 -->
            <tbody>
              <!-- 이미지박스 컨테이너 컴포넌트 생성 후 재사용 중, slot 이용 해당 내용 전달 -->
              <ImageBox>
                <template #thName>셀러프로필</template>
                <template #infoText01>
                  <i class="xi-info">셀러 프로필 확장자는 jpg, jpeg, png 만 가능하며, 허용 가능한 최대 파일사이즈 크기는 5MB 입니다.</i>
                </template>
              </ImageBox>
            </tbody>
            <!-- 셀러 상태 테이블 -->
            <tbody>
              <tr>
                <th>셀러 상태</th>
                <td>{{infoDatas.data.name}}</td>
              </tr>
            </tbody>
            <!-- 셀러 속성 테이블 -->
            <!-- <tbody>
              <tr>
                <th>셀러속성</th>
                <td>
                  <div class="option">
                    <input type="radio" id="option1" name="option" value="option1" />
                    <label for="option1">쇼핑몰</label>
                    <input type="radio" id="option2" name="option" value="option2" />
                    <label for="option2">마켓</label>
                    <input type="radio" id="option3" name="option" value="option3" />
                    <label for="option3">로드샵</label>
                  </div>
                </td>
              </tr>
            </tbody>-->
            <!-- 셀러 한글명 -->
            <tbody>
              <tr>
                <th>셀러 한글명</th>
                <td>{{infoDatas.data.kor_name}}</td>
              </tr>
            </tbody>
            <!-- 셀러 영문명 -->
            <tbody>
              <tr>
                <th>셀러 영문명</th>
                <td>{{infoDatas.data.eng_name}}</td>
              </tr>
            </tbody>
            <!-- 셀러 계정 -->
            <tbody>
              <tr>
                <th>셀러 계정</th>
                <td>{{infoDatas.data.user_id}}</td>
              </tr>
            </tbody>
          </template>
        </v-simple-table>
      </div>
    </div>
    <!-- 상세 정보 시작 -->
    <div class="cmpWrap">
      <div class="cmpTitle">
        <i class="xi-user">상세 정보</i>
      </div>
      <div class="cmpTable">
        <v-simple-table>
          <template>
            <!-- 테이블 시작 영역 -->
            <tbody>
              <!-- 셀러페이지 배경이미지 -->
              <ImageBox>
                <template #thName>셀러페이지 배경 이미지</template>
                <template #infoText01>
                  <i class="xi-info">셀러 프로필 확장자는 jpg, jpeg, png 만 가능하며, 허용 가능한 최대 파일사이즈 크기는 5MB 입니다.</i>
                </template>
                <template #infoText02>
                  <i class="xi-info">배경이미지는 1200 * 850 사이즈 이상으로 등록해주세요.</i>
                </template>
                <template #infoText03>
                  <i class="xi-info">확장자는 jpg, jpeg, png 만 가능하며, 허용 가능한 최대 파일사이즈 크기는 5MB 입니다.</i>
                </template>
              </ImageBox>
            </tbody>
            <!-- 셀러 한줄 소개 -->
            <tbody>
              <InputBox v-model="simple_introduction" placeholder="셀러 한줄 소개">
                <template #thName>셀러 한줄 소개</template>
              </InputBox>
            </tbody>
            <!-- 셀러 상세 소개 -->
            <tbody>
              <TextAreaBox v-model="detail_introduction" placeholder="셀러 상세 소개">
                <template #thName>셀러 상세 소개</template>
                <template #infoText01>
                  <i class="xi-info">셀러 상세 소개 글은 최소10자 이상 입니다.</i>
                </template>
              </TextAreaBox>
            </tbody>
            <!-- 셀러 사이트 URL -->
            <tbody>
              <InputBox v-model="site_url" placeholder="셀러 사이트 URL">
                <template #thName>셀러 사이트 URL</template>
              </InputBox>
            </tbody>
            <!-- 담당자 정보 -->
            <tbody>
              <tr>
                <th>담당자정보</th>
                <td></td>
                <!-- <td class="threeInput">
                  <input
                    type="text"
                    v-model="supervisors[0].name"
                    @input="supervisors[0].name = $event.target.value"
                    placeholder="담당자명"
                  />
                  <input
                    type="text"
                    v-model="supervisors[0].phone_number"
                    @input="supervisors[0].phone_number = $event.target.value"
                    placeholder="담당자 번호"
                  />
                  <input
                    type="text"
                    v-model="supervisors[0].email"
                    @input="supervisors[0].email = $event.target.value"
                    placeholder="담당자 이메일"
                  />
                </td>
                <td class="threeInput">
                  <input
                    type="text"
                    v-model="supervisors[1].name"
                    @input="supervisors[1].name = $event.target.value"
                    placeholder="담당자명"
                  />
                  <input
                    type="text"
                    v-model="supervisors[1].phone_number"
                    @input="supervisors[1].phone_number = $event.target.value"
                    placeholder="담당자 번호"
                  />
                  <input
                    type="text"
                    v-model="supervisors[1].email"
                    @input="supervisors[1].email = $event.target.value"
                    placeholder="담당자 이메일"
                  />
                </td>
                <td class="threeInput">
                  <input
                    type="text"
                    v-model="supervisors[2].name"
                    @input="supervisors[2].name = $event.target.value"
                    placeholder="담당자명"
                  />
                  <input
                    type="text"
                    v-model="supervisors[2].phone_number"
                    @input="supervisors[2].phone_number = $event.target.value"
                    placeholder="담당자 번호"
                  />
                  <input
                    type="text"
                    v-model="supervisors[2].email"
                    @input="supervisors[2].email = $event.target.value"
                    placeholder="담당자 이메일"
                  />
                </td>-->
              </tr>
            </tbody>
            <!-- 고객센터 -->
            <tbody>
              <InputBox v-model="service_number" placeholder="고객센터 전화번호">
                <template #thName>고객센터</template>
              </InputBox>
            </tbody>
            <!-- 택배 -->
            <tbody>
              <th>택배주소</th>
              <td></td>
            </tbody>
            <!-- 고객센터 운영시간(주중) -->
            <tbody>
              <th>고객센터 운영시간(주중)</th>
              <td></td>
            </tbody>
            <!-- 정산정보 입력 -->
            <tbody>
              <tr>
                <th>정산정보 입력</th>
                <td class="threeInput">
                  <input type="text" v-model="bank" placeholder="정산은행" />
                  <input type="text" v-model="account_owner" placeholder="계좌주" />
                  <input type="text" v-model="bank_account" placeholder="계좌번호" />
                </td>
              </tr>
            </tbody>

            <!-- 셀러상태 변경기록 -->
            <tbody>
              <th>셀러상태 변경기록</th>
              <td
                class="historyBox"
                v-for="history in infoDatas.data.seller_histories"
                :key="history.id"
              >
                <tbody>
                  <tr>
                    <th>셀러상태 변경 적용일시</th>
                  </tr>
                  <tr>
                    <td>{{history.start_date}}</td>
                  </tr>
                </tbody>
                <tbody>
                  <tr>
                    <th>셀러상태</th>
                  </tr>
                  <tr>
                    <td>{{history.name}}</td>
                  </tr>
                </tbody>
                <tbody>
                  <tr>
                    <th>변경 실행자</th>
                  </tr>
                  <tr>
                    <td>{{history.editor}}</td>
                  </tr>
                </tbody>
              </td>
            </tbody>
          </template>
        </v-simple-table>
      </div>
    </div>
    <!-- 배달 정보 시작 영역 -->
    <div class="cmpWrap">
      <div class="cmpTitle">
        <i class="xi-user">배송정보 및 교환/환불 정보</i>
      </div>
      <div class="cmpTable">
        <v-simple-table>
          <!-- 테이블 시작 영역 -->
          <tbody class="test">
            <TextAreaBox
              v-model="shipping_information"
              placeholder="ex) 도서산간 지역은 배송비가 추가비용이 발생할 수 있습니다. 결제 완료 후 1~3일 후 출고됩니다."
            >
              <template #thName>배송 정보</template>
              <template #infoText01>
                <i class="xi-info">문장이 끝나면 엔터로 줄바꿈을 해주세요.</i>
              </template>
            </TextAreaBox>
          </tbody>
          <tbody>
            <TextAreaBox
              v-model="refund_information"
              placeholder="ex) 브랜디는 소비자보호법 및 전자상거래법을 기반한 환불보장제를 운영 중에 있습니다. 정당하지 않은 사유로 인한 환불 거부 등은 제재 사유가 될 수 있는 점 참고 부탁드립니다."
            >
              <template #thName>교환/환불 정보</template>
              <template #infoText01>
                <i class="xi-info">문장이 끝나면 엔터로 줄바꿈을 해주세요.</i>
              </template>
            </TextAreaBox>
          </tbody>
        </v-simple-table>
      </div>
    </div>
    <!-- 관리브랜드 정보 -->
    <div class="cmpWrap">
      <div class="cmpTitle">
        <i class="xi-user">관리브랜드 정보</i>
      </div>
      <div class="cmpTable">
        <v-simple-table>
          <!-- 테이블 시작 영역 -->
          <tbody>
            <tr>
              <th>관리 브랜드</th>
              <td></td>
            </tr>
          </tbody>
        </v-simple-table>
      </div>
    </div>
    <!-- 셀러 모델 사이즈 정보 -->
    <div class="cmpWrap">
      <div class="cmpTitle">
        <i class="xi-user">셀러 모델 사이즈 정보</i>
      </div>
      <div class="cmpTable">
        <v-simple-table>
          <!-- 테이블 시작 영역 -->
          <tbody>
            <InputBox v-model="model_height" placeholder="키">
              <template #thName>키</template>
              <template #infoText01>
                <i class="xi-info">ex) 160cm => 160</i>
              </template>
            </InputBox>
          </tbody>
          <tbody>
            <InputBox v-model="model_size_top" placeholder="상의 사이즈">
              <template #thName>상의 사이즈</template>
              <template #infoText01>
                <i class="xi-info">ex) 55사이즈 => 55</i>
              </template>
            </InputBox>
          </tbody>
          <tbody>
            <InputBox v-model="model_size_bottom" placeholder="하의 사이즈">
              <template #thName>하의 사이즈</template>
              <template #infoText01>
                <i class="xi-info">ex) 27사이즈 => 27</i>
              </template>
            </InputBox>
          </tbody>
          <tbody>
            <InputBox v-model="model_size_foot" placeholder="발 사이즈">
              <template #thName>발 사이즈</template>
              <template #infoText01>
                <i class="xi-info">ex) 240mm => 240</i>
              </template>
            </InputBox>
          </tbody>
        </v-simple-table>
      </div>
    </div>
    <!-- 쇼핑 업데이트 메시지 -->
    <div class="cmpWrap">
      <div class="cmpTitle">
        <i class="xi-user">쇼핑 업데이트 메시지</i>
      </div>
      <div class="cmpTable">
        <v-simple-table>
          <!-- 테이블 시작 영역 -->
          <tbody>
            <tr>
              <td class="infoTd">
                <i class="xi-info">신상품 업데이트 시 / 내 스토어를 팔로잉하는 회원의 쇼핑피드에 자동으로 노출됩니다.</i>
                <i class="xi-info">아래 메시지를 기재하시면 노출될 때 해당 메시지를 회원의 쇼핑피드에 함께 노출할 수 있습니다.</i>
                <i class="xi-info">해당 메시지 미 기재 시 디폴트로 다음의 문구가 출력됩니다.</i>
                <span>"000 스토어에 신상이 올라왔어요"</span>
              </td>
            </tr>
          </tbody>
          <tbody>
            <tr>
              <td>
                <textarea
                  v-model="feed_message"
                  placeholder="ex) 안녕하세요 000에요!! 봄에 어울리는 신상이 입고 되었습니다."
                ></textarea>
              </td>
            </tr>
          </tbody>
        </v-simple-table>
      </div>
    </div>
    <!-- 신청 클릭 하면 패치로 포스트 해보자 -->
    <div class="btnBox">
      <!-- 신청 클릭 하면 패치로 포스트 해보자 -->
      <div class="editBtn" @click="putInfoDatas">수정</div>
      <div class="cancelBtn" @click="cancelEdit">취소</div>
    </div>
  </div>
</template>


<script>
import axios from "axios";
import { SJ_URL } from "../../../config/urlConfig";
import ImageBox from "../Slots/ImageBox";
import InputBox from "../Slots/InputBox";
import TextAreaBox from "../Slots/TextAreaBox";
// .get(`${SJ_URL}/seller_details`, {
export default {
  //첫 마운트가 되면 셀러의 기존 입력된 정보들을 불러오게 합니다.
  mounted: function() {
    axios
      .get(`${SJ_URL}/seller_details`, {
        headers: {
          Authorization: localStorage.access_token
        }
      })
      .then(response => {
        this.infoDatas = response.data;
        this.profile = this.infoDatas.data.profile;
        this.background_image = this.infoDatas.data.background_image;
        this.simple_introduction = this.infoDatas.data.simple_introduction;
        this.detail_introduction = this.infoDatas.data.detail_introduction;
        this.background_image = this.infoDatas.data.background_image;
        this.site_url = this.infoDatas.data.site_url;
        this.supervisors = this.infoDatas.data.supervisors;
        this.service_number = this.infoDatas.data.service_number;
        this.zip_code = this.infoDatas.data.zip_code;
        this.address = this.infoDatas.data.address;
        this.detail_address = this.infoDatas.data.detail_address;
        this.buisness_hours = this.infoDatas.data.buisness_hours;
        this.bank = this.infoDatas.data.bank;
        this.account_owner = this.infoDatas.data.account_owner;
        this.bank_account = this.infoDatas.data.bank_account;
        this.shipping_information = this.infoDatas.data.shipping_information;
        this.refund_information = this.infoDatas.data.refund_information;
        this.model_height = this.infoDatas.data.model_height;
        this.model_size_top = this.infoDatas.data.model_size_top;
        this.model_size_bottom = this.infoDatas.data.model_size_bottom;
        this.model_size_foot = this.infoDatas.data.model_size_foot;
        this.feed_message = this.infoDatas.data.feed_message;
      });
  },
  methods: {
    // 수정버튼을 누르면 백엔드로 인풋에 입력된 모든 내용을 보냅니다.
    putInfoDatas: function() {
      if (confirm("셀러정보를 수정 하시겠습니까?") == true) {
        axios
          .put(
            `${SJ_URL}/seller`,
            {
              profile: "url",
              background_image: "url",
              simple_introduction: this.simple_introduction,
              detail_introduction: this.detail_introduction,
              site_url: this.site_url,
              supervisors: [
                {
                  supervisor_name: "이원철",
                  supervisor_phone_number: "010-1234-1234",
                  supervisor_email: "lwc@lwc.com",
                  order: 1
                },
                {
                  supervisor_name: "이원철",
                  supervisor_phone_number: "010-1234-1234",
                  supervisor_email: "lwc@lwc.com",
                  order: 2
                },
                {
                  supervisor_name: "이원철",
                  supervisor_phone_number: "010-1234-1234",
                  supervisor_email: "lwc@lwc.com",
                  order: 3
                }
              ],
              service_number: this.service_number,
              zip_code: "우편번호",
              address: "주소 (택배 수령지)",
              detail_address: "상세주소 (택배 수령지)",
              buisness_hours: [
                {
                  start_time: "9:00:00",
                  end_time: "6:00:00",
                  is_weekend: "0"
                },
                {
                  start_time: "9:00:00",
                  end_time: "6:00:00",
                  is_weekend: "1"
                }
              ],
              bank: this.bank,
              account_owner: this.account_owner,
              bank_account: this.bank_account,
              shipping_information: this.shipping_information,
              refund_information: this.refund_information,
              model_height: Number(this.model_height),
              model_size_top: Number(this.model_size_top),
              model_size_bottom: Number(this.model_size_bottom),
              model_size_foot: Number(this.model_size_foot),
              feed_message: this.feed_message
            },
            {
              headers: {
                Authorization: localStorage.access_token
              }
            }
          )
          .then(res => {
            if (res.status === 200) {
              alert("셀러정보가 정상적으로 수정되었습니다.");
            }
          })
          .catch(error => console.log(error.response.data.message));
      }
    },
    cancelEdit: function() {
      if (
        confirm("수정을 취소하겠습니까? 확인을 누르면 새로고침됩니다.") == true
      ) {
        window.location.reload();
      }
    }
  },
  data() {
    return {
      infoDatas: [],
      profile: "",
      background_image: "",
      simple_introduction: "",
      detail_introduction: "",
      background_image: "",
      site_url: "",
      supervisors: null,
      service_number: "",
      zip_code: "",
      address: "",
      detail_address: "",
      buisness_hours: "",
      bank: "",
      account_owner: "",
      bank_account: "",
      shipping_information: "",
      refund_information: "",
      model_height: "",
      model_size_top: "",
      model_size_bottom: "",
      model_size_foot: "",
      feed_message: ""
    };
  },

  components: {
    ImageBox,
    InputBox,
    TextAreaBox
  }
};
</script>
  <style lang="scss" >
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
  .cmpTable {
    border-left: 1px solid lightgrey;
    border-right: 1px solid lightgrey;
    border-bottom: 1px solid lightgrey;

    border-radius: 3px;
    margin: 10px;

    th {
      border-right: 1px solid lightgray;
      border-top: 1px solid lightgray;
      vertical-align: middle;
      width: 149px;
    }
    td {
      display: flex;
      padding: 10px;
      height: 100%;
      vertical-align: middle;
    }
    td:first-of-type {
      border-top: 1px solid lightgray;
    }

    input {
      border: 1px solid lightgray;
      border-radius: 3px;
      width: 40%;
      padding: 6px 12px 6px 33px;
      font-size: 14px;
      font-weight: 500;
      color: #333333;
    }

    textarea {
      width: 531px;
      height: 100px;
      padding: 6px 12px;
      border: 1px solid lightgray;
      border-radius: 3px;
    }

    .infoTd {
      display: flex;
      flex-direction: column;
      padding: 0 10px 10px 10px;
      color: rgb(30, 144, 255);
      .xi-info {
        color: rgb(30, 144, 255);
      }
    }

    .option {
      input {
        width: 10px;
        height: 10px;
        margin-right: 10px;
        background-color: white;
      }
      label {
        margin-right: 10px;
      }
    }
    .threeInput {
      display: flex;
      flex-direction: column;
      input {
        margin-bottom: 20px;
      }
    }
  }
  .historyBox {
    width: 100%;
    th,
    td {
      border: 1px solid lightgray;
    }
    th {
      background-color: #eee;
    }
  }
  .timeTable {
    display: flex;
    .mid {
      border: 1px solid red;
      width: 100px;
      vertical-align: middle;
    }
    #inspire {
      width: 500px;
      height: 100px;
      #dropdown-example {
      }
      input {
        all: unset;
      }
    }
  }
}

.btnBox {
  display: flex;
  flex-direction: row;
  justify-content: center;
  background-color: #ffffff;
  div {
    padding: 10px 10px;
    color: #ffffff;
    font-size: 14px;
    font-weight: 400;
    cursor: pointer;
  }
  .editBtn {
    width: 50px;
    height: 35px;
    background-color: rgb(92, 184, 92);
    border-top-left-radius: 4px;
    border-bottom-left-radius: 4px;
  }
  .cancelBtn {
    width: 50px;
    height: 35px;
    background-color: #eee;
    border-top-right-radius: 4px;
    border-bottom-right-radius: 4px;
    color: black;
  }
  a:visited {
    color: black;
  }
}
</style>;
