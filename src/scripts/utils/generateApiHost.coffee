module.exports = ( config ) ->
    config.sll  ?= false
    config.host ?= "localhost"
    config.port ?= null
    config.path ?= null

    # Return
    host  = "#{if config.sll then "https://" else "http://"}"
    host += config.host
    host += ":#{config.port}" if config.port
    host += "/#{config.path}" if config.path
