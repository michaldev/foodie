# Foodie

## Requirements:

In order to run the server you'll need `node.js`, `gulp` and `browserify` installed on your machine.

In order to install `node.js`, go to the [Node.js website](https://nodejs.org/en/) and download the binary file for your operating system.

In order to install `gulp`, execute this command in your CLI:

    npm install -g gulp

In order to install `broswerify`, execute this command in your CLI:

    npm install -g browserify

Once you have installed all the requirements, you can go to the `./gulp` folder and install others `node.js` dependencies:

    npm install

Then you should be able to use all the gulp commands.

At the end, you should create a configuration file (basically `src/scripts/configuration.example.coffee` to `src/scripts/configuration.coffee`). For more informations about configuring your project, checkout comments in the configuration file.

## Commands

| Command | Description |
|---------|-------------|
| watch   | Watches for changes and dynamically re-compiles. Creates a server and opens it in the browser. Refreshes browser on every change. |
| build   | Compiles the app and outputs the compiled code in `dest` folder in the root of the project |
| clean   | Deletes the `dest` folder. |

For more command, checkout the `/gulp/tasks` folder.

In order to use one of those commands, you must be in the `gulp` folder in your CLI. Usage:

    gulp <command>

First build may take some time to execute because it will copy all of the large dependencies like `Angular`, `jQuery`, `[...]` to the `dest` file. On first build, your should run `gulp build` command and then `gulp watch`, otherwise it will return `Could not GET /` error.

## Server

Actually, it will only work when it runs on a server (you can use the `gulp watch` command to create one). It will requests data from the `django` server. For more information about how to run the Foodie server, checkout the `master` of this project.

Once you have a working Foodie server, you must configure the WebApp. You can find the configuration file in `./src/scripts/configuration.coffee` directory.
