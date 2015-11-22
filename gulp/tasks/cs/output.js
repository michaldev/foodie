var gulp       = require( "gulp" );
var minify     = require( "gulp-uglify" );
var rename     = require( "gulp-rename" );
var config     = require( "./../../configfile" );

gulp.task( "cs-output", function () {
    return gulp.src( config.paths.tmp + "/browserified/app.coffee" )
        //.pipe( minify() )
        .pipe( rename( "app.js" ) )
        .pipe( gulp.dest( config.js.out ) );
} );
