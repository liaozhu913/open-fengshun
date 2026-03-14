#!/usr/bin/env python3
"""Batch 2: Fill remaining 9 towns + new discoveries"""
import json, os
from datetime import datetime

base = '/home/gem/workspace/agent/workspace/projects/kaifeng-fengshun'

with open(f'{base}/data/businesses.json', 'r') as f:
    data = json.load(f)

existing = {b['name'] for b in data['businesses']}

NEW = [
{"name":"汤坑温泉老汤湖","category":"温泉","subcategory":"公共温泉","town":"汤坑镇","address":"汤坑镇汤坑路南侧","phone":"","description":"广东省规模最大的免费自然温泉公共浴池，水温85度，医疗氡水含量全省第一。","price_range":"免费","rating":4.5,"tags":["免费","历史","氡温泉"],"source":"xiaohongshu"},
{"name":"水岸汇庭温泉酒店","category":"住宿","subcategory":"温泉酒店","town":"汤坑镇","address":"汤坑镇中心","phone":"","description":"人均200+享受24小时私家温泉池，1200米深天然硫磺泉。","price_range":"200-400","rating":4.4,"tags":["私汤","硫磺泉","性价比"],"source":"xiaohongshu"},
{"name":"华茂空中温泉","category":"温泉","subcategory":"空中温泉","town":"汤坑镇","address":"金河大道1号维纳斯酒店14楼","phone":"","description":"空中温泉，室内外温泉池、湿蒸房、儿童乐园，俯瞰丰顺全景。","price_range":"80-168","rating":4.3,"tags":["空中温泉","俯瞰","儿童乐园"],"source":"xiaohongshu"},
{"name":"顺豪温泉酒店","category":"住宿","subcategory":"温泉酒店","town":"汤坑镇","address":"汶水河畔","phone":"","description":"集住宿餐饮娱乐于一体的精品酒店，含KTV土特产店。","price_range":"200-500","rating":4.3,"tags":["河畔","KTV","度假"],"source":"xiaohongshu"},
{"name":"好日子农庄","category":"餐饮","subcategory":"农家乐","town":"汤坑镇","address":"距龙归寨瀑布15分钟","phone":"","description":"三星级农家乐，客家本地菜、河溪鲜及粤菜。","price_range":"人均50-80","rating":4.3,"tags":["三星农家乐","客家菜","河鲜"],"source":"xiaohongshu"},
{"name":"阿云私房菜","category":"餐饮","subcategory":"私房菜","town":"汤坑镇","address":"汤坑镇","phone":"","description":"本地人力荐私房菜，香辣猪肉脯口碑突出。","price_range":"人均50-80","rating":4.4,"tags":["私房菜","本地人推荐"],"source":"xiaohongshu"},
{"name":"朱阿菊咸菜煲店","category":"餐饮","subcategory":"客家菜","town":"潘田镇","address":"潘田镇新公路","phone":"","description":"咸菜煲获丰顺2024十大特色名菜，承接宴席设包厢。","price_range":"人均40-60","rating":4.5,"tags":["咸菜煲","2024名菜"],"source":"web_crawl"},
{"name":"老胖新鲜牛肉店","category":"餐饮","subcategory":"牛肉","town":"潘田镇","address":"潘田镇","phone":"","description":"中餐熟食，新鲜牛肉系列。","price_range":"人均40-60","rating":4.2,"tags":["牛肉","中餐"],"source":"web_crawl"},
{"name":"流坑公园","category":"旅游","subcategory":"公园","town":"潘田镇","address":"潘田镇","phone":"","description":"吊床秋千滑索，免费茶叶水电，休闲放松。","price_range":"免费","rating":4.0,"tags":["公园","休闲","免费"],"source":"web_crawl"},
{"name":"凤坪畲族村","category":"旅游","subcategory":"文化体验","town":"潭江镇","address":"潭江镇凤坪村","phone":"","description":"干栏式民居推窗见茶园，畲族早餐服饰文化及非遗展演。","price_range":"免费","rating":4.5,"tags":["畲族","文化","茶园","非遗"],"source":"web_crawl"},
{"name":"银溪村富硒古树茶","category":"旅游","subcategory":"茶旅","town":"潭江镇","address":"潭江镇银溪村","phone":"","description":"中国最大富硒古树茶村落，体验采茶茶乡风情。","price_range":"免费","rating":4.4,"tags":["茶旅","富硒","古树茶"],"source":"web_crawl"},
{"name":"韩江饭店","category":"餐饮","subcategory":"客家菜","town":"潭江镇","address":"潭江镇","phone":"","description":"潭江镇本地人气餐厅，客家畲族风味融合。","price_range":"人均40-60","rating":4.2,"tags":["客家菜","畲族风味"],"source":"web_crawl"},
{"name":"畲乡农家乐","category":"餐饮","subcategory":"农家乐","town":"潭江镇","address":"潭江镇","phone":"","description":"乌米饭、竹筒饭、畲族土鸡汤等特色菜。","price_range":"人均50-80","rating":4.3,"tags":["畲族菜","乌米饭","竹筒饭"],"source":"web_crawl"},
{"name":"老猫私房菜","category":"餐饮","subcategory":"私房菜","town":"汤南镇","address":"汤南镇S224省道蓝玉村","phone":"","description":"私房菜，晚餐夜宵，本地人气。","price_range":"人均50-80","rating":4.2,"tags":["私房菜","夜宵"],"source":"web_crawl"},
{"name":"御品牛肉火锅","category":"餐饮","subcategory":"牛肉火锅","town":"汤南镇","address":"珠光新城御景","phone":"","description":"牛肉火锅，餐饮服务食品销售。","price_range":"人均60-90","rating":4.2,"tags":["牛肉火锅"],"source":"web_crawl"},
{"name":"40年薯粉豆干老店","category":"餐饮","subcategory":"传统小吃","town":"汤南镇","address":"汤南镇深巷","phone":"","description":"40年老店，炸豆干外酥里嫩配甜辣酱。","price_range":"人均10-20","rating":4.4,"tags":["豆干","老字号"],"source":"web_crawl"},
{"name":"联兴饭店","category":"餐饮","subcategory":"饭店","town":"北斗镇","address":"北斗镇政府南206国道","phone":"0753-6830023","description":"北斗镇主要饭店，206国道旁。","price_range":"人均40-60","rating":4.1,"tags":["饭店","国道旁"],"source":"web_crawl"},
{"name":"广昇加油站","category":"生活服务","subcategory":"加油站","town":"北斗镇","address":"北斗镇庆瑶村","phone":"18088851884","description":"成品油零售、餐饮住宿、停车场、充电站。","price_range":"","rating":4.0,"tags":["加油站","充电站"],"source":"web_crawl"},
{"name":"建桥围","category":"旅游","subcategory":"古村落","town":"建桥镇","address":"建桥镇建安村","phone":"","description":"岭南古村落，客家船形围屋，3街12巷9座祠堂，小香港之称。","price_range":"免费","rating":4.3,"tags":["古村落","客家围屋","免费"],"source":"web_crawl"},
{"name":"建桥嘉顺饭店","category":"餐饮","subcategory":"饭店","town":"建桥镇","address":"建桥镇建安村","phone":"","description":"建桥镇主要餐饮，客家菜。","price_range":"人均30-50","rating":4.0,"tags":["饭店","客家菜"],"source":"web_crawl"},
{"name":"廣源饮食店","category":"餐饮","subcategory":"饭店","town":"龙岗镇","address":"龙岗镇","phone":"","description":"入选2024丰顺名店评选，龙岗镇代表性餐饮。","price_range":"人均30-50","rating":4.2,"tags":["名店","2024评选"],"source":"web_crawl"},
{"name":"武记饭店","category":"餐饮","subcategory":"饭店","town":"龙岗镇","address":"龙岗镇","phone":"","description":"入选2024丰顺名店评选，龙岗镇人气餐厅。","price_range":"人均30-50","rating":4.2,"tags":["名店","2024评选"],"source":"web_crawl"},
{"name":"龙岗源盛糕饼厂","category":"购物","subcategory":"食品加工","town":"龙岗镇","address":"龙岗镇龙华路191号","phone":"","description":"姜糖、云片糕、花生芝麻软糖等传统糕饼，丰顺手信。","price_range":"人均10-30","rating":4.1,"tags":["姜糖","云片糕","手信"],"source":"web_crawl"},
{"name":"龙鲸河漂流","category":"旅游","subcategory":"体验项目","town":"大龙华镇","address":"大龙华镇至黄金镇清溪河段","phone":"","description":"漂程9.8公里落差40米，激流探险生态观光，粤东知名漂流。","price_range":"约100","rating":4.5,"tags":["漂流","探险","夏季"],"source":"web_crawl"},
{"name":"大田村","category":"旅游","subcategory":"美丽乡村","town":"大龙华镇","address":"大龙华镇大田村","phone":"","description":"新晋宝藏村，白溪河古朴水车文艺彩绘墙。","price_range":"免费","rating":4.2,"tags":["乡村","拍照","免费"],"source":"web_crawl"},
{"name":"石龙饭店","category":"餐饮","subcategory":"饭店","town":"大龙华镇","address":"大龙华镇","phone":"","description":"入选丰顺名店评选，大龙华镇代表性餐饮。","price_range":"人均40-60","rating":4.2,"tags":["名店"],"source":"web_crawl"},
{"name":"小胜火旺饭店","category":"餐饮","subcategory":"饭店","town":"小胜镇","address":"小胜镇新胜街8号","phone":"","description":"餐饮服务食品销售，小胜镇主要餐饮。","price_range":"人均30-50","rating":4.0,"tags":["饭店"],"source":"web_crawl"},
{"name":"小胜镇特产","category":"购物","subcategory":"农产品","town":"小胜镇","address":"小胜镇","phone":"","description":"一村一品：朝天椒、丝苗米、猕猴桃、油茶。","price_range":"","rating":4.1,"tags":["朝天椒","猕猴桃","油茶"],"source":"web_crawl"},
{"name":"潭山镇野温泉","category":"温泉","subcategory":"野温泉","town":"潭山镇","address":"潭山镇","phone":"","description":"天然温泉资源，水温适中富含矿物质，原生态体验。","price_range":"免费/低价","rating":4.2,"tags":["野温泉","原生态"],"source":"web_crawl"},
]

added = 0
for b in NEW:
    if b['name'] not in existing:
        data['businesses'].append(b)
        existing.add(b['name'])
        added += 1

data['meta']['total_records'] = len(data['businesses'])
data['meta']['version'] = '0.3'

with open(f'{base}/data/businesses.json','w',encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

# Update TS
ts = f'''import {{ Business }} from './types'
export const BUSINESSES: Business[] = {json.dumps(data['businesses'], ensure_ascii=False, indent=2)}
export function getBusinesses(): Business[] {{ return BUSINESSES }}
export function getBusinessesByCategory(c: string): Business[] {{ return BUSINESSES.filter(b => b.category === c) }}
export function getBusinessesByTown(t: string): Business[] {{ return BUSINESSES.filter(b => b.town === t) }}
export function searchBusinesses(q: string): Business[] {{
  const s = q.toLowerCase()
  return BUSINESSES.filter(b => b.name.toLowerCase().includes(s) || b.description.toLowerCase().includes(s) || b.tags.some(t => t.toLowerCase().includes(s)))
}}
export function getStats() {{
  const c: Record<string,number> = {{}}; const t: Record<string,number> = {{}}
  BUSINESSES.forEach(b => {{ c[b.category]=(c[b.category]||0)+1; t[b.town]=(t[b.town]||0)+1 }})
  return {{ totalBusinesses: BUSINESSES.length, totalCategories: Object.keys(c).length, totalTowns: Object.keys(t).length, categories: c, towns: t }}
}}
'''
with open(f'{base}/web/src/data/businesses.ts','w') as f:
    f.write(ts)

cats = {}; towns = {}
for b in data['businesses']:
    cats[b['category']] = cats.get(b['category'],0)+1
    towns[b['town']] = towns.get(b['town'],0)+1

print(f"Added {added}, Total: {len(data['businesses'])}")
print(f"Towns: {len(towns)}/16")
for t,c in sorted(towns.items(), key=lambda x:-x[1]): print(f"  {t}: {c}")
