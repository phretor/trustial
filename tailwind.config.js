module.exports = {
  content: ["./layouts/**/*.html", "./content/**/*.md", "./hugo_stats.json"],
  safelist: [
    // Critical navigation classes that must never be purged
    "sr-only",
    "sticky",
    "top-0",
    "z-30",
    "order-0",
    "order-1",
    "order-3",

    // Add other critical classes if needed
    "header",
    "navbar",
    "nav-link",
    "nav-item",

    // Classes that may be inconsistently detected between environments
    "top-1/2",
    "left-1/2",
    "z-10",
    "m-3",
    "mr-5",
    "ml-2",
    "ml-auto",
    "hidden",
    "inline-flex",
    "h-6",
    "-translate-x-1/2",
    "-translate-y-1/2",
  ],
  theme: {
    extend: {},
  },
  plugins: [],
};
