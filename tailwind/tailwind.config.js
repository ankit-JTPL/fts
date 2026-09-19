/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "../templates/**/*.html",
    "../**/templates/**/*.html",
    "../static/**/*.js",
  ],

  theme: {
    screens: {
      sm: "567px",
      md: "768px",
      lg: "1024px",
      xl: "1280px",
      "2xl": "1400px",
    },

    extend: {},
  },

  plugins: [],
};