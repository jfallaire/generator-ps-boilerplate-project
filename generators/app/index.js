'use strict';
const path = require('path');
const Generator = require('yeoman-generator');
const askName = require('inquirer-npm-name');
const _ = require('lodash');
const extend = require('deep-extend');
const mkdirp = require('mkdirp');
const chalk = require('chalk');
const yosay = require('yosay');

module.exports = class extends Generator {

    initializing() {
        this.props = {};
    }

    prompting() {
        // Have Yeoman greet the user.
        this.log(yosay(
            'Welcome to the fabulous ' + chalk.red('ps-boilerplate-project') + ' generator!'
        ));

        var prompts = [
            {
                type: 'input',
                name: 'customer',
                message: 'Your customer (project) name?',
                default: path.basename(process.cwd())
            }
        ];

        return this.prompt(prompts).then(function (props) {
            this.props = props;
            this.props.repoName = utils.makeRepoName(this.props.customer);
            // this.props.customerSafeName = _.snakeCase(this.props.customer);
            this.props.customerSafeName = _.camelCase(this.props.customer);
        }.bind(this));

    }

    default () {
        if (path.basename(this.destinationPath()) !== this.props.repoName) {
            this.log(
                'You must be inside a folder named ' + this.props.repoName + '\n' +
                'I\'ll automatically create this folder.'
            );
            mkdirp(this.props.repoName);
            this.destinationRoot(this.destinationPath(this.props.repoName));
        }

        this.composeWith(require.resolve('generator-ps-search-ui-sfdc/generators/app'), {})
        this.composeWith(require.resolve('generator-ps-iow/generators/app'), {})
    }

    writing() {
        // const pkg = this.fs.readJSON(this.destinationPath('package.json'), {});
        // const templatePkg = this.fs.readJSON(this.templatePath('package.json'), {});
        // const templateObj = {
        //     customerSafeName: this.props.customerSafeName,
        //     capitalizeCustomerSafeName: this.props.customerSafeName.replace(/\b\w/g, l => l.toUpperCase())
        // }

        // extend(pkg, {
        //     dependencies: templatePkg.dependencies,
        //     devDependencies: templatePkg.devDependencies,
        //     keywords: templatePkg.keywords,
        //     main: templatePkg.main,
        //     engines: templatePkg.engines,
        //     eslintConfig: templatePkg.eslintConfig
        // });

        // // overwrite default scripts by template ones
        // pkg.scripts = templatePkg.scripts

        // this.fs.writeJSON(this.destinationPath('package.json'), pkg);

        // Copy all dotfiles
        this.fs.copyTpl(
            this.templatePath('.*'),
            this.destinationRoot()
        );
    }

    install() {
        this.log(this.props);
        // make sure to overwrite gulpfile with our template before installation.
        const templateObj = {
            customerSafeName: this.props.customerSafeName,
            capitalizeCustomerSafeName: this.props.customerSafeName.replace(/\b\w/g, l => l.toUpperCase())
        }
    }

    end() {

    }
};