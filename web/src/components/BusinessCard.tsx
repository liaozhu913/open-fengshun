import { Business, CATEGORIES } from '@/data/types'

export default function BusinessCard({ business }: { business: Business }) {
  const cat = CATEGORIES[business.category] || { name: business.category, icon: '📌' }

  return (
    <div className="bg-white rounded-xl p-5 shadow-sm border border-gray-100 card-hover">
      <div className="flex items-start justify-between mb-2">
        <div className="flex items-center space-x-2">
          <span className="text-xl">{cat.icon}</span>
          <span className="text-xs text-gray-400">{business.subcategory}</span>
        </div>
        <div className="flex items-center space-x-1 text-amber-500">
          <span>⭐</span>
          <span className="text-sm font-medium">{business.rating}</span>
        </div>
      </div>

      <h3 className="font-bold text-lg text-gray-800 mb-1">{business.name}</h3>

      <p className="text-gray-500 text-sm mb-2">📍 {business.town}</p>

      <p className="text-gray-600 text-sm mb-3 line-clamp-2">{business.description}</p>

      <div className="flex flex-wrap mb-3">
        {business.tags.slice(0, 3).map(tag => (
          <span key={tag} className="tag">{tag}</span>
        ))}
      </div>

      <div className="flex items-center justify-between text-sm">
        {business.price_range && (
          <span className="text-fengshun-600 font-medium">💰 {business.price_range}</span>
        )}
        {business.phone && (
          <a href={`tel:${business.phone}`} className="text-blue-500 hover:underline">
            📞 {business.phone}
          </a>
        )}
      </div>
    </div>
  )
}
