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

![Interactive demo - customerABC](https://coveojfallaire.bitbucket.io/generator-ps-boilerplate-project/boilerplate-project.svg)


### Creating a new project with npm <= 5.2

If you use npm 5.1 or earlier, you can't use npx. Instead, install the generator globally:

    npm install -g generator-ps-boilerplate-project

Now you can run:

    yo ps-boilerplate-project

## What do you get?

Scaffolds out a complete generator directory structure for you:

```
.
├── commitlint.config.js
├── customer-abc-iow
├── customer-abc-search-ui
└── package.json
```

No configuration or complicated folder structures, just the files you need to start off your project. For further details about the folder structures of `<your-customer>-iow` and `<your-customer>-search-ui`, please refer to the following documentation: 

* [generator-ps-search-ui-sfdc](https://github.com/jfallaire/generator-ps-search-ui-sfdc#readme)
* [generator-ps-iow](https://github.com/jfallaire/generator-ps-iow#readme)
