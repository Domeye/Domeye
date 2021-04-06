import axios from 'axios'

export default function request(config) {
    const instance = axios.create({
      //baseURL: 'http://api.ipv6rank.com:7077/',
      baseURL: 'http://10.99.8.12:7077/',
      //baseURL: 'http://[2001:da8:215:9fa1::112]:7077/',
      timeout: 500000,
    })
  
    instance.interceptors.request.use(config => {
      return config
    }, error => {
      console.log(error);
    })
  
    instance.interceptors.response.use(response => {
      return response.data
    }, error => {
      console.log(error);
    })
  
    return instance(config)
  }
  