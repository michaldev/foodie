module.exports = ( path ) ->
    length   = path.length
    lastChar = path.substring length - 1, length

    return path.substring 0, length - 1 if lastChar == "/"
    return path
