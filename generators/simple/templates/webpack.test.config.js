
const path = require('path');
require('dotenv-defaults').config();

module.exports = {
  mode: 'development',
  entry: {
    'test': [path.join(__dirname, 'test/test.ts')]
  },
  target: 'node',
  devtool: 'inline-source-map',
  output: {
    library: '<%= customerSafeName %>test',
    libraryTarget: 'var',
    path: path.join(__dirname, 'dist/tests'),
    filename: `[name].js`
  },
  resolve: {
    extensions: ['.tsx', '.ts', '.js'],
  },
  externals: {
    'coveo-search-ui': 'Coveo',
    underscore: '_'
  },
  module: {
    rules: [
      {
        test: /\.tsx?$/,
        loader: 'ts-loader',
        exclude: /node_modules/
      }
    ]
  }
};
