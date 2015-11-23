class Product extends Controller
    constructor : ( $scope, $stateParams, $http ) ->
        $scope.slug = $stateParams.productSlug

        $http.get "http://127.0.0.1:8000/basefood/product/#{$scope.slug}"
            .success ( data, status, headers, config ) ->
                console.log "Product: #{data}, #{$scope.slug}"
                $scope.product = data
            .error ( data, status, headers, config ) ->
                console.log "Could not get product data for slug #{$scope.slug}"
