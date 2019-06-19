const gulp = require('gulp');
const rename = require('gulp-rename');
const log = require('fancy-log');
const path = require('path');
const fs = require('fs-extra')
const transform = require('gulp-transform');

const staticResourceBaseFolderPath = 'force-app/main/default/staticresources';
const metaXmlExtension = '.resource-meta.xml'

const metaXmlTemplate = (contentType, cacheControl = 'Public') => `<?xml version="1.0" encoding="UTF-8"?>
<StaticResource xmlns="http://soap.sforce.com/2006/04/metadata">
    <cacheControl>${cacheControl}</cacheControl>
    <contentType>${contentType}</contentType>
</StaticResource>`

/**
 * 
 * @param {Buffer | String} content 
 * @param {File} file 
 */
const generateXML = (content, file) => {
  switch (path.extname(file.path)) {
    case '.js':
      return metaXmlTemplate('application/json')
    case '.html':
      return metaXmlTemplate('text/html')
    default:
      log(`Bad file ext: ${file.path}`)
      return content;
  }
}

const getFolders = (dir) => {
  return fs.readdirSync(dir)
    .filter(function (file) {
      return fs.statSync(path.join(dir, file)).isDirectory();
    });
}

// Generate metadata XML files for the files that are not bundled in a zip. (i.e. at the root of the staticresource folder)
const staticresourcesFiles = () => {
  return gulp.src([`${staticResourceBaseFolderPath}/*.*`, `!./**/*${metaXmlExtension}`])
    .pipe(transform('utf8', generateXML))
    .pipe(rename({ extname: metaXmlExtension }))
    .pipe(gulp.dest(staticResourceBaseFolderPath))
}

// Generate metadata XML files for the folders that are at the root of the staticresource folder (i.e. ye old zip files).
const staticresourcesFolders = (done) => {
  getFolders(staticResourceBaseFolderPath).map(folder => {
    fs.writeFileSync(path.join(staticResourceBaseFolderPath, `${folder}${metaXmlExtension}`), metaXmlTemplate('application/zip'));
  })
  done();
}


staticresourcesFiles.displayName = 'metadata:staticresourcesFiles';
staticresourcesFolders.displayName = 'metadata:staticresourcesFolders';

const metadata = gulp.parallel(
  staticresourcesFiles,
  staticresourcesFolders
);

module.exports = { metadata: metadata }
