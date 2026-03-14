export interface Business {
  name: string
  category: string
  subcategory: string
  town: string
  address: string
  phone: string
  description: string
  price_range: string
  rating: number
  tags: string[]
  source: string
}

export interface Category {
  id: string
  name: string
  icon: string
  count: number
}

export interface Town {
  id: string
  name: string
  count: number
}

export const CATEGORIES: Record<string, { name: string; icon: string }> = {
  '餐饮': { name: '餐饮美食', icon: '🍜' },
  '住宿': { name: '住宿酒店', icon: '🏨' },
  '温泉': { name: '温泉养生', icon: '♨️' },
  '旅游': { name: '旅游景点', icon: '🏞️' },
  '医疗': { name: '医疗健康', icon: '🏥' },
  '生活服务': { name: '生活服务', icon: '🏪' },
  '购物': { name: '购物消费', icon: '🛒' },
  '教育': { name: '教育培训', icon: '🎓' },
  '政务': { name: '政务办事', icon: '🏛️' },
}

export const TOWNS = [
  '汤坑镇', '丰良镇', '潘田镇', '黄金镇', '留隍镇',
  '潭江镇', '汤南镇', '埔寨镇', '北斗镇', '八乡山镇',
  '建桥镇', '龙岗镇', '大龙华镇', '小胜镇', '砂田镇', '潭山镇'
]
