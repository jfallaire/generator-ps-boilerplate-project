
const webpackConfig = require('./webpack.test.config');
require('dotenv-defaults').config();

// process.env.CHROME_BIN = require('puppeteer').executablePath()

const configuration = {
  singleRun: true,
  port:9876,
  customLaunchers: {
    ChromeHeadlessCustom: {
      base: 'ChromeHeadless',
      flags: ['--no-sandbox']
    }
  },
  browsers: ['ChromeHeadlessCustom'],
  frameworks: ['jasmine'],
  browserDisconnectTimeout: 120000,
  browserNoActivityTimeout: 120000,
  captureTimeout: 120000,
  processKillTimeout: 120000,
  browserDisconnectTolerance: 10,
  files: [
    { pattern: 'node_modules/coveo-search-ui/bin/js/CoveoJsSearch.js', watched: false },
    { pattern: 'test/test.ts', watched: true }
  ],
  preprocessors: {
    'test/test.ts': ['webpack', 'sourcemap', 'coverage']
  },
  // logLevel: 'OFF',
  webpack: webpackConfig,
  webpackMiddleware: {
    stats: 'errors-only',
    logLevel: 'silent'
  },
  plugins: [
    'karma-webpack',
    'karma-jasmine',
    'karma-coverage',
    'karma-chrome-launcher',
    'karma-sourcemap-loader',
    'karma-mocha-reporter',
  ],
  reporters: ['mocha', 'coverage'],
  coverageReporter: {
    dir: './dist/reports/coverage',
    reporters: [
      { type: 'html', subdir: 'report-html' },
      { type: 'lcov', subdir: 'report-lcov' }
    ]
  }
}

module.exports = function(config) {
  config.set(configuration);
}
