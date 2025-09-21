module.exports = {
  content: [
    './layouts/**/*.html',
    './content/**/*.md',
    './hugo_stats.json'
  ],
  safelist: [
    // Critical navigation classes that must never be purged
    'sr-only',
    'sticky',
    'top-0',
    'z-30',
    'order-0',
    'order-1',
    'order-3',

    // Add other critical classes if needed
    'header',
    'navbar',
    'nav-link',
    'nav-item'
  ],
  theme: {
    extend: {},
  },
  plugins: [],
}