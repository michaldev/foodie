var gulp   = require( "gulp" );
var sync   = require( "browser-sync" );
var config = require( "./../configfile" );

gulp.task( "sync", function () {
    sync( config.browserSync );
} );
