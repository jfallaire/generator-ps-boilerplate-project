const merge = require('webpack-merge');
const path = require('path');
const common = require('./webpack.common.config.js');
const TerserJSPlugin = require('terser-webpack-plugin');
const MiniCssExtractPlugin = require('mini-css-extract-plugin');
const OptimizeCSSAssetsPlugin = require('optimize-css-assets-webpack-plugin');
const MetadataUtils = require('./utils/metadata');

const entries = {
  'local.min': [path.join(__dirname, 'src/stylesheets/local.scss')],
  '<%= customerSafeName %>.bundle.min': [path.join(__dirname, 'src/typescripts/Index.ts')]
};

const vfComponents = {
  <% for (var i = 0; i < vfComponentSamples.length; i++) { %>
  '<%=vfComponentSamples[i]%>': { templatePath: path.resolve(__dirname, './views/partials/<%=vfComponentSamples[i]%>/search-interface.ejs'), templateData: {} },
  <% } %>
}

const plugins = [
  ...MetadataUtils.getComponentFilePlugins(vfComponents),
]

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