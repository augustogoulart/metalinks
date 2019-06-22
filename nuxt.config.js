import pkg from './package'

export default {
  mode: 'spa',

  /*
  ** Headers of the page
  */
  head: {
    title: pkg.name,
    meta: [
      { charset: 'utf-8' },
      { name: 'viewport', content: 'width=device-width, initial-scale=1' },
      { hid: 'description', name: 'description', content: pkg.description }
    ],
    link: [
      { rel: 'icon', type: 'image/x-icon', href: '/favicon.ico' }
    ]
  },

  /*
  ** Customize the progress-bar color
  */
  loading: { color: '#fff' },

  /*
  ** Global CSS
  */
  css: [
    '~/assets/css/tailwind.css'
  ],

  /*
  ** Plugins to load before mounting the App
  */
  plugins: [
  ],

  /*
  ** Nuxt.js modules
  */
  // modules: [
  //   '@nuxtjs/pwa',
  // ],

  /*
  ** Build configuration
  */
  build: {
    publicPath: '/static/_nuxt/',
    swURL: '/static/',
    postcss: {
      plugins: {
        tailwindcss: './tailwind.config.js'
      }
    },


    /*
    ** You can extend webpack config here
    */
    extend(config, ctx) {
    }
  }
}
