import { Business } from './types'

// All data embedded for static generation
const BUSINESSES: Business[] = [
  {"name":"鹿湖温泉度假村","category":"温泉","subcategory":"度假村","town":"留隍镇","address":"丰顺县留隍镇","phone":"","description":"国家AAAA旅游景区，东南亚园林式建筑，客家文化主题，21个特色温泉池，别墅配私家温泉池，主打氢温泉养生。","price_range":"640+","rating":4.8,"tags":["AAAA景区","高端","别墅私汤","氢温泉"],"source":"web_crawl"},
  {"name":"金德宝凯悦国际温泉度假酒店","category":"住宿","subcategory":"四星级酒店","town":"汤坑镇","address":"丰顺县汤坑镇","phone":"","description":"四星级，巴厘岛风情，92℃高温硫磺泉，40多个户外温泉池，配备儿童乐园、SPA会所。","price_range":"600-1200","rating":4.7,"tags":["四星","巴厘岛风情","亲子","硫磺泉"],"source":"web_crawl"},
  {"name":"千江温泉酒店","category":"住宿","subcategory":"四星级酒店","town":"汤坑镇","address":"丰顺县汤坑镇新城区","phone":"","description":"四星级，客家草药蒸汽房，近市中心，性价比高。","price_range":"150-300","rating":4.5,"tags":["四星","性价比","客家草药"],"source":"web_crawl"},
  {"name":"御逸温泉度假村","category":"温泉","subcategory":"度假村","town":"汤坑镇","address":"丰顺县","phone":"","description":"国家AAA景区，半山悬崖药浴池，碳酸氢钠泉，水温55-65℃，配套水上乐园。","price_range":"300-600","rating":4.5,"tags":["AAA景区","悬崖药浴","水上乐园","亲子"],"source":"web_crawl"},
  {"name":"宝丰温泉酒店","category":"住宿","subcategory":"温泉酒店","town":"汤坑镇","address":"丰顺县梅汕高速出口附近","phone":"","description":"400多米深氡温泉，30多个空中温泉池，2000平方米室内空中SPA温泉。","price_range":"200-400","rating":4.4,"tags":["氡温泉","空中温泉","商务"],"source":"web_crawl"},
  {"name":"维纳斯国际酒店","category":"住宿","subcategory":"高档酒店","town":"汤坑镇","address":"丰顺县华茂","phone":"","description":"屋顶无边泳池，免费接站，获评丰顺高档酒店榜No.1。","price_range":"300-500","rating":4.6,"tags":["无边泳池","免费接站","高档"],"source":"web_crawl"},
  {"name":"龙归寨瀑布","category":"旅游","subcategory":"自然景观","town":"汤坑镇","address":"丰顺县汤坑镇","phone":"","description":"国家AAA景区，粤东第一瀑。落差115-125米，晴天常现彩虹。门票约50元。","price_range":"50","rating":4.6,"tags":["AAA景区","瀑布","粤东第一瀑"],"source":"web_crawl"},
  {"name":"八乡山大峡谷","category":"旅游","subcategory":"自然景观","town":"八乡山镇","address":"丰顺县八乡山镇","phone":"","description":"国家AAA景区，天然氧吧，全长3.5公里，森林覆盖率90%以上。门票约45元。","price_range":"45","rating":4.5,"tags":["AAA景区","峡谷","避暑","徒步"],"source":"web_crawl"},
  {"name":"铜鼓峰","category":"旅游","subcategory":"自然景观","town":"砂田镇","address":"丰顺县砂田镇","phone":"","description":"粤东第一峰，海拔1559.5米。赏日出、云海、风车群。免费。","price_range":"免费（停车20元）","rating":4.7,"tags":["粤东第一峰","云海","日出","徒步"],"source":"web_crawl"},
  {"name":"韩山历史文化生态区","category":"旅游","subcategory":"文化景区","town":"丰良镇","address":"丰顺县丰良镇","phone":"","description":"国家AAAA景区，因韩愈驻足得名，融合茶园风光、历史文化。","price_range":"","rating":4.6,"tags":["AAAA景区","文化","茶园","避暑"],"source":"web_crawl"},
  {"name":"种玊上围","category":"旅游","subcategory":"人文景观","town":"汤坑镇","address":"丰顺县汤坑镇","phone":"","description":"粤东独特古寨堡，360余年历史，方形围屋结构。","price_range":"免费","rating":4.3,"tags":["古寨","客家建筑","历史"],"source":"web_crawl"},
  {"name":"万佛园（丰顺公园）","category":"旅游","subcategory":"公园","town":"汤坑镇","address":"丰顺县汤坑镇","phone":"","description":"县城休闲地标，含中华龙、观音阁、九曲桥。","price_range":"免费","rating":4.2,"tags":["公园","休闲","爬山"],"source":"web_crawl"},
  {"name":"龙鲸河漂流景区","category":"旅游","subcategory":"体验项目","town":"黄金镇","address":"丰顺县黄金镇","phone":"","description":"国家AAA景区，龙鲸河漂流，夏季热门项目。","price_range":"","rating":4.4,"tags":["AAA景区","漂流","夏季"],"source":"web_crawl"},
  {"name":"埔寨火龙","category":"旅游","subcategory":"非遗文化","town":"埔寨镇","address":"丰顺县埔寨镇","phone":"","description":"国家级非遗，元宵节铁水金花表演，场面震撼。","price_range":"免费","rating":4.9,"tags":["非遗","火龙","元宵节","民俗"],"source":"web_crawl"},
  {"name":"金贵农庄","category":"餐饮","subcategory":"农家菜","town":"汤坑镇","address":"金贵大道田园好日子农庄北100米","phone":"0753-6682388","description":"特色农家菜，风味牛肉、焗猪肚为招牌。","price_range":"人均71元","rating":4.3,"tags":["农家菜","牛肉","焗猪肚"],"source":"web_crawl"},
  {"name":"鸿兴客家王","category":"餐饮","subcategory":"客家菜","town":"汤坑镇","address":"丰顺县汤坑镇","phone":"","description":"客家菜餐厅，全猪汤为招牌（25元/碗）。","price_range":"人均30-50","rating":4.2,"tags":["客家菜","全猪汤"],"source":"web_crawl"},
  {"name":"汤坑捆粄（丰顺总店）","category":"餐饮","subcategory":"客家小吃","town":"汤坑镇","address":"丰顺县汤坑镇东山路","phone":"","description":"客家传统小吃，捆粄、牛肉丸汤、菜粿。早餐推荐。","price_range":"人均10-20","rating":4.4,"tags":["捆粄","客家小吃","早餐"],"source":"web_crawl"},
  {"name":"埔寨圆盘新鲜牛肉老店","category":"餐饮","subcategory":"牛肉火锅","town":"汤坑镇","address":"丰顺县世纪路5号","phone":"13825939116","description":"新鲜牛肉系列，牛肉火锅。埔寨牛肉在丰顺非常有名。","price_range":"人均50-80","rating":4.5,"tags":["牛肉火锅","埔寨牛肉","老字号"],"source":"web_crawl"},
  {"name":"辉程汤粉店","category":"餐饮","subcategory":"汤粉","town":"汤坑镇","address":"丰顺县汤坑镇","phone":"","description":"腌水牛肉、牛杂、牛百叶，水牛肉口感细嫩。","price_range":"人均15-30","rating":4.3,"tags":["汤粉","水牛肉","牛杂"],"source":"web_crawl"},
  {"name":"老杨兜汤","category":"餐饮","subcategory":"夜宵","town":"汤坑镇","address":"丰顺县汤坑镇","phone":"","description":"夜宵名店，牛肉兜汤15元/碗。","price_range":"15元/碗","rating":4.3,"tags":["夜宵","牛肉兜汤"],"source":"web_crawl"},
  {"name":"不可炸鸡（丰顺店）","category":"餐饮","subcategory":"炸鸡小吃","town":"汤坑镇","address":"锦江A区B栋19号","phone":"","description":"拉丝芝士球为特色，炸鸡套餐。","price_range":"人均20+","rating":4.1,"tags":["炸鸡","芝士球"],"source":"web_crawl"},
  {"name":"老苏南卤鹅饭店","category":"餐饮","subcategory":"潮汕菜","town":"汤坑镇","address":"丰顺县罗湖二路30号","phone":"","description":"潮汕风味，卤鹅为招牌。","price_range":"人均40-60","rating":4.2,"tags":["潮汕菜","卤鹅"],"source":"web_crawl"},
  {"name":"鸿香饭店","category":"餐饮","subcategory":"客家菜","town":"汤坑镇","address":"丰顺县汤坑镇","phone":"","description":"客家菜，盐焗鸡为招牌。","price_range":"人均40-60","rating":4.1,"tags":["客家菜","盐焗鸡"],"source":"web_crawl"},
  {"name":"汤坑老街薯粄","category":"餐饮","subcategory":"客家小吃","town":"汤坑镇","address":"丰顺县汤坑老街","phone":"","description":"传统客家小吃薯粄，5元/个。","price_range":"5元/个","rating":4.3,"tags":["薯粄","客家小吃","老街"],"source":"web_crawl"},
  {"name":"仙人粄（仙草冻）","category":"餐饮","subcategory":"甜品","town":"汤坑镇","address":"丰顺县汤坑镇","phone":"","description":"仙人粄（仙草冻），搭配蜂蜜，5元/碗。","price_range":"5元/碗","rating":4.2,"tags":["仙草冻","甜品","消暑"],"source":"web_crawl"},
  {"name":"丰顺县人民医院","category":"医疗","subcategory":"综合医院","town":"汤坑镇","address":"丰顺县汤坑镇","phone":"","description":"二级甲等综合医院，创建于1949年，开放床位350张。","price_range":"","rating":4.3,"tags":["二甲","综合医院","医保定点"],"source":"web_crawl"},
  {"name":"丰顺县中医院","category":"医疗","subcategory":"中医院","town":"汤坑镇","address":"丰顺县汤坑镇新院区","phone":"","description":"二级甲等公立中医院，开放床位300张，19个临床医技科室。","price_range":"","rating":4.2,"tags":["二甲","中医院","康复"],"source":"web_crawl"},
  {"name":"丰顺县妇幼保健院","category":"医疗","subcategory":"专科医院","town":"汤坑镇","address":"丰顺县汤坑镇","phone":"","description":"妇幼保健专科机构。","price_range":"","rating":4.0,"tags":["妇幼保健","专科"],"source":"web_crawl"},
  {"name":"留隍镇中心卫生院","category":"医疗","subcategory":"镇级卫生院","town":"留隍镇","address":"丰顺县留隍镇","phone":"","description":"挂丰顺县第二人民医院牌子。","price_range":"","rating":3.8,"tags":["卫生院"],"source":"web_crawl"},
  {"name":"邮储银行丰顺县支行","category":"生活服务","subcategory":"银行","town":"汤坑镇","address":"丰顺县汤坑镇花园街46-1号","phone":"","description":"网点面积310㎡，设智能服务区、理财洽谈区。","price_range":"","rating":4.0,"tags":["银行","邮储"],"source":"web_crawl"},
  {"name":"中国农业银行丰顺县支行","category":"生活服务","subcategory":"银行","town":"汤坑镇","address":"丰顺县汤坑镇大山背东山路19号","phone":"0753-6623151","description":"设智能服务区、财富管理区，支持存取款、开卡、生活缴费。","price_range":"","rating":4.0,"tags":["银行","农行"],"source":"web_crawl"},
  {"name":"丰顺农商银行","category":"生活服务","subcategory":"银行","town":"汤坑镇","address":"丰顺县汤坑镇","phone":"","description":"布放自助取款机45台、村居e支付POS机具282台。","price_range":"","rating":4.0,"tags":["银行","农商行","社保卡"],"source":"web_crawl"},
  {"name":"中国银行丰顺支行","category":"生活服务","subcategory":"银行","town":"汤坑镇","address":"丰顺县汤坑镇汤坑路43号","phone":"","description":"中国银行丰顺网点。","price_range":"","rating":3.9,"tags":["银行","中行"],"source":"web_crawl"},
]

export function getBusinesses(): Business[] {
  return BUSINESSES
}

export function getBusinessesByCategory(category: string): Business[] {
  return BUSINESSES.filter(b => b.category === category)
}

export function getBusinessesByTown(town: string): Business[] {
  return BUSINESSES.filter(b => b.town === town)
}

export function searchBusinesses(query: string): Business[] {
  const q = query.toLowerCase()
  return BUSINESSES.filter(b =>
    b.name.toLowerCase().includes(q) ||
    b.description.toLowerCase().includes(q) ||
    b.tags.some(t => t.toLowerCase().includes(q)) ||
    b.town.toLowerCase().includes(q) ||
    b.category.toLowerCase().includes(q)
  )
}

export function getStats() {
  const categories: Record<string, number> = {}
  const towns: Record<string, number> = {}

  for (const b of BUSINESSES) {
    categories[b.category] = (categories[b.category] || 0) + 1
    towns[b.town] = (towns[b.town] || 0) + 1
  }

  return {
    total: BUSINESSES.length,
    categories,
    towns,
    townCount: Object.keys(towns).length
  }
}
