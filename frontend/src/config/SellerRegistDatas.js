export const infos = [
  {
    infoTitle: "기본 정보",
    infoContent: [
      { header: "셀러 프로필 *", value: [{ type: "file", text: "이미지 선택" }, { type: "info", text: "셀러 프로필 확장자는 jpg, jpeg, png 만 가능하며, 허용 가능한 최대 파일사이즈 크기는 5MB 입니다." }] },
      { header: "셀러 상태", value: [{ type: "text", text: "입점" }] },
      { header: "셀러 속성", value: [{ state: "master", type: "radio", option1: "쇼핑몰", option2: "마켓", option3: "로드샵" }] },
      { header: "셀러 한글명", value: [{ type: "text", text: "아이디" }] },
      { header: "셀러 영문명", value: [{ type: "text", text: "아이디" }] },
      { header: "셀러 계정", value: [{ type: "text", text: "아이디" }] }]
  },
  {
    infoTitle: "상세 정보",
    infoContent: [
      { header: "셀러페이지 배경이미지", value: [{ type: "file", text: "이미지 선택" }, { type: "Btn", text: "이미지 선택" }, { type: "info", text: "브랜디 앱과 웹 사이트의 셀러 페이지에 보여질 배경이미지입니다." }, { type: "info", text: " 배경이미지는 1200 * 850 사이즈 이상으로 등록해주세요." }, { type: "info", text: " 확장자는 jpg, jpeg, png 만 가능하며, 허용 가능한 최대 파일사이즈 크기는 5MB 입니다." }] },
      { header: "셀러 한줄 소개", value: [{ type: "input", text: "셀러 한줄 소개 인풋" }] },
      { header: "셀러 상세 소개", value: [{ type: "textarea", text: "셀러 상세 소개" }, { type: "info", text: " 셀러 상세 소개 글은 최소10자 이상 입니다." }] },
      { header: "사이트 URL", value: [{ type: "input", text: "사이트 URL" }] },
      { header: "담당자 정보", value: [{ type: "input", text: "담당자명" }, { type: "input", text: "담당자 핸드폰번호" }, { type: "input", text: "담당자 이메일" }] },
      { header: "인스타그램 아이디", value: [{ type: "input", text: "인스타그램 아이디" }, { type: "info" }] },
      { header: "고객 센터", value: [{ type: "input", text: "전화번호" }] },
      { header: "택배 주소", value: [{ type: "input", text: "우편번호" }, { type: "input", text: "주소(택배 수령지)" }, { type: "input", text: "상세주소(택배 수령지)" }] },
      { header: "고객센터 운영시간(주중)", value: [{ type: "input", text: "타임테이블" }] },
      { header: "정산정보 입력", value: [{ type: "input", text: "정산은행" }, { type: "input", text: "계좌주" }, { type: "input", text: "계좌번호" }] },
      { header: "셀러상태 변경기록", value: [{ type: "input", text: "히스토리..." }] },
    ]
  },
  {
    infoTitle: "배송정보 및 교환/환불 정보",
    infoContent: [
      { header: "배송 정보", value: [{ type: "textarea", text: "ex) 도서산간 지역은 배송비가 추가비용이 발생할 수 있습니다. 결제 완료 후 1~3일 후 출고됩니다." }, { tpye: "info", text: " 문장이 끝나면 엔터로 줄바꿈을 해주세요." }] },
    ]
  },
  {
    infoTitle: "관리 브랜드 정보",
    infoContent: [
      { header: "관리브랜드", value: [{ type: "text", text: "" }] },
    ]
  },
  {
    infoTitle: "셀러 모델 사이즈 정보",
    infoContent: [
      { header: "", value: [{ type: "info", text: "셀러 모델 사이즈 정보는 선택사항입니다. 단, 입력하실 때는 4가지 항목을 모두 입력하셔야합니다." }] },
      { header: "키", value: [{ type: "input", text: "키" }, { type: "info", text: "ex) 160cm => 160" }] },
      { header: "상의 사이즈", value: [{ type: "input", text: "상의 사이즈" }, { type: "info", text: "ex) 55사이즈 => 55" }] },
      { header: "하의 사이즈", value: [{ type: "input", text: "하의 사이즈" }, { type: "info", text: "ex) 27사이즈 => 27" }] },
      { header: "발 사이즈", value: [{ type: "input", text: "발 사이즈" }, { type: "info", text: "ex) 240mm => 240" }] },
    ]
  },
  {
    infoTitle: "셀러 모델 사이즈 정보",
    infoContent: [
      { header: "", value: [{ type: "info", text: "각 항목 별로 태그는 1개만 선택 가능합니다. (기타 항목에 있는 태그는 정책상 사용할 수 없는 태그입니다.)" }] },
      { header: "키", value: [{ type: "input", text: "키" }, { type: "info", text: "ex) 160cm => 160" }] },
      { header: "상의 사이즈", value: [{ type: "input", text: "상의 사이즈" }, { type: "info", text: "ex) 55사이즈 => 55" }] },
      { header: "하의 사이즈", value: [{ type: "input", text: "하의 사이즈" }, { type: "info", text: "ex) 27사이즈 => 27" }] },
      { header: "발 사이즈", value: [{ type: "input", text: "발 사이즈" }, { type: "info", text: "ex) 240mm => 240" }] },
    ]
  },
  {
    infoTitle: "쇼핑피드 업데이트 메시지",
    infoContent: [
      { header: "", value: [{ type: "info", text: " 신상품 업데이트 시 / 내 스토어를 팔로잉하는 회원의 쇼핑피드에 자동으로 노출됩니다." }, { type: "info", text: "아래 메시지를 기재하시면 노출될 때 해당 메시지를 회원의 쇼핑피드에 함께 노출할 수 있습니다." }, { type: "info", text: "해당 메시지 미 기재 시 디폴트로 다음의 문구가 출력됩니다." }, { type: "info", text: "000 스토어에 신상이 올라왔어요" }] },
      { header: "키", value: [{ type: "input", text: "키" }, { type: "info", text: "ex) 160cm => 160" }] },
      { header: "상의 사이즈", value: [{ type: "textarea", text: "ex) 안녕하세요 000에요!! 봄에 어울리는 신상이 입고 되었습니다." }] },
    ]
  },

]

// export const infos = [
//   {
//     infoTitle: "기본 정보",
//     infoContent: [
//       { header: "셀러 프로필 *", value: [{ type: "file", text: "이미지 선택" }, { type: "info", text: "셀러 프로필 확장자는 jpg, jpeg, png 만 가능하며, 허용 가능한 최대 파일사이즈 크기는 5MB 입니다." }] },
//       { header: "셀러 상태", value: [{ type: "text", text: "입점" }] },
//       { header: "셀러 한글명", value: [{ type: "text", text: "아이디" }] },
//       { header: "셀러 영문명", value: [{ type: "text", text: "아이디" }] },
//       { header: "셀러 계정", value: [{ type: "text", text: "아이디" }] }]
//   },
//   {
//     infoTitle: "상세 정보",
//     infoContent: [
//       { header: "셀러페이지 배경이미지", value: [{ type: "file", text: "이미지 선택" }, { type: "Btn", text: "이미지 선택" }, { type: "info", text: "브랜디 앱과 웹 사이트의 셀러 페이지에 보여질 배경이미지입니다." }, { type: "info", text: " 배경이미지는 1200 * 850 사이즈 이상으로 등록해주세요." }, { type: "info", text: " 확장자는 jpg, jpeg, png 만 가능하며, 허용 가능한 최대 파일사이즈 크기는 5MB 입니다." }] },
//       { header: "셀러 한줄 소개", value: [{ type: "input", text: "셀러 한줄 소개 인풋" }] },
//       { header: "셀러 상세 소개", value: [{ type: "textarea", text: "셀러 상세 소개" }, { type: "info", text: " 셀러 상세 소개 글은 최소10자 이상 입니다." }] },
//       { header: "사이트 URL", value: [{ type: "input", text: "사이트 URL" }] },
//       { header: "담당자 정보", value: [{ type: "input", text: "담당자명" }, { type: "input", text: "담당자 핸드폰번호" }, { type: "input", text: "담당자 이메일" }] },
//       { header: "인스타그램 아이디", value: [{ type: "input", text: "인스타그램 아이디" }, { type: "info" }] },
//       { header: "고객 센터", value: [{ type: "input", text: "전화번호" }] },
//       { header: "택배 주소", value: [{ type: "input", text: "우편번호" }, { type: "input", text: "주소(택배 수령지)" }, { type: "input", text: "상세주소(택배 수령지)" }] },
//       { header: "고객센터 운영시간(주중)", value: [{ type: "input", text: "타임테이블" }] },
//       { header: "정산정보 입력", value: [{ type: "input", text: "정산은행" }, { type: "input", text: "계좌주" }, { type: "input", text: "계좌번호" }] },
//       { header: "셀러상태 변경기록", value: [{ type: "input", text: "히스토리..." }] },
//     ]
//   },
//   {
//     infoTitle: "수수료",
//     infoContent: [
//       { header: "A안", value: [{ type: "text", text: "수수료 11%" }] },
//     ]
//   },
//   {
//     infoTitle: "배송정보 및 교환/환불 정보",
//     infoContent: [
//       { header: "배송 정보", value: [{ type: "textarea", text: "ex) 도서산간 지역은 배송비가 추가비용이 발생할 수 있습니다. 결제 완료 후 1~3일 후 출고됩니다." }, { tpye: "info", text: " 문장이 끝나면 엔터로 줄바꿈을 해주세요." }] },
//     ]
//   },
//   {
//     infoTitle: "관리 브랜드 정보",
//     infoContent: [
//       { header: "관리브랜드", value: [{ type: "text", text: "" }] },
//     ]
//   },
//   {
//     infoTitle: "셀러 모델 사이즈 정보",
//     infoContent: [
//       { header: "", value: [{ type: "info", text: "셀러 모델 사이즈 정보는 선택사항입니다. 단, 입력하실 때는 4가지 항목을 모두 입력하셔야합니다." }] },
//       { header: "키", value: [{ type: "input", text: "키" }, { type: "info", text: "ex) 160cm => 160" }] },
//       { header: "상의 사이즈", value: [{ type: "input", text: "상의 사이즈" }, { type: "info", text: "ex) 55사이즈 => 55" }] },
//       { header: "하의 사이즈", value: [{ type: "input", text: "하의 사이즈" }, { type: "info", text: "ex) 27사이즈 => 27" }] },
//       { header: "발 사이즈", value: [{ type: "input", text: "발 사이즈" }, { type: "info", text: "ex) 240mm => 240" }] },
//     ]
//   },
//   {
//     infoTitle: "셀러 모델 사이즈 정보",
//     infoContent: [
//       { header: "", value: [{ type: "info", text: "각 항목 별로 태그는 1개만 선택 가능합니다. (기타 항목에 있는 태그는 정책상 사용할 수 없는 태그입니다.)" }] },
//       { header: "키", value: [{ type: "input", text: "키" }, { type: "info", text: "ex) 160cm => 160" }] },
//       { header: "상의 사이즈", value: [{ type: "input", text: "상의 사이즈" }, { type: "info", text: "ex) 55사이즈 => 55" }] },
//       { header: "하의 사이즈", value: [{ type: "input", text: "하의 사이즈" }, { type: "info", text: "ex) 27사이즈 => 27" }] },
//       { header: "발 사이즈", value: [{ type: "input", text: "발 사이즈" }, { type: "info", text: "ex) 240mm => 240" }] },
//     ]
//   },
//   {
//     infoTitle: "쇼핑피드 업데이트 메시지",
//     infoContent: [
//       { header: "", value: [{ type: "info", text: " 신상품 업데이트 시 / 내 스토어를 팔로잉하는 회원의 쇼핑피드에 자동으로 노출됩니다." }, { type: "info", text: "아래 메시지를 기재하시면 노출될 때 해당 메시지를 회원의 쇼핑피드에 함께 노출할 수 있습니다." }, { type: "info", text: "해당 메시지 미 기재 시 디폴트로 다음의 문구가 출력됩니다." }, { type: "info", text: "000 스토어에 신상이 올라왔어요" }] },
//       { header: "키", value: [{ type: "input", text: "키" }, { type: "info", text: "ex) 160cm => 160" }] },
//       { header: "상의 사이즈", value: [{ type: "textarea", text: "ex) 안녕하세요 000에요!! 봄에 어울리는 신상이 입고 되었습니다." }] },
//     ]
//   },

// ]