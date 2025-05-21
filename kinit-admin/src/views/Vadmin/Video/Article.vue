<template>
  <ContentWrap title="第三方稿件管理">
    <Search :schema="searchSchema" @search="setSearchParams" @reset="setSearchParams" />
    <Table
      ref="tableRef"
      :columns="columns"
      :data="list"
      :loading="loading"
      :pagination="pagination"
      v-model:currentPage="pagination.page"
      v-model:pageSize="pagination.pageSize"
      @refresh="fetchList"
      @edit="handleEdit"
      @delete="handleDelete"
      @sort-change="handleSortChange"
    >
      <template #title="{ row }">
        <a :href="row.url" target="_blank" rel="noopener noreferrer">{{ row.title }}</a>
      </template>
      <template #publishTime="{ row }">
        {{ row.publishTime ? dayjs(row.publishTime).format('YYYY-MM-DD HH:mm:ss') : '' }}
      </template>
    </Table>
    <Dialog v-model:visible="dialogVisible" title="编辑稿件" @ok="handleSave">
      <Form :model="form" :rules="rules" ref="formRef">
        <el-form-item label="稿件标题" prop="title">
          <el-input v-model="form.title" />
        </el-form-item>
        <el-form-item label="稿件类型" prop="articletype">
          <el-input v-model="form.articletype" />
        </el-form-item>
        <el-form-item label="发布时间" prop="publishTime">
          <el-input v-model="form.publishTime" />
        </el-form-item>
        <el-form-item label="原网url" prop="url">
          <el-input v-model="form.url" />
        </el-form-item>
        <!-- 可根据实际表结构补充更多字段 -->
      </Form>
    </Dialog>
  </ContentWrap>
</template>

<script setup lang="ts">
import { ref, reactive, onMounted, watch } from 'vue'
import { ContentWrap } from '@/components/ContentWrap'
import { Table } from '@/components/Table'
import { Dialog } from '@/components/Dialog'
import { Form } from '@/components/Form'
import { ElFormItem, ElInput } from 'element-plus'
import {
  getArticles,
  createArticle,
  updateArticle,
  deleteArticle
} from '@/api/vadmin/video/article'
import dayjs from 'dayjs'
import { Search } from '@/components/Search'
import { FormSchema } from '@/components/Form'

const list = ref([])
const loading = ref(false)
const pagination = reactive({ page: 1, pageSize: 10, total: 0 })
const columns = [
  { field: 'id', prop: 'id', label: '编号', width: 100, show: true },
  { field: 'articletype', prop: 'articletype', label: '稿件类型', show: true, width: 140 },
  { field: 'title', prop: 'title', label: '稿件标题', show: true, slot: 'title', width: 240 },
  { field: 'dataSourceName', prop: 'dataSourceName', label: '数据源名称', show: true },
  {
    field: 'readcount',
    prop: 'readcount',
    label: '阅读量',
    show: true,
    width: 80,
    sortable: 'custom'
  },
  {
    field: 'agreecount',
    prop: 'agreecount',
    label: '点赞量',
    show: true,
    width: 80,
    sortable: 'custom'
  },
  {
    field: 'forwardcount',
    prop: 'forwardcount',
    label: '转发量',
    show: true,
    width: 80,
    sortable: 'custom'
  },
  {
    field: 'commentcount',
    prop: 'commentcount',
    label: '评论量',
    show: true,
    width: 80,
    sortable: 'custom'
  },
  {
    field: 'collectcount',
    prop: 'collectcount',
    label: '收藏量',
    show: true,
    width: 80,
    sortable: 'custom'
  },
  {
    field: 'watchcount',
    prop: 'watchcount',
    label: '在看量',
    show: true,
    width: 80,
    sortable: 'custom'
  },
  { field: 'degree', prop: 'degree', label: '热度', show: true, width: 80, sortable: 'custom' },
  {
    field: 'publishTime',
    prop: 'publishTime',
    label: '发布时间',
    show: true,
    slot: 'publishTime',
    sortable: 'custom'
  },
  { field: 'actions', prop: 'actions', label: '操作', slot: 'actions', width: 180, show: true }
]
const dialogVisible = ref(false)
const form = reactive({
  id: null,
  articletype: '',
  title: '',
  publishTime: '',
  url: '',
  dataSourceName: '',
  readcount: 0,
  agreecount: 0,
  forwardcount: 0,
  commentcount: 0,
  collectcount: 0,
  watchcount: 0,
  degree: 0
})
const rules = {
  title: [{ required: true, message: '请输入标题' }],
  articletype: [{ required: true, message: '请输入稿件类型' }]
}
const formRef = ref()
const sortParams = reactive({ field: '', order: '' })
const searchSchema = reactive<FormSchema[]>([
  {
    field: 'articletype',
    label: '稿件类型',
    component: 'Select',
    componentProps: {
      clearable: true,
      style: { width: '180px' },
      options: [
        { label: '微信', value: '微信' },
        { label: '微博', value: '微博' },
        { label: '第三方平台入驻媒体号', value: '第三方平台入驻媒体号' }
      ]
    }
  },
  {
    field: 'title',
    label: '标题',
    component: 'Input',
    componentProps: {
      clearable: true,
      style: { width: '200px' }
    }
  }
])

const searchParams = ref({})
const setSearchParams = (data: any) => {
  pagination.page = 1
  searchParams.value = data
  fetchList()
}

function fetchList() {
  loading.value = true
  getArticles({
    page: pagination.page,
    limit: pagination.pageSize,
    v_order_field: sortParams.field,
    v_order: sortParams.order,
    ...searchParams.value
  })
    .then((res) => {
      list.value = res.data
      pagination.total = res.count || res.total || 0
    })
    .finally(() => (loading.value = false))
}

function handleEdit(row: any) {
  Object.assign(form, row)
  dialogVisible.value = true
}

function handleDelete(row: any) {
  deleteArticle(row.id).then(fetchList)
}

function handleSave() {
  formRef.value.validate((valid: boolean) => {
    if (!valid) return
    const api = form.id ? updateArticle : createArticle
    api(form).then(() => {
      dialogVisible.value = false
      fetchList()
    })
  })
}

function handleSortChange({ prop, order }) {
  // 只处理量化数据字段
  sortParams.field = prop
  sortParams.order = order === 'descending' ? 'desc' : order === 'ascending' ? 'asc' : ''
  pagination.page = 1
  fetchList()
}

watch(
  () => [pagination.page, pagination.pageSize],
  () => {
    fetchList()
  }
)

onMounted(fetchList)
</script>
