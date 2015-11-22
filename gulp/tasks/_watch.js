var gulp   = require( "gulp" );
var sync   = require( "browser-sync" );
var config = require( "./../configfile" );

gulp.task( "watch", [ "build", "sync" ], function () {
    gulp.watch( config.js.src + "/**/*.js", [ "build-js", sync.reload ] );
    gulp.watch( config.js.src + "/**/*.coffee", [ "build-cs", sync.reload ] );
    gulp.watch( config.img.src + "/**/*.*", [ "build-img", sync.reload ] );
    gulp.watch( config.css.src + "/**/*.{css,scss,sass}", [ "build-css", sync.reload ] );
    gulp.watch( config.html.src + "/**/*.html", [ "build-html", sync.reload ] );
} );
