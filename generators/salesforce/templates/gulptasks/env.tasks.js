const dotenv = require('dotenv-defaults');
const path = require('path');
const fs = require('fs-extra');

const setEnv = cb => {
  // Set the config.
  let envPath;
  try {
    fs.accessSync(path.resolve(__dirname, '.env'));
    envPath = path.resolve(__dirname, '.env');
  } catch (error) {
    console.log('.env not found, continue using the machine env');
  }
  dotenv.config({ path: envPath });
  console.log(process.env.SERVER_PORT)
  cb();
};

module.exports.setEnv = setEnv;