configuration   = require "./../configuration"
generateApiHost = require "./../utils/generateApiHost"
debug           = require( "./../utils/debug" )( configuration.debug )

class Category extends Controller
    constructor : ( $scope, $stateParams, $http ) ->
        apiHost = generateApiHost configuration.api

        $scope.id           = $stateParams.categoryID
        $scope.categoryName = $stateParams.categoryName
        $scope.category     = undefined

        $http.get "#{apiHost}/products?category=#{$scope.id}"
            .success ( data, status, headers, config ) ->
                debug "[CATEGORY] Categories:", data, $scope.id
                $scope.category = data
            .error ( data, status, headers, config ) ->
                debug "[CATEGORY] Category error"
