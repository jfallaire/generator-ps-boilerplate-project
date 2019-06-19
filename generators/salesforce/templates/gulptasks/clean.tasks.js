const gulp = require('gulp');
const gulpClean = require('gulp-clean');

const clean = () => {
  return gulp.src(['force-app/main/default/staticresources/<%= customerSafeName %>_bundle_assets'], { allowEmpty: true }).pipe(gulpClean());
};

module.exports = {
  clean: clean
}