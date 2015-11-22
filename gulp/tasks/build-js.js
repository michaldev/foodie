var gulp       = require( "gulp" );
var changed    = require( "gulp-changed" );
var minify     = require( "gulp-uglify" );
var config     = require( "./../configfile" );

gulp.task( "build-js", function () {
    return gulp.src( config.js.src + "/**/*.js" )
        .pipe( changed( config.js.out ) )
        .pipe( minify() )
        .pipe( gulp.dest( config.js.out ) );
} );
