import type { Config } from 'tailwindcss';

const config: Config = {
  content: [
    './pages/**/*.{js,ts,jsx,tsx,mdx}',
    './components/**/*.{js,ts,jsx,tsx,mdx}',
    './app/**/*.{js,ts,jsx,tsx,mdx}',
  ],
  theme: {
    extend: {
      colors: {
        primary: '#BFC5AB',
        backg: '#F1ECE9',
        secondary: '#F1ECE9F2',
        btn: '#b49384',
      },
      spacing: {
        '182': '44rem',
      },
    },
  },
  plugins: [],
};
export default config;
