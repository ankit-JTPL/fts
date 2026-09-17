/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "../templates/**/*.html",
    "../**/templates/**/*.html",
    "../static/**/*.js",
    "../static/**/*.css"
  ],
  theme: {
    screens: {
      'sm': '567px',   // mobile
      'md': '768px',   // Small Tablets
      'lg': '1024px',  // Small Laptops
      'xl': '1280px',  // Laptops/Desktops
      '2xl': '1400px', // large screen
    },
    extend: {},
  },
  plugins: [],
}

