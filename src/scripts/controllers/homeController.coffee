class Home extends Controller
    constructor : ( $scope, $stateParams, $http, $cookies ) ->
        $scope.search = []
        $scope.search.searchItem = ( item ) ->
            console.log "Searching #{$scope.search.searchText}"

            $scope.search.isClicked = true

            $http.get "http://127.0.0.1:8000/basefood/productsearch?search=#{$scope.search.searchText}"
                .success ( data, status, headers, config ) ->
                    $scope.search.itemsToShow = data;
                    console.log "Search data #{data}"
                .error ( data, status, headers, config ) ->
                    console.log "Could not search"
