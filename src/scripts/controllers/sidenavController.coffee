class Sidenav extends Controller
    constructor : ( $scope, $http, $mdSidenav ) ->
        $scope.categories = []
        $scope.filterText = ""

        $scope.closeSideNav = ->
            $mdSidenav( "left" ).close()

        $http.get "http://127.0.0.1:8000/basefood/category"
            .success ( data, status, headers, config ) ->
                $scope.categories = data
                console.log "Sidenav categories: ", data
            .error ( data, status, headers, config ) ->
                console.log "Could not get categories for SideNav"
