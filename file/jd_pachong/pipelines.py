# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql

class JdPachongPipeline(object):
    def process_item(self, item, spider):
        try:
            conn = pymysql.connect(host='localhost', port=9500, user='admin', passwd='123456', db='jd_data', charset='utf8')
            sql = "insert into jd_information(id,company,id_sort,product,price,user_product,expression) values("+"'" + item['id']+"'"+','+"'"+ item['company']+"'"+','+"'"+item['id_sort']+"'"+','+"'"+ item['product']+"'"+','+"'"+ item['price']+"'"+','+"'"+ item['user_product']+"'"+','+"'"+ item['expression']+"'"+")"
            conn.query(sql)
            print(item['id'], item['company'], item['id_sort'], item['product'], item['price'], item['user_product'], item['expression'])
            print('---------------------------------------------------------------')
            conn.commit()
            conn.close()
        except Exception:
             pass
        return item

