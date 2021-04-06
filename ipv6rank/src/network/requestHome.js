import request from "./request";
import requestWeb from "./requestWeb";
import requestPos3 from "./requestPos3";
export function requestBasic(IP) {
  return request({
    method: 'post',
    url: 'longest_as_prefix',
    data:{
      ip_address: IP
    }
  })
}
export function requestAddress(IP) {
  return request({
    method: 'post',
    url: 'as_prefix_all',
    data: {
      ip_address: IP
    }
  })
}

export function requestRoute6(IP) {
  return request({
    method: 'post',
    url: 'longest_route6_prefix',
    data:{
      ip_address: IP
    }
  })
}

export function requestInet6(IP) {
  return request({
    method: 'post',
    url: 'longest_inet6_prefix',
    data:{
      ip_address: IP
    }
  })
}

export function reqeustWhoIs(IP) {
  return request({
    method: 'post',
    url: 'whois',
    data:{
      ip_address: IP
    }
  })
}
export function requestWebSite(IP) {
  return requestWeb({
    method:'post',
    url:'domain',
    data:{
      ip_address:IP
    }
  })
}
export function requestPos3Data(IP) {
  return requestPos3({
    method:'post',
    url:'picture',
    data:{
      ip_address:IP
    }
  })
}

export function requestMapData(IP) {
  return request({
    method:'post',
    url:'location',
    data:{
      ip_address:IP
    }
  })
}
