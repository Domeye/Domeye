import $network from '@/network/networktry'; // 引入封装的axios实例

// 获取本地json数据
export const getWorldJsonDataApi = () => {
  return $network({
    url: `../static/data/countrytolat.json`, // json文件地址
    method: 'GET',
  });
};
