<template>
  <ContentWrap title="视频稿件管理">
    <Table
      ref="tableRef"
      :columns="columns"
      :data="list"
      :loading="loading"
      :pagination="pagination"
      @refresh="fetchList"
      @edit="handleEdit"
      @delete="handleDelete"
    />
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
import { ref, reactive, onMounted } from 'vue'
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

const list = ref([])
const loading = ref(false)
const pagination = reactive({ page: 1, pageSize: 10, total: 0 })
const columns = [
  { field: 'id', prop: 'id', label: 'ID', width: 60, show: true },
  { field: 'articleID', prop: 'articleID', label: '标题相似值', show: true },
  { field: 'sameid', prop: 'sameid', label: '正文相似值', show: true },
  { field: 'sameid3', prop: 'sameid3', label: '正文相似值3', show: true },
  { field: 'articletype', prop: 'articletype', label: '稿件类型', show: true },
  { field: 'title', prop: 'title', label: '稿件标题', show: true },
  { field: 'publishTime', prop: 'publishTime', label: '发布时间', show: true },
  { field: 'url', prop: 'url', label: '原网url', show: true },
  { field: 'dataSourceID', prop: 'dataSourceID', label: '数据源ID', show: true },
  { field: 'dataSourceName', prop: 'dataSourceName', label: '数据源名称', show: true },
  { field: 'mediaID', prop: 'mediaID', label: '媒体ID', show: true },
  { field: 'mediaName', prop: 'mediaName', label: '媒体名称', show: true },
  { field: 'keywords', prop: 'keywords', label: '关键词', show: true },
  { field: 'readcount', prop: 'readcount', label: '阅读量', show: true },
  { field: 'agreecount', prop: 'agreecount', label: '点赞量', show: true },
  { field: 'forwardcount', prop: 'forwardcount', label: '转发量', show: true },
  { field: 'commentcount', prop: 'commentcount', label: '评论量', show: true },
  { field: 'collectcount', prop: 'collectcount', label: '收藏量', show: true },
  { field: 'watchcount', prop: 'watchcount', label: '在看量', show: true },
  { field: 'degree', prop: 'degree', label: '热度', show: true },
  { field: 'video_article_id', prop: 'video_article_id', label: '视频关联id', show: true },
  { field: 'created_at', prop: 'created_at', label: '创建时间', show: true },
  { field: 'updated_at', prop: 'updated_at', label: '更新时间', show: true },
  { field: 'deleted_at', prop: 'deleted_at', label: '删除时间', show: true },
  { field: 'actions', prop: 'actions', label: '操作', slot: 'actions', width: 180, show: true }
]
const dialogVisible = ref(false)
const form = reactive({
  id: null,
  articleID: '',
  sameid: '',
  sameid3: '',
  articletype: '',
  title: '',
  publishTime: '',
  url: '',
  dataSourceID: '',
  dataSourceName: '',
  mediaID: '',
  mediaName: '',
  keywords: '',
  readcount: 0,
  agreecount: 0,
  forwardcount: 0,
  commentcount: 0,
  collectcount: 0,
  watchcount: 0,
  degree: 0,
  video_article_id: 0,
  created_at: '',
  updated_at: '',
  deleted_at: ''
})
const rules = {
  title: [{ required: true, message: '请输入标题' }],
  articletype: [{ required: true, message: '请输入稿件类型' }]
}
const formRef = ref()

function fetchList() {
  loading.value = true
  getArticles({ page: pagination.page, limit: pagination.pageSize })
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

onMounted(fetchList)
</script>
