import request from '@/config/axios'

export function getArticles(params: any) {
  return request.get({ url: '/vadmin/video/article', params })
}

export function createArticle(data: any) {
  return request.post({ url: '/vadmin/video/article', data })
}

export function updateArticle(data: any) {
  return request.put({ url: `/vadmin/video/article/${data.id}`, data })
}

export function deleteArticle(id: number) {
  return request.delete({ url: `/vadmin/video/article/${id}` })
}
