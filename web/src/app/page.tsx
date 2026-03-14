import { getStats } from '@/data/businesses'
import { CATEGORIES, TOWNS } from '@/data/types'
import SearchBar from '@/components/SearchBar'
import BusinessCard from '@/components/BusinessCard'
import { getBusinesses } from '@/data/businesses'

export default function Home() {
  const stats = getStats()
  const featured = getBusinesses().filter(b => b.rating >= 4.5).slice(0, 6)

  return (
    <div>
      {/* Hero Section */}
      <section className="hero-gradient text-white py-16 md:py-24">
        <div className="max-w-6xl mx-auto px-4 text-center">
          <h1 className="text-4xl md:text-5xl font-bold mb-4">
            丰顺人的生活指南
          </h1>
          <p className="text-xl md:text-2xl opacity-90 mb-8">
            温泉 · 美食 · 旅游 · 商家 — 开源共建，一网打尽
          </p>
          <SearchBar />
          <div className="mt-6 text-sm opacity-80">
            已收录 <strong>{stats.totalBusinesses}</strong> 家商家 · 覆盖 <strong>{stats.totalTowns}</strong> 个镇
          </div>
        </div>
      </section>

      {/* Categories */}
      <section className="max-w-6xl mx-auto px-4 py-12">
        <h2 className="text-2xl font-bold mb-6 text-gray-800">📂 分类导航</h2>
        <div className="grid grid-cols-3 md:grid-cols-5 lg:grid-cols-9 gap-3">
          {Object.entries(CATEGORIES).map(([id, cat]) => {
            const count = stats.categories[id] || 0
            return (
              <a
                key={id}
                href={`/category/${encodeURIComponent(id)}`}
                className="bg-white rounded-xl p-4 text-center card-hover shadow-sm border border-gray-100"
              >
                <div className="category-icon">{cat.icon}</div>
                <div className="text-sm font-medium text-gray-700">{cat.name}</div>
                {count > 0 && (
                  <div className="text-xs text-gray-400 mt-1">{count} 家</div>
                )}
              </a>
            )
          })}
        </div>
      </section>

      {/* 快捷入口 */}
      <section className="max-w-6xl mx-auto px-4 py-8">
        <h2 className="text-2xl font-bold mb-6 text-gray-800">⚡ 生活服务</h2>
        <div className="grid grid-cols-2 md:grid-cols-4 gap-4">
          <a href="/koubei.html" className="bg-white rounded-xl p-5 shadow-sm border border-gray-100 hover:shadow-md transition-shadow">
            <div className="text-3xl mb-2">📖</div>
            <div className="font-semibold text-gray-800">口碑簿</div>
            <div className="text-xs text-gray-500 mt-1">乡亲真实推荐</div>
          </a>
          <a href="/yellowpages.html" className="bg-white rounded-xl p-5 shadow-sm border border-gray-100 hover:shadow-md transition-shadow">
            <div className="text-3xl mb-2">📞</div>
            <div className="font-semibold text-gray-800">丰顺黄页</div>
            <div className="text-xs text-gray-500 mt-1">政务·医疗·银行·快递</div>
          </a>
          <a href="/guide.html" className="bg-white rounded-xl p-5 shadow-sm border border-gray-100 hover:shadow-md transition-shadow">
            <div className="text-3xl mb-2">📋</div>
            <div className="font-semibold text-gray-800">办事指南</div>
            <div className="text-xs text-gray-500 mt-1">怎么办·去哪办·带什么</div>
          </a>
          <a href="/submit.html" className="bg-white rounded-xl p-5 shadow-sm border border-gray-100 hover:shadow-md transition-shadow">
            <div className="text-3xl mb-2">✍️</div>
            <div className="font-semibold text-gray-800">共建提交</div>
            <div className="text-xs text-gray-500 mt-1">推荐商家/地点</div>
          </a>
        </div>
      </section>

      {/* Featured */}
      <section className="max-w-6xl mx-auto px-4 py-8">
        <h2 className="text-2xl font-bold mb-6 text-gray-800">⭐ 精选推荐</h2>
        <div className="grid md:grid-cols-2 lg:grid-cols-3 gap-4">
          {featured.map((b, i) => (
            <BusinessCard key={i} business={b} />
          ))}
        </div>
      </section>

      {/* Towns */}
      <section className="max-w-6xl mx-auto px-4 py-12">
        <h2 className="text-2xl font-bold mb-6 text-gray-800">📍 按镇浏览</h2>
        <div className="flex flex-wrap gap-2">
          {TOWNS.map(town => {
            const count = stats.towns[town] || 0
            return (
              <a
                key={town}
                href={`/town/${encodeURIComponent(town)}`}
                className={`px-4 py-2 rounded-full text-sm border transition-colors ${
                  count > 0
                    ? 'bg-fengshun-50 border-fengshun-200 text-fengshun-700 hover:bg-fengshun-100'
                    : 'bg-gray-50 border-gray-200 text-gray-400'
                }`}
              >
                {town} {count > 0 && `(${count})`}
              </a>
            )
          })}
        </div>
      </section>

      {/* About */}
      <section className="max-w-6xl mx-auto px-4 py-12">
        <div className="bg-gradient-to-r from-orange-50 to-amber-50 rounded-2xl p-8 border border-orange-100">
          <h2 className="text-2xl font-bold mb-4 text-gray-800">🦞 关于开源丰顺</h2>
          <p className="text-gray-600 mb-4">
            开源丰顺是一个用 AI + 开源技术打造的丰顺县本地生活目录。
            我们相信信息应该自由流通，帮助丰顺人和游客更好地发现这座美丽的"中国温泉之城"。
          </p>
          <div className="flex flex-wrap gap-4 text-sm">
            <a href="https://github.com/openfengshun" className="text-fengshun-600 hover:underline">
              ⭐ GitHub 开源
            </a>
            <a href="/category" className="text-fengshun-600 hover:underline">
              📂 浏览全部分类
            </a>
            <a href="/town" className="text-fengshun-600 hover:underline">
              📍 浏览全部乡镇
            </a>
          </div>
        </div>
      </section>
    </div>
  )
}
