import axios from 'axios'

export default function request(config) {
  const instance = axios.create({
    baseURL: 'http://10.6.101.12:7078/',
    //baseURL: 'http://[2001:da8:215:9fa1::112]:7071/',
    // baseURL: 'http://api.ipv6rank.com:7071/',
    timeout: 5000,
  })

  instance.interceptors.request.use(config => {
    // 对发送的请求进行相关的操作
    return config
  }, error => {
    // 出错时的操作
    console.log(error);
  })

  instance.interceptors.response.use(response => {
    // 对服务器的相应结果的操作
    return response.data
  }, error => {
    // 出错时的操作
    console.log(error);
  })

  return instance(config)
}
