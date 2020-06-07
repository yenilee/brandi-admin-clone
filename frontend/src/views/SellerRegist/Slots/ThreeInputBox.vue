<template>
  <tr>
    <th>
      <slot name="thName"></slot>
    </th>
    <!-- 1번째 담당자 정보 -->
    <td class="threeInput" v-if="supervisors.length > 0">
      <input type="text" v-model="name01" :placeholder="placeholder01" />
      <input type="text" :value="supervisors[0].phone_number" :placeholder="placeholder02" />
      <input type="text" :value="supervisors[0].email" :placeholder="placeholder03" />
    </td>
    <!-- 2번째 담당자 정보 -->
    <td class="threeInput" v-if="supervisors.length > 1">
      <input type="text" :value="supervisors[1].name" :placeholder="placeholder01" />
      <input type="text" :value="supervisors[1].phone_number" :placeholder="placeholder02" />
      <input type="text" :value="supervisors[1].email" :placeholder="placeholder03" />
    </td>
    <!-- 3번째 담당자 정보 -->
    <td class="threeInput" v-if="supervisors.length > 2">
      <input type="text" :value="supervisors[2].name" :placeholder="placeholder01" />
      <input type="text" :value="supervisors[2].phone_number" :placeholder="placeholder02" />
      <input type="text" :value="supervisors[2].email" :placeholder="placeholder03" />
    </td>
  </tr>
</template>

<script>
export default {
  props: [
    "supervisors",
    "placeholder01",
    "placeholder02",
    "placeholder03",
    "value01_name",
    "value01_phone",
    "value01_email",
    "value02_name",
    "value02_phone",
    "value02_email",
    "value03_name",
    "value03_phone",
    "value03_email"
  ],
  data() {
    return {
      clickCount: 0,
      name01: this.supervisors[0].name,
      phon
    };
  }
};
</script>

<style lang="scss" scoped>
.threeInput {
  display: flex;
  flex-direction: column;
  input {
    margin-bottom: 20px;
  }
}
</style>