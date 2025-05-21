<template>
  <ContentWrap title="抖音榜">
    <Search :schema="searchSchema" @search="setSearchParams" @reset="setSearchParams" />
    <Table
      :columns="columns"
      :data="list"
      :loading="loading"
      :pagination="pagination"
      v-model:currentPage="pagination.page"
      v-model:pageSize="pagination.pageSize"
      @refresh="fetchList"
    >
      <template #title="{ row }">
        <el-tooltip placement="top" :content="row.title">
          <span class="rank-title">{{ row.title }}</span>
        </el-tooltip>
      </template>
      <template #douyin_score="{ row }">
        <el-popover placement="right" width="300" trigger="hover">
          <template #reference>
            <span class="rank-score">{{ row.douyin_score }}</span>
            <el-icon style="margin-left: 4px"><i class="el-icon-info"></i></el-icon>
          </template>
          <div>
            <div>发布时间：{{ row.publishTime }}</div>
            <div>稿件ID：{{ row.articleID }}</div>
            <div>
              指数得分：{{ row.douyin_score }}<br />
              = 点赞数 {{ row.agreecount }} × 50 + 评论数 {{ row.commentcount }} × 20 + 转发数
              {{ row.forwardcount }} × 20
            </div>
          </div>
        </el-popover>
      </template>
    </Table>
    <div class="rank-desc">
      当前榜单指数规则：指数得分 = 点赞数 × 50 + 评论数 × 20 + 转发数 × 20
    </div>
  </ContentWrap>
</template>

<script setup lang="tsx">
import { ref, reactive, onMounted, watch } from 'vue'
import { ContentWrap } from '@/components/ContentWrap'
import { Table } from '@/components/Table'
import { Search } from '@/components/Search'
import { ElMessage } from 'element-plus'
import { getDouyinRank } from '@/api/vadmin/video/rank'
import type { FormSchema } from '@/components/Form'

const list = ref([])
const loading = ref(false)
const pagination = reactive({ page: 1, pageSize: 10, total: 0 })
const searchSchema: FormSchema[] = [
  {
    field: 'title',
    label: '标题',
    component: 'Input',
    componentProps: { clearable: true, style: { width: '200px' } }
  },
  {
    field: 'publishTimeRange',
    label: '发布时间',
    component: 'DatePicker',
    componentProps: {
      type: 'datetimerange',
      valueFormat: 'YYYY-MM-DD HH:mm:ss',
      startPlaceholder: '开始时间',
      endPlaceholder: '结束时间',
      style: { width: '320px' },
      clearable: true
    }
  }
]
const searchParams = ref({})
const setSearchParams = (data: any) => {
  pagination.page = 1
  searchParams.value = data
  fetchList()
}

const columns = [
  {
    field: 'rank',
    label: '排名',
    width: 80,
    show: true,
    formatter: (_: any, __: any, idx: number) => idx + 1
  },
  {
    field: 'title',
    label: '标题',
    show: true,
    slot: 'title',
    minWidth: 200
  },
  {
    field: 'mediaName',
    label: '部门',
    show: true
  },
  {
    field: 'dataSourceName',
    label: '作者',
    show: true
  },
  {
    field: 'douyin_score',
    label: '指数得分',
    show: true,
    slot: 'douyin_score',
    minWidth: 120
  }
]

function fetchList() {
  loading.value = true
  let params: any = { ...searchParams.value }
  if (params.publishTimeRange && params.publishTimeRange.length === 2) {
    params.start = params.publishTimeRange[0]
    params.end = params.publishTimeRange[1]
  }
  delete params.publishTimeRange
  getDouyinRank({
    page: pagination.page,
    limit: pagination.pageSize,
    ...params
  })
    .then((res) => {
      if (res && res.code === 200) {
        list.value = res.data || []
        pagination.total = res.count || res.total || 0
      } else {
        ElMessage.error('获取榜单失败')
      }
    })
    .catch(() => {
      ElMessage.error('接口异常')
    })
    .finally(() => (loading.value = false))
}

onMounted(fetchList)
watch(
  () => [pagination.page, pagination.pageSize],
  () => {
    fetchList()
  }
)
</script>

<style scoped>
.rank-title {
  font-weight: 500;
  color: #222;
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
  max-width: 350px;
}
.rank-score {
  font-size: 18px;
  font-weight: bold;
  color: #1976d2;
}
.rank-desc {
  margin-top: 24px;
  color: #888;
  font-size: 15px;
  text-align: right;
}
</style>
