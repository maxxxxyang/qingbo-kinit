import request from '@/config/axios'

export function getDouyinRank(params: any) {
  return request.get({ url: '/vadmin/video/rank/douyin', params })
}
