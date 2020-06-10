<template>
  <div class="container">
    <div class="box">
      <router-view @keyChange="keyChange" :keyId="keyId"></router-view>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      keyId: null
    };
  },
  methods: {
    keyChange: function(id) {
      this.keyId = id;
    }
  }
};
</script>