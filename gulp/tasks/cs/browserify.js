var gulp       = require( "gulp" );
var browserify = require( "gulp-browserify" );
var config     = require( "./../../configfile" );

gulp.task( "cs-browserify", function () {
    return gulp.src( config.paths.tmp + "/**/*.coffee", { read : false } )
        .pipe( browserify( {
            transform  : [ "coffeeify" ],
            extensions : [ ".coffee" ]
        } ) )
        .pipe( gulp.dest( config.paths.tmp + "/browserified" ) );
} );
