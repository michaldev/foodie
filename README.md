# Foodie

## Requirements:

In order to run the server you'll need `node.js`, `gulp` and `browserify` installed on your machine.

In order to install `node.js`, go to the `node.js` website and download the binary file for your operating system:

    https://nodejs.org/en/

In order to install `gulp`, execute this command in your CLI:

    npm install -g gulp

In order to install `broswerify`, execute this command in your CLI:

    npm install -g browserify

Once you have installed all the requirements, you can go to the `./gulp` folder and install `node.js` dependencies:

    npm install

Then you should be able to use all the gulp commands.

## Commands

| Command | Description |
|---------|-------------|
| watch   | Watches for changes and dynamically re-compiles. Creates a server and opens it in the browser. Refreshes browser on every change. |
| build   | Compiles the app and outputs the compiled code in `dest` folder in the root of the project |
| clean   | Deletes the `dest` folder. |

For more command, checkout the `/gulp/tasks` folder.

In order to use one of those commands, you must be in the `gulp` folder in your CLI. Usage:

    gulp <command>

First build may take some time to execute because it will copy all of the large dependencies like `Angular`, `jQuery`, `[...]` to the `dest` file.

## Server

Actually, it will only work when it runs on a server (you can use the `gulp watch` command to create one). It will requests data from the `django` server from `http://127.0.0.1:8000/`.
