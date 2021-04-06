// 封装axios实例
import axios from 'axios';

const service = axios.create({
  baseURL: 'http://10.6.101.12:7072', // 请求本地json文件，那么baseURL取空字符串，域名就会是项目域名
  timeout: 30000,
});

// 添加请求拦截器
service.interceptors.request.use(config => {
  // 对发送的请求进行相关的操作
  return config
}, error => {
  // 出错时的操作
  console.log(error);
})

// 添加响应拦截器
service.interceptors.response.use(response => {
  // 对服务器的相应结果的操作
  return response.data
}, error => {
  // 出错时的操作
  console.log(error);
})

export default service;