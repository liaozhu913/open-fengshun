'use client'

import { useSearchParams } from 'next/navigation'
import { Suspense } from 'react'
import { searchBusinesses } from '@/data/businesses'
import BusinessCard from '@/components/BusinessCard'

function SearchResults() {
  const searchParams = useSearchParams()
  const query = searchParams.get('q') || ''
  const results = query ? searchBusinesses(query) : []

  return (
    <div className="max-w-6xl mx-auto px-4 py-8">
      <div className="mb-8">
        <a href="/" className="text-fengshun-600 hover:underline text-sm">← 返回首页</a>
        <h1 className="text-3xl font-bold mt-2 text-gray-800">
          🔍 搜索：{query}
        </h1>
        <p className="text-gray-500 mt-1">找到 {results.length} 个结果</p>
      </div>

      {results.length > 0 ? (
        <div className="grid md:grid-cols-2 lg:grid-cols-3 gap-4">
          {results.map((b, i) => (
            <BusinessCard key={i} business={b} />
          ))}
        </div>
      ) : (
        <div className="text-center py-16 text-gray-400">
          <p className="text-4xl mb-4">🔍</p>
          <p>没有找到相关结果，换个关键词试试？</p>
        </div>
      )}
    </div>
  )
}

export default function SearchPage() {
  return (
    <Suspense fallback={<div className="text-center py-16">搜索中...</div>}>
      <SearchResults />
    </Suspense>
  )
}
