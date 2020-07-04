# -*- coding: utf-8 -*-

import pymysql
import base64

def gen_coupon(id, goods):
    coupon = dict()
    coupon['id'] = id
    coupon['goods'] = goods
    raw = '/'.join([k + ':' + v for k, v in coupon.items()])
    raw_b64 = base64.urlsafe_b64encode(raw.encode('utf-8'))
    coupon_code = raw_b64.decode()
    return coupon_code


def safe_in_db(coupon_code):
    pass


def gen_all_coupon(n=200):
    coupons = []
    for i in range(1000, 1000 + n):
        id, goods = str(i), str(i*2)
        coupon_code = gen_coupon(id, goods)
        coupons.append((id, goods, coupon_code))
    return coupons


def save_coupon(coupons, host, user, passwd, db):
    db = pymysql.connect(host, user, passwd, db)
    cursor = db.cursor()
    cursor.execute(r'DROP TABLE IF EXISTS coupon')
    cursor.execute(r"""
        CREATE TABLE coupon (
            id CHAR(10) NOT NULL,
            goods CHAR(24),
            code CHAR(128),
            PRIMARY KEY(id)
        ) ENCRYPTION='N' """)
    try:
        cursor.executemany(r"INSERT INTO coupon VALUES (%s, %s, %s)", coupons)
        db.commit()
    except:
        db.rollback()
        raise
    # cursor.execute(r"SELECT * FROM coupon")
    # out = cursor.fetchall()
    # print(out)
    db.close()


if __name__ == '__main__':
    coupons = gen_all_coupon()
    save_coupon(coupons, 'localhost', 'test_user', 'test_pwd', 'test_db')


