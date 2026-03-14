#!/usr/bin/env python3
"""
丰顺县商家数据采集脚本
从多个公开数据源采集丰顺县 16 个镇的商家信息
"""

import json
import csv
import os
import time
import subprocess
import re
from datetime import datetime

# 丰顺县 16 个镇
TOWNS = [
    "汤坑镇", "丰良镇", "潘田镇", "黄金镇", "留隍镇",
    "潭江镇", "汤南镇", "埔寨镇", "北斗镇", "八乡山镇",
    "建桥镇", "龙岗镇", "大龙华镇", "小胜镇", "砂田镇", "潭山镇"
]

# 搜索关键词分类
CATEGORIES = {
    "餐饮": ["美食", "餐厅", "饭店", "小吃", "特色菜", "客家菜", "潮汕菜"],
    "住宿": ["酒店", "宾馆", "民宿", "旅馆", "度假村"],
    "温泉": ["温泉", "泡汤", "温泉酒店", "温泉度假"],
    "旅游": ["景区", "景点", "旅游", "漂流", "瀑布", "公园"],
    "购物": ["超市", "商场", "市场", "特产", "购物"],
    "医疗": ["医院", "诊所", "药店", "卫生院"],
    "教育": ["学校", "培训", "幼儿园", "辅导"],
    "生活服务": ["维修", "美容", "理发", "快递", "银行", "加油站"],
    "政务": ["政府", "派出所", "社保", "税务", "办证"],
}

DATA_DIR = os.path.dirname(os.path.abspath(__file__)) + "/../data"
os.makedirs(DATA_DIR, exist_ok=True)


def search_baidu_maps(keyword, region="丰顺县"):
    """通过百度地图搜索 POI"""
    url = f"https://map.baidu.com/search/{keyword}/@12677389.68,2629518.73,13z?querytype=s&wd={region}{keyword}&c=257"
    return url


def generate_search_queries():
    """生成所有搜索查询组合"""
    queries = []
    for town in TOWNS:
        for category, keywords in CATEGORIES.items():
            for keyword in keywords[:2]:  # 每类取前 2 个关键词
                queries.append({
                    "town": town,
                    "category": category,
                    "keyword": f"{town} {keyword}",
                    "search_term": f"丰顺县{town}{keyword}"
                })
    return queries


def save_raw_data(data, filename):
    """保存原始采集数据"""
    filepath = os.path.join(DATA_DIR, filename)
    with open(filepath, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    print(f"  ✅ 保存 {len(data)} 条数据到 {filename}")
    return filepath


def deduplicate(records):
    """基于名称和地址去重"""
    seen = set()
    unique = []
    for r in records:
        key = (r.get('name', '').strip(), r.get('address', '').strip())
        if key not in seen and key[0]:
            seen.add(key)
            unique.append(r)
    return unique


def main():
    print("=" * 60)
    print("🏪 开源丰顺 - 商家数据采集")
    print(f"📍 目标区域：丰顺县（{len(TOWNS)} 个镇）")
    print(f"📂 分类：{len(CATEGORIES)} 个大类")
    print(f"📅 开始时间：{datetime.now().strftime('%Y-%m-%d %H:%M')}")
    print("=" * 60)

    queries = generate_search_queries()
    print(f"\n📋 共生成 {len(queries)} 条搜索查询\n")

    # 保存搜索计划
    save_raw_data(queries, "search_queries.json")

    # 生成待爬取 URL 列表
    crawl_tasks = []
    for q in queries:
        crawl_tasks.append({
            "query": q,
            "urls": [
                f"https://map.baidu.com/search/{q['search_term']}",
                f"https://www.dianping.com/search/keyword/1026/0_{q['search_term']}",
            ]
        })

    save_raw_data(crawl_tasks, "crawl_tasks.json")

    print("\n" + "=" * 60)
    print("✅ Phase 1.1 准备完成")
    print(f"   - {len(queries)} 条搜索查询")
    print(f"   - {len(crawl_tasks)} 组爬取任务")
    print(f"   - 数据目录: {DATA_DIR}")
    print("=" * 60)

    return queries


if __name__ == "__main__":
    queries = main()
