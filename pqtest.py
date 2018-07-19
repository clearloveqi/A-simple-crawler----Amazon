from pyquery import PyQuery as pq
import random


def get_url(url):
    header = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Accept-Encoding': 'gzip, deflate, sdch',
        'Accept-Language': 'zh-CN,zh;q=0.8',
        'Connection': 'keep-alive',
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.235'
    }
    timeout = random.choice(range(40, 80))
    urls = pq(url, headers=header, timeout=timeout)
    return urls


def get_amazon(urls):
    # get_li = []                         items将其转化为生成器
    uls = urls('.s-result-item.celwidget').items()   # 得到ul 's-result-item  celwidget' 有空格就多加一个点
    for li in uls:
        data_asin = li.attr('data-asin')   # 获取属性
        get_title = li.find('h2').text()   # 获取标题
        get_price = li('.sx-price-whole').text()  # 获取价格
        get_star = li('.a-icon-alt').text()  # 获取星级
        get_img = li('img').attr('src')
        print("{},  {}, ${} ,  {} ,{}\n".format(data_asin, get_title, get_price, get_star, get_img))
        # get_li.append('{},  {}, ${} ,  {}'.format(data_asin, get_title, get_price, get_star))
    # return get_li


if __name__ == "__main__":
    test = get_url('https://www.amazon.com/s/browse/ref=br_msw_pdt-2?_encoding=UTF8&node=17897065011&smid=ATVPD \
                KIKX0DER&pf_rd_m=ATVPDKIKX0DER&pf_rd_s=&pf_rd_r=VHMNX4N58AHVFXC09BJP&pf_rd_t=36701&pf_rd_p=ce \
                3b7bd8-d6cf-446b-94e5-6d1e99478794&pf_rd_i=desktop')
    get_amazon(test)
