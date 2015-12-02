module.exports = ( debug = true ) ->
    -> console.log.apply( console, arguments ) if debug
