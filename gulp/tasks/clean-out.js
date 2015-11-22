var gulp   = require( "gulp" );
var del    = require( "del" );
var config = require( "./../configfile" );

gulp.task( "clean-out", function () {
    del( config.paths.out, {
        force: true
    } );
} );
