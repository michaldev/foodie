class Vitamins extends Controller
    constructor : ( $scope, $stateParams, $http, $state ) ->
        $scope.vitaminSlug  = $stateParams.vitaminSlug
        $scope.vitaminID    = $stateParams.vitaminID
        $scope.functions    = []

        $scope.functions.vitamineChange = ( vitaminSlug, vitaminID ) ->
            console.log "Vitamin slug: #{$scope.vitaminSlug}"

            $scope.vitaminSlug  = vitaminSlug
            $scope.vitaminID    = vitaminID

        $http.get "http://127.0.0.1:8000/basefood/vitamins"
            .success ( data, status, headers, config ) ->
                console.log "Vitamins: #{data}"
                $scope.vitamins = data
            .error ( data, status, headers, config ) ->
                console.log "Could not get vitamins"
