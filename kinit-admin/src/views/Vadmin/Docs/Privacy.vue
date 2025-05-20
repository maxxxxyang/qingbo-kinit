<script setup lang="ts">
import { ref } from 'vue'
import { getSystemPrivacyApi } from '@/api/vadmin/system/settings'

const content = ref(null)

// 获取隐私协议内容
const getSystemConfig = async () => {
  const res = await getSystemPrivacyApi()
  if (res) {
    content.value = res.data
  }
}

getSystemConfig()
</script>

<template>
  <div class="content-view" v-html="content"></div>
</template>

<style scoped lang="less">
.content-view {
  height: 100%;
  padding: 20px;
  overflow: hidden scroll;
}
</style>
