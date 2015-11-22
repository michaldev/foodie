class Preservatives extends Controller
    constructor: ( $scope, $stateParams, $http ) ->
        $scope.preservativeID   = $stateParams.preservativeID
        $scope.preservativeSlug = $stateParams.preservativeSlug
        $scope.functions        = []

        $scope.functions.preservativeChange = ( preservativeSlug, id ) ->
            $scope.preservativeID   = id
            $scope.preservativeSlug = preservativeSlug

        $http.get "http://127.0.0.1:8000/basefood/preservatives"
            .success ( data, status, headers, config ) ->
                console.log "Preservatives: #{data}"
                $scope.preservatives = data
            .error ( data, status, headers, config ) ->
                console.log "Could not get preservatives"
