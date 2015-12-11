var gulp   = require( "gulp" );
var config = require( "./../configfile" );

gulp.task( "copy", function () {
    return gulp.src( config.paths.src + "/**/*.{txt,md,gif}" )
        .pipe( gulp.dest( config.paths.out ) );
} );
