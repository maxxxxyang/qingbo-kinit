import request from '@/utils/request'

export function getArticles(params: any) {
  return request.get('/video/articles', { params })
}

export function createArticle(data: any) {
  return request.post('/video/articles', data)
}

export function updateArticle(data: any) {
  return request.put(`/video/articles/${data.id}`, data)
}

export function deleteArticle(id: number) {
  return request.delete(`/video/articles/${id}`)
}
