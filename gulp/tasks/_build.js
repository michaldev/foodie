var gulp = require( "gulp" );
var runs = require( "run-sequence" );

gulp.task( "build", function () {
    runs(
        //"clean-out",
        "clean-tmp",
        [
            "copy",
            "build-js",
            "build-css",
            "build-img",
            "build-html",
            "build-cs"
        ]
    );
} );