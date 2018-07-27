import pymysql
def process_item():
    # try:
    item ={}
    item['expression'] = 'b'
    item['user_product'] ='b'
    item['price'] = 'b'
    item['product'] ='b'
    item['id_sort'] = 'b'
    item['company'] = 'b'
    item['id'] = '2000'
    conn = pymysql.connect(host='localhost',port=9500,user='admin',passwd='123456',db='jd_data',charset='utf8')
    sql = "insert into jd_information(id,company,id_sort,product,price,user_product,expression) values(" + "'" + item[
        'id'] + "'" + ',' + "'" + item['company'] + "'" + ',' + "'" + item['id_sort'] + "'" + ',' + "'" + item[
              'product'] + "'" + ',' + "'" + item['price'] + "'" + ',' + "'" + item['user_product'] + "'" + ',' + "'" + \
          item['expression'] + "'" + ")"
    conn.query(sql)
    print(item['id'], item['company'], item['id_sort'], item['product'], item['price'], item['user_product'],
          item['expression'])
    print('---------------------------------------------------------------')
    conn.commit()
    conn.close()

a = process_item()