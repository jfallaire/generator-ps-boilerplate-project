'use strict';
const _ = require('lodash');
const path = require('path');
const extend = _.merge;
const Generator = require('yeoman-generator');
const utils = require('../../utils');

module.exports = class extends Generator {
  constructor(args, options) {
    super(args, options);

    this.option('customer', {
        type: String,
        required: true,
        desc:'Customer/Project name'
    });

    this.option('orgid', {
        type: String,
        required: false,
        default: 'searchuisamples',
        desc:'Coveo org id'
    });

    this.option('apiKey', {
        type: String,
        required: false,
        default: 'xx564559b1-0045-48e1-953c-3addd1ee4457',
        desc:'Coveo api key'
    });

    this.option('portNumber', {
        type: String,
        required: false,
        default: '3000',
        desc:'Port number on which your app is listening to'
    });
  }

  initializing(){
    this.props = {
      customerName: this.options.customer,
      customerSafeName: _.camelCase(this.options.customer),
      customerSnakeCase: _.snakeCase(this.options.customer),
      capitalizeCustomerSafeName: _.camelCase(this.options.customer).replace(/\b\w/g, l => l.toUpperCase()),
      orgid: this.options.orgid,
      apiKey: this.options.apiKey,
      portNumber: this.options.portNumber
    };
  }

  _readPkg() {
    return this.fs.readJSON(this.destinationPath('package.json'), {});
  }

  writing() {
    const pkg = this._readPkg();
    const templatePkg = this.fs.readJSON(this.templatePath('package.json'), {});

    let tagNameParts = this.props.coveo_latest_tag_name.split('.');
    if(tagNameParts[0] != '2'){
        this.log('***WARNING***: this project generator does not support the current Coveo latest version : ' +  this.props.coveo_latest_tag_name);
    }

    const templateObj = extend(this.props, {        
        coveoSearchUIVersion: `${tagNameParts[0]}.${tagNameParts[1]}`
    });
    
    // Copy simple configuration files
    this.fs.copyTpl(
        this.templatePath("**"),
        this.destinationRoot(),
        templateObj,
        undefined,
        { globOptions: { dot: true }}
    );
    
    this.fs.delete('**/Project*.ts');

    // Custo
    this.fs.copyTpl(
      this.templatePath('src/typescripts/custo/ProjectCusto.ts'),
      this.destinationPath(path.join('src', 'typescripts', 'custo', templateObj.capitalizeCustomerSafeName + 'Custo.ts')),
      templateObj 
    );
    this.fs.copyTpl(
      this.templatePath('test/typescripts/custo/ProjectCustoTest.ts'),
      this.destinationPath(path.join('test', 'typescripts', 'custo', templateObj.capitalizeCustomerSafeName + 'CustoTest.ts')),
      templateObj 
    );

    // Helper
    this.fs.copyTpl(
      this.templatePath('src/typescripts/custo/ProjectHelper.ts'),
      this.destinationPath(path.join('src', 'typescripts', 'custo', templateObj.capitalizeCustomerSafeName + 'Helper.ts')),
      templateObj 
    );
    this.fs.copyTpl(
      this.templatePath('test/typescripts/custo/ProjectHelperTest.ts'),
      this.destinationPath(path.join('test', 'typescripts', 'custo', templateObj.capitalizeCustomerSafeName + 'HelperTest.ts')),
      templateObj 
    );

    // ProjectCore.ts
    this.fs.copyTpl(
      this.templatePath('src/typescripts/ProjectCore.ts'),
      this.destinationPath(path.join('src', 'typescripts', templateObj.capitalizeCustomerSafeName + 'Core.ts')),
      templateObj 
    );

    let extendedPkg = extend({}, pkg, templatePkg);
    // overwrite default scripts by template ones
    extendedPkg.scripts = templatePkg.scripts || pkg.scripts;
    this.fs.writeJSON(this.destinationPath('package.json'), extendedPkg);

    // make sure template variables are getting replaced.
    this.fs.copyTpl(
        this.destinationPath('package.json'),
        this.destinationPath('package.json'),
        templateObj
    );

    // create .env file (required for docker setup)
    this.fs.copyTpl(
      this.destinationPath('.env.example'),
      this.destinationPath('.env'),
      templateObj
    );
  }
  
  getCoveoLatestVersion() {

      return utils.getNpmLatestVersion('coveo-search-ui').then((res) => {
          this.log('latest release info >>> ' + res.stdout);
          this.props.coveo_latest_tag_name = res.stdout.trim();
      }, (err) => {
          this.log('something went wrong >>> ' + err);
      });
  }

};