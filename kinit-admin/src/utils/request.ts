import axios from 'axios'

const request = axios.create({
  // baseURL: '/api', // 可根据实际情况配置
  timeout: 10000
})

// 请求拦截器
request.interceptors.request.use(
  (config) => {
    // 可在此处添加 token 等通用逻辑
    return config
  },
  (error) => {
    return Promise.reject(error)
  }
)

// 响应拦截器
request.interceptors.response.use(
  (response) => {
    return response.data
  },
  (error) => {
    return Promise.reject(error)
  }
)

export default request
