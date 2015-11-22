var src = "./../src";
var out = "./../dest";
var tmp = "./../temp";

module.exports = {
    paths : {
        src : src,
        out : out,
        tmp : tmp
    },

    html : {
        src : src,
        out : out,

        options : {
            empty        : false,
            cdata        : false,
            spare        : false,
            quotes       : true,
            comments     : false,
            conditionals : true
        }
    },

    img : {
        src : src + "/images",
        out : out + "/images"
    },

    fonts : {
        src : src + "/fonts",
        out : out + "/fonts"
    },

    css : {
        src : src + "/styles",
        out : out + "/styles"
    },

    js : {
        src : src + "/scripts",
        out : out + "/scripts"
    },

    browserSync : {
        server: {
            baseDir : out
        }
    }
};
