<template>
  <tr class="fileBox">
    <th>
      <slot name="thName"></slot>
    </th>
    <td>이미지박스로고</td>
    <td>
      <label for="imgFile">이미지선택</label>
      <input type="file" id="imgFile" />
    </td>
    <td class="infoTd">
      <slot name="infoText01"></slot>
      <slot name="infoText02"></slot>
      <slot name="infoText03"></slot>
    </td>
  </tr>
</template>

<script>
export default {};
</script>

<style lang="scss" scoped>
label {
  border: 1px solid lightgray;
  font-size: 14px;
  font-weight: 400;
  line-height: 1.42857143;
  text-align: center;
  white-space: nowrap;
  padding: 8px 13px;
  border-radius: 3px;
  cursor: pointer;
  background-color: white;
}
input {
  display: none;
}
</style>