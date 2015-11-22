var gulp   = require( "gulp" );
var sass   = require( "gulp-sass" );
var concat = require( "gulp-concat" );
var minify = require( "gulp-minify-css" );
var prefix = require( "gulp-autoprefixer" );
var config = require( "./../configfile" );

gulp.task( "build-css", function () {
    return gulp.src( config.css.src + "/**/*.scss" )
        .pipe( sass().on( "error", sass.logError ) )
        .pipe( minify() )
        .pipe( prefix() )
        .pipe( concat( "style.css" ) )
        .pipe( gulp.dest( config.css.out ) );
} );
