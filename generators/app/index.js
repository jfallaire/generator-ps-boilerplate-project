'use strict';
const path = require('path');
const Generator = require('yeoman-generator');
const parseAuthor = require('parse-author');
const _ = require('lodash');
const extend = _.merge;
const mkdirp = require('mkdirp');
const chalk = require('chalk');
const yosay = require('yosay');


module.exports = class extends Generator {

  constructor(args, options) {
    super(args, options);

    this.option('customer', {
      type: String,
      required: true,
      desc: 'Customer/Project name'
    });

    this.option('iow', {
      type: Boolean,
      required: false,
      default: true,
      desc: 'Include iow'
    });

    this.option('integrationType', {
      type: String,
      required: true,
      default: 'basic',
      desc: 'Type of integration'
    });

    this.option('skipInstall', {
      type: Boolean,
      default: false,
      desc: 'flag to skip install'
    })
  }

  initializing() {
    // Have Yeoman greet the user.
    this.log(yosay(
      'Welcome to the fabulous ' + chalk.red('ps-boilerplate-project') + ' generator!'
    ));

    this.pkg = this.fs.readJSON(this.destinationPath('package.json'), {});
    // Pre set the default props from the information we have at this point
    this.props = {
      name: this.pkg.name,
      description: this.pkg.description,
      version: this.pkg.version,
    };

    if (_.isObject(this.pkg.author)) {
      this.props.authorName = this.pkg.author.name;
      this.props.authorEmail = this.pkg.author.email;
      this.props.authorUrl = this.pkg.author.url;
    } else if (_.isString(this.pkg.author)) {
      const info = parseAuthor(this.pkg.author);
      this.props.authorName = info.name;
      this.props.authorEmail = info.email;
      this.props.authorUrl = info.url;
    }
  }

  _askFor() {
    const prompts = [
      {
        type: 'input',
        name: 'customer',
        message: 'Your customer (project) name?',
        default: path.basename(process.cwd()),
        when: !this.props.customer
      },
      {
        type: 'list',
        name: 'integrationType',
        message: 'What type of configuration do you need?',
        choices: ['simple', 'salesforce']
      },
      {
        name: 'description',
        message: 'Description',
        when: !this.props.description
      },
      {
        name: 'authorName',
        message: "Author's Name",
        when: !this.props.authorName,
        default: this.user.git.name(),
        store: true
      },
      {
        name: 'authorEmail',
        message: "Author's Email",
        when: !this.props.authorEmail,
        default: this.user.git.email(),
        store: true
      }
    ];
    return this.prompt(prompts).then(props => {
      this.props = extend(this.props, props);
      this.props.customerSafeName = _.camelCase(this.props.customer);
      this.props.customerSnakeCase = _.snakeCase(this.props.customer);
      this.props.root = process.cwd();
    });
  }

  _askForEnv() {
    const prompts = [
        {
          type: 'input',
          name: 'portNumber',
          message: 'Which port is your app listening to?',
          default: 3000
        },
        {
          type: 'input',
          name: 'orgid',
          message: 'What is your Coveo org ID (default to a sample org id) ?',
          default: 'searchuisamples'
        },
        {
          type: 'input',
          name: 'apiKey',
          message: 'What is your api key (default to sample access token) ?',
          default: 'xx564559b1-0045-48e1-953c-3addd1ee4457'
        }
      ];
      return this.prompt(prompts).then(props => {
        this.props = extend(this.props, props);
      });
    }

  _askForSalesforce() {
    const prompts = [
      {
        type: 'confirm',
        name: 'needSamples',
        message: 'Do you need sample(s) to start up with?',
        when: this.props.integrationType === 'salesforce'
      },
      {
        type: 'checkbox',
        name: 'samples',
        message: 'Select samples',
        when: this.props.integrationType === 'salesforce' && this.props.needSamples,
        choices: [
          { type: 'separator', line: ' == Lightning Community == ' },
          { name: 'Lightning Community SearchBox', value: 'LexCommunitySearchBox' },
          { name: 'Lightning Community Full Search', value: 'LexCommunitySearch' },
          { name: 'Lightning Community Case Deflection', value: 'LexCommunityCaseDeflection' },
        ]
      }
    ];

    return this.prompt(prompts).then(props => {
      this.props = extend(this.props, props);
    });
  }

  prompting() {
    return this._askFor()
      .then(this._askForEnv.bind(this))
      .then(this._askForSalesforce.bind(this));
  }

  writing() {
    // Re-read the content at this point because a composed generator might modify it.
    const currentPkg = this.fs.readJSON(this.destinationPath('package.json'), {});
    const pkg = extend(
      {
        name: this.props.customerSafeName,
        version: '0.0.0',
        description: this.props.description,
        author: {
          name: this.props.authorName,
          email: this.props.authorEmail
        }
      },
      currentPkg
    );

    // Let's extend package.json so we're not overwriting user previous fields
    this.fs.writeJSON(this.destinationPath('package.json'), pkg);
  }

  default() {

    this.composeWith(require.resolve('../simple'), {
      customer: this.props.customer,
      orgid: this.props.orgid,
      apiKey: this.props.apiKey,
      portNumber: this.props.portNumber
    });

    if (this.options.iow) {
      this.composeWith(require.resolve('../iow'), {
        customer: this.props.customer
      });
    }

    if (this.props.integrationType !== 'simple') {
      this.composeWith(require.resolve(`../${this.props.integrationType}`), {
        customer: this.props.customer,
        samples: this.props.samples
      });
    }
  }

  // cleanup() {
  //   return new Promise((resolve, reject) => {
     
  //     resolve();
  //   });
  // }

  // install() {
    
  //   if (!this.options.skipInstall) {
  //     this.spawnCommand('make', ['setup']);
  //   }
  // }

  end() {

    // this.conflicter.force = true;
    // this.fs.delete('package.*.json');
    // this.fs.delete('**/Project*.ts');

    this.fs.commit([], ()=>{
      this.log(chalk.green('Your project is now ready to run in a Docker container!'));
      this.log('Setup your environment (refer to README.md) and then Run ' + chalk.green('make') + ' to build a Docker image and run your app in a container.');
      this.log('Thanks for using CoveoPS project generator.');
    });
  }

};