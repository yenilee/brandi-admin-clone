<template>
  <div class="main-container">
    <v-navigation-drawer
      clipped
      app
      dark
      style="width: 256px; height: unset; position:unset; max-height: unset; top:unset"
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
                <v-list-item-title style="font-size: 14px;font-weight: 400;">{{item.text}}</v-list-item-title>
              </v-list-item-content>
            </template>

            <!-- 아래 목록 버튼 생성 -->
            <v-list-item
              v-for="(child, i) in item.children"
              :key="i"
              @click="detailPage(item.children[i].path)"
              link
            >
              <v-list-item-title
                style="padding-left : 14px;font-size: 14px;font-weight: 400;"
              >{{child.text}}</v-list-item-title>
            </v-list-item>
          </v-list-group>
        </template>
      </v-list>
    </v-navigation-drawer>
    <!-- 보여지는 페이지 공간 -->
    <div class="about">
      <slot></slot>
    </div>
  </div>
</template>

<script>
import { items } from "../config/Items";

export default {
  data() {
    return {
      items: items
    };
  },
  methods: {
    detailPage(path) {
      this.$router.push(`/main/${path}`);
    }
  }
};
</script>

<style lang="scss" scoped>
.main-container {
  height: 100%;
  padding-top: 45px;
  display: flex;
  .about {
    min-height: 100vh !important;
    width: calc(100vw - 256px);
    color: black;
    background: white;
    .container {
      width: unset !important;
      overflow: hidden;
      margin: 0 0 50px 0 !important;
      max-width: unset;
    }
  }

  .v-icon {
    font-size: 18px;
    color: gray;
    transform: rotate(-90deg);
  }
}
</style>
