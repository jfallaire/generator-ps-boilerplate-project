const express = require('express');
const path = require('path');
const fs = require('fs');
const router = express.Router();
const middleware = require('../utils/middleware');

router.use((req, res, next) => {
  req.filter = process.env.COVEO_COMMON_FILTER || '@uri';
  next();
});

router.get('/favicon.ico', (req, res) => res.status(204));
router.get('/', (req, res) => {
  var dirPath = path.resolve('./views/pages');
  var fileType = '.ejs';
  var files = [];
  fs.readdir(dirPath, function (err, list) {
    if (err) throw err;
    for (var i = 0; i < list.length; i++) {
      if (path.extname(list[i]) === fileType) {
        files.push(list[i]);
      }
    }
    res.render('pages/index', {
      config: {
        coveo_cdn: process.env.COVEO_CDN_BASE_URL,
        coveo_rest_uri: process.env.COVEO_REST_URI,
        coveo_org_id: process.env.COVEO_ORG_ID
      }, 
      title: '<%= capitalizeCustomerSafeName %> Playground App',
      pages: files
    });
  });
});

router.get('/:name', (req, res, next) => {
  req.filter = req.query.userType === 'Employee' ? 
    process.env.COVEO_EMPLOYEE_FILTER : 
    process.env.COVEO_GUEST_FILTER;
  next();
}, middleware.ensureTokenGenerated, (req, res, next) => {
  res.render('pages/' + req.params.name, {
    title: req.params.name,
    locale: {
      language: req.query.language || 'en',
      langLocale: req.query.langLocale || 'en_US'
    },
    context: {
      subject: req.query.subject || '',
      description: req.query.description || '',
    },
    config: {
      coveo_cdn: process.env.COVEO_CDN_BASE_URL,
      coveo_rest_uri: process.env.COVEO_REST_URI,
      coveo_org_id: process.env.COVEO_ORG_ID
    },
    token: req.session.tokens[req.originalUrl]
  });
});

module.exports = router;