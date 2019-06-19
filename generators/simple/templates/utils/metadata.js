const path = require('path');
const ejs = require('ejs');
const fs = require('fs');
const _ = require('underscore');
const CreateFileWebpack = require('create-file-webpack');

const sfdxBaseFolderPath = path.resolve(__dirname, '../force-app/main/default');
const metaXmlExtensions = {
    staticresource: '.resource-meta.xml',
    component: '.component-meta.xml'
}

const metaXmlComponentTemplate = (label, apiVersion = '45.0') => `<?xml version="1.0" encoding="UTF-8"?>
<ApexComponent xmlns="urn:metadata.tooling.soap.sforce.com" fqn="${label}">
    <apiVersion>${apiVersion}</apiVersion>
    <label>${label}</label>
</ApexComponent>`

const getComponentFilePlugins = (entries, options = { path: sfdxBaseFolderPath}) => {
    var plugins = [];
    _.each(entries, (entry, k) => {
      const str = fs.readFileSync(entry.templatePath, 'utf-8');
      plugins.push(new CreateFileWebpack({
        path: options.path,
        fileName: `./components/${k}.component`,
        content: ejs.render(`<apex:component>${str}</apex:component>`, { ...entry.templateData, filename: entry.templatePath })
      }));
      plugins.push(new CreateFileWebpack({
        path: options.path,
        fileName: `./components/${k}${metaXmlExtensions.component}`,
        content: metaXmlComponentTemplate(k)
      }));
    });
    return plugins;
}

module.exports = {
    getComponentFilePlugins: getComponentFilePlugins
}
