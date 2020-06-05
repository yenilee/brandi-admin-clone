<template>
  <tr class="textAreaBox">
    <th>
      <slot name="thName"></slot>
    </th>
    <td>
      <textarea :value="value" :placeholder="placeholder"></textarea>
    </td>
    <td class="infoTd">
      <slot name="infoText01"></slot>
    </td>
  </tr>
</template>

<script>
export default {
  props: ["placeholder", "value"]
};
</script>

<style lang="scss">
</style>