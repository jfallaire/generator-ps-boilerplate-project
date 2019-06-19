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

    this.option('generateInto', {
      type: String,
      required: false,
      defaults: 'iow/',
      desc: 'Relocate the location of the generated files.'
    });
  }

  initializing(){
    this.props = {};
    this.props.customerName = this.options.customer;
    this.props.customerSafeName = _.camelCase(this.options.customer);
  }

  writing() {

    const templateObj = {
        customerSafeName: this.props.customerSafeName,
        capitalizeCustomerSafeName: this.props.customerSafeName.replace(/\b\w/g, l => l.toUpperCase())
    }

    this.fs.copyTpl(
        this.templatePath("**"),
        this.destinationPath(this.options.generateInto),
        templateObj
    );
  }
};