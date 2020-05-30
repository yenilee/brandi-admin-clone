<template>
  <div class="main-container">
    <v-navigation-drawer
      v-model="drawer"
      clipped
      app
      dark
      style="width: 256px; height: unset;border:1px solid red; position:unset; max-height: unset; top:unset"
    >
      <v-list dense>
        <v-container></v-container>

        <template v-for="item in items">
          <v-list-group
            v-if="item.children"
            :key="item.text"
            v-model="item.model"
            prepend-icon
            :append-icon="item.icon"
          >
            <!-- More 버튼 생성 -->
            <template v-slot:activator>
              <v-list-item-content>
                <v-list-item-title style="font-weight: 300;">{{item.text}}</v-list-item-title>
              </v-list-item-content>
            </template>

            <!-- 아래 목록 버튼 생성 -->
            <v-list-item
              v-for="(child, i) in item.children"
              :key="i"
              @click="detailPage(item.children[i].path)"
              link
            >
              <v-list-item-title style="padding-left : 15px; font-weight: 300;">{{child.text}}</v-list-item-title>
            </v-list-item>
          </v-list-group>
        </template>
      </v-list>
    </v-navigation-drawer>
    <div :class="mainPageLayout">
      <slot></slot>
    </div>
  </div>
</template>

<script>
import { items } from "../config/Itmes";
export default {
  data() {
    return {
      drawer: true,
      items: items,
      right: false,
      miniVariant: false
    };
  },
  computed: {
    mainPageLayout() {
      return this.drawer ? "about" : "non";
    }
  },
  methods: {
    detailPage(path) {
      this.$router.push(`/main/${path}`);
    }
  }
};
</script>

<style lang="scss">
.main-container {
  height: 100%;
  padding-top: 45px;
  display: flex !important;
  .about {
    width: 100%;
    height: 1000px;
    transition: all 0.3s ease-in-out;
    color: black;
    background: white;
  }
  .non {
    height: calc(100vh - 48px);
    width: 100%;
    margin-top: 48px;
    margin-left: 0;
    color: black;
    background: white;
  }
  .v-icon {
    font-size: 18px;
    color: gray;
    transform: rotate(-90deg);
  }
}
</style>
