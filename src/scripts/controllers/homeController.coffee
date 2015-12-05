configuration   = require "./../configuration"
generateApiHost = require "./../utils/generateApiHost"
debug           = require( "./../utils/debug" )( configuration.debug )

class Home extends Controller
    constructor : ( $scope, $stateParams, $http, $cookies ) ->
        apiHost = generateApiHost configuration.api

        $scope.search = []
        $scope.search.itemsToShow = undefined
        $scope.search.searchText  = undefined
        $scope.search.foundData   = undefined
        $scope.search.showTable   = false

        $scope.search.searchItem = ( item ) ->
            if not $scope.search.searchText
                $scope.search.showTable = false
                return

            $scope.search.showTable = true

            $http.get "#{apiHost}/productsearch?search=#{$scope.search.searchText}"
                .success ( data, status, headers, config ) ->
                    if data.length
                        $scope.search.foundData   = true
                        $scope.search.itemsToShow = data
                        debug "[HOME] Search:", data
                    else
                        $( "#search-product" ).addClass( "md-input-invalid" )
                        $scope.search.foundData = false
                .error ( data, status, headers, config ) ->
                    $( "#search-product" ).addClass( "md-input-invalid" )
                    $scope.search.foundData = false
                    debug "[HOME] Search Error"

        $scope.search.listenForEnter = ( event ) ->
            if event.keyCode == 13 and $scope.search.searchText?
                $scope.search.searchItem $scope.search.searchText
            else
                $( "#search-product" ).removeClass( "md-input-invalid" )
                $scope.search.foundData = false
                $scope.search.showTable = false
