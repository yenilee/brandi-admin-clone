<template >
  <div>
    <div class="cmpWrap" v-for="(info) in infos" :key="info.name">
      <div class="cmpTitle">
        <i class="xi-user">{{info.infoTitle}}</i>
      </div>
      <div class="cmpTable">
        <v-simple-table>
          <template v-slot:default>
            <tbody v-for="(content) in info.infoContent" :key="content.name">
              <tr>
                <th>{{ content.header }}</th>
                <td v-for="item in content.value" :key="item.name">{{ item.text }}</td>
              </tr>
            </tbody>
          </template>
        </v-simple-table>
      </div>
    </div>
  </div>
</template>


<script>
import { infos } from "../../../config/SellerRegistDatas";
export default {
  data() {
    return {
      infos: infos
    };
  }
};
</script>
  <style lang="scss" scoped></style>;
