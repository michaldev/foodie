var gulp       = require( "gulp" );
var ngClassify = require( "gulp-ng-classify" );
var config     = require( "./../../configfile" );

gulp.task( "cs-classify", function () {
    return gulp.src( config.js.src + "/**/*.coffee" )
        .pipe( ngClassify() )
        .pipe( gulp.dest( config.paths.tmp ) );
} );
