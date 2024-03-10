/** @type {import('tailwindcss').Config} */
export default {
  content: [
    "./index.html",
    "./src/**/*.{js,ts,jsx,tsx}",
  ],
  theme: {
    extend: {
      colors: {
        alpha: '#053e2f',
        bravo: '#065542',
        charlie: '#076e62',
        delta: '#098667',
        echo: '#0a9e97',
        gradient_alpha: 'rgba(0, 255, 234, 0.08)',
        gradient_bravo: 'rgba(61, 200, 255, 0.08)',
      },
      backgroundImage: {
        'radial-gradient': 'radial-gradient(var(--tw-gradient-stops))',
      },

      fontFamily: {
        'merri': ['Merriweather Sans', 'sans-serif'],
        'satoshi-regular': ['Satoshi-Regular', 'sans-serif'],
        'satoshi-bold': ['Satoshi-Bold', 'sans-serif'],
        'satoshi-medium': ['Satoshi-Medium', 'sans-serif'],
        'satoshi-black': ['Satoshi-Black', 'sans-serif'],
        'satoshi-light': ['Satoshi-Light', 'sans-serif'],
        'satoshi-italic': ['Satoshi-Italic', 'sans-serif'],
        'satoshi-bolditalic': ['Satoshi-BoldItalic', 'sans-serif'],
        'satoshi-mediumitalic': ['Satoshi-MediumItalic', 'sans-serif'],
        'satoshi-blackitalic': ['Satoshi-BlackItalic', 'sans-serif'],
        'satoshi-lightitalic': ['Satoshi-LightItalic', 'sans-serif']
      },
      animation: {
        'spin-slow': 'spin 5s linear infinite',
      },
    },
  },
  plugins: [
    function ({ addBase}) {
      addBase({
        '@font-face': [
          {
            fontFamily: 'Satoshi-Regular',
            fontStyle: 'normal',
            fontWeight: 'normal',
            src: `url('/fonts/satoshi/Satoshi-Regular.woff2') format('woff2'),
                  url('/fonts/satoshi/Satoshi-Regular.woff') format('woff')`,
          },
          {
            fontFamily: 'Satoshi-Bold',
            fontStyle: 'normal',
            fontWeight: 'bold',
            src: `url('/fonts/satoshi/Satoshi-Bold.woff2') format('woff2'),
                  url('/fonts/satoshi/Satoshi-Bold.woff') format('woff')`,
          },
          {
            fontFamily: 'Satoshi-Medium',
            fontStyle: 'normal',
            fontWeight: '500',
            src: `url('/fonts/satoshi/Satoshi-Medium.woff2') format('woff2'),
                  url('/fonts/satoshi/Satoshi-Medium.woff') format('woff')`,
          },
          {
            fontFamily: 'Satoshi-Italic',
            fontStyle: 'italic',
            fontWeight: 'normal',
            src: `url('/fonts/satoshi/Satoshi-Italic.woff2') format('woff2'),
                  url('/fonts/satoshi/Satoshi-Italic.woff') format('woff')`,
          },
          {
            fontFamily: 'Satoshi-Black',
            fontStyle: 'normal',
            fontWeight: '900',
            src: `url('/fonts/satoshi/Satoshi-Black.woff2') format('woff2'),
                  url('/fonts/satoshi/Satoshi-Black.woff') format('woff')`,
          },
          {
            fontFamily: 'Satoshi-Light',
            fontStyle: 'normal',
            fontWeight: '300',
            src: `url('/fonts/satoshi/Satoshi-Light.woff2') format('woff2'),
                  url('/fonts/satoshi/Satoshi-Light.woff') format('woff')`,
          },
          {
            fontFamily: 'Satoshi-Variable',
            fontStyle: 'normal',
            fontWeight: 'normal',
            fontVariationSettings: '"wght" 100, "wdth" 100',
            src: `url('/fonts/satoshi/Satoshi-Variable.woff2') format('woff2'),
                  url('/fonts/satoshi/Satoshi-Variable.woff') format('woff')`,
          },
          {
            fontFamily: 'Satoshi-BoldItalic',
            fontStyle: 'italic',
            fontWeight: 'bold',
            src: `url('/fonts/satoshi/Satoshi-BoldItalic.woff2') format('woff2'),
                  url('/fonts/satoshi/Satoshi-BoldItalic.woff') format('woff')`,
          },
          {
            fontFamily: 'Satoshi-MediumItalic',
            fontStyle: 'italic',
            fontWeight: '500',
            src: `url('/fonts/satoshi/Satoshi-MediumItalic.woff2') format('woff2'),
                  url('/fonts/satoshi/Satoshi-MediumItalic.woff') format('woff')`,
          },
          {
            fontFamily: 'Satoshi-LightItalic',
            fontStyle: 'italic',
            fontWeight: '300',
            src: `url('/fonts/satoshi/Satoshi-LightItalic.woff2') format('woff2'),
                  url('/fonts/satoshi/Satoshi-LightItalic.woff') format('woff')`,
          },
        ],
      });
    },
  ],
}