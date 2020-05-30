<template>
  <div>
    <Header />
    <Layout>
      <router-view></router-view>
    </Layout>
    <MainFooter />
  </div>
</template>

<script>
import Header from "../components/Header";
import Layout from "../components/Layout";
import MainFooter from "../components/MainFooter";
export default {
  components: {
    Header,
    Layout,
    MainFooter
  }
};
</script>

<style lang="scss">
</style>
