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
        this.pkg = this.fs.readJSON(this.destinationPath('package.json'), {});
        // Pre set the default props from the information we have at this point
        this.props = {
            name: this.pkg.name,
            description: this.pkg.description,
            version: this.pkg.version,
            homepage: this.pkg.homepage,
            repositoryName: this.options.repositoryName
        };

        if(this.options.customer){
            this.props.customer = this.options.customer;
        }
    }

    _askFor() {
        const prompts = [{
            type: 'input',
            name: 'customer',
            message: 'Your customer (project) name?',
            default: path.basename(process.cwd()),
            when: !this.props.customer
        }];
        return this.prompt(prompts).then(props => {
            this.props = extend(this.props, props);
            this.props.customerSafeName = _.camelCase(this.props.customer);
            this.props.root = process.cwd();
        });
    }

    prompting() {

        // Have Yeoman greet the user.
        this.log(yosay(
            'Welcome to the fabulous ' + chalk.red('ps-boilerplate-project') + ' generator!'
        ));

        return this._askFor();
    }

    default () {
        
    }

    writing() {
        // const templatePkg = this.fs.readJSON(this.templatePath('package.json'), {});
        const templateObj = {
            customerSafeName: this.props.customerSafeName,
            capitalizeCustomerSafeName: this.props.customerSafeName.replace(/\b\w/g, l => l.toUpperCase())
        }

        // Copy all files
        this.fs.copyTpl(
            this.templatePath('*'),
            this.destinationRoot(),
            templateObj
        );

        this.composeWith(require.resolve('generator-ps-iow/generators/app'), {
            customer: this.props.customer,
            root: this.props.root
        })

        this.composeWith(require.resolve('generator-ps-search-ui-sfdc/generators/app'), {
            customer: this.props.customer,
            root: this.props.root
        })
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