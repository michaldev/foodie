var gulp = require( "gulp" );
var runs = require( "run-sequence" );

gulp.task( "build-cs", function () {
    runs( "clean-tmp", "cs-classify", "cs-browserify", "cs-output" );
} );
