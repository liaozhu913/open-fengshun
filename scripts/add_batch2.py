#!/usr/bin/env python3
"""批量添加第二批数据（剩余9镇 + 补充商家）"""
import json, os
from datetime import datetime

DATA_DIR = os.path.dirname(os.path.abspath(__file__)) + "/../data"

# 加载现有数据
with open(os.path.join(DATA_DIR, "businesses.json"), 'r') as f:
    data = json.load(f)

existing_names = {b['name'] for b in data['businesses']}

NEW_BUSINESSES = [
    # ===== 补充：汤坑镇新发现 =====
    {"name": "汤坑温泉（老汤湖）", "category": "温泉", "subcategory": "公共温泉", "town": "汤坑镇", "address": "汤坑镇汤坑路南侧、东秀村金贵大道边", "phone": "", "description": "广东省规模最大的免费自然温泉公共浴池，历史可追溯至明万历年间，水温85℃，医疗氡水含量全省第一。丰顺标志性体验。", "price_range": "免费", "rating": 4.5, "tags": ["免费", "历史", "氡温泉", "公共浴池"], "source": "xiaohongshu"},
    {"name": "水岸汇庭温泉酒店", "category": "住宿", "subcategory": "温泉酒店", "town": "汤坑镇", "address": "丰顺县汤坑镇中心", "phone": "", "description": "人均200+元即可享受房间内24小时私家温泉池（1200米深天然硫磺泉），私密性强，毗邻丰顺广场及特色美食店。", "price_range": "200-400", "rating": 4.4, "tags": ["私汤", "硫磺泉", "市中心", "性价比"], "source": "xiaohongshu"},
    {"name": "华茂空中温泉", "category": "温泉", "subcategory": "空中温泉", "town": "汤坑镇", "address": "金河大道1号（维纳斯国际酒店14楼）", "phone": "", "description": "空中温泉，含室内外温泉池、凉泉池、湿蒸房、儿童乐园，不受天气影响，可俯瞰丰顺全景，融合欧式风格。", "price_range": "80-168", "rating": 4.3, "tags": ["空中温泉", "俯瞰", "欧式", "儿童乐园"], "source": "xiaohongshu"},
    {"name": "顺豪温泉酒店", "category": "住宿", "subcategory": "温泉酒店", "town": "汤坑镇", "address": "丰顺县汶水河畔", "phone": "", "description": "集住宿、餐饮、娱乐于一体的精品酒店，位于汶水河畔，含KTV、土特产店，适合休闲度假。", "price_range": "200-500", "rating": 4.3, "tags": ["河畔", "KTV", "度假"], "source": "xiaohongshu"},
    {"name": "好日子农庄", "category": "餐饮", "subcategory": "农家乐", "town": "汤坑镇", "address": "丰顺县（距龙归寨瀑布15分钟车程）", "phone": "", "description": "三星级农家乐，主打客家本地菜、河溪鲜及粤菜，性价比高。距龙归寨瀑布近。", "price_range": "人均50-80", "rating": 4.3, "tags": ["三星农家乐", "客家菜", "河鲜", "景区周边"], "source": "xiaohongshu"},
    {"name": "阿云私房菜", "category": "餐饮", "subcategory": "私房菜", "town": "汤坑镇", "address": "丰顺县汤坑镇", "phone": "", "description": "本地人力荐私房菜，香辣猪肉脯口碑突出。", "price_range": "人均50-80", "rating": 4.4, "tags": ["私房菜", "本地人推荐", "猪肉脯"], "source": "xiaohongshu"},

    # ===== 潘田镇 =====
    {"name": "朱阿菊咸菜煲店", "category": "餐饮", "subcategory": "客家菜", "town": "潘田镇", "address": "潘田镇新公路（美宜佳对面）", "phone": "", "description": "特色菜品"咸菜煲"获丰顺县2024年十大特色名菜，承接宴席，设包厢及大厅。潘田镇代表性餐厅。", "price_range": "人均40-60", "rating": 4.5, "tags": ["咸菜煲", "名菜", "宴席", "2024十大名菜"], "source": "web_crawl"},
    {"name": "老胖新鲜牛肉店", "category": "餐饮", "subcategory": "牛肉", "town": "潘田镇", "address": "丰顺县潘田镇", "phone": "", "description": "主营中餐、熟食，兼营住宿，新鲜牛肉系列。", "price_range": "人均40-60", "rating": 4.2, "tags": ["牛肉", "中餐", "兼营住宿"], "source": "web_crawl"},
    {"name": "流坑公园", "category": "旅游", "subcategory": "公园", "town": "潘田镇", "address": "丰顺县潘田镇", "phone": "", "description": "提供吊床、秋千、滑索等设施，免费茶叶、水电，适合休闲放松。", "price_range": "免费", "rating": 4.0, "tags": ["公园", "休闲", "免费"], "source": "web_crawl"},

    # ===== 潭江镇 =====
    {"name": "凤坪畲族村", "category": "旅游", "subcategory": "文化体验", "town": "潭江镇", "address": "丰顺县潭江镇凤坪村", "phone": "", "description": "干栏式民居，推窗见茶园，可体验畲族早餐、服饰文化及非遗展演。畲族茶制作技艺列入县级非遗。", "price_range": "免费", "rating": 4.5, "tags": ["畲族", "文化", "茶园", "非遗", "免费"], "source": "web_crawl"},
    {"name": "银溪村（富硒古树茶村）", "category": "旅游", "subcategory": "茶旅", "town": "潭江镇", "address": "丰顺县潭江镇银溪村", "phone": "", "description": "中国最大富硒古树茶村落，可乘便民小巴（票价5-10元）前往，体验采茶及茶乡风情。", "price_range": "免费", "rating": 4.4, "tags": ["茶旅", "富硒", "古树茶", "采茶体验"], "source": "web_crawl"},
    {"name": "韩江饭店", "category": "餐饮", "subcategory": "客家菜", "town": "潭江镇", "address": "丰顺县潭江镇", "phone": "", "description": "潭江镇本地人气餐厅，客家与畲族风味融合。", "price_range": "人均40-60", "rating": 4.2, "tags": ["客家菜", "畲族风味"], "source": "web_crawl"},
    {"name": "畲乡农家乐", "category": "餐饮", "subcategory": "农家乐", "town": "潭江镇", "address": "丰顺县潭江镇", "phone": "", "description": "本地人气餐厅，提供乌米饭、竹筒饭、畲族土鸡汤等特色菜。", "price_range": "人均50-80", "rating": 4.3, "tags": ["畲族菜", "乌米饭", "竹筒饭", "农家乐"], "source": "web_crawl"},

    # ===== 汤南镇 =====
    {"name": "老猫私房菜", "category": "餐饮", "subcategory": "私房菜", "town": "汤南镇", "address": "汤南镇S224省道蓝玉新铺村门口1号", "phone": "", "description": "私房菜，提供晚餐、夜宵，本地人气餐厅。", "price_range": "人均50-80", "rating": 4.2, "tags": ["私房菜", "夜宵"], "source": "web_crawl"},
    {"name": "御品牛肉火锅店", "category": "餐饮", "subcategory": "牛肉火锅", "town": "汤南镇", "address": "珠光新城御景A2地块S1-16", "phone": "", "description": "牛肉火锅，餐饮服务及食品销售。", "price_range": "人均60-90", "rating": 4.2, "tags": ["牛肉火锅"], "source": "web_crawl"},
    {"name": "40年薯粉豆干老店", "category": "餐饮", "subcategory": "传统小吃", "town": "汤南镇", "address": "丰顺县汤南镇深巷中", "phone": "", "description": "40年老店，以炸豆干外酥里嫩、搭配甜辣酱为特色，承载地方乡愁记忆。汤南特色。", "price_range": "人均10-20", "rating": 4.4, "tags": ["豆干", "老字号", "传统小吃"], "source": "web_crawl"},

    # ===== 北斗镇 =====
    {"name": "联兴饭店（206国道店）", "category": "餐饮", "subcategory": "饭店", "town": "北斗镇", "address": "北斗镇政府南（206国道西）", "phone": "0753-6830023", "description": "北斗镇主要饭店，位于206国道旁，交通便利。", "price_range": "人均40-60", "rating": 4.1, "tags": ["饭店", "国道旁"], "source": "web_crawl"},
    {"name": "广昇加油站", "category": "生活服务", "subcategory": "加油站", "town": "北斗镇", "address": "北斗镇庆瑶村（原北斗粮食管理所）", "phone": "18088851884", "description": "提供成品油零售、餐饮服务、住宿服务、停车场、集中式快速充电站等综合服务。", "price_range": "", "rating": 4.0, "tags": ["加油站", "充电站", "综合服务"], "source": "web_crawl"},

    # ===== 建桥镇 =====
    {"name": "建桥围", "category": "旅游", "subcategory": "古村落", "town": "建桥镇", "address": "丰顺县建桥镇建安村", "phone": "", "description": "岭南古村落，客家古围建筑，布局呈"船形围"，外圆内方，保存3街12巷格局，有9座祠堂及传统商铺，历史上曾商贾云集，有"小香港"之称。", "price_range": "免费", "rating": 4.3, "tags": ["古村落", "客家围屋", "历史", "免费"], "source": "web_crawl"},
    {"name": "建桥嘉顺饭店", "category": "餐饮", "subcategory": "饭店", "town": "建桥镇", "address": "丰顺县建桥镇建安村", "phone": "", "description": "建桥镇主要餐饮服务，提供客家菜。", "price_range": "人均30-50", "rating": 4.0, "tags": ["饭店", "客家菜"], "source": "web_crawl"},

    # ===== 龙岗镇 =====
    {"name": "廣源饮食店", "category": "餐饮", "subcategory": "饭店", "town": "龙岗镇", "address": "丰顺县龙岗镇", "phone": "", "description": "入选2024年丰顺县"名店"评选活动，龙岗镇代表性餐饮商家。", "price_range": "人均30-50", "rating": 4.2, "tags": ["名店", "2024评选"], "source": "web_crawl"},
    {"name": "武记饭店", "category": "餐饮", "subcategory": "饭店", "town": "龙岗镇", "address": "丰顺县龙岗镇", "phone": "", "description": "入选2024年丰顺县"名店"评选活动，龙岗镇人气餐厅。", "price_range": "人均30-50", "rating": 4.2, "tags": ["名店", "2024评选"], "source": "web_crawl"},
    {"name": "龙岗源盛糕饼厂", "category": "购物", "subcategory": "食品加工", "town": "龙岗镇", "address": "龙岗镇龙华路191号（龙岗客运站附近）", "phone": "", "description": "加工、销售姜糖、云片糕、花生/芝麻软糖等传统糕饼。丰顺传统手信。", "price_range": "人均10-30", "rating": 4.1, "tags": ["姜糖", "云片糕", "手信", "老字号"], "source": "web_crawl"},

    # ===== 大龙华镇 =====
    {"name": "龙鲸河漂流", "category": "旅游", "subcategory": "体验项目", "town": "大龙华镇", "address": "丰顺县大龙华镇至黄金镇清溪河段", "phone": "", "description": "漂程9.8公里，落差40多米，集激流探险、生态观光于一体，沿河可观赏"狮象迎宾""冰臼奇观"等景点，粤东知名漂流项目。", "price_range": "约100元", "rating": 4.5, "tags": ["漂流", "探险", "生态", "夏季"], "source": "web_crawl"},
    {"name": "大田村", "category": "旅游", "subcategory": "美丽乡村", "town": "大龙华镇", "address": "丰顺县大龙华镇大田村", "phone": "", "description": ""新晋宝藏村"，以清澈的白溪河、古朴水车、文艺彩绘墙及充满烟火气的街道为特色，适合休闲漫步与拍照打卡。", "price_range": "免费", "rating": 4.2, "tags": ["乡村", "拍照", "免费"], "source": "web_crawl"},
    {"name": "石龙饭店", "category": "餐饮", "subcategory": "饭店", "town": "大龙华镇", "address": "丰顺县大龙华镇", "phone": "", "description": "入选"丰顺名店"评选，大龙华镇代表性餐饮商家。", "price_range": "人均40-60", "rating": 4.2, "tags": ["名店", "评选"], "source": "web_crawl"},

    # ===== 小胜镇 =====
    {"name": "小胜火旺饭店", "category": "餐饮", "subcategory": "饭店", "town": "小胜镇", "address": "小胜镇新胜街8号", "phone": "", "description": "餐饮服务、食品销售，小胜镇主要餐饮商家。", "price_range": "人均30-50", "rating": 4.0, "tags": ["饭店"], "source": "web_crawl"},
    {"name": "小胜镇特产（朝天椒·猕猴桃·油茶）", "category": "购物", "subcategory": "农产品", "town": "小胜镇", "address": "丰顺县小胜镇", "phone": "", "description": ""一村一品"特色产业：朝天椒、丝苗米、猕猴桃、油茶，通过"产业村长"模式发展，近两年农林牧渔业总产值累计达1.96亿元。", "price_range": "", "rating": 4.1, "tags": ["朝天椒", "猕猴桃", "油茶", "特产"], "source": "web_crawl"},

    # ===== 潭山镇 =====
    {"name": "潭山镇温泉资源", "category": "温泉", "subcategory": "野温泉", "town": "潭山镇", "address": "丰顺县潭山镇", "phone": "", "description": "潭山镇拥有天然温泉资源，水温适中，富含矿物质，尚未大规模开发，保留原生态体验。", "price_range": "免费/低价", "rating": 4.2, "tags": ["野温泉", "原生态", "矿物质"], "source": "web_crawl"},
]

# 添加新数据（跳过已存在的）
added = 0
for b in NEW_BUSINESSES:
    if b['name'] not in existing_names:
        data['businesses'].append(b)
        existing_names.add(b['name'])
        added += 1

data['meta']['total_records'] = len(data['businesses'])
data['meta']['version'] = '0.3'
data['meta']['collected_at'] = datetime.now().isoformat()

# 保存
with open(os.path.join(DATA_DIR, "businesses.json"), 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print(f"✅ 新增 {added} 条，总计 {len(data['businesses'])} 条商家数据")

# 统计
categories = {}
towns = {}
for b in data['businesses']:
    cat = b['category']
    town = b['town']
    categories[cat] = categories.get(cat, 0) + 1
    towns[town] = towns.get(town, 0) + 1

print(f"\n📊 分类统计:")
for cat, count in sorted(categories.items(), key=lambda x: -x[1]):
    print(f"   {cat}: {count} 家")

print(f"\n📍 镇覆盖: {len(towns)} / 16 个镇")
for town, count in sorted(towns.items(), key=lambda x: -x[1]):
    print(f"   {town}: {count} 家")
