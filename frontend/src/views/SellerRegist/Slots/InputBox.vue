<template>
  <tr>
    <th>
      <slot name="thName"></slot>
    </th>
    <td>
      <input
        type="text"
        :value="value"
        @input="$emit('input',$event.target.value)"
        :placeholder="placeholder"
      />
    </td>
    <td class="infoTd">
      <slot name="infoText01"></slot>
    </td>
  </tr>
</template>

<script>
export default {
  props: {
    placeholder: {
      type: String
    },
    value: {
      type: String
    }
  },

  methods: {}
};
</script>

<style lang="scss">
</style>