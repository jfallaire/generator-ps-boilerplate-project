# Docker Playground Development

A dockerized Playground development environment, to work locally and be able to actively develop and/or make modifications to the current implementation. The main dependency for this project is the [Coveo Javascript Search Framework](https://github.com/coveo/search-ui). This local development setup is meant to improve productivity for any search interfaces that need to be integrated in SFDC. The output destination folder (`./dist`) is where asset files will be generated.

## Getting Started

Make sure you have Docker setup. There’s a graphical installer for Windows and Mac that makes installing Docker easy. Here are instructions for each OS:

  * [Windows](https://docs.docker.com/docker-for-windows/install/)
  * [MacOS](https://docs.docker.com/docker-for-mac/install/)
  * [Linux](https://docs.docker.com/engine/installation/linux/docker-ce/ubuntu/)

To check that the Docker client and docker-compose is correctly installed, here are a few test commands:

  * `docker --version`: Returns information on the Docker version running on your local machine.
  * `docker-compose --version`: Returns information on the docker-compose version running on your local machine.
  * `docker run hello-world`: Runs the hello-world image and verifies that Docker is correctly installed and functioning.

> **_NOTE:_**  For Windows users, make sure Volume sharing is enabled. To enable volume sharing in the Docker CE for Windows :  
> 1. Right-click **Docker for Windows** in notification area, and then select **Settings**. 
> 2. Select **Shared Drives** and share the system drive along with the drive where the project resides.

## Setup environment

Create the `.env` file at the root of this project using `.env.example` as starting point and make sure to replace all emptied variables `<...>` by the proper information of your organization.

### Coveo related configuration section 

Make sure to populate following ones: 

  * `COVEO_ORG_ID`: your Coveo org ID
  * `COVEO_API_KEY`: read [Manage API Key](https://docs.coveo.com/en/1718/cloud-v2-administrators/manage-api-keys)

## Build and Run Container

For this section we’ll be covering the Linux and macOS (Unix) instructions of running Docker. The examples we’ll provide should be run in your terminal application (Unix), or the DOS prompt (Windows). While we’ll highlight the Unix shell commands, the Windows commands should be similar (refer to `Makefile`).

### Linux and macOS (Unix) instructions

To build and run the container:

```
make
```

Wait for the following lines

```
Creating network "<%= customerSafeName %>_default" with the default driver
Creating <%= customerSafeName %>-dev        ... done
```

To enter the dev container:

```
make enter
```

### Windows instructions

To build and run the container, execute the following commands in your Command Prompt (regardless of if you're using `cmd.exe`, `Powershell`, or any other command prompt) :

#### step 0:setup 

first, create the external volume where npm modules will be stored.

```
docker volume create nodemodules_<%= customerSnakeCase %>
```

then install npm modules

```
docker-compose -f docker-compose.builder.yml run --rm install
```

#### step 1:build

```
docker-compose down
docker-compose build 
docker-compose up -d --remove-orphans
```

Wait for the following lines

```
Creating network "<%= customerSafeName %>_default" with the default driver
Creating <%= customerSafeName %>-dev        ... done
```

#### step 2:consume

At this point, the container should be running. To enter into the dev container:

```
docker exec -it <%= customerSnakeCase %>-dev /bin/sh
```
## Go build applications, test, iow and more!

Now you've got Node.js on the container. It's time to start exploring! You can run your code within the container:

```
npm run build
```

This will build the entire project. All resources will be available under `./dist` folder.


## Dev Server

You can start the dev-server outside the container by running the following command (from macOS or linux):

```
make dev
```

or from windows machine: 

```
docker exec -it <%= customerSnakeCase %>-dev npm run dev
```

Any time you hit **Save** in a source file (anything under `./src`), the bundle will be recompiled and the dev page will reload.

This will start a [webpack-dev-server instance](https://webpack.github.io/docs/webpack-dev-server.html).

You can now load <http://localhost:3000> in a web browser.

## Tests


Tests are written using Jasmine. You can use `npm run test` to run the tests in Chrome Headless. If you wish to write new unit tests, you might need to debug your unit tests.

### Debugging unit tests run by Karma using Chrome DevTools.

If you are using Karma and the test fails, and you might want to debug the unit test step by step. You can do so by running the following command:

```
npm run test:searchui -- --singleRun false
```

Click on the launched Chrome instance (which now stays on) and click `Debug` button

The browser opens second tab with url <http://localhost:9876/debug.html>. You can open Chrome DevTools in this tab and look at the loaded sources tab.

Every time you hit Save in a source file or a test file, karma will reload and re-run your tests.

## Documentation (IOW)


To build the whole documentation and generate its output in the `./dist/iow`. Enter into the dev container and run the following command:

```
npm run iow:build
```

To start a webserver for the IOW, issue the following command:

```
npm run iow:dev
```

then visit the webpage served at <http://localhost:8000>. Each time a change to the documentation source is detected, the HTML is rebuilt and the browser automatically reloaded.
