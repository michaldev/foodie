class Home extends Controller
    constructor : ( $scope, $stateParams, $http, $cookies ) ->
        $scope.search = []
        $scope.search.itemsToShow = []
        $scope.search.searchText  = ""
        $scope.search.showTable   = false

        $scope.search.searchItem = ( item ) ->
            if not $scope.search.searchText
                $scope.search.showTable = false
                return

            $scope.search.showTable = true

            console.log "Searching #{$scope.search.searchText}"
            $http.get "http://127.0.0.1:8000/basefood/productsearch?search=#{$scope.search.searchText}"
                .success ( data, status, headers, config ) ->
                    $scope.search.foundData   = true
                    $scope.search.itemsToShow = data
                    console.log "Search data #{data}"
                .error ( data, status, headers, config ) ->
                    $( "#search-product" ).addClass( "md-input-invalid" )
                    $scope.search.foundData = false
                    console.log "Could not search"

        $scope.search.listenForEnter = ( event ) ->
            if event.keyCode == 13 and $scope.search.searchText?
                $scope.search.searchItem $scope.search.searchText
            else
                $( "#search-product" ).removeClass( "md-input-invalid" )
                $scope.search.foundData = false
                $scope.search.showTable = false
