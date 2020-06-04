<template>
  <div class="basicInfoContainer cmpWrap">
    <div class="basicInfoTitle cmpTitle">
      <i class="xi-user">상세 정보</i>
    </div>
    <div class="basicInfoTable cmpTable">
      <v-simple-table>
        <template v-slot:default>
          <tbody v-for="info in detailInfos" :key="info.name">
            <tr>
              <th>{{ info.header }}</th>
              <td v-for="(item, index) in info.value" :key="item.name">{{ info.value[index].text }}</td>
            </tr>
          </tbody>
        </template>
      </v-simple-table>
    </div>
  </div>
</template>


<script>
import { detailInfos } from "../../../config/SellerRegistDatas";
export default {
  data() {
    return {
      detailInfos: detailInfos
    };
  }
};
</script>
  <style lang="scss" scoped></style>;
