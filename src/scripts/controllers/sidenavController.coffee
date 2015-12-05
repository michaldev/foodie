configuration   = require "./../configuration"
generateApiHost = require "./../utils/generateApiHost"
debug           = require( "./../utils/debug" )( configuration.web.debug )

class Sidenav extends Controller
    constructor : ( $scope, $http, $mdSidenav ) ->
        apiHost = generateApiHost configuration.api

        $scope.categories = []
        $scope.filterText = ""

        $scope.closeSideNav = ->
            $mdSidenav( "left" ).close()

        $http.get "#{apiHost}/category"
            .success ( data, status, headers, config ) ->
                $scope.categories = data
                debug "[SIDENAV] Sidenav:", data
            .error ( data, status, headers, config ) ->
                debug "[SIDENAV] Sidenav error"
