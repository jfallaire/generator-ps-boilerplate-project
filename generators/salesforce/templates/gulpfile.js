const build = require('./gulpTasks/build.tasks');
const env = require('./gulptasks/env.tasks')
const dev = require('./gulpTasks/dev.tasks');

// Entrypoint to externalize.
const metadata = require('./gulpTasks/metadata.tasks');
const compute = require('./gulpTasks/compute.tasks');

module.exports = {
  ...env,
  ...compute,
  ...metadata,
  ...build,
  ...dev,
  default: build.build
};
