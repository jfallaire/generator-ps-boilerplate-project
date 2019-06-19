'use strict';
const _ = require('lodash');
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

    this.option('samples', {
        type: String,
        desc:'Samples'
    });
  }

  initializing(){

    this.props = {
      customerName: this.options.customer,
      customerSafeName: _.camelCase(this.options.customer),
      customerSnakeCase: _.snakeCase(this.options.customer),
      samples: _.compact(this.options.samples.split(',')) || [],
      capitalizeCustomerSafeName: _.camelCase(this.options.customer).replace(/\b\w/g, l => l.toUpperCase())
    };

    this.props.auraComponentSamples = _.map(_.clone(this.props.samples), (i) => { return i.replace('Lex', 'Lex_Coveo_') });
    this.props.vfComponentSamples = _.pull(_.clone(this.props.samples), 'LexCommunitySearchBox');
    
  }

  _readPkg() {
    return this.fs.readJSON(this.destinationPath('package.json'), {});
  }

  writing() {
    const pkg = this._readPkg();
    const templatePkg = this.fs.readJSON(this.templatePath('package.json'), {});
    const templateObj = extend(this.props, {});

    this.fs.copyTpl(
        this.templatePath('**'),
        this.destinationRoot(),
        templateObj,
        undefined,
        { globOptions: { dot: true }}
    );

    this.fs.delete('**/views/pages/Lex_Coveo*');
    this.fs.delete('**/views/partials/LexCommunity*/**');
    this.fs.delete('**/src/stylesheets/Lex_Coveo*');
    this.fs.delete('**/Project*.ts');
    
    _.each(templateObj.auraComponentSamples, (sample) => {
      this.fs.copyTpl(
        this.templatePath(`views/pages/${sample}.ejs`),
        this.destinationPath(`views/pages/${sample}.ejs`),
        templateObj,
      );
      this.fs.copyTpl(
        this.templatePath(`src/stylesheets/${sample}.scss`),
        this.destinationPath(`src/stylesheets/${sample}.scss`),
        templateObj,
      )
      this.fs.copyTpl(
        this.templatePath(`views/partials/${sample.replace('Lex_Coveo_', 'Lex')}/**`),
        this.destinationPath(`views/partials/${sample.replace('Lex_Coveo_', 'Lex')}`),
        templateObj,
      );
    });
    
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
  }
};