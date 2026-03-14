/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    './src/pages/**/*.{js,ts,jsx,tsx,mdx}',
    './src/components/**/*.{js,ts,jsx,tsx,mdx}',
    './src/app/**/*.{js,ts,jsx,tsx,mdx}',
  ],
  theme: {
    extend: {
      colors: {
        'fengshun': {
          50: '#fef7ee',
          100: '#fdecd7',
          200: '#fad5ae',
          300: '#f6b77b',
          400: '#f19046',
          500: '#ed7421',
          600: '#de5a17',
          700: '#b84315',
          800: '#933619',
          900: '#772f18',
        }
      }
    },
  },
  plugins: [],
}
