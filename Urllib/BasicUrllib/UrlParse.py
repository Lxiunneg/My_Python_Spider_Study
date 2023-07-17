from urllib.parse import unquote

url = 'https://www.baidu.com/s?wd=%E9%82%93%E4%BC%A6%E8%A2%AB%E7%94%B3%E8%AF%B7%E5%BC%BA%E5%88%B6%E6%89%A7%E8%A1%8C&rsv_spt=1&rsv_iqid=0xae0aab3f000648d6&issp=1&f=3&rsv_bp=1&rsv_idx=2&ie=utf-8&tn=44004473_8_oem_dg&rsv_enter=1&rsv_dl=ts_1&rsv_sug3=1&rsv_sug1=1&rsv_sug7=100&rsv_sug2=1&rsv_btype=i&prefixsug=d&rsp=1&inputT=1334&rsv_sug4=1335'
print(unquote(url))