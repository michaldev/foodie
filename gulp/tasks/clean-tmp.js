var gulp   = require( "gulp" );
var del    = require( "del" );
var config = require( "./../configfile" );

gulp.task( "clean-tmp", function () {
    del( config.paths.tmp, {
        force: true
    } );
} );
