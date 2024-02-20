/** @type {import('tailwindcss').Config} */
module.exports = {
  darkMode:"class",
  content: ["./**/*.html"],
  theme: {
    extend: {
      colors: {
        // Using modern `rgb`
        white: 'rgb(var(--white) / <alpha-value>)',
        black: 'rgb(var(--black) / <alpha-value>)',
        primery: 'rgb(var(--orange) / <alpha-value>)',
        input: 'rgb(var(--input) / <alpha-value>)',

      }
    },
  },
  plugins: [],
}

