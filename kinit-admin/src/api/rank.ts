import request from '@/utils/request'

export function getDouyinRank(params: any) {
  return request.get('/vadmin/video/rank/douyin', { params })
}
 