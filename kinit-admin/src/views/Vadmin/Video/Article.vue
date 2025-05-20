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
        <el-form-item label="标题" prop="title">
          <el-input v-model="form.title" />
        </el-form-item>
        <el-form-item label="作者" prop="author">
          <el-input v-model="form.author" />
        </el-form-item>
        <el-form-item label="稿件状态" prop="status">
          <el-select v-model="form.status">
            <el-option value="draft" label="草稿" />
            <el-option value="published" label="已发布" />
          </el-select>
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
import { ElFormItem, ElInput, ElSelect, ElOption } from 'element-plus'
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
  { field: 'title', prop: 'title', label: '标题', show: true },
  { field: 'url', prop: 'url', label: '稿件URL', show: true },
  { field: 'created_at', prop: 'created_at', label: '创建时间', show: true },
  { field: 'actions', prop: 'actions', label: '操作', slot: 'actions', width: 180, show: true }
]
const dialogVisible = ref(false)
const form = reactive({ id: null, title: '', author: '', status: 'draft' })
const rules = {
  title: [{ required: true, message: '请输入标题' }],
  author: [{ required: true, message: '请输入作者' }]
}
const formRef = ref()

function fetchList() {
  loading.value = true
  getArticles({ page: pagination.page, pageSize: pagination.pageSize })
    .then((res) => {
      list.value = res.data
      pagination.total = res.total
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
