'use client'

import { useState } from 'react'
import { useRouter } from 'next/navigation'

export default function SearchBar() {
  const [query, setQuery] = useState('')
  const router = useRouter()

  const handleSearch = (e: React.FormEvent) => {
    e.preventDefault()
    if (query.trim()) {
      router.push(`/search?q=${encodeURIComponent(query.trim())}`)
    }
  }

  return (
    <form onSubmit={handleSearch} className="max-w-xl mx-auto">
      <div className="relative">
        <input
          type="text"
          value={query}
          onChange={(e) => setQuery(e.target.value)}
          placeholder="搜索商家、景点、美食...（如：温泉、捆粄、瀑布）"
          className="w-full px-6 py-4 rounded-full text-gray-800 text-lg shadow-lg focus:outline-none focus:ring-4 focus:ring-orange-200"
        />
        <button
          type="submit"
          className="absolute right-2 top-1/2 -translate-y-1/2 bg-fengshun-500 hover:bg-fengshun-600 text-white px-6 py-2 rounded-full transition-colors"
        >
          搜索
        </button>
      </div>
    </form>
  )
}
