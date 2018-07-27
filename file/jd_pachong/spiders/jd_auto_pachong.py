# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from scrapy.http import Request
from jd_pachong.items import JdPachongItem
import re
import urllib.request

class JdAutoPachongSpider(CrawlSpider):
    st = ''
    name = 'jd_auto_pachong'
    allowed_domains = ['jd.com']
    start_urls = ['https://www.jd.com/']
    aget = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'
    rules = (
        Rule(LinkExtractor(allow=''), callback='parse_item', follow=True),
    )

    opener = urllib.request.build_opener()
    opener.addheaders = [("User_Agent", aget)]
    urllib.request.install_opener(opener)

    def parse_item(self, response):
        i = JdPachongItem()
        url = response.url
        pat = r'https://item.jd.com/(\d*?).html'
        id = re.search(pat,url)
        # print(id)
        try:
                if id:
                    # print(i['id'])
                    company_data= response.xpath('//ul[@id="parameter-brand"]/li/a/text()').extract()
                    # print(data[0])
                    company_url ='https://question.jd.com/question/getQuestionAnswerList.action?callback=jQuery453308&page=1&productId='+id[1]
                    data = urllib.request.urlopen(company_url).read().decode('utf-8','ignore')
                    pat = r'"firstCategoryName":"(.*?)",'
                    id_soort_data = re.compile(pat).findall(data)
                    # print(data[0])
                    product_data = response.xpath('//div[@class="itemInfo-wrap"]/div[@class="sku-name"]/text()').extract()
                    # print(data[0].strip())
                    price_url = 'https://c0.3.cn/stock?skuId='+id[1]+'&area=1_72_2799_0&venderId=1000000127&cat=9987,653,655&buyNum=1&choseSuitSkuIds=&extraParam={%22originid%22:%221%22}&ch=1&fqsp=0&pduid=340805467&pdpin=&detailedAdd=null&callback=jQuery6785641'
                    # print(price_url)
                    price_data = urllib.request.urlopen(price_url).read().decode('utf-8','ignore')
                    # print(price_data)
                    pat = r'"p":"(.*?)"'
                    p_data = re.compile(pat).findall(price_data)
                    # print(data[0])
                    usr_product_url = 'https://club.jd.com/comment/productCommentSummaries.action?referenceIds='+id[1]+'7512626&callback=jQuery9578067&_=1532414307070'
                    # print(usr_product_url)
                    usr_product_data = urllib.request.urlopen(usr_product_url).read().decode('utf-8','ignore')
                    usr_product_pat = r'"GoodRateShow":(.*?),'
                    u_data = re.compile(usr_product_pat).findall(usr_product_data)
                    # print(data[0])
                    # data = response.xpath('//ul[@class="parameter2 p-parameter-list"]/li/text()').extract()
                    ex_data = response.xpath('//ul[@class="parameter2 p-parameter-list"]/li/text()').extract()

                    if ex_data and u_data and p_data and product_data and id_soort_data and id[1] and company_data:
                        if len(ex_data)==1:
                            i['expression'] = ex_data[0]
                        elif len(ex_data)==2:
                            i['expression'] = ex_data[0] + ex_data[1]
                        elif len(ex_data)==3:
                            i['expression'] = ex_data[0] + ex_data[1]+ ex_data[2]
                        elif len(ex_data)==4:
                            i['expression'] = ex_data[0] + ex_data[1]+ ex_data[2]+ ex_data[3]
                        else:
                            i['expression'] = ex_data[0] + ex_data[1]+ ex_data[2]+ ex_data[3]+ ex_data[4]
                        i['user_product'] = u_data[0]
                        i['price'] = p_data[0]
                        i['product'] = product_data[0].strip()
                        i['id_sort'] = id_soort_data[0]
                        i['company'] = company_data[0]
                        i['id'] = id[1]
                else:
                    pass
        except Exception:
            pass
        #i['domain_id'] = response.xpath('//input[@id="sid"]/@value').extract()
        #i['name'] = response.xpath('//div[@id="name"]').extract()
        #i['description'] = response.xpath('//div[@id="description"]').extract()
        return i
