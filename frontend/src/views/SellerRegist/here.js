this.simple_introduction = this.infoDatas.simple_introduction;
this.detail_introduction = this.infoDatas.detail_introduction;
this.background_image = this.infoDatas.background_image;
this.site_url = this.infoDatas.site_url;
this.supervisors = [
  {
    supervisor_name: this.infoDatas.supervisors[0]
      ? this.infoDatas.supervisors[0].name
      : null,
    supervisor_phone_number: this.infoDatas.supervisors[0]
      ? this.infoDatas.supervisors[0].phone_number
      : null,
    supervisor_email: this.infoDatas.supervisors[0]
      ? this.infoDatas.supervisors[0].email
      : null,
    order: 1
  },
  {
    supervisor_name: this.infoDatas.supervisors[1]
      ? this.infoDatas.supervisors[1].name
      : null,
    supervisor_phone_number: this.infoDatas.supervisors[1]
      ? this.infoDatas.supervisors[1].phone_number
      : null,
    supervisor_email: this.infoDatas.supervisors[1]
      ? this.infoDatas.supervisors[1].email
      : null,
    order: 2
  },
  {
    supervisor_name: this.infoDatas.supervisors[2]
      ? this.infoDatas.supervisors[2].name
      : null,
    supervisor_phone_number: this.infoDatas.supervisors[2]
      ? this.infoDatas.supervisors[2].phone_number
      : null,
    supervisor_email: this.infoDatas.supervisors[2]
      ? this.infoDatas.supervisors[2].email
      : null,
    order: 3
  }
];
this.service_number = this.infoDatas.service_number;
this.zip_code = this.infoDatas.zip_code;
this.address = this.infoDatas.address;
this.detail_address = this.infoDatas.detail_address;
(this.buisness_hours = [
  {
    start_time: this.infoDatas.buisness_hours[0].start_time,
    end_time: this.infoDatas.buisness_hours[0].end_time,
    is_weekend: "0"
  },
  {
    start_time:
      this.infoDatas.buisness_hours.length == 1
        ? null
        : this.infoDatas.buisness_hours[1].start_time,
    end_time:
      this.infoDatas.buisness_hours.length == 1
        ? null
        : this.infoDatas.buisness_hours[1].end_time,
    is_weekend: "1"
  }
]),
  (this.bank = this.infoDatas.bank);
this.account_owner = this.infoDatas.account_owner;
this.bank_account = this.infoDatas.bank_account;
this.shipping_information = this.infoDatas.shipping_information;
this.refund_information = this.infoDatas.refund_information;
this.model_height = this.infoDatas.model_height;
this.model_size_top = this.infoDatas.model_size_top;
this.model_size_bottom = this.infoDatas.model_size_bottom;
this.model_size_foot = this.infoDatas.model_size_foot;
this.feed_message = this.infoDatas.feed_message;
this.tableCount = this.infoDatas.supervisors.length;
this.btnCount = this.infoDatas.supervisors.length;