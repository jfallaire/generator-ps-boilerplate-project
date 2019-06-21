const merge = require('webpack-merge');
const common = require('./webpack.common.config.js');
const path = require('path');
const session = require('express-session');
const middleware = require('./utils/middleware');
const MiniCssExtractPlugin = require('mini-css-extract-plugin');

module.exports = merge(common, {
  mode: 'development',
  devtool: 'inline-source-map',
  devServer: {
    stats: {
      colors: true
    },
    watchOptions: {
      poll:true
    },
    writeToDisk: true,
    contentBase: [
        path.join(__dirname, 'dist'),
        path.join(__dirname, 'node_modules/@salesforce-ux/design-system'),
        path.join(__dirname, 'src/vendor/CoveoV2')
    ],
    publicPath: '/assets/',
    compress: true,
    host: process.env.SERVER_IP_ADDRESS,
    port: process.env.SERVER_PORT,
    before(app) {
      app.set('view engine', 'ejs');
      app.use(session({ secret: 'keyboard cat', resave: true, saveUninitialized: false, cookie: { maxAge: 3600*1000 } }));
      app.use(require(path.resolve('./routes/errors')));
      app.use(require(path.resolve('./routes/pages')));
      app.use(middleware.errorHandling);
    }
  },
  module: {
    rules: [
      {
        test: /\.scss$/,
        exclude: /node_modules/,
        use: [
          'style-loader',
          {
            loader: MiniCssExtractPlugin.loader,
            options: {
              hmr: true
            }
          },
          'css-loader',
          'sass-loader'
        ]
      }
    ]
  }
});

