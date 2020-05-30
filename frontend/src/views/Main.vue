<template>
  <div>
    <Header />
    <Layout>
      <router-view></router-view>
    </Layout>
  </div>
</template>

<script>
import Header from "../components/Header";
import Layout from "../components/Layout";
export default {
  components: {
    Header,
    Layout
  }
};
</script>

<style lang="scss">
div {
}
</style>
