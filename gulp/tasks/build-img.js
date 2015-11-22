var gulp    = require( "gulp" );
var minify  = require( "gulp-imagemin" );
var changed = require( "gulp-changed" );
var config  = require( "./../configfile" );

gulp.task( "build-img", function () {
    return gulp.src( config.img.src + "/**/*.*" )
        .pipe( changed( config.img.out ) )
        .pipe( minify() )
        .pipe( gulp.dest( config.img.out ) );
} );
