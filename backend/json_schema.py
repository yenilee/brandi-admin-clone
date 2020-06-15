#셀러 회원가입 스키마
seller_sign_up_schema = {
    "$schema": "http://json-schema.org/draft-07/schema",
    "$id": "http://example.com/example.json",
    "type": "object",
    "default": {},
    "examples": [
        {
            "user": "test3",
            "seller_attribute_id": 3,
            "password": "1q2w3e4r!",
            "phone_number": "010-1111-2222",
            "name": "테스트03",
            "eng_name": "brandi",
            "service_number": "010-1234-1234",
            "site_url": "http://www.naver.com"
        }
    ],
    "required": [
        "user",
        "seller_attribute_id",
        "password",
        "phone_number",
        "name",
        "eng_name",
        "service_number",
        "site_url"
    ],
    "additionalProperties": True,
    "properties": {
        "user": {
            "$id": "#/properties/user",
            "type": "string",
            "default": "",
            "examples": [
                "test3"
            ],
            "pattern": "^[A-Za-z0-9][A-Za-z0-9_-]{4,20}$"
        },
        "seller_attribute_id": {
            "$id": "#/properties/seller_attribute_id",
            "type": "integer",
            "default": 0,
            "examples": [
                3
            ],
            "maximum": 7,
            "minimum": 1
        },
        "password": {
            "$id": "#/properties/password",
            "type": "string",
            "default": "",
            "examples": [
                "1q2w3e4r!"
            ],
            "pattern": "(?=.*[A-Za-z])(?=.*\\d)(?=.*[$@$!%*#?&])[A-Za-z\\d$@$!%*#?&]{7,20}$"
        },
        "phone_number": {
            "$id": "#/properties/phone_number",
            "type": "string",
            "default": "",
            "examples": [
                "010-1111-2222"
            ],
            "pattern": "\\d{3}-\\d{3,4}-\\d{4}$"
        },
        "name": {
            "$id": "#/properties/name",
            "type": "string",
            "default": "",
            "examples": [
                "테스트03"
            ],
            "pattern": "^[ㄱ-ㅣ가-힣-0-9A-Za-z]([0-9ㄱ-ㅣ가-힣A-Za-z]){0,20}$"
        },
        "eng_name": {
            "$id": "#/properties/eng_name",
            "type": "string",
            "default": "",
            "examples": [
                "brandi"
            ],
            "pattern": "^[a-z]*$"
        },
        "service_number": {
            "$id": "#/properties/service_number",
            "type": "string",
            "default": "",
            "examples": [
                "010-1234-1234"
            ],
            "pattern": "(02.{0}|^01.{1}|[0-9]{4})-([0-9]+)-([0-9]{4})"
        },
        "site_url": {
            "$id": "#/properties/site_url",
            "type": "string",
            "default": "",
            "examples": [
                "http://www.naver.com"
            ],
            "pattern": "(http|https):\\/\\/(\\w+:{0,1}\\w*@)?(\\S+)(:[0-9]+)?(\\/|\\/([\\w#!:.?+=&%@!\\-\\/].[^\\s]*$))?"
        }
    }
}

# 상품 등록 수정 parameter validation
seller_register_schema = {
    "$schema": "http://json-schema.org/draft-07/schema",
    "$id": "http://example.com/example.json",
    "type": "object",
    "default": {},
    "examples": [
        {
            "profile": "url",
            "background_image": "url",
            "simple_introduction": "안녕 난 진아야 안녕",
            "detail_introduction": "셀러 상세 소개",
            "site_url": "http://www.naver.com",
            "supervisors": [
                {
                    "supervisor_name": "담당자1",
                    "supervisor_phone_number": "담당자1 핸드폰번호",
                    "supervisor_email": "담당자1 이메일",
                    "order": 1
                },
                {
                    "supervisor_name": "담당자",
                    "supervisor_phone_number": "담당자2 핸드폰번호",
                    "supervisor_email": "담당자2 이메일",
                    "order": 2
                },
                {
                    "supervisor_name": "담당자3",
                    "supervisor_phone_number": "담당자3 핸드폰번호",
                    "supervisor_email": "담당자3 이메일",
                    "order": 3
                }
            ],
            "service_number": "010-5338-7244",
            "zip_code": "우편번호",
            "address": "주소 (택배 수령지)",
            "detail_address": "상세주소 (택배 수령지)",
            "buisness_hours": [
                {
                    "start_time": "9:00:00",
                    "end_time": "6:00:00",
                    "is_weekend": "0"
                },
                {
                    "start_time": "9:00:00",
                    "end_time": "6:00:00",
                    "is_weekend": "1"
                }
            ],
            "bank": "정산은행",
            "account_owner": "계좌주",
            "bank_account": "110-333-3333",
            "shipping_information": "배송정보",
            "refund_information": "교환 / 환불 정보",
            "model_height": 177,
            "model_size_top": 50,
            "model_size_bottom": 30,
            "model_size_foot": 255,
            "feed_message": "안녕하세요 OOO에요! 봄에 어울리는 신상이 입고 되었습니다."
        }
    ],
    "required": [
        "simple_introduction",
        "site_url",
        "service_number",
        "detail_address",
        "bank",
        "account_owner",
        "bank_account",
        "shipping_information",
        "refund_information",
        "model_height",
        "supervisors",
        "buisness_hours"
    ],
    "additionalProperties": True,
    "properties": {
        "profile": {
            "$id": "#/properties/profile",
            "type": "string",
            "default": "",
            "examples": [
                "url"
            ]
        },
        "background_image": {
            "$id": "#/properties/background_image",
            "type": "string",
            "default": "",
            "examples": [
                "url"
            ]
        },
        "simple_introduction": {
            "$id": "#/properties/simple_introduction",
            "type": "string",
            "default": "",
            "examples": [
                "안녕 난 진아야 안녕"
            ],
            "minLength": 1
        },
        "detail_introduction": {
            "$id": "#/properties/detail_introduction",
            "type": ["string", "null"],
            "default": "",
            "examples": [
                "셀러 상세 소개"
            ]
        },
        "site_url": {
            "$id": "#/properties/site_url",
            "type": "string",
            "default": "",
            "examples": [
                "http://www.naver.com"
            ],
            "pattern": "(http|https):\\/\\/(\\w+:{0,1}\\w*@)?(\\S+)(:[0-9]+)?(\\/|\\/([\\w#!:.?+=&%@!\\-\\/].[^\\s]*$))?"
        },
        "supervisors": {
            "$id": "#/properties/supervisors",
            "type": ["array", "null"],
            "default": [],
            "examples": [
                [
                    {
                        "supervisor_name": "담당자1",
                        "supervisor_phone_number": "담당자1 핸드폰번호",
                        "supervisor_email": "담당자1 이메일",
                        "order": 1
                    },
                    {
                        "supervisor_name": "담당자",
                        "supervisor_phone_number": "담당자2 핸드폰번호",
                        "supervisor_email": "담당자2 이메일",
                        "order": 2
                    }
                ]
            ],
            "additionalItems": True,
            "items": {
                "anyOf": [
                    {
                        "$id": "#/properties/supervisors/items/anyOf/0",
                        "type": "object",
                        "default": {},
                        "examples": [
                            {
                                "supervisor_name": "담당자1",
                                "supervisor_phone_number": "담당자1 핸드폰번호",
                                "supervisor_email": "담당자1 이메일",
                                "order": "1"
                            }
                        ],
                        "required": [
                        ],
                        "additionalProperties": True,
                        "properties": {
                            "supervisor_name": {
                                "$id": "#/properties/supervisors/items/anyOf/0/properties/supervisor_name",
                                "type": ["string", "null"],                 
                                "default": "",
                                "examples": [
                                    "담당자1"
                                ]
                            },
                            "supervisor_phone_number": {
                                "$id": "#/properties/supervisors/items/anyOf/0/properties/supervisor_phone_number",
                                "type": ["string", "null"],                       
                                "default": "",
                                "examples": [
                                    "담당자1 핸드폰번호"
                                ],
                                "pattern": "(02.{0}|^01.{1}|[0-9]{4})-([0-9]+)-([0-9]{4})"
                            },
                            "supervisor_email": {
                                "$id": "#/properties/supervisors/items/anyOf/0/properties/supervisor_email",
                                "type":["string", "null"],                          
                                "default": "",
                                "examples": [
                                    "담당자1 이메일"
                                ]
                            },
                            "order": {
                                "$id": "#/properties/supervisors/items/anyOf/0/properties/order",
                                "type": "integer",                       
                                "default": "",
                                "examples": [
                                    "1"
                                ]
                            }
                        }
                    }
                ],
                "$id": "#/properties/supervisors/items"
            }
        },
        "service_number": {
            "$id": "#/properties/service_number",
            "type": "string",      
            "default": "",
            "examples": [
                "010-5338-7244"
            ],
            "pattern": "(02.{0}|^01.{1}|[0-9]{4})-([0-9]+)-([0-9]{4})"
        },
        "zip_code": {
            "$id": "#/properties/zip_code",
            "type": "string",
            "default": "",
            "examples": [
                "우편번호"
            ]
        },
        "address": {
            "$id": "#/properties/address",
            "type": "string",
            "default": "",
            "examples": [
                "주소 (택배 수령지)"
            ]
        },
        "detail_address": {
            "$id": "#/properties/detail_address",
            "type": "string",
            "default": "",
            "examples": [
                "상세주소 (택배 수령지)"
            ]
        },
        "buisness_hours": {
            "$id": "#/properties/buisness_hours",
            "type": "array",
            "default": [],
            "examples": [
                [
                    {
                        "start_time": "9:00:00",
                        "end_time": "6:00:00",
                        "is_weekend": "0"
                    },
                    {
                        "start_time": "9:00:00",
                        "end_time": "6:00:00",
                        "is_weekend": "1"
                    }
                ]
            ],
            "additionalItems": True,
            "items": {
                "anyOf": [
                    {
                        "$id": "#/properties/buisness_hours/items/anyOf/0",
                        "type": "object",
                        "default": {},
                        "examples": [
                            {
                                "start_time": "9:00:00",
                                "end_time": "6:00:00",
                                "is_weekend": "0"
                            }
                        ],
                        "required": [
                            "start_time",
                            "end_time",
                            "is_weekend"
                        ],
                        "additionalProperties": True,
                        "properties": {
                            "start_time": {
                                "$id": "#/properties/buisness_hours/items/anyOf/0/properties/start_time",
                                "type": ["string", "null"],
                                "default": "",
                                "examples": [
                                    "9:00:00"
                                ]
                            },
                            "end_time": {
                                "$id": "#/properties/buisness_hours/items/anyOf/0/properties/end_time",
                                "type": ["string", "null"],
                                "default": "",
                                "examples": [
                                    "6:00:00"
                                ]
                            },
                            "is_weekend": {
                                "$id": "#/properties/buisness_hours/items/anyOf/0/properties/is_weekend",
                                "type": "integer",
                                "default": "",
                                "examples": [
                                    "0"
                                ]
                            }
                        }
                    }
                ],
                "$id": "#/properties/buisness_hours/items"
            }
        },
        "bank": {
            "$id": "#/properties/bank",
            "type": "string",
            "default": "",
            "examples": [
                "정산은행"
            ]
        },
        "account_owner": {
            "$id": "#/properties/account_owner",
            "type": "string",
            "default": "",
            "examples": [
                "계좌주"
            ]
        },
        "bank_account": {
            "$id": "#/properties/bank_account",
            "type": "string",
            "default": "",
            "examples": [
                "계좌번호"
            ],
            "pattern": "^[0-9-]*$"
        },
        "shipping_information": {
            "$id": "#/properties/shipping_information",
            "type": "string",
            "default": "",
            "examples": [
                "배송정보"
            ]
        },
        "refund_information": {
            "$id": "#/properties/refund_information",
            "type": "string",
            "default": "",
            "examples": [
                "교환 / 환불 정보"
            ]
        },
        "model_height": {
            "$id": "#/properties/model_height",
            "type": "integer",
            "default": 0,
            "examples": [
                177
            ]
        },
        "model_size_top": {
            "$id": "#/properties/model_size_top",
            "type": "integer",
            "default": 0,
            "examples": [
                50
            ]
        },
        "model_size_bottom": {
            "$id": "#/properties/model_size_bottom",
            "type": "integer",
            "default": 0,
            "examples": [
                30
            ]
        },
        "model_size_foot": {
            "$id": "#/properties/model_size_foot",
            "type": "integer",
            "default": 0,
            "examples": [
                255
            ]
        },
        "feed_message": {
            "$id": "#/properties/feed_message",
            "type": ["string", "null"],
            "default": "",
            "examples": [
                "안녕하세요 OOO에요! 봄에 어울리는 신상이 입고 되었습니다."
            ]
        }
    }
}

seller_action_schema = {
    "$schema": "http://json-schema.org/draft-07/schema",
    "$id": "http://example.com/example.json",
    "type": "object",
    "default": {},
    "examples": [
        {
            "user": 9,
            "action_type": "입점 승인"
        }
    ],
    "required": [
        "user",
        "action_type"
    ],
    "additionalProperties": True,
    "properties": {
        "user": {
            "$id": "#/properties/user",
            "type": "integer",
            "default": 0,
            "examples": [
                9
            ]
        },
        "action_type": {
            "$id": "#/properties/action_type",
            "type": "string",
            "default": "",
            "examples": [
                "입점 승인"
            ]
        }
    }
}

# 상품 리스트 필터링 parameter validation
product_list_queryset_schema = {
    "$schema": "http://json-schema.org/draft-07/schema",
    "$id": "http://example.com/example.json",
    "type": "object",
    "default": {},
    "examples": [
        {
            "user": "test",
            "product_code": "brandi13",
            "is_onsale": 1,
            "is_displayed": 0,
            "is_discount": 0,
            "seller_attribute_id": 2,
            "product_number": 1
        }
    ],
    "required": [],
    "additionalProperties": True,
    "properties": {
        "user": {
            "$id": "#/properties/user",
            "type": "string",
            "default": "",
            "examples": [
                "test"
            ],
            "pattern": "[A-Za-z0-9]"
        },
        "product_code": {
            "$id": "#/properties/product_code",
            "type": "string",
            "default": "",
            "examples": [
                "brandi13"
            ],
            "pattern" : "[A-Za-z0-9]"
        },
        "is_onsale": {
            "$id": "#/properties/is_onsale",
            "type": "string",
            "default": 0,
            "examples": [
                1
            ],
            "pattern" : "[0-1]"
        },
        "is_displayed": {
            "$id": "#/properties/is_displayed",
            "type": "string",
            "title": "The is_displayed schema",
            "description": "An explanation about the purpose of this instance.",
            "default": 0,
            "examples": [
                0
            ],
            "pattern" : "[0-1]"
        },
        "is_discount": {
            "$id": "#/properties/is_discount",
            "type": "string",
            "default": 0,
            "examples": [
                0
            ],
            "pattern" : "[0-1]"
        },
        "seller_attribute_id": {
            "$id": "#/properties/seller_attribute_id",
            "type": "string",
            "default": 0,
            "examples": [
                2
            ],
            "pattern" : "[0-7]"
        },
        "product_number": {
            "$id": "#/properties/product_number",
            "type": "string",
            "default": 0,
            "examples": [
                1
            ],
            "pattern" : "[0-9]"
        }
    }
}

product_register_schema = {
    "$schema": "http://json-schema.org/draft-07/schema",
    "$id": "http://example.com/example.json",
    "type": "object",
    "title": "The root schema",
    "description": "The root schema comprises the entire JSON document.",
    "default": {},
    "examples": [
        {
            "seller_key_id": 18,
            "is_onsale": 1,
            "is_displayed": 1,
            "color_filter_id": 1,
            "first_category_id": 15,
            "second_category_id": 1,
            "is_detail_reference": 0,
            "manufacture": {
                "manufacturer": "예은",
                "manufacture_date": "2020-05-15",
                "origin": "중국"
            },
            "name": "청바지",
            "simple_description": "편해요",
            "details": "뛰어다닐 수 있어요",
            "options": [
                {
                    "size": "XL",
                    "color": "Gray",
                    "quantity": 88
                }, {
                    "size": "L",
                    "color": "Gray",
                    "quantity": 88
                }
            ],
            "wholesale_price": 30000,
            "price": 68000,
            "discount_rate": 10,
            "discount_start": "2020-06-01 08:30:00",
            "discount_end": "2020-06-03 23:59:59",
            "maximum_quantity": 1000,
            "minimum_quantity": 40,
            "tags": [
                "태그88",
                "태그97",
                "태그94"
            ]
        }
    ],
    "required": [
        "is_onsale",
        "is_displayed",
        "first_category_id",
        "second_category_id",
        "is_detail_reference",
        "name",
        "simple_description",
        "details",
        "options",
        "price",
        "discount_rate",
        "tags"
    ],
    "additionalProperties": True,
    "properties": {
        "seller_key_id": {
            "$id": "#/properties/seller_key_id",
            "type": "integer",
            "default": 0
        },
        "is_onsale": {
            "$id": "#/properties/is_onsale",
            "type": "integer",
            "default": 0
        },
        "is_displayed": {
            "$id": "#/properties/is_displayed",
            "type": "integer",
            "default": 0
        },
        "color_filter_id": {
            "$id": "#/properties/color_filter_id",
            "type": ["integer", "null"],
            "default": "null",
        },
        "first_category_id": {
            "$id": "#/properties/first_category_id",
            "type": "integer",
            "default": 0
        },
        "second_category_id": {
            "$id": "#/properties/second_category_id",
            "type": "integer",
            "default": 0,
        },
        "is_detail_reference": {
            "$id": "#/properties/is_detail_reference",
            "type": "integer",
            "default": 0
        },
        "manufacture": {
            "$id": "#/properties/manufacture",
            "type": ["object", "null"],
            "default": {},
            "examples": [
                {
                    "manufacturer": "예은",
                    "manufacture_date": "2020-05-15",
                    "origin": "중국"
                }
            ],
            "required": [
                "manufacturer",
                "manufacture_date",
                "origin"
            ],
            "additionalProperties": True,
            "properties": {
                "manufacturer": {
                    "$id": "#/properties/manufacture/properties/manufacturer",
                    "type": "string",
                    "default": ""
                },
                "manufacture_date": {
                    "$id": "#/properties/manufacture/properties/manufacture_date",
                    "type": "string",
                    "default": ""
                },
                "origin": {
                    "$id": "#/properties/manufacture/properties/origin",
                    "type": "string",
                    "default": "",
                }
            }
        },
        "name": {
            "$id": "#/properties/name",
            "type": "string",
            "default": ""
        },
        "simple_description": {
            "$id": "#/properties/simple_description",
            "type": "string",
            "default": ""
        },
        "details": {
            "$id": "#/properties/details",
            "type": "string",
            "default": ""
        },
        "options": {
            "$id": "#/properties/options",
            "type": "array",
            "default": [],
            "examples": [
                [
                    {
                        "size": "XL",
                        "color": "Gray",
                        "quantity": 88
                    },
                    {
                    "size": "L",
                    "color": "Gray",
                    "quantity": 88
                }
                ]
            ],
            "additionalItems": True,
            "items": {
                "anyOf": [
                    {
                        "$id": "#/properties/options/items/anyOf/0",
                        "type": "object",
                        "default": {},
                        "examples": [
                            {
                                "size": 5,
                                "color": 4,
                                "quantity": 88
                            }
                        ],
                        "required": [
                            "size",
                            "color"
                            "",
                            "quantity"
                        ],
                        "additionalProperties": True,
                        "properties": {
                            "size": {
                                "$id": "#/properties/options/items/anyOf/0/properties/size",
                                "type": "string",
                                "default": 0
                            },
                            "color": {
                                "$id": "#/properties/options/items/anyOf/0/properties/color",
                                "type": "string",
                                "default": 0
                            },
                            "quantity": {
                                "$id": "#/properties/options/items/anyOf/0/properties/quantity",
                                "type": "integer",
                                "default": 0
                            }
                        }
                    }
                ],
                "$id": "#/properties/options/items"
            }
        },
        "wholesale_price": {
            "$id": "#/properties/wholesale_price",
            "type": ["integer", "null"],
            "default": 0,
        },
        "price": {
            "$id": "#/properties/price",
            "type": "integer",
            "default": 0,
        },
        "discount_rate": {
            "$id": "#/properties/discount_rate",
            "type": ["integer"],
            "default": 0,
            "minimum" : 1,
            "maximum": 100
        },
        "discount_start": {
            "$id": "#/properties/discount_start",
            "type": ["string", "null"],
            "default": "",
        },
        "discount_end": {
            "$id": "#/properties/discount_end",
            "type": ["string", "null"],
            "default": "",
        },
        "maximum_quantity": {
            "$id": "#/properties/maximum_quantity",
            "type": ["integer", "null"],
            "default": 1,
            "minimum" : 20,
            "maximum": 20
        },
        "minimum_quantity": {
            "$id": "#/properties/minimum_quantity",
            "type": ["integer", "null"],
            "default": 20,
            "minimum" : 1,
            "maximum": 20
        },
        "tags": {
            "$id": "#/properties/tags",
            "type": "array",
            "default": [],
            "uniqueItems" : True,
            "errorMessage": "Please add a short description",
            "miniItems" : 1,
            "additionalItems": True,
            "items": {

                "anyOf": [
                    {
                        "$id": "#/properties/tags/items/anyOf/0",
                        "type": "string",
                        "default": "",
                    }
                ],
                "$id": "#/properties/tags/items"
            }
        }
    }
}