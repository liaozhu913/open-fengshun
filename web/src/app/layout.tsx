import type { Metadata } from 'next'
import './globals.css'

export const metadata: Metadata = {
  title: '开源丰顺 - 丰顺人的生活指南',
  description: '丰顺县最全本地生活目录。温泉、美食、旅游、商家信息一网打尽。开源共建，AI 驱动。',
  keywords: '丰顺,丰顺县,温泉,旅游,美食,客家,潮汕,梅州市,鹿湖温泉,铜鼓峰,埔寨火龙',
}

export default function RootLayout({
  children,
}: {
  children: React.ReactNode
}) {
  return (
    <html lang="zh-CN">
      <body className="font-sans">
        <nav className="bg-white shadow-sm sticky top-0 z-50">
          <div className="max-w-6xl mx-auto px-4 py-3 flex items-center justify-between">
            <a href="/" className="flex items-center space-x-2">
              <span className="text-2xl">🦞</span>
              <span className="font-bold text-xl text-fengshun-700">开源丰顺</span>
            </a>
            <div className="hidden md:flex space-x-6 text-gray-600">
              <a href="/" className="hover:text-fengshun-600">首页</a>
              <a href="/category" className="hover:text-fengshun-600">分类</a>
              <a href="/town" className="hover:text-fengshun-600">乡镇</a>
              <a href="https://github.com/openfengshun" target="_blank" className="hover:text-fengshun-600">GitHub</a>
            </div>
          </div>
        </nav>
        <main>{children}</main>
        <footer className="bg-gray-900 text-gray-400 py-8 mt-16">
          <div className="max-w-6xl mx-auto px-4 text-center">
            <p className="text-lg mb-2">🦞 开源丰顺 OpenFengshun</p>
            <p className="text-sm">丰顺人的生活指南 · 开源共建 · AI 驱动</p>
            <p className="text-xs mt-4">© 2026 OpenFengshun. 开源协议 MIT.</p>
          </div>
        </footer>
      </body>
    </html>
  )
}
