angular.module( "app" ).factory "changeStateFactory", ->
    changeStateFactory = []

    changeStateFactory.setFab = (value) ->
        changeStateFactory.isProduct = value

    changeStateFactory.getFab = ->
        return isProduct

    return changeStateFactory
