configuration   = require "./../configuration"
generateApiHost = require "./../utils/generateApiHost"
debug           = require( "./../utils/debug" )( configuration.web.debug )

class Home extends Controller
    constructor : ( $rootScope, $scope, $stateParams, $http, $cookies ) ->
        apiHost = generateApiHost configuration.api

        $scope.results   = []
        $scope.slug      = undefined
        $scope.dataFound = false
        $scope.showTable = false

        # random products
        $scope.randomIds = {}
        $scope.random    = {}

        # Generating a list of last 6 products of each category
        $http.get "#{apiHost}/category"
            .success ( data, status, headers, config ) ->
                for id, item of data
                    return unless id < 3 # How many categories should be shown
                    $scope.randomIds[ item.name ] = item.id
                    $scope.getLastProducts item.id, item.name

        $scope.getLastProducts = ( id, category ) ->
            $http.get "#{apiHost}/products?category=#{id}"
                .success ( data, status, headers, config ) ->
                    $scope.random[ category ] = data.slice -6

        $scope.makeInputInvalid = ->
            $( "#search-product" ).addClass( "md-input-invalid" )

        $scope.makeInputValid = ->
            $( "#search-product" ).removeClass( "md-input-invalid" )

        # Hides errors, shows table
        $scope.canShowResults = ( results ) ->
            $scope.dataFound = true
            $scope.showTable = true
            $scope.results   = results

        # Shows errors, hides table
        $scope.cantShowResults = ->
            $scope.dataFound = false
            $scope.showTable = true
            $scope.results   = []

        # Hides errors, hides table
        $scope.hideResults = ->
            $scope.dataFound = false
            $scope.showTable = false
            $scope.results   = []

        $scope.search = ( slug ) ->
            # If user search for an empty slug
            if not $scope.slug
                $scope.makeInputInvalid()
                $scope.cantShowResults()
                return false

            $http.get "#{apiHost}/productsearch?search=#{$scope.slug}"
                .success ( data, status, headers, config ) ->
                    if data.length
                        data[ key ].image ?= "images/template/default-product.jpg" for value, key in data
                        $scope.canShowResults( data )
                        debug "[HOME] Search:", data
                    else
                        $scope.makeInputInvalid()
                        $scope.cantShowResults()
                        debug "[HOME] No items has been found"
                .error ( data, status, headers, config ) ->
                    $scope.makeInputInvalid()
                    $scope.cantShowResults()
                    debug "[HOME] Search Error"

        $scope.listenForEnter = ( event ) ->
            if event.keyCode == 13 and $scope.slug?
                $scope.search $scope.slug
            else
                $scope.makeInputValid()
                $scope.hideResults()
