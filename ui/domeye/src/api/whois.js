import $network from '@/network/networkWhois';

  export const getWhoisApi = (ip_address) => {
    return $network({
      url: `/whois`, // json文件地址
      method: 'POST',
      data: {ip_address},
    });
  };