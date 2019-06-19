const gulp = require('gulp');
const sfdxBaseFolderPath = './force-app/main/default';

// List your aura components 
const auraComponents = [
    <% for (var i = 0; i < auraComponentSamples.length; i++) { %>
    "<%=auraComponentSamples[i]%>",
    <% } %>
];
 
const staticresources = () => {
  return gulp.src(['dist/**/<%= customerSafeName %>.bundle.*', 'dist/**/cultures/*'])
    .pipe(gulp.dest(`${sfdxBaseFolderPath}/staticresources/<%= customerSafeName %>_bundle_assets`))
}

const aura = (done) => {
    const tasks = auraComponents.map((cmp, i) => { 
        const task = () => { 
            return gulp.src([`./dist/css/${cmp}.css`])
                .pipe(gulp.dest(`${sfdxBaseFolderPath}/aura/${cmp}/`)); 
        };
        task.displayName = `compute:aura:${cmp}`;
        if(i == auraComponents.length-1) {
            done();
        }
        return task;
    });

    return gulp.parallel(...tasks)();
}

staticresources.displayName = 'compute:staticresources:<%= customerSafeName %>_bundle_assets';
aura.displayName = 'compute:aura';

const compute = gulp.parallel(
    aura,
    staticresources
);

compute.displayName = 'compute';

module.exports = { compute: compute }