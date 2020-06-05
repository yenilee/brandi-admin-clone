<template>
  <tr>
    <th>
      <slot name="thName"></slot>
    </th>
    <td>
      <input type="text" :value="value" :placeholder="placeholder" />
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