# generator-ps-boilerplate-project

> Scaffolds out a template directory structure to help out CoveoPS folks when starting off a new project for a customer in order to standardize the work ethics over the course of a project by enforcing conventional commits standard and run your project inside of a Docker container. 

![Solutions Specialist, you've been served!](https://i.imgflip.com/1jaox9.jpg)

## Usage

You’ll need to have Node 8.10.0 or later on your local development machine. You can use [nvm](https://github.com/creationix/nvm#installation) (macOS/Linux) or [nvm-windows](https://github.com/coreybutler/nvm-windows#node-version-manager-nvm-for-windows) to easily switch Node versions between different projects.

### Creating a new project with npm >= 5.2

This creates a new project in the current directory using npx:

First, uninstall a previously installed global package **generator-ps-boilerplate-project**

    npm uninstall -g generator-ps-boilerplate-project

then run :

    npx -p yo -p generator-ps-boilerplate-project@latest -- yo ps-boilerplate-project


### Creating a new project with npm <= 5.2

If you use npm 5.1 or earlier, you can't use npx. Instead, install the generator globally:

    npm install -g generator-ps-boilerplate-project

Now you can run:

    yo ps-boilerplate-project

![Interactive demo - customerABC](https://coveojfallaire.bitbucket.io/generator-ps-boilerplate-project/demo-boilerplate-project-Jun-20-2019.gif)

## What do you get?

Scaffolds out a complete generator directory structure for you.

### Simple configuration

```
.
├── Dockerfile
├── Makefile
├── README.md
├── commitlint.config.js
├── docker-compose.builder.yml
├── docker-compose.yml
├── iow
│   ├── CoveoCloudPlatform
│   ├── Customization
│   ├── Deployment
│   ├── Downloads
│   ├── Makefile
│   ├── Overview
│   ├── README.md
│   ├── _static
│   ├── _templates
│   ├── appendixA.rst
│   ├── conf.py
│   ├── dev.rst
│   ├── index.rst
│   └── requirements.txt
├── karma.conf.js
├── package.json
├── routes
│   ├── errors.js
│   └── pages.js
├── src
│   ├── fonts
│   ├── platform
│   ├── stylesheets
│   ├── typescripts
│   └── utilities
├── test
│   ├── Fake.ts
│   ├── MockEnvironment.ts
│   ├── Simulate.ts
│   ├── test.ts
│   └── typescripts
├── tsconfig.json
├── utils
│   ├── cloudplatformAPI.js
│   ├── metadata.js
│   ├── middleware.js
│   └── routesUtils.js
├── views
│   ├── pages
│   ├── partials
│   ├── templates
│   └── utilities
├── webpack.common.config.js
├── webpack.dev.config.js
├── webpack.prod.config.js
└── webpack.test.config.js
```

### Salesforce configuration

```
.
├── Dockerfile
├── Makefile
├── README.md
├── commitlint.config.js
├── config
│   └── project-scratch-def.json
├── docker-compose.builder.yml
├── docker-compose.yml
├── docker-entrypoint.sh
├── force-app
│   └── main
├── gulpfile.js
├── gulptasks
│   ├── build.tasks.js
│   ├── clean.tasks.js
│   ├── compute.tasks.js
│   ├── dev.tasks.js
│   ├── env.tasks.js
│   └── metadata.tasks.js
├── iow
│   ├── CoveoCloudPlatform
│   ├── Customization
│   ├── Deployment
│   ├── Downloads
│   ├── Makefile
│   ├── Overview
│   ├── README.md
│   ├── _static
│   ├── _templates
│   ├── appendixA.rst
│   ├── conf.py
│   ├── dev.rst
│   ├── index.rst
│   └── requirements.txt
├── karma.conf.js
├── manifest
│   └── package.xml.example
├── package.json
├── routes
│   ├── errors.js
│   └── pages.js
├── sfdx-project.json
├── src
│   ├── fonts
│   ├── platform
│   ├── stylesheets
│   ├── typescripts
│   ├── utilities
│   └── vendor
├── test
│   ├── Fake.ts
│   ├── MockEnvironment.ts
│   ├── Simulate.ts
│   ├── test.ts
│   └── typescripts
├── tsconfig.json
├── utils
│   ├── cloudplatformAPI.js
│   ├── metadata.js
│   ├── middleware.js
│   └── routesUtils.js
├── views
│   ├── pages
│   ├── partials
│   ├── templates
│   └── utilities
├── webpack.common.config.js
├── webpack.dev.config.js
├── webpack.prod.config.js
└── webpack.test.config.js
```


No configuration or complicated folder structures, just the files you need to start off your project.
