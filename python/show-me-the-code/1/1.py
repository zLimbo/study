# -*- coding: utf-8 -*-

import base64

def gen_coupon(id, good):
    coupon = dict()
    coupon['id'] = id
    coupon['good'] = good
    raw = '/'.join([k + ':' + v for k, v in coupon.items()])
    raw_b64 = base64.b64encode(raw.encode('utf-8'))
    coupon_code = raw_b64.decode()
    return coupon_code


def save_coupon(coupon_code):
    with open('coupon.txt', 'a+') as fp:
        fp.write(coupon_code + '\n')


def gen_all_coupon(num=200):
    for i in range(1000, 1000+num):
        coupon_code = gen_coupon(str(i), str(i*2))
        save_coupon(coupon_code)


if __name__ == '__main__':
    gen_all_coupon()
