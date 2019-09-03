const path = require('path');
require('dotenv-defaults').config();
const CleanWebpackPlugin = require('clean-webpack-plugin');
const MiniCssExtractPlugin = require('mini-css-extract-plugin');
var test = `${}`
const plugins = [
  new CleanWebpackPlugin(),
  new MiniCssExtractPlugin({
    filename: './css/[name].css'
  })
]
const entries = {
  'local': [path.join(__dirname, 'src/stylesheets/local.scss')],
  '<%= customerSafeName %>.bundle': [path.join(__dirname, 'src/typescripts/Index.ts')],
  <% for (var i = 0; i < auraComponentSamples.length; i++) { %>
  '<%=auraComponentSamples[i]%>': [path.join(__dirname, 'src/stylesheets/<%=auraComponentSamples[i]%>.scss')],
  <% } %>
};

module.exports = {
  entry: entries,
  output: {
    // See SwapVar.ts as for why this need to be a temporary variable
    library: '<%=`Coveo${capitalizeCustomerSafeName}Extension` %>',
    libraryTarget: 'umd',
    path: path.join(__dirname, 'dist'),
    publicPath: '/assets/',
    filename: `./js/[name].js`
  },
  resolve: {
    extensions: ['.tsx', '.ts', '.js', '.svg', '.scss'],
    alias: {
      svg: path.resolve('./src/images/svg'),
      sass: path.resolve('./src/stylesheets')
    }
  },
  externals: {
    'coveo-search-ui': 'Coveo',
    underscore: '_'
  },
  plugins: plugins,
  module: {
    rules: [{
        test: /\.(png|jpg|gif)$/,
        use: [{
          loader: 'file-loader',
          options: {
            name: 'images/[name].[ext]'
          }
        }]
      },
      {
        test: /\.(ttf|eot|woff|woff2|otf)$/,
        loader: 'file-loader',
        options: {
          name: 'fonts/[name].[ext]'
        }
      },
      {
        test: /cultures.*\.(js)$/,
        loader: 'file-loader',
        exclude: /node_modules/,
        options: {
          name: 'js/cultures/[name].[ext]'
        }
      },
      {
        test: /\.tsx?$/,
        loader: 'ts-loader',
        exclude: /node_modules/
      },
      {
        test: /\.css$/,
        use: ['style-loader', 'css-loader']
      },
      {
        test: /\.svg$/,
        exclude: /node_modules/,
        use: [{
          loader: 'svg-inline-loader'
        }]
      }
    ]
  }
};
