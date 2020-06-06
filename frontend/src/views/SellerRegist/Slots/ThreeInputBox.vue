<template>
  <tr>
    <th>
      <slot name="thName"></slot>
    </th>
    <td class="threeInput">
      <input type="text" :value="value01" :placeholder="placeholder01" />
      <input type="text" :value="value02" :placeholder="placeholder02" />
      <input type="text" :value="value03" :placeholder="placeholder03" />
    </td>
  </tr>
</template>

<script>
export default {
  props: [
    "placeholder01",
    "placeholder02",
    "placeholder03",
    "value01",
    "value02",
    "value03"
  ]
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