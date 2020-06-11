seller_register_schema = {
    "$schema": "http://json-schema.org/draft-07/schema",
    "$id": "http://example.com/example.json",
    "type": "object",
    "title": "The root schema",
    "description": "The root schema comprises the entire JSON document.",
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
            "title": "The profile schema",
            "description": "An explanation about the purpose of this instance.",
            "default": "",
            "examples": [
                "url"
            ]
        },
        "background_image": {
            "$id": "#/properties/background_image",
            "type": "string",
            "title": "The background_image schema",
            "description": "An explanation about the purpose of this instance.",
            "default": "",
            "examples": [
                "url"
            ]
        },
        "simple_introduction": {
            "$id": "#/properties/simple_introduction",
            "type": "string",
            "title": "The simple_introduction schema",
            "description": "An explanation about the purpose of this instance.",
            "default": "",
            "examples": [
                "안녕 난 진아야 안녕"
            ],
            "minLength": 1
        },
        "detail_introduction": {
            "$id": "#/properties/detail_introduction",
            "type": ["string", "null"],
            "title": "The detail_introduction schema",
            "description": "An explanation about the purpose of this instance.",
            "default": "",
            "examples": [
                "셀러 상세 소개"
            ]
        },
        "site_url": {
            "$id": "#/properties/site_url",
            "type": "string",
            "title": "The site_url schema",
            "description": "An explanation about the purpose of this instance.",
            "default": "",
            "examples": [
                "http://www.naver.com"
            ],
            "pattern": "(http|https):\\/\\/(\\w+:{0,1}\\w*@)?(\\S+)(:[0-9]+)?(\\/|\\/([\\w#!:.?+=&%@!\\-\\/].[^\\s]*$))?"
        },
        "supervisors": {
            "$id": "#/properties/supervisors",
            "type": ["array", "null"],
            "title": "The supervisors schema",
            "description": "An explanation about the purpose of this instance.",
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
                        "title": "The first anyOf schema",
                        "description": "An explanation about the purpose of this instance.",
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
                                "title": "The supervisor_name schema",
                                "description": "An explanation about the purpose of this instance.",
                                "default": "",
                                "examples": [
                                    "담당자1"
                                ]
                            },
                            "supervisor_phone_number": {
                                "$id": "#/properties/supervisors/items/anyOf/0/properties/supervisor_phone_number",
                                "type": ["string", "null"],
                                "title": "The supervisor_phone_number schema",
                                "description": "An explanation about the purpose of this instance.",
                                "default": "",
                                "examples": [
                                    "담당자1 핸드폰번호"
                                ],
                                "pattern": "(02.{0}|^01.{1}|[0-9]{4})-([0-9]+)-([0-9]{4})"
                            },
                            "supervisor_email": {
                                "$id": "#/properties/supervisors/items/anyOf/0/properties/supervisor_email",
                                "type":["string", "null"],
                                "title": "The supervisor_email schema",
                                "description": "An explanation about the purpose of this instance.",
                                "default": "",
                                "examples": [
                                    "담당자1 이메일"
                                ]
                            },
                            "order": {
                                "$id": "#/properties/supervisors/items/anyOf/0/properties/order",
                                "type": "integer",
                                "title": "The order schema",
                                "description": "An explanation about the purpose of this instance.",
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
            "title": "The service_number schema",
            "description": "An explanation about the purpose of this instance.",
            "default": "",
            "examples": [
                "010-5338-7244"
            ],
            "pattern": "(02.{0}|^01.{1}|[0-9]{4})-([0-9]+)-([0-9]{4})"
        },
        "zip_code": {
            "$id": "#/properties/zip_code",
            "type": "string",
            "title": "The zip_code schema",
            "description": "An explanation about the purpose of this instance.",
            "default": "",
            "examples": [
                "우편번호"
            ]
        },
        "address": {
            "$id": "#/properties/address",
            "type": "string",
            "title": "The address schema",
            "description": "An explanation about the purpose of this instance.",
            "default": "",
            "examples": [
                "주소 (택배 수령지)"
            ]
        },
        "detail_address": {
            "$id": "#/properties/detail_address",
            "type": "string",
            "title": "The detail_address schema",
            "description": "An explanation about the purpose of this instance.",
            "default": "",
            "examples": [
                "상세주소 (택배 수령지)"
            ]
        },
        "buisness_hours": {
            "$id": "#/properties/buisness_hours",
            "type": "array",
            "title": "The buisness_hours schema",
            "description": "An explanation about the purpose of this instance.",
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
                        "title": "The first anyOf schema",
                        "description": "An explanation about the purpose of this instance.",
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
                                "title": "The start_time schema",
                                "description": "An explanation about the purpose of this instance.",
                                "default": "",
                                "examples": [
                                    "9:00:00"
                                ]
                            },
                            "end_time": {
                                "$id": "#/properties/buisness_hours/items/anyOf/0/properties/end_time",
                                "type": ["string", "null"],
                                "title": "The end_time schema",
                                "description": "An explanation about the purpose of this instance.",
                                "default": "",
                                "examples": [
                                    "6:00:00"
                                ]
                            },
                            "is_weekend": {
                                "$id": "#/properties/buisness_hours/items/anyOf/0/properties/is_weekend",
                                "type": "integer",
                                "title": "The is_weekend schema",
                                "description": "An explanation about the purpose of this instance.",
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
            "title": "The bank schema",
            "description": "An explanation about the purpose of this instance.",
            "default": "",
            "examples": [
                "정산은행"
            ]
        },
        "account_owner": {
            "$id": "#/properties/account_owner",
            "type": "string",
            "title": "The account_owner schema",
            "description": "An explanation about the purpose of this instance.",
            "default": "",
            "examples": [
                "계좌주"
            ]
        },
        "bank_account": {
            "$id": "#/properties/bank_account",
            "type": "string",
            "title": "The bank_account schema",
            "description": "An explanation about the purpose of this instance.",
            "default": "",
            "examples": [
                "계좌번호"
            ],
            "pattern": "^[0-9-]*$"
        },
        "shipping_information": {
            "$id": "#/properties/shipping_information",
            "type": "string",
            "title": "The shipping_information schema",
            "description": "An explanation about the purpose of this instance.",
            "default": "",
            "examples": [
                "배송정보"
            ]
        },
        "refund_information": {
            "$id": "#/properties/refund_information",
            "type": "string",
            "title": "The refund_information schema",
            "description": "An explanation about the purpose of this instance.",
            "default": "",
            "examples": [
                "교환 / 환불 정보"
            ]
        },
        "model_height": {
            "$id": "#/properties/model_height",
            "type": "integer",
            "title": "The model_height schema",
            "description": "An explanation about the purpose of this instance.",
            "default": 0,
            "examples": [
                177
            ]
        },
        "model_size_top": {
            "$id": "#/properties/model_size_top",
            "type": "integer",
            "title": "The model_size_top schema",
            "description": "An explanation about the purpose of this instance.",
            "default": 0,
            "examples": [
                50
            ]
        },
        "model_size_bottom": {
            "$id": "#/properties/model_size_bottom",
            "type": "integer",
            "title": "The model_size_bottom schema",
            "description": "An explanation about the purpose of this instance.",
            "default": 0,
            "examples": [
                30
            ]
        },
        "model_size_foot": {
            "$id": "#/properties/model_size_foot",
            "type": "integer",
            "title": "The model_size_foot schema",
            "description": "An explanation about the purpose of this instance.",
            "default": 0,
            "examples": [
                255
            ]
        },
        "feed_message": {
            "$id": "#/properties/feed_message",
            "type": ["string", "null"],
            "title": "The feed_message schema",
            "description": "An explanation about the purpose of this instance.",
            "default": "",
            "examples": [
                "안녕하세요 OOO에요! 봄에 어울리는 신상이 입고 되었습니다."
            ]
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
            "color_filter_id": 2,
            "first_category_id": 1,
            "second_category_id": 25,
            "is_displayed": 1,
            "is_onsale": 1,
            "name": "멋진 옷",
            "is_detail_reference": 1,
            "simple_description": "good",
            "details": "사세요",
            "maximum_quantity": 10,
            "price": 8000,
            "wholesale_price": 8000,
            "discount_rate": 0,
            "discount_start": "2018-05-31",
            "discount_end": "2019-04-10",
            "manufacturer": "브랜디",
            "manufacture_date": "1991-04-01 12:00:59",
            "origin": "한국",
            "tag_name": [
                "큐트",
                "러블리"
            ]
        }
    ],
    "required": [
        "first_category_id",
        "second_category_id",
        "is_displayed",
        "is_onsale",
        "name",
        "is_detail_reference",
        "details",
        "price",
        "discount_rate",
        "tag_name"
    ],
    "additionalProperties": True,
    "properties": {
        "color_filter_id": {
            "$id": "#/properties/color_filter_id",
            "type": "integer",
            "title": "The color_filter_id schema",
            "description": "An explanation about the purpose of this instance.",
            "default": 0,
            "examples": [
                2
            ]
        },
        "first_category_id": {
            "$id": "#/properties/first_category_id",
            "type": "integer",
            "title": "The first_category_id schema",
            "description": "An explanation about the purpose of this instance.",
            "default": 0,
            "examples": [
                1
            ]
        },
        "second_category_id": {
            "$id": "#/properties/second_category_id",
            "type": "integer",
            "title": "The second_category_id schema",
            "description": "An explanation about the purpose of this instance.",
            "default": 0,
            "examples": [
                25
            ]
        },
        "is_displayed": {
            "$id": "#/properties/is_displayed",
            "type": "integer",
            "title": "The is_displayed schema",
            "description": "An explanation about the purpose of this instance.",
            "default": 0,
            "examples": [
                1
            ]
        },
        "is_onsale": {
            "$id": "#/properties/is_onsale",
            "type": "integer",
            "title": "The is_onsale schema",
            "description": "An explanation about the purpose of this instance.",
            "default": 0,
            "examples": [
                1
            ]
        },
        "name": {
            "$id": "#/properties/name",
            "type": "string",
            "title": "The name schema",
            "description": "An explanation about the purpose of this instance.",
            "default": "",
            "examples": [
                "멋진 옷"
            ]
        },
        "is_detail_reference": {
            "$id": "#/properties/is_detail_reference",
            "type": "integer",
            "title": "The is_detail_reference schema",
            "description": "An explanation about the purpose of this instance.",
            "default": 0,
            "examples": [
                1
            ]
        },
        "simple_description": {
            "$id": "#/properties/simple_description",
            "type": "string",
            "title": "The simple_description schema",
            "description": "An explanation about the purpose of this instance.",
            "default": "",
            "examples": [
                "good"
            ]
        },
        "details": {
            "$id": "#/properties/details",
            "type": "string",
            "title": "The details schema",
            "description": "An explanation about the purpose of this instance.",
            "default": "",
            "examples": [
                "사세요"
            ]
        },
        "maximum_quantity": {
            "$id": "#/properties/maximum_quantity",
            "type": ["integer", "null"],
            "title": "The maximum_quantity schema",
            "description": "An explanation about the purpose of this instance.",
            "default": 0,
            "examples": [
                10
            ]
        },
        "minimum_quantity": {
            "$id": "#/properties/minimum_quantity",
            "type": ["integer", "null"],
            "title": "The minimum_quantity schema",
            "description": "An explanation about the purpose of this instance.",
            "default": 0,
            "examples": [
                10
            ]
        },
        "price": {
            "$id": "#/properties/price",
            "type": ["integer", "null"],
            "title": "The price schema",
            "description": "An explanation about the purpose of this instance.",
            "default": 0,
            "examples": [
                8000
            ]
        },
        "wholesale_price": {
            "$id": "#/properties/wholesale_price",
            "type": ["integer", "null"],
            "title": "The wholesale_price schema",
            "description": "An explanation about the purpose of this instance.",
            "default": 0,
            "examples": [
                8000
            ]
        },
        "discount_rate": {
            "$id": "#/properties/discount_rate",
            "type": "integer",
            "title": "The discount_rate schema",
            "description": "An explanation about the purpose of this instance.",
            "default": 0,
            "examples": [
                0
            ]
        },
        "discount_start": {
            "$id": "#/properties/discount_start",
            "type": ["string", "null"],
            "title": "The discount_start schema",
            "description": "An explanation about the purpose of this instance.",
            "default": "",
            "examples": [
                "2018-05-31"
            ]
        },
        "discount_end": {
            "$id": "#/properties/discount_end",
            "type": ["string", "null"],
            "title": "The discount_end schema",
            "description": "An explanation about the purpose of this instance.",
            "default": "",
            "examples": [
                "2019-04-10"
            ]
        },
        "manufacturer": {
            "$id": "#/properties/manufacturer",
            "type": ["string", "null"],
            "title": "The manufacturer schema",
            "description": "An explanation about the purpose of this instance.",
            "default": "",
            "examples": [
                "브랜디"
            ]
        },
        "manufacture_date": {
            "$id": "#/properties/manufacture_date",
            "type": ["string", "null"],
            "title": "The manufacture_date schema",
            "description": "An explanation about the purpose of this instance.",
            "default": "",
            "examples": [
                "1991-04-01 12:00:59"
            ]
        },
        "origin": {
            "$id": "#/properties/origin",
            "type": ["string", "null"],
            "title": "The origin schema",
            "description": "An explanation about the purpose of this instance.",
            "default": "",
            "examples": [
                "한국"
            ]
        },
        "tag_name": {
            "$id": "#/properties/tag_name",
            "type": "array",
            "title": "The tag_name schema",
            "description": "An explanation about the purpose of this instance.",
            "default": [],
            "examples": [
                [
                    "큐트",
                    "러블리"
                ]
            ],
            "additionalItems": True,
            "items": {
                "anyOf": [
                    {
                        "$id": "#/properties/tag_name/items/anyOf/0",
                        "type": "string",
                        "title": "The first anyOf schema",
                        "description": "An explanation about the purpose of this instance.",
                        "default": "",
                        "examples": [
                            "큐트",
                            "러블리"
                        ]
                    }
                ],
                "$id": "#/properties/tag_name/items"
            }
        }
    }
}

seller_action_schema = {
    "$schema": "http://json-schema.org/draft-07/schema",
    "$id": "http://example.com/example.json",
    "type": "object",
    "title": "The root schema",
    "description": "The root schema comprises the entire JSON document.",
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
            "title": "The user schema",
            "description": "An explanation about the purpose of this instance.",
            "default": 0,
            "examples": [
                9
            ]
        },
        "action_type": {
            "$id": "#/properties/action_type",
            "type": "string",
            "title": "The action_type schema",
            "description": "An explanation about the purpose of this instance.",
            "default": "",
            "examples": [
                "입점 승인"
            ]
        }
    }
}