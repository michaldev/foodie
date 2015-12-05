configuration   = require "./../configuration"
generateApiHost = require "./../utils/generateApiHost"
debug           = require( "./../utils/debug" )( configuration.debug )

class Product extends Controller
    constructor : ( $scope, $stateParams, $http ) ->
        apiHost = generateApiHost configuration.api

        $scope.slug     = $stateParams.productSlug
        $scope.product  = undefined

        $http.get "#{apiHost}/product/#{$scope.slug}"
            .success ( data, status, headers, config ) ->
                $scope.product        = data
                $scope.product.image ?= "images/template/default-product.jpg"

                debug "[PRODUCT] Product:", $scope.slug, data
            .error ( data, status, headers, config ) ->
                debug "[PRODUCT] Product error"
