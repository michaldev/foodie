var gulp   = require( "gulp" );
var minify = require( "gulp-minify-html" );
var config = require( "./../configfile" );

gulp.task( "build-html", function () {
    return gulp.src( config.html.src + "/**/*.html" )
        .pipe( minify( config.html.options ) )
        .pipe( gulp.dest( config.html.out ) );
} );
