const merge = require('webpack-merge');
const path = require('path');
const common = require('./webpack.common.config.js');
const TerserJSPlugin = require('terser-webpack-plugin');
const MiniCssExtractPlugin = require('mini-css-extract-plugin');
const OptimizeCSSAssetsPlugin = require('optimize-css-assets-webpack-plugin');

// your production entries here
const entries = {
  'local.min': [path.join(__dirname, 'src/stylesheets/local.scss')],
  '<%= customerSafeName %>.bundle.min': [path.join(__dirname, 'src/typescripts/Index.ts')],
};

const plugins = [
];

module.exports = merge(common, {
  mode: 'production',
  entry: entries,
  plugins: plugins,
  optimization: {
    minimizer: [
      new TerserJSPlugin({ test: /\.min\.js$/i }),
      new OptimizeCSSAssetsPlugin({ assetNameRegExp: /\.min\.css$/i })
    ]
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
              hmr: false
            }
          },
          'css-loader',
          'sass-loader'
        ]
      }
    ]
  }
});