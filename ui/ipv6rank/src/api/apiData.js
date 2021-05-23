import requestLabelData from "@/network/requestLabelData";
import requestAsinfo from "@/network/requestAsinfo";


export const getasinfo = (search) => {
	return requestAsinfo({
		method: 'post',
		url: 'asinfo',
		data: {
			input_search: search,
		}
	})
}

export const getjudgeResult = (search) => {
	return requestLabelData({
		method: 'post',
		url: '',
		data: {
			input_search: search,
		}
	})
}

export const getmapDot = (search) => {
	return requestLabelData({
		method: 'post',
		url: 'geo_position',
		data: {
			input_search: search,
		}
	})
}

export const getlongestAsPrefix = (search) => {
  return requestLabelData({
		method: 'post',
		url: 'longest_as_prefix',
		data: {
			input_search: search,
		}
	}) 
}

export const getlongestInet6Prefix = (search) => {
  return requestLabelData({
		method: 'post',
		url: 'longest_inet6_prefix',
		data: {
			input_search: search,
		}
	}) 
}

export const getpathGraph = (search) => {
  return requestLabelData({
		method: 'post',
		url: 'path_graph',
		data: {
			input_search: search,
		}
	}) 
}

export const get3Picture = (search) => {
  return requestLabelData({
		method: 'post',
		url: 'three_picture',
		data: {
			input_search: search,
		}
	}) 
}

export const getrelationGraph = (search) => {
  return requestLabelData({
		method: 'post',
		url: 'relation_graph',
		data: {
			input_search: search,
		}
	}) 
}

export const getWhois = (search) => {
  return requestLabelData({
		method: 'post',
		url: 'whois',
		data: {
			input_search: search,
		}
	}) 
}

export const getwebDomain = (search) => {
  return requestLabelData({
		method: 'post',
		url: 'website_domain',
		data: {
			input_search: search,
		}
	}) 
}