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
                <td>{{infoDatas.data.name || ""}}</td>
              </tr>
            </tbody>
            <!-- 셀러 속성 테이블 -->
            <tbody>
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
            </tbody>
            <!-- 셀러 한글명 -->
            <tbody>
              <InputBox :value="infoDatas.data.kor_name" placeholder="셀러 한글명">
                <template #thName>셀러 한글명</template>
              </InputBox>
            </tbody>
            <!-- 셀러 영문명 -->
            <tbody>
              <InputBox :value="infoDatas.data.eng_name" placeholder="셀러 영문명">
                <template #thName>셀러 영문명</template>
              </InputBox>
            </tbody>
            <!-- 셀러 계정 -->
            <tbody>
              <tr>
                <th>셀러 계정</th>
                <td>{{infoDatas.data.user_id || ""}}</td>
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
              <InputBox :value="infoDatas.data.simple_introduction" placeholder="셀러 한줄 소개">
                <template #thName>셀러 한줄 소개</template>
              </InputBox>
            </tbody>
            <!-- 셀러 상세 소개 -->
            <tbody>
              <TextAreaBox :value="infoDatas.data.detail_introduction" placeholder="셀러 상세 소개">
                <template #thName>셀러 상세 소개</template>
                <template #infoText01>
                  <i class="xi-info">셀러 상세 소개 글은 최소10자 이상 입니다.</i>
                </template>
              </TextAreaBox>
            </tbody>
            <!-- 셀러 사이트 URL -->
            <tbody>
              <InputBox :value="infoDatas.data.site_url" placeholder="셀러 사이트 URL">
                <template #thName>셀러 사이트 URL</template>
              </InputBox>
            </tbody>
            <!-- 담당자 정보 -->
            <tbody>
              <ThreeInputBox
                :supervisors="infoDatas.data.supervisors"
                placeholder01="담당자명"
                placeholder02="담당자 핸드폰번호"
                placeholder03="담당자 이메일"
              >
                <template #thName>담당자 정보</template>
              </ThreeInputBox>
            </tbody>
            <!-- 고객센터 -->
            <tbody>
              <InputBox :value="infoDatas.data.servie_number" placeholder="고객센터 전화번호">
                <template #thName>고객센터</template>
              </InputBox>
            </tbody>
            <!-- 택배 -->
            <tbody>
              <th>택배주소</th>
            </tbody>
            <!-- 고객센터 운영시간(주중) -->
            <tbody>
              <th>고객센터 운영시간(주중)</th>
            </tbody>
            <!-- 정산정보 입력 -->
            <tbody>
              <tr>
                <th>정산정보 입력</th>
                <td class="threeInput">
                  <input type="text" :value="infoDatas.data.bank" placeholder="정산은행" />
                  <input type="text" :value="infoDatas.data.account_owner" placeholder="계좌주" />
                  <input type="text" :value="infoDatas.data.bank_account" placeholder="계좌번호" />
                </td>
              </tr>
            </tbody>

            <!-- 셀러상태 변경기록 -->
            <tbody>
              <th>셀러상태 변경기록</th>
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
              :value="infoDatas.data.shipping_information"
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
              :value="infoDatas.data.refund_information"
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
            <InputBox :value="infoDatas.data.model_height" placeholder="키">
              <template #thName>키</template>
              <template #infoText01>
                <i class="xi-info">ex) 160cm => 160</i>
              </template>
            </InputBox>
          </tbody>
          <tbody>
            <InputBox :value="infoDatas.data.model_size_top" placeholder="상의 사이즈">
              <template #thName>상의 사이즈</template>
              <template #infoText01>
                <i class="xi-info">ex) 55사이즈 => 55</i>
              </template>
            </InputBox>
          </tbody>
          <tbody>
            <InputBox :value="infoDatas.data.model_size_bottom" placeholder="하의 사이즈">
              <template #thName>하의 사이즈</template>
              <template #infoText01>
                <i class="xi-info">ex) 27사이즈 => 27</i>
              </template>
            </InputBox>
          </tbody>
          <tbody>
            <InputBox :value="infoDatas.data.model_size_foot" placeholder="발 사이즈">
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
                  :value="infoDatas.data.feed_message"
                  placeholder="ex) 안녕하세요 000에요!! 봄에 어울리는 신상이 입고 되었습니다."
                ></textarea>
              </td>
            </tr>
          </tbody>
        </v-simple-table>
      </div>
    </div>
  </div>
</template>


<script>
import axios from "axios";
import { URL } from "../../../config/urlConfig";
import ImageBox from "../Slots/ImageBox";
import InputBox from "../Slots/InputBox";
import TextAreaBox from "../Slots/TextAreaBox";
import ThreeInputBox from "../Slots/ThreeInputBox";
export default {
  mounted: function() {
    axios
      .get(`${URL}/sellerregist.json`, {
        headers: {
          Authorization:
            "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoyNCwiYXV0aG9yaXR5X2lkIjoyLCJleHAiOjE1OTE2MjA3OTN9.NpnYcqVJRF5JBkn_YQflfdfgEu-XjOBCPr9lcFyscns"
        }
      })
      .then(response => {
        this.infoDatas = response.data;
        console.log(this.infoDatas.data.supervisors[0].name);
      });
    // mounted: function() {
    //   axios
    //     .get(`${SJ_URL}/seller_details`, {
    //       headers: {
    //         Authorization:
    //           "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoyNCwiYXV0aG9yaXR5X2lkIjoyLCJleHAiOjE1OTE2MjA3OTN9.NpnYcqVJRF5JBkn_YQflfdfgEu-XjOBCPr9lcFyscns"
    //       }
    //     })
    //     .then(response => {
    //       this.infoDatas = response.data;
    //       console.log(this.infoDatas.data.name);
    //     });
  },
  data() {
    return {
      infoDatas: []
    };
  },
  components: {
    ImageBox,
    InputBox,
    TextAreaBox,
    ThreeInputBox
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
      width: 295px;
      height: 34px;
      padding: 6px 12px 6px 33px;
      font-size: 14px;
      font-weight: 500;
      color: #333333;
    }

    textarea {
      width: 531px;
      height: 100px;
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
}
</style>;
