const gulp = require('gulp');
const PluginError = require('plugin-error');
const opn = require('opn');

const webpack = require('webpack');
const WebpackDevServer = require('webpack-dev-server');
const webpackSettings = require('../webpack.dev.config');

const dev = () => {
    const compiler = webpack(webpackSettings);
    const devServer = new WebpackDevServer(compiler, webpackSettings.devServer);
    devServer.listen(webpackSettings.devServer.port, webpackSettings.devServer.host, err => {
        if (err) throw new PluginError('webpack-dev-server', err);
    });
    opn(`http://${webpackSettings.devServer.host}:${webpackSettings.devServer.port}`, { wait: false })
};

module.exports = {
    dev: dev
}