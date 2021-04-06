import $network from '@/network/networkSearch';

// ip_address为我传过去的。。
export const getRelatedASApi = (ip_address) => {
  return $network({
    url: `/related_as`, // json文件地址
    method: 'POST',
    data: {ip_address},
  });
};

export const getAllPrefixApi = (ip_address) => {
    return $network({
      url: `/all_prefix`, // json文件地址
      method: 'POST',  // 提交数据
      data: {ip_address},
    });
  };

  export const getLongestASPrefixApi = (ip_address) => {
    return $network({
      url: `/longest_as_prefix`, // json文件地址
      method: 'POST',
      data: {ip_address},
    });
  };

  export const getRelationGraphApi = (ip_address) => {
    return $network({
      url: `/relation_graph`, // json文件地址
      method: 'POST',
      data: {ip_address},
    });
  };