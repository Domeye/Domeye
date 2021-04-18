import axios from 'axios'

export default function request(config) {
    const instance = axios.create({
      baseURL: 'http://10.99.8.12:7078/',
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
  