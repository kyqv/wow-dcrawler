# coding: utf-8
host = '0.0.0.0'
rootDir = 'D:\www\dcrawler'
port = 5000
# debug = True
debug = False
name = 'dcrawler'
version = '1.0.0'
selfApiUrl = 'https://sandbox-listing-service.eccang.com'
productCenterUrl = 'https://sandbox-product-service.eccang.com/'
szListingDynamicProxyUrl = 'http://sz-listing-dynamic-proxy.eccang.com/'
rancherUrl = 'https://k8s-rancher.ecgtool.com'
yixiaobaoCrwalerUrl = 'http://112.74.107.95:6614'
rancherProjectsBasicAuth = ''
rancherProjectName = 'listing'
rancherProjects = {
    rancherProjectName: {
        'test': 'c-9rw74:p-6xfxf',
        'preview': 'c-9rw74:p-j29ts',
        'production': 'c-9rw74:p-rl2lp'
    }
}
runningServerLocation = 'inside'
# 是否是异步任务
isUrlsChannelsAsynchrTask = False
isTask = False
runTaskLog = [
        #类型，平台，站点，第一方法需要执行多少个，第二方法需要执行多少个，第三方法需要执行多少个
        '1,shopee,ph,consumerGetCrawlerDataPushEs:1,consumerSalesDataCrawlerRedis:10,getEsSalesDataPushRedis:1',
        '1,shopee,id,consumerGetCrawlerDataPushEs:1,consumerSalesDataCrawlerRedis:10,getEsSalesDataPushRedis:1',
        '1,shopee,my,consumerGetCrawlerDataPushEs:1,consumerSalesDataCrawlerRedis:10,getEsSalesDataPushRedis:1',
        '1,shopee,th,consumerGetCrawlerDataPushEs:1,consumerSalesDataCrawlerRedis:10,getEsSalesDataPushRedis:1',
        # 'o,urlsChannels,0,1,10',
        # 'o,urlsChannels,0,1,10',
        # 'o,urlsChannels,0,1,10',
        # 'o,urlsChannels,0,1,10',
        # 'o,urlsChannels,0,1,10',
    ]

isGevent = True
processesNum = 1
threadedStatus = False
specialSegmentationSymbol = '8-8=,=8-8'
freeProxyPoolNum = 1
trueProxyPoolNum = 3
allowProxyDict = {
    'inside': [
        #'pp16ipyun',
        # 'pp66ip',
        # 'pp89ip',
        # 'ppData5u',
        # 'ppGoubanjia',
        # 'ppIp3366',
        # 'ppIphai',
        # 'ppJiangxianli',
        # 'ppKuaidaili',
        # 'ppProxyCoderBusy',
        # 'ppXicidali',
        # 'ppXiLadali',
         'ppZhiMadali',
        # 'ppIpIdea',
    ],
    'outside': [
        'ppCnProxy',
        'ppProxyList',
        'ppProxyListPlus',
    ],
}
amz_domain_mapping = {
    # 中国站
    'cn': 'https://www.amazon.cn',
    # 加拿大站
    'ca': 'https://www.amazon.ca',
    # 印度站
    'in': 'https://www.amazon. in',
    # 墨西哥站
    'mx': 'https://www.amazon.com.mx',
    # 德国站
    'de': 'https://www.amazon.de',
    # 意大利站
    'it': 'https://www.amazon.it',
    # 新加坡站
    'sg': 'https://www.amazon.sg',
    # 日本站
    'jp': 'https://www.amazon.co.jp',
    # 法国站
    'fr': 'https://www.amazon.fr',
    # 澳大利亚站
    'au': 'https://www.amazon.com.au',
    # 美国站
    'us': 'https://www.amazon.com',
    # 英国站
    'uk': 'https://www.amazon.co.uk',
    # 荷兰站
    'nl': 'https://www.amazon.nl',
    # 西班牙站
    'es': 'https://www.amazon.es',
    # 阿联酋站
    'ae': 'https://www.amazon.ae',
    # 波兰
    'pl': 'https://www.amazon.pl',
}


# 各接口缓存存活时间
taobao_life_time = {
    'info': 86400 * 10,
    'keyword': 86400 * 0,
    'creg': 86400 * 1.5,
    'shop': 86400 * 5,
    'library':86400 * 5
}
pdd_life_time = {
    'info': 86400 * 7,
    'keyword': 86400 * 3,
    'creg': 86400 * 1.5,
    'shop': 86400 * 5,
    'library': 86400 * 5
}
shopee_life_time = {
    'info': 86400 * 5,
    'keyword': 86400 * 3,
    'creg': 86400 * 1.5,
    'shop': 86400 * 5,
    'library':86400 * 5
}
lazada_life_time = {
    'info': 86400 * 5,
    'keyword': 86400 * 3,
    'creg': 86400 * 1.5,
    'shop': 86400 * 5
}
soukuan_life_time = {
    'info': 86400 * 5,
    'keyword': 86400 * 3,
    'creg': 86400 * 1.5,
    'shop': 86400 * 5
}
ali1688_life_time = {
    'info': 86400 * 5,
    'keyword': 86400 * 3,
    'creg': 86400 * 1.5,
    'shop': 86400 * 5
}
ebay_life_time = {
    'info': 86400 * 5,
    'keyword': 86400 * 3,
    'creg': 86400 * 1.5,
    'shop': 86400 * 5
}
aliexpress_life_time = {
    'info': 86400 * 5,
    'keyword': 86400 * 3,
    'creg': 86400 * 1.5,
    'shop': 86400 * 5
}
amazon_life_time = {
    'info': 86400 * 5,
    'keyword': 86400 * 3,
    'creg': 86400 * 1.5,
    'shop': 86400 * 5,
    "info_v": 86400 * 5,
}
bao66_life_time = {
    'info': 86400 * 5,
    'keyword': 86400 * 3,
    'creg': 86400 * 1.5,
    'shop': 86400 * 5
}


