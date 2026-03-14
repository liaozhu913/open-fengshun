#!/usr/bin/env python3
import json
import os

script_dir = os.path.dirname(os.path.abspath(__file__))
data_path = os.path.join(script_dir, '../data/businesses.json')
ts_path = os.path.join(script_dir, '../web/src/data/businesses.ts')

with open(data_path, 'r') as f:
    data = json.load(f)

businesses = data['businesses']

ts_content = f'''import {{ Business }} from './types'

export const BUSINESSES: Business[] = {json.dumps(businesses, ensure_ascii=False, indent=2)}

export function getBusinesses(): Business[] {{
  return BUSINESSES
}}

export function getBusinessesByCategory(category: string): Business[] {{
  return BUSINESSES.filter(b => b.category === category)
}}

export function getBusinessesByTown(town: string): Business[] {{
  return BUSINESSES.filter(b => b.town === town)
}}

export function searchBusinesses(query: string): Business[] {{
  const q = query.toLowerCase()
  return BUSINESSES.filter(b =>
    b.name.toLowerCase().includes(q) ||
    b.description.toLowerCase().includes(q) ||
    b.category.toLowerCase().includes(q) ||
    b.town.toLowerCase().includes(q) ||
    b.tags.some(t => t.toLowerCase().includes(q))
  )
}}

export function getStats() {{
  const categories = new Set(BUSINESSES.map(b => b.category))
  const towns = new Set(BUSINESSES.map(b => b.town))
  return {{
    totalBusinesses: BUSINESSES.length,
    totalCategories: categories.size,
    totalTowns: towns.size,
  }}
}}
'''

with open(ts_path, 'w') as f:
    f.write(ts_content)

print(f'✅ Updated businesses.ts with {len(businesses)} records')
