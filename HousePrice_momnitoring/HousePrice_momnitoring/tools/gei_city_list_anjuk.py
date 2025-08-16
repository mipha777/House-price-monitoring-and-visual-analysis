# -*- coding: utf-8 -*-
"""
@Author   : shaozi
@Version  : Python 3.12
@Date     : 2025/8/15 03:40
@Desc     : 
"""
import requests

cookies = {
    'xxzlxxid': 'pfmxJRUGRg0YwaXIGF/6+W/EpZZSRL+EXdzPuobWbd74LXaGN92vmlWylhU7+73VJppQ',
    'aQQ_ajkguid': 'E6DC6C42-72F9-49B9-851D-98F201F526D0',
    'sessid': 'D95E31B6-EC0C-44FD-85F5-AAA354A17A33',
    'ajk-appVersion': '',
    '58tj_uuid': '5b673635-d078-41bf-86cc-79e6877ab485',
    'id58': 'CrIqjWiaM0cp+1BzS7gJAg==',
    'xxzlclientid': 'adaa65b0-e20b-4445-9d8d-1754936135252',
    'fzq_h': '9de6a23aafbd1d40f8be6cd152169d08_1755198349417_95f71f7406f14d998a185463bffb7f2c_2027637618',
    'new_uv': '3',
    'ctid': '18',
    'twe': '2',
    'obtain_by': '1',
    'xxzlbbid': 'pfmbM3wxMDM0NnwxLjEwLjF8MTc1NTIwMDMyODUxMjk4ODAyNnxMOWEzTFVjZEh4VUhidjQwc2JrbEd2WUk1REFKZk4wdFUzUzRxUXZrbTB3PXw1YWUyZDFkMmRkNWM5Y2QwYzIzNzBjYmU5Y2E3YTFhMF8xNzU1MjAwMzI3NjA0XzQzNGU4NGM0ZGVmMzRmYTFhMTg2MWFhN2I0NjU4YTljXzIwMjc2Mzc2MTh8NjFhNTQ4MmEyNGY0YjNlYTc5MjQzZjVlMGI1M2I5OTJfMTc1NTIwMDMyODE2NV8yNTQ=',
}

headers = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8',
    'cache-control': 'no-cache',
    'pragma': 'no-cache',
    'priority': 'u=0, i',
    'referer': 'https://hangzhou.anjuke.com/',
    'sec-ch-ua': '"Not;A=Brand";v="99", "Google Chrome";v="139", "Chromium";v="139"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36',
    # 'cookie': 'xxzlxxid=pfmxJRUGRg0YwaXIGF/6+W/EpZZSRL+EXdzPuobWbd74LXaGN92vmlWylhU7+73VJppQ; aQQ_ajkguid=E6DC6C42-72F9-49B9-851D-98F201F526D0; sessid=D95E31B6-EC0C-44FD-85F5-AAA354A17A33; ajk-appVersion=; 58tj_uuid=5b673635-d078-41bf-86cc-79e6877ab485; id58=CrIqjWiaM0cp+1BzS7gJAg==; xxzlclientid=adaa65b0-e20b-4445-9d8d-1754936135252; fzq_h=9de6a23aafbd1d40f8be6cd152169d08_1755198349417_95f71f7406f14d998a185463bffb7f2c_2027637618; new_uv=3; ctid=18; twe=2; obtain_by=1; xxzlbbid=pfmbM3wxMDM0NnwxLjEwLjF8MTc1NTIwMDMyODUxMjk4ODAyNnxMOWEzTFVjZEh4VUhidjQwc2JrbEd2WUk1REFKZk4wdFUzUzRxUXZrbTB3PXw1YWUyZDFkMmRkNWM5Y2QwYzIzNzBjYmU5Y2E3YTFhMF8xNzU1MjAwMzI3NjA0XzQzNGU4NGM0ZGVmMzRmYTFhMTg2MWFhN2I0NjU4YTljXzIwMjc2Mzc2MTh8NjFhNTQ4MmEyNGY0YjNlYTc5MjQzZjVlMGI1M2I5OTJfMTc1NTIwMDMyODE2NV8yNTQ=',
}

response = requests.get('https://www.anjuke.com/sy-city.html', cookies=cookies, headers=headers)

from lxml import etree
res = etree.HTML(response.text)
all = res.xpath('//ul[@class="ajk-city-cell-content"]/li')
print(len(all))
names = {}
city = {
"北京市": {
"北京": 0
},
"天津市": {
"天津": 0
},
"上海市": {
"上海": 0
},
"重庆市": {
"重庆": 0
},
"河北": {
"石家庄": 0,
"唐山": 0,
"秦皇岛": 0,
"邯郸": 0,
"邢台": 0,
"保定": 0,
"张家口": 0,
"承德": 0,
"沧州": 0,
"廊坊": 0,
"衡水": 0
},
"山西": {
"太原": 0,
"大同": 0,
"阳泉": 0,
"长治": 0,
"晋城": 0,
"朔州": 0,
"晋中": 0,
"运城": 0,
"忻州": 0,
"临汾": 0,
"吕梁": 0
},
"辽宁": {
"沈阳": 0,
"大连": 0,
"鞍山": 0,
"抚顺": 0,
"本溪": 0,
"丹东": 0,
"锦州": 0,
"营口": 0,
"阜新": 0,
"辽阳": 0,
"盘锦": 0,
"铁岭": 0,
"朝阳": 0,
"葫芦岛": 0
},
"吉林": {
"长春": 0,
"吉林": 0,
"四平": 0,
"辽源": 0,
"通化": 0,
"白山": 0,
"松原": 0,
"白城": 0,
"延边朝": 0
},
"黑龙江": {
"哈尔滨": 0,
"齐齐哈尔": 0,
"鸡西": 0,
"鹤岗": 0,
"双鸭山": 0,
"大庆": 0,
"伊春": 0,
"佳木斯": 0,
"七台河": 0,
"牡丹江": 0,
"黑河": 0,
"绥化": 0,
"大兴安岭地区": 0
},
"江苏": {
"南京": 0,
"无锡": 0,
"徐州": 0,
"常州": 0,
"苏州": 0,
"南通": 0,
"连云港": 0,
"淮安": 0,
"盐城": 0,
"扬州": 0,
"镇江": 0,
"泰州": 0,
"宿迁": 0
},
"浙江": {
"杭州": 0,
"宁波": 0,
"温州": 0,
"嘉兴": 0,
"湖州": 0,
"绍兴": 0,
"金华": 0,
"衢州": 0,
"舟山": 0,
"台州": 0,
"丽水": 0
},
"安徽": {
"合肥": 0,
"芜湖": 0,
"蚌埠": 0,
"淮南": 0,
"马鞍山": 0,
"淮北": 0,
"铜陵": 0,
"安庆": 0,
"黄山": 0,
"滁州": 0,
"阜阳": 0,
"宿州": 0,
"六安": 0,
"亳州": 0,
"池州": 0,
"宣城": 0
},
"福建": {
"福州": 0,
"厦门": 0,
"莆田": 0,
"三明": 0,
"泉州": 0,
"漳州": 0,
"南平": 0,
"龙岩": 0,
"宁德": 0
},
"江西": {
"南昌": 0,
"景德镇": 0,
"萍乡": 0,
"九江": 0,
"新余": 0,
"鹰潭": 0,
"赣州": 0,
"吉安": 0,
"宜春": 0,
"抚州": 0,
"上饶": 0
},
"山东": {
"济南": 0,
"青岛": 0,
"淄博": 0,
"枣庄": 0,
"东营": 0,
"烟台": 0,
"潍坊": 0,
"济宁": 0,
"泰安": 0,
"威海": 0,
"日照": 0,
"临沂": 0,
"德州": 0,
"聊城": 0,
"滨州": 0,
"菏泽": 0
},
"河南": {
"郑州": 0,
"开封": 0,
"洛阳": 0,
"平顶山": 0,
"安阳": 0,
"鹤壁": 0,
"新乡": 0,
"焦作": 0,
"濮阳": 0,
"许昌": 0,
"漯河": 0,
"三门峡": 0,
"南阳": 0,
"商丘": 0,
"信阳": 0,
"周口": 0,
"驻马店": 0,
"济源": 0
},
"湖北": {
"武汉": 0,
"黄石": 0,
"十堰": 0,
"宜昌": 0,
"襄阳": 0,
"鄂州": 0,
"荆门": 0,
"孝感": 0,
"荆州": 0,
"黄冈": 0,
"咸宁": 0,
"随州": 0,
"恩施土家族": 0,
"潜江": 0,
"天门": 0,
"仙桃": 0,
"神农架林区": 0
},
"湖南": {
"长沙": 0,
"株洲": 0,
"湘潭": 0,
"衡阳": 0,
"邵阳": 0,
"岳阳": 0,
"常德": 0,
"张家界": 0,
"益阳": 0,
"郴州": 0,
"永州": 0,
"怀化": 0,
"娄底": 0,
"湘西土家族": 0
},
"广东": {
"广州": 0,
"韶关": 0,
"深圳": 0,
"珠海": 0,
"汕头": 0,
"佛山": 0,
"江门": 0,
"湛江": 0,
"茂名": 0,
"肇庆": 0,
"惠州": 0,
"梅州": 0,
"汕尾": 0,
"河源": 0,
"阳江": 0,
"清远": 0,
"东莞": 0,
"中山": 0,
"潮州": 0,
"揭阳": 0,
"云浮": 0
},
"广西": {
"南宁": 0,
"柳州": 0,
"桂林": 0,
"梧州": 0,
"北海": 0,
"防城港": 0,
"钦州": 0,
"贵港": 0,
"玉林": 0,
"百色": 0,
"贺州": 0,
"河池": 0,
"来宾": 0,
"崇左": 0
},
"海南": {
"海口": 0,
"三亚": 0,
"三沙": 0,
"儋州": 0
},
"四川": {
"成都": 0,
"自贡": 0,
"攀枝花": 0,
"泸州": 0,
"德阳": 0,
"绵阳": 0,
"广元": 0,
"遂宁": 0,
"内江": 0,
"乐山": 0,
"南充": 0,
"眉山": 0,
"宜宾": 0,
"广安": 0,
"达州": 0,
"雅安": 0,
"巴中": 0,
"资阳": 0,
"阿坝藏族": 0,
"甘孜": 0,
"凉山": 0
},
"贵州": {
"贵阳": 0,
"六盘水": 0,
"遵义": 0,
"安顺": 0,
"毕节": 0,
"铜仁": 0,
"黔西南": 0,
"黔东南": 0,
"黔南": 0
},
"云南": {
"昆明": 0,
"曲靖": 0,
"玉溪": 0,
"保山": 0,
"昭通": 0,
"丽江": 0,
"普洱": 0,
"临沧": 0,
"楚雄": 0,
"红河": 0,
"文山": 0,
"西双版纳": 0,
"大理": 0,
"德宏傣族景": 0,
"怒江傈": 0,
"迪庆": 0
},
"西藏": {
"拉萨": 0,
"昌都": 0,
"山南": 0,
"日喀则": 0,
"那曲": 0,
"阿里地区": 0,
"林芝": 0
},
"陕西": {
"西安": 0,
"铜川": 0,
"宝鸡": 0,
"咸阳": 0,
"渭南": 0,
"延安": 0,
"汉中": 0,
"榆林": 0,
"安康": 0,
"商洛": 0
},
"甘肃": {
"兰州": 0,
"嘉峪关": 0,
"金昌": 0,
"白银": 0,
"天水": 0,
"酒泉": 0,
"张掖": 0,
"武威": 0,
"定西": 0,
"陇南": 0,
"平凉": 0,
"庆阳": 0,
"临夏": 0,
"甘南": 0
},
"青海": {
"西宁": 0,
"海东": 0,
"海北": 0,
"黄南": 0,
"海南": 0,
"果洛": 0,
"玉树": 0,
"海西蒙古族": 0
},
"宁夏": {
"银川": 0,
"石嘴山": 0,
"吴忠": 0,
"固原": 0,
"中卫": 0
},
"新疆": {
"乌鲁木齐": 0,
"克拉玛依": 0,
"吐鲁番": 0,
"哈密": 0,
"昌吉": 0,
"博尔塔拉": 0,
"巴音郭楞": 0,
"阿克苏地区": 0,
"克孜勒苏柯尔": 0,
"喀什地区": 0,
"和田地区": 0,
"伊犁哈": 0,
"塔城地区": 0,
"阿勒泰地区": 0,
"石河子": 0,
"阿拉尔": 0,
"图木舒克": 0,
"五家渠": 0,
"胡杨河": 0,
"可克达拉": 0
},
"内蒙古": {
"呼和浩特": 0,
"包头": 0,
"乌海": 0,
"赤峰": 0,
"通辽": 0,
"鄂尔多斯": 0,
"呼伦贝尔": 0,
"巴彦淖尔": 0,
"乌兰察布": 0,
"兴安盟": 0,
"锡林郭勒盟": 0,
"阿拉善盟": 0
},
"香港特别行政区": {
"中国香港": 0
}
}

for i,j in city.items():
    for a, b in j.items():
        for each in all:
            url = each.xpath('./a/@href')[0]
            name = each.xpath('./a/text()')[0]
            if a == name:
                j[a] = url

print(len(city))
print(city)
