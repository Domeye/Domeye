import $network from '@/network/networkPicture';

  export const getPictureApi = (ip_address) => {
    return $network({
      url: `/picture`, // json文件地址
      method: 'POST',
      data: {ip_address},
    });
  };