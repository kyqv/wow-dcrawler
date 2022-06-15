# -*- coding: utf-8 -*-
# @Time:  2021/1/13 13: 44
# @Author:  foolminx
# @File:  site.py

site = {
    # amazon:
    'amazon': {
        'amazon.com': 'US',
        'www.amazon.com': 'US',
        'www.amazon.de': 'DE',
        'amazon.de': 'DE',
        'www.amazon.co.uk': 'UK',
        'amazon.co.uk': 'UK',
        'www.amazon.ca': 'CA',
        'amazon.ca': 'CA',
        'www.amazon.co.jp': 'JP',
        'amazon.co.jp': 'JP',
        'www.amazon.it': 'IT',
        'amazon.it': 'IT',
        'www.amazon.cn': 'CN',
        'amazon.cn': 'CN',
        'www.amazon.es': 'ES',
        'amazon.es': 'ES',
        'www.amazon.com.au': 'AU',
        'amazon.com.au': 'AU',
        'www.amazon.ae': 'AE',
        'amazon.ae': 'AE',
        'www.amazon.in': 'IN',
        'amazon.in': 'IN',
        'www.amazon.fr': 'FR',
        'amazon.fr': 'FR',
        'www.amazon.com.mx': 'MX',
        'amazon.com.mx': 'MX',
        'www.amazon.sg': 'SG',
        'amazon.sg': 'SG',
        'www.amazon.nl': 'NL',
        'amazon.nl': 'NL',
    },

    # 淘宝
    'taobao': {
        'www.taobao.com': 'CN',
        'taobao.com': 'CN',
        'item.taobao.com': 'CN',
    },

    # 天猫
    'tmall': {
        'detail.tmall.com': 'CN',
        'tmall.com': 'CN',
        'www.tmall.com': 'CN',
    },

    # joom
    'joom': {
        'www.joom.com': 'US',
        'joom.com': 'RUS',
    },

    # wish
    'wish': {
        'www.wish.com': 'US',
        'wish.com': 'US',
    },

    # shopee
    'shopee': {
        'shopee.co.th': 'TH',
        'shopee.com.my': 'MY',
        'shopee.sg':'SG',#新加坡
        'shopee.co.id':'ID',
        'shopee.vn':'VN',
        'shopee.ph':'PH', #菲律宾
        'xiapi.xiapibuy.com':'TW', #台湾
        'ph.xiapibuy.com':'PH', #菲律宾
        'shopee.com.br':'BR' #巴西 
    },

    #lazada
     'lazada': {
        'lazada.co.th': 'TH',
        'lazada.com.my': 'MY',
        'lazada.co.id':'ID'
    },
    # jd
    'jd': {
        'item.jd.com': 'CN',
        'jd.com': 'CN',
    },

    # ebay
    'ebay': {
        'ebay.com': 'US',
        'www.ebay.com': 'US',
    },

    # aliexpress
    'aliexpress': {
        'aliexpress.com': 'US',
        'www.aliexpress.com': 'US',
    },

    # 宝66
    'bao66': {
        'www.bao66.cn': 'CN',
        'bao66.cn': 'CN',
    },

    # 1688
    '1688': {
        'detail.1688.com': 'CN',
        'img.alicdn.com': 'CN',
        'itemcdn.tmall.com': 'CN',
        'desc.alicdn.com': 'CN',
    },

    # alibaba

    #vvic
    'vvic': {
        'www.vvic.com': 'CN'
    },
    #coupang
    'coupang': {
        'www.coupang.com': 'KP'
    },
    #walmart
    'walmart': {
        'www.walmart.com': 'US'
    }

}

# 对外仅用于展示支持采集的平台站点
briefSite = {
    "Amazon": {
        "中国站": [
            "https://www.amazon.cn"
        ],
        "加拿大站": [
            "https://www.amazon.ca"
        ],
        "印度站": [
            "https://www.amazon.in"
        ],
        "墨西哥站": [
            "https://www.amazon.com.mx"
        ],
        "德国站": [
            "https://www.amazon.de"
        ],
        "意大利站": [
            "https://www.amazon.it"
        ],
        "新加坡站": [
            "https://www.amazon.sg"
        ],
        "日本站": [
            "https://www.amazon.co.jp"
        ],
        "法国站": [
            "https://www.amazon.fr"
        ],
        "澳大利亚站": [
            "https://www.amazon.com.au"
        ],
        "美国站": [
            "https://www.amazon.com"
        ],
        "英国站": [
            "https://www.amazon.co.uk"
        ],
        "荷兰站": [
            "https://www.amazon.nl"
        ],
        "西班牙站": [
            "https://www.amazon.es"
        ],
        "阿联酋站": [
            "https://www.amazon.ae"
        ]
    },
    "淘宝": {
        "中国站": [
            "https://www.taobao.com"
        ]
    },
    "天猫": {
        "-": [
            "https://www.tmall.com"
        ]
    },
    "JOOM": {
        "所有站点": [
            "https://www.joom.com"
        ]
    },
    "Wish": {
        "所有站点": [
            "https://www.wish.com"
        ]
    },
    "Shopee": {
        "马来西亚站": [
            "https://shopee.com.my"
        ],
        "泰国站": [
            "https://shopee.co.th"
        ],
        "菲律宾站": [
            "https://shopee.ph"
        ],
        "越南站": [
            "https://shopee.vn"
        ],
        "巴西站": [
            "https://shopee.com.br"
        ],
        "印尼站": [
            "https://shopee.co.id"
        ],
        "新加坡站": [
            "https://shopee.sg"
        ],
    },
    "JD": {
        "中国站": [
            "https://www.jd.com"
        ]
    },
    "eBay": {
        "所有站点": [
            "https://www.ebay.com"
        ]
    },
    "Aliexpress": {
        "所有站点": [
            "https://www.aliexpress.com"
        ]
    },
    "bao66": {
        "-": [
            "https://www.bao66.cn"
        ]
    },
    "1688": {
        "-": [
            "https://www.1688.com"
        ]
    },
    "coupang": {
            "-": [
                "https://www.coupang.com/"
            ]
        },
    "walmart": {
            "-": [
                "https://www.walmart.com/"
            ]
        },
}

charset = {
    '1688': {
        'utf-8': {
            "default": [
                "tmall.com",
            ],
            "point": [
                "itemcdn.tmall.com",
            ],
        },
        "gbk": {
            "default": [
                "alicdn.com",
            ],
            "point": [
                "img.alicdn.com",
            ],
        }
    }
}

siteLanguage = {
    ''
}

canUseSite = [
    {
        'platform': 'Amazon',
        'site': '美国站',
        'domain': [
            'amazon.com',
            ''
        ],
    }
]
