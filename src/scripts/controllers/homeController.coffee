class Home extends Controller
    constructor: ( $scope, $stateParams, $http, $cookies ) ->
        $scope.searchCtrl = []
        $scope.searchCtrl.searchItem = ( item ) ->
            console.log "Searching #{$scope.searchCtrl.searchText}"

            $scope.searchCtrl.isClicked = true

            $http.get "http://127.0.0.1:8000/basefood/productsearch?search=#{$scope.searchCtrl.searchText}"
                .success ( data, status, headers, config ) ->
                    $scope.searchCtrl.itemsToShow = data;
                    console.log "Search data #{data}"
                .error ( data, status, headers, config ) ->
                    console.log "Could not search"
