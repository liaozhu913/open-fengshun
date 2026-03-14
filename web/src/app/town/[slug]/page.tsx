import { getBusinessesByTown } from '@/data/businesses'
import BusinessCard from '@/components/BusinessCard'

export default function TownPage({ params }: { params: { slug: string } }) {
  const town = decodeURIComponent(params.slug)
  const businesses = getBusinessesByTown(town)

  return (
    <div className="max-w-6xl mx-auto px-4 py-8">
      <div className="mb-8">
        <a href="/" className="text-fengshun-600 hover:underline text-sm">← 返回首页</a>
        <h1 className="text-3xl font-bold mt-2 text-gray-800">
          📍 {town}
        </h1>
        <p className="text-gray-500 mt-1">共 {businesses.length} 家商家</p>
      </div>

      {businesses.length > 0 ? (
        <div className="grid md:grid-cols-2 lg:grid-cols-3 gap-4">
          {businesses.map((b, i) => (
            <BusinessCard key={i} business={b} />
          ))}
        </div>
      ) : (
        <div className="text-center py-16 text-gray-400">
          <p className="text-4xl mb-4">🏗️</p>
          <p>该镇数据正在收集中，欢迎通过 GitHub 贡献！</p>
        </div>
      )}
    </div>
  )
}
