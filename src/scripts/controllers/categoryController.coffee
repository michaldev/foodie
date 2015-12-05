configuration   = require "./../configuration"
generateApiHost = require "./../utils/generateApiHost"
debug           = require( "./../utils/debug" )( configuration.web.debug )

class Category extends Controller
    constructor : ( $scope, $stateParams, $http ) ->
        apiHost = generateApiHost configuration.api

        $scope.id           = $stateParams.categoryID
        $scope.categoryName = $stateParams.categoryName
        $scope.category     = undefined

        $http.get "#{apiHost}/products?category=#{$scope.id}"
            .success ( data, status, headers, config ) ->
                data[ key ].image ?= "images/template/default-product.jpg" for value, key in data
                $scope.category = data

                debug "[CATEGORY] Categories:", data, $scope.id
            .error ( data, status, headers, config ) ->
                debug "[CATEGORY] Category error"
