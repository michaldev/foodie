class Category extends Controller
    constructor: ( $scope, $stateParams, $http ) ->
        $scope.id           = $stateParams.categoryID
        $scope.categoryName = $stateParams.categoryName

        $http.get "http://127.0.0.1:8000/basefood/products?category=#{$scope.id}"
            .success ( data, status, headers, config ) ->
                console.log "Category: #{data}, #{$scope.id}"
                $scope.category = data
            .error ( data, status, headers, config ) ->
                console.log "Could not get category for slug #{$scope.id}"
