const gulp = require('gulp');
const log = require('fancy-log');
const webpack = require('webpack');
const webpackSettings = require('../webpack.prod.config');
const clean = require('./clean.tasks').clean;
const metadata = require('./metadata.tasks').metadata;
const compute = require('./compute.tasks').compute;

const compile = async () => {
    var compiler = webpack(webpackSettings);

    return new Promise((resolve, reject) => {
        compiler.run((err, stats) => {
            if (err) {
                reject(err);
            }
            log('[webpack:build]', stats.toString({ chunks: false, colors: true }));
            if (stats.hasErrors()) {
                reject(new Error('Webpack compile with errors, check the webpack log for more information.'));
            }
            resolve();
        });
    })
};

const build = gulp.series(
    clean,
    compile,
    compute,
    metadata
);
build.displayName = 'build';

module.exports = {
    build: build,
};