# 开源丰顺 - 执行路线图

## Phase 1: 数据基建（本周，Day 1-3）⚡ 进行中

### 1.1 数据采集
- [x] 基础调研（丰顺概况、产业、旅游资源）
- [ ] 采集 16 个镇的商家/服务机构数据
  - 来源：百度地图 POI、高德地图、大众点评
  - 分类：餐饮、住宿、旅游、生活服务、医疗、教育、政府
- [ ] 数据清洗和去重
- [ ] 结构化入库（JSON/CSV）

### 1.2 数据 Schema 设计
```
businesses {
  id, name, category, subcategory,
  address, town, phone, website,
  lat, lng, description, images[],
  rating, price_level, hours,
  source, verified, created_at, updated_at
}

categories {
  id, name, slug, icon, parent_id,
  description, sort_order
}

towns {
  id, name, slug, description,
  population, highlights[]
}
```

### 1.3 分类体系
- 🍜 餐饮美食
- 🏨 住宿酒店（重点：温泉酒店）
- ♨️ 温泉养生
- 🏞️ 旅游景点
- 🛒 购物消费
- 🏥 医疗健康
- 🎓 教育培训
- 🏛️ 政务办事
- 🔧 生活服务
- 🚗 交通出行

---

## Phase 2: MVP 搭建（Day 4-7）

### 2.1 网站 MVP
- [ ] Next.js 项目初始化
- [ ] 首页：搜索 + 分类导航 + 热门推荐
- [ ] 分类列表页：按镇/分类筛选
- [ ] 商家详情页：信息展示 + 地图 + 联系方式
- [ ] 搜索功能：Meilisearch 集成
- [ ] SEO 基础：Meta tags + Sitemap + 结构化数据

### 2.2 部署上线
- [ ] Vercel 部署
- [ ] 域名购买：kaifengshun.com / fengshun.life
- [ ] CDN + 基础缓存

---

## Phase 3: 内容填充（Week 2）

### 3.1 核心页面
- [ ] 丰顺旅游攻略
- [ ] 温泉大全（丰顺最核心的旅游卖点）
- [ ] 美食地图
- [ ] 各镇介绍（16 个镇）

### 3.2 SEO 长尾页面
- AI 自动生成长尾关键词页面，例如：
  - "丰顺温泉哪家好"
  - "丰顺美食推荐"
  - "丰顺鹿湖温泉度假村攻略"
  - "丰顺一日游路线"

---

## Phase 4: 变现启动（Week 3-4）

### 4.1 商家合作
- [ ] 制作商家合作方案（PPT/单页）
- [ ] 联系 20 家核心商家（温泉酒店、景区、餐饮）
- [ ] 免费收录 → 体验增值功能 → 付费转化

### 4.2 导流合作
- [ ] 申请携程/美团分销联盟
- [ ] 温泉酒店预订链接嵌入

### 4.3 广告位预留
- [ ] 首页 Banner
- [ ] 分类页推荐位
- [ ] 详情页相关推荐

---

## Phase 5: 社区共建（Month 2+）

### 5.1 开源社区
- [ ] GitHub 开源仓库
- [ ] 贡献指南
- [ ] 数据贡献机制（PR 提交商家信息）

### 5.2 本地推广
- [ ] 丰顺本地微信群推广
- [ ] 与丰顺自媒体合作
- [ ] 本地论坛/贴吧

### 5.3 模式复制
- [ ] 文档化整套流程
- [ ] 复制到梅州市其他县（大埔、蕉岭、平远等）

---

## 关键指标 (KPIs)

| 阶段 | 目标 | 时间 |
|------|------|------|
| Phase 1 | 1000+ 条商家数据 | 3 天 |
| Phase 2 | MVP 网站上线 | 7 天 |
| Phase 3 | 50+ 内容页面 | 14 天 |
| Phase 4 | 10 家付费商家 | 30 天 |
| Phase 5 | 日 UV 500+ | 60 天 |
